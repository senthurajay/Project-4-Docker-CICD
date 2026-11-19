pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Getting source code from GitHub'
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Snake Game Docker Image'
                sh 'docker build -t snake-game:latest .'
            }
        }
    }
}