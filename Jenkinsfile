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
    }

    post {
        success {
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
