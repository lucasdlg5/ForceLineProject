from fabric.api import *

env.hosts = ['206.81.8.182']
env.user = 'root'
env.key_filename = './deploy_key'
env.deploy_project_root = '/project/ForceLineProject'

def docker_deployer():
	with cd('%s' % env.deploy_project_root):

		print('getting the changes of github')
		sudo("git pull")

		print('executing ngok domain')
		sudo("ngrok http -region=us -hostname=kevinmikio.ngrok.io 8000 > /dev/null &")

		print('executing django app')
		sudo("python3 todoapp/manage.py runserver")