pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/SunilKumar-QA/Api_Automation_Playwright.git'
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
