pipeline {
    agent any
    
    stages {
        stage('Setup') {
            steps {
                sh """
                    cd Application/api
                    virtualenv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                """
            }
        }
        stage('Test') {
            steps {
                sh """
                    cd Application/api
                    virtualenv venv
                    . venv/bin/activate
                    python3 manage.py test
                """
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
