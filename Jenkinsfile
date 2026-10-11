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
            description: 'Greeting'
        )
    }

    stages {
        stage('Environment Check') {
            steps {
                sh 'python3 --version'
                sh 'git --version'
            }
        }

        stage('Greeting') {
            steps {
                sh '''
                    echo "$GREETING, $STUDENT! Variant 3"
                    echo "Build number: $BUILD_NUMBER"
                    echo "Job name: $JOB_NAME"
                '''
            }
        }

        stage('Check Application Files') {
            steps {
                sh '''
                    ls -la
                    test -f app.py
                    test -f Dockerfile
                    test -f requirements.txt
                    echo "Application files checked"
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully'
        }
        failure {
            echo 'Pipeline failed'
        }
    }
}
