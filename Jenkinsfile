pipeline {
    agent any

    stages {
        stage('Clonar proyecto') {
            steps {
                echo 'Proyecto clonado correctamente.'
            }
        }

        stage('Build') {
            steps {
                sh 'docker build -t vulnerable-app .'
            }
        }

        stage('Ejecutar aplicación') {
            steps {
                sh 'docker run -d --rm --name vulnerable-app-container -p 5000:5000 vulnerable-app'
            }
        }
        stage('Test') {
            steps {
                sh 'docker run --rm vulnerable-app pytest -v'
            }
        }
    }
}