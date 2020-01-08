import sys, subprocess, json

def use_cmd(g):
	user = g.args
	if len(user) == 0 or len(user) > 1:
		print('use cmd wrong argss')
		sys.exit(1)


	if user[0] not in g.data.users:
		print('user does not exist. use add.')
		sys.exit(1)

	config_set_cmd = ['git', 'config']
	if g.glob:
		config_set_cmd.append('--global')

	subprocess.check_output(config_set_cmd + ['user.name', g.data.users[user[0]]['username']])
	subprocess.check_output(config_set_cmd + ['user.email', g.data.users[user[0]]['email']])

	g.data.current_user = user[0]
	g.write_configs()

def list_cmd(g):
	# can this be done better?
	print(subprocess.check_output(['git', 'config', '--list']).decode("utf-8").replace("\\n","\n"))

def ls_cmd(g):
	print(json.dumps(g.data.__dict__, sort_keys=True, indent=4))

def add_cmd(g):
	alias = input('Alias for user: ')
	username = input('Git username: ')
	email = input('Git email: ')
	switch = input('Switch to this user? (Y/N): ')
	
	if alias in g.data.users:
		print('\nAlias already exists')
	else:
		g.data.users[alias] = {
			'username': username,
			'email': email
		}

	# todo: combine with use user
	if switch.lower() == 'y':
		g.data.current_user = alias
		config_set_cmd = ['git', 'config']
		if g.glob:
			config_set_cmd.append('--global')

		subprocess.check_output(config_set_cmd + ['user.name', username])
		subprocess.check_output(config_set_cmd + ['user.email', email])
	g.write_configs()



def del_cmd(g):
	user = g.args
	if len(user) == 0 or len(user) > 1:
		print('del cmd wrong args')
		sys.exit(1)
	
	if user[0] == g.data.current_user:
		print('\nCannot delete the current user')
	elif user[0] not in g.data.users:
		print('\nUser does not exist')
	else:
		del g.data.users[user[0]]
		g.write_configs()


def dispatch_cmd(g):
	# todo: add flag support (i.e. --username user will bypass prompts) 
	cmd_map = {
		'use': use_cmd,
		'add': add_cmd,
		'list': list_cmd,
		'ls': ls_cmd,
		'rm': del_cmd,
	}
	cmd_map[g.cmd](g)
