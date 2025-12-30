pipeline {
    agent any [cite: 29]

    environment {
        APP_NAME = 'ToyStore' [cite: 58]
    }

    stages {
        stage('Build') { [cite: 56]
            steps {
                echo 'Building the application...' [cite: 35]
            }
        }

        stage('Test') { [cite: 56]
            steps {
                // הרצת הבדיקות ויצירת דוח XML
                sh 'pytest --junitxml=results.xml' [cite: 74, 75]
            }
        }

        stage('Deploy') { [cite: 56]
            steps {
                echo 'Deploying to store inventory...' [cite: 44]
            }
        }
    }

    post { [cite: 60]
        always {
            // הצגת תוצאות הבדיקות בממשק Jenkins
            junit 'results.xml' [cite: 76, 77]
        }
    }
}