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
                sh 'docker-compose build'
            }
        }
        stage('Run') {
            steps {
                sh 'docker-compose up'
            }
        }
        stage('Test') {
            steps {
                sh 'python tests/e2e.py'
            }
        }
        stage('Finalize') {
            steps {
                sh 'docker-compose down'
                sh 'docker push xazmo/scoresweb:latest'
            }
        }
    }
}