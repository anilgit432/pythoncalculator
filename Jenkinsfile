pipeline{
    agent any
    stages{
        stage('checkout'){
            steps{
                git(
                    branch: 'main',
                    url: 'https://github.com/anilgit432/pythoncalculator.git'
                )
            }
        }
        stage ('build'){
            steps {
                sh 'python3 --version'
                sh 'python3 -m py_compile app.py'
            }
        }
        stage ('test'){
            steps{
                sh 'python3 -m unittest discover -v'
            }
        }
        
            
            
        
    }
}

    




    

