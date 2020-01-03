import sys, subprocess

def use_cmd(g):
	# global PARSER
	user = g.args
	if len(user) == 0 or len(user) > 1:
		print('use cmd wrong argss')
		sys.exit(1)


	if user[0] not in g.data.users_list:
		print('user does not exist. use add.')
		sys.exit(1)

	config_set_cmd = ["git", "config"]
	if g.glob:
		config_set_cmd.append('--global')

	subprocess.check_output(config_set_cmd + ["user.name", g.data.users_list[user[0]]['username']])
	subprocess.check_output(config_set_cmd + ["user.email", g.data.users_list[user[0]]['email']])

	g.data.current_user = user[0]

def dispatch_cmd(g):
	cmd_map = {
		'use': use_cmd
	}
	cmd_map[g.cmd](g)
