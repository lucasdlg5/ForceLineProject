from fabric.api import *

# host
env.hosts = ['206.81.8.182']

# username
env.user = 'root'

# or, specify path to server public key here:
env.key_filename = '~/.ssh/id_rsa.pub'

# specify path to deploy root dir - you need to create this
env.deploy_project_root = '/project/ForceLineProject'

def move():
	# move to the correct directory
	with cd('%s' % env.deploy_project_root):
		# pull latest code
		print('fetching updates from github')
		sudo('bash ./bash_deployer.sh')