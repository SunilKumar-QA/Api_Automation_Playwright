pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'master', url: 'https://github.com/SunilKumar-QA/Api_Automation_Playwright.git'
            }
        }

        stage('Start JSON Server') {
            steps {
                echo 'Starting JSON Server...'
                // Start json-server in the background using Windows CMD
                bat "start /B json-server --watch C:\\Users\\LENOVO\\apis\\db.json --port 3000"
                sleep time: 5, unit: 'SECONDS'  // Give server time to start
            }
        }

        stage('Setup Python VirtualEnv') {
            steps {
                bat 'python -m venv venv'
                bat 'venv\\Scripts\\activate && python -m pip install --upgrade pip'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'venv\\Scripts\\activate && pip install -r requirements.txt'
                bat 'venv\\Scripts\\activate && playwright install'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'venv\\Scripts\\activate && pytest'
            }
        }
    }

    post {
        
        success {
            echo '✅ All API tests passed.'
        }
        failure {
            echo '❌ Some API tests failed.'
        }
    }
}
