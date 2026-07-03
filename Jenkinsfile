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
        stage('Análisis de Seguridad - OWASP ZAP') {
            steps {
                sh '''
                    docker network create zap-net || true
                    docker network connect zap-net vulnerable-app-container || true
                    mkdir -p zap-reports
                    chmod -R 777 zap-reports
                    docker run --rm --network zap-net \
                    -v $(pwd)/zap-reports:/zap/wrk/:rw \
                    zaproxy/zap-stable zap-baseline.py \
                    -t http://vulnerable-app-container:5000 \
                    -r zap_report.html || true
                '''
            }
        }
    }
}