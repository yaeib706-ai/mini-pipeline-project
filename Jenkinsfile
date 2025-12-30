pipeline {
    agent any

    environment {
        APP_NAME = 'Toy Store'
    }

    stages {
        stage('Build') {
            steps {
                echo "Building ${env.APP_NAME}..."
                // התקנת pytest כדי לוודא שהוא קיים בשרת
                bat 'C:\\Python312\\python.exe -m pip install pytest'
            }
        }
        stage('Test') {
            steps {
                echo "Running Tests..."
                // הרצת הבדיקות
                bat 'C:\\Python312\\python.exe -m pytest --junitxml=results.xml'
            }
        }
        stage('Deploy') {
            steps {
                echo "Deploying to Production..."
            }
        }
    }

    post {
        always {
            // יצירת הדו"ח הגרפי
            junit 'results.xml'
        }
    }
}