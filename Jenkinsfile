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
                // הרצת הבדיקות ויצירת דוח XML כפי שמוסבר במצגת
                sh 'pytest --junitxml=results.xml'
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
            // הצגת תוצאות הבדיקות בממשק ה-JUnit של ג'נקינס
            junit 'results.xml'
        }
    }
}