pipeline {
    agent any
    
    stages {
        stage('Setup') {
            steps {
                sh """
                    cd Application/api
                    pwd
                    virtualenv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                    pwd
                """
            }
        }
        stage('Test') {
            steps {
                sh 'pwd'
                sh 'python3 manage.py students.test'
                sh 'pwd'
            }
        }
    }
}






// pipeline {
//     agent any
    
//     stages {
//         stage('Setup') {
//             steps {
//                 sh """
//                     cd Application/api
//                     virtualenv venv
//                     source venv/bin/activate
//                     'pip install -r requirements.txt'
//                 """
//             }
//         }
//         stage('Test') {
//             steps {
//                 sh 'python3 manage.py test'
//             }
//         }
//     }
// }
