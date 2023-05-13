pipeline {
    
    agent any

    stages {
        stage('Test') {
            steps {
                sh """
                    cd Application/api
                    virtualenv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                    python3 manage.py test
                """
            }
        }
            stage('Build'){
             steps {

                withCredentials([usernamePassword(credentialsId: 'dockerhub', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')])            {

                sh """
                    docker login -u ${USERNAME} -p ${PASSWORD}
                    cd Application/api
                    docker build . -t ${USERNAME}/django:v$BUILD_NUMBER
                    docker push ${USERNAME}/django:v$BUILD_NUMBER
                    cd ..
                    cd app
                    docker build . -t ${USERNAME}/react:v$BUILD_NUMBER
                    docker push ${USERNAME}/react:v$BUILD_NUMBER
                """
                }
              }
        }
        stage('Deploy'){
            steps {

                withCredentials([file(credentialsId: 'accesscluster', variable: 'config')]){
                    sh """
                        gcloud auth activate-service-account --key-file=${config}
                        gcloud container clusters get-credentials my-private-cluster --zone us-central1-c --project melior-task
                        sed -i 's/tag/${BUILD_NUMBER}/g' Deployment/frontend/deployment.yaml
                        sed -i 's/tag/${BUILD_NUMBER}/g' Deployment/backend/deployment.yaml
                        kubectl apply -Rf Deployment
                    """
                }
            }
        }
    }
}

