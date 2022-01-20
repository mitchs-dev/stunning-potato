pipeline {
    agent {
        node {
            label 'MyAgent'
        }
    }

    stages {
        stage('Checkout code from SCM') {
            steps {
                // This step checks out the code
                checkout scm
            }
        }
        stage('Build Image') {
            steps {
                sh 'docker image rm -f doz2h:session6'
                sh 'docker build -t doz2h:session6 .'
            }
        }
        stage('Run Program') {
            steps {
                // This is going to display the rules for our Rock, Paper, Scissor game
                sh 'docker run --rm --name doz2h-session6-rules-container doz2h:session6 python session6.py --rules'
                // This is going to actually run our program
                sh 'docker run --rm --name doz2h-session-6-container doz2h:session6'
            }
        }
        stage('Cleanup') {
            steps {
                sh 'docker image rm -f doz2h:session6'
                cleanWs()
            }
        }
    }
}
