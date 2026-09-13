pipeline{
	agent{ label 'built-in'}
	stages{
		stage('checkout'){
			steps{
				git(
					url: 'https://github.com/Binitmaharjan-hub/assignment-10-jenkins.git',
					branch: 'main',
					credentialsId: '8341fc18-c98d-4e01-961a-902890af7960'
				)
			}
		}
		stage('install dependencies'){
			steps{
				sh '''
				python3 -m venv venv
				. venv/bin/activate
				pip install -r backend/requirements.txt
				'''
			}
		}
		stage('build'){
			steps{
				sh 'docker build -t assignment-10-jenkins:latest .'
				sh 'docker tag assignment-10-jenkins:latest binitmaharjan/assignment-10-jenkins:latest'
			}
		}
		stage('push'){
			steps{
				withCredentials([usernamePassword(credentialsId:'5f36b2c6-26a6-4811-ac9e-766ad2c7117c',usernameVariable:'USERNAME',passwordVariable:'PASSWORD')]){
					sh ''' 
						echo $PASSWORD | docker login -u $USERNAME --password-stdin
						docker push binitmaharjan/assignment-10-jenkins:latest
					'''
				}
			}
		}
		stage('verify'){
			steps{
				sh 'docker run -d --name assignment-test -p 5000:5000 assignment-10-jenkins:latest'
				sh 'sleep 5'
				sh 'curl https://localhost:5000/fact'
			}
		}
		stage('cleanup'){
			steps{
				sh 'docker logout'
				sh 'docker rmi assignment-10-jenkins:latest'
				sh 'docker rmi binitmaharjan/assignment-10-jenkins:latest'
		}
	}
	}
}
