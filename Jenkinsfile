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
				sh 'pip install -r requirements.txt'
			}
		}
		stage('build'){
			steps{
				sh 'docker build -t assignment-10-jenkins .'
				sh 'docker tag assignment-10-jenkins:latest '
			}
		}
		stage('push'){
			steps{
				withcredentials([usernamePassword(credentialsId:'5f36b2c6-26a6-4811-ac9e-766ad2c7117c',usernameVariable:'USERNAME',passwordVariable:'PASSWORD')]){
					sh ''' 
						echo $PASSWORD | docker login -u $USERNAME --password-stdin
						docker push assignment-10-jenkins:latest				
					'''
				}
			}
		}
		}
	}
