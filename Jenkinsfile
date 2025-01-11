pipeline {
    agent any
    stages {
        stage('checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/Karnz1/Vog.git']])
            }
        }
        stage('Build') {
            steps {
                //sh 'docker-compose build'
                bat 'docker-compose build'
            }
        }
        stage('Run') {
            steps {
                //sh 'docker-compose up'
                bat 'docker-compose up -d'
            }
        }
        stage('Test') {
            steps {
                //sh 'python tests/e2e.py'
                bat 'python tests/e2e.py'
            }
        }
        stage('Finalize') {
            steps {
                //sh 'docker-compose down'
                //sh 'docker push xazmo/scoresweb:latest'
                bat 'docker-compose down'
                bat 'docker push xazmo/scoresweb:latest'
            }
        }
    }
}
