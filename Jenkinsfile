pipeline {
    agent any

    stages {
        stage('Start JSON Server') {
            steps {
                echo '🚀 Starting json-server from server.js...'
                bat 'start "" cmd /c "cd C:\\Users\\LENOVO\\apis && node server.js"'
                sleep time: 5, unit: 'SECONDS'
            }
        }

        stage('Install Python Dependencies') {
            steps {
                echo '📦 Installing Python dependencies...'
                bat 'cd C:\\ProgramData\\Jenkins\\.jenkins\\workspace\\API_Playwright_CI && pip install -r requirements.txt'
            }
        }

        stage('Install Node.js Dependencies') {
            steps {
                echo '📦 Installing Node.js dependencies...'
                bat 'cd C:\\Users\\LENOVO\\apis && npm install'
            }
        }

        stage('Run Playwright API Tests') {
            steps {
                echo '🚀 Running Playwright API tests...'
                bat 'cd C:\\ProgramData\\Jenkins\\.jenkins\\workspace\\API_Playwright_CI && pytest apis/'
            }
        }

        stage('Stop JSON Server') {
            steps {
                echo '🛑 Stopping json-server...'
                bat 'taskkill /F /IM node.exe || echo "json-server already stopped."'
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
        always {
            echo '🧹 Cleaning up...'
            bat 'taskkill /F /IM node.exe || echo "json-server already stopped."'
        }
    }
}
