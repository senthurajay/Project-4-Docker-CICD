
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

        stage('Test Application') {
            steps {
                echo 'Testing Snake Game application'

                sh '''
                    docker rm -f snake-game-test-ci || true
                    docker run -d --name snake-game-test-ci snake-game:latest
                    sleep 5
                    docker exec snake-game-test-ci python -c "import urllib.request; response = urllib.request.urlopen('http://127.0.0.1:5000'); print('HTTP Status:', response.status); assert response.status == 200"
                    docker rm -f snake-game-test-ci
                '''
            }
        }

        stage('Deploy Application') {
            steps {
                echo 'Deploying Snake Game application'

                sh '''
                    docker rm -f snake-game-deploy || true
                    docker run -d --name snake-game-deploy -p 5003:5000 snake-game:latest
                '''
            }
        }
    }
}

