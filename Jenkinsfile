pipeline {
    agent any

    environment {
        PROJECT_DIR = 'C:\\Users\\LENOVO\\apis'
    }

    stages {
        stage('Start JSON Server') {
            steps {
                echo '🚀 Starting json-server from server.js...'
                bat 'start "" cmd /c "cd %PROJECT_DIR% && node server.js"'
                sleep time: 5, unit: 'SECONDS' // Give server time to start
            }
        }

        stage('Install Python Dependencies') {
            steps {
                echo '📦 Installing Python dependencies...'
                bat 'cd %PROJECT_DIR% && pip install -r requirements.txt'
            }
        }

        stage('Install Node Dependencies') {
            steps {
                echo '📦 Installing Node.js dependencies...'
                bat 'cd %PROJECT_DIR% && npm install'
            }
        }

        stage('Run Playwright API Tests') {
            steps {
                echo '🧪 Running API tests...'
                bat 'cd %PROJECT_DIR% && pytest --maxfail=1 --disable-warnings -v'
            }
        }

        stage('Stop JSON Server') {
            steps {
                echo '🛑 Stopping json-server...'
                bat 'taskkill /F /IM node.exe || echo "json-server was already stopped."'
            }
        }
    }

    post {
        always {
            echo '🧹 Cleaning up...'
            bat 'taskkill /F /IM node.exe || echo "json-server already stopped."'
        }
        success {
            echo '✅ All API tests passed.'
        }
        failure {
            echo '❌ Some API tests failed.'
        }
    }
}
