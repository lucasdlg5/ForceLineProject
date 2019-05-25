from fabric.api import *

env.hosts = ['206.81.8.182']
env.user = 'root'
env.key_filename = './deploy_key'
env.deploy_project_root = '/project/ForceLineProject'

def docker_deployer():
	with cd('%s' % env.deploy_project_root):

		print('stop and deleting docker')
		sudo("docker stop forceline")
		sudo("docker rm forceline")

		print('getting the changes of github')
		sudo("git pull")

		print("login docker")
		sudo("docker login -u 'forcelinerobot' -p '789456qwe'")

		print("creating docker")
		cd('/todoapp/')
		sudo("docker build -t forcelineproject:latest . ")

		print("runing docker")
		sudo("docker run -d --name forceline --restart=always -p 8000:8000 forcelineproject:latest")