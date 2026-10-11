pipeline {
    agent any

    parameters {
        string(
            name: 'STUDENT',
            defaultValue: 'Zhumabaeva',
            description: 'Student surname'
        )

        choice(
            name: 'GREETING',
            choices: ['Salem', 'Hello', 'Privet'],
            description: 'Greeting language'
        )
    }

    stages {
        stage('Environment Check') {
            steps {
                sh 'git --version'
                sh 'echo "Jenkins environment checked"'
            }
        }

        stage('Greeting') {
            steps {
                sh 'echo "$GREETING, $STUDENT! Variant 3"'
                sh 'echo "Build number: $BUILD_NUMBER"'
                sh 'echo "Job name: $JOB_NAME"'
            }
        }

        stage('Check Application Files') {
            steps {
                sh 'ls -la'
                sh 'test -f app.py'
                sh 'test -f Dockerfile'
                sh 'test -f requirements.txt'
                echo 'All application files are present.'
            }
        }

        stage('Create Report Artifact') {
            steps {
                sh '''
                    echo "JOB_NAME=$JOB_NAME" > report-3.txt
                    echo "BUILD_NUMBER=$BUILD_NUMBER" >> report-3.txt
                    echo "VARIANT=3" >> report-3.txt
                    echo "DATETIME=$(date '+%Y-%m-%d %H:%M:%S')" >> report-3.txt
                    echo "COMMIT=$(git rev-parse --short HEAD)" >> report-3.txt

                    cat report-3.txt
                '''
            }
        }
    }

    post {
        success {
            archiveArtifacts artifacts: 'report-*.txt',
                             fingerprint: true
            echo 'Pipeline completed successfully!'
        }

        failure {
            echo 'Pipeline failed'
        }

        always {
            echo 'Pipeline execution finished.'
        }
    }
}
