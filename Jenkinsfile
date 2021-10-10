node('OVH') {
    def image = null
    stage('Checkout') {
        checkout scm
    }

    stage('Build') {
        image = docker.build("metrics-api:${env.BUILD_ID}")
    }

    stage('Deploy'){
        try{
            sh 'docker stop metrics-api && docker rm metrics-api'
        }catch(Exception e){
            echo e.getMessage()
        }

        withCredentials([string(credentialsId: 'metrics-db-password', variable: 'metrics-db-password')]) {
            withCredentials([string(credentialsId: 'metrics-db-user', variable: 'metrics-db-user')]) {
                def runArgs = '\
-e "DB_USER=$metrics-db-user" \
-e "DB_PASSWORD=$metrics-db-password" \
--restart unless-stopped \
--network metrics \
--name metrics-api'

                def container = image.run(runArgs)

                sh 'docker network connect --ip 172.18.1.3 HTTP_SERVICES metrics-api'
            }
        }

    }
}