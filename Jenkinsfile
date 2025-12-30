pipeline {
    agent any

    environment {
        APP_NAME = 'Toy Store'
    }

    stages {
        stage('Build') {
            steps {
                echo "Building ${env.APP_NAME}..."
            }
        }
        stage('Test') {
            steps {
                echo "Running Tests..."
                // שינינו מ-sh ל-bat עבור מערכת הפעלה Windows
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
            junit 'results.xml'
        }
    }
}