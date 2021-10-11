node('OVH') {
    def image = null
    def image_name = "metrics-api"
    stage('Checkout') {
        checkout scm
    }

    stage('Build') {
        image = docker.build("${image_name}:${env.BUILD_ID}")
    }

    stage('Deploy'){
        try{
            sh "docker stop ${image_name} && docker rm ${image_name}"
        }catch(Exception e){
            echo e.getMessage()
        }

        withCredentials([string(credentialsId: 'metrics-db-password', variable: 'dbpassword')]) {
        withCredentials([string(credentialsId: 'metrics-db-user', variable: 'dbuser')]) {
                def runArgs = '\
-e "DB_USER=${dbuser}" \
-e "DB_PASSWORD=${dbpassword}" \
--restart unless-stopped \
--network metrics \
--name ' + image_name

                def container = image.run(runArgs)

                sh "docker network connect --ip 172.18.1.3 HTTP_SERVICES ${image_name}"
         }
        }

    }
}