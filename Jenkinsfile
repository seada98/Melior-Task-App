pipeline {
    agent any
    
    stages {
        stage('Setup') {
            steps {
                sh 'virtualenv venv'
                sh 'source venv/bin/activate'
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh 'python manage.py test <app_name>'
            }
        }
    }
}
