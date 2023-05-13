pipeline {
    agent any
    
     stages {
        stage('Test') {
            steps {
                sh 'pwd'
                sh 'cd ./Application/api'
                sh 'pwd'
                sh 'python3 manage.py test'
            }
        }
    }
}
