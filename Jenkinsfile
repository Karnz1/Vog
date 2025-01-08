pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                script {
                    // Add your build commands here
                    echo 'Building...'
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    // Add your test commands here
                    echo 'Testing...'
                }
            }
        }
        stage('Push') {
            steps {
                script {
                    // Add your push commands here
                    echo 'Pushing...'
                }
            }
        }
    }
}