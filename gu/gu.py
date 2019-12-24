import os, json, subprocess

CONFIG_FILE_NAME = '.gu_config'

class Configs:
	def __init__(self, current_user, users_list):
		self.current_user = current_user
		self.users_list = users_list

def object_decoder(obj):
    if '__type__' in obj and obj['__type__'] == 'Configs':
        return Configs(obj['current_user'], obj['users_list'])
    return obj

def write_configs(c, config_file):
	config_dict = c.__dict__
	config_dict['__type__'] = 'Configs'
	json_string = json.dumps(config_dict)

	with open(config_file, "w+") as f:
		f.write(json_string)


def open_configs():
	'''open_configs opens and returns a confguration file. creates a new file if one doesnt exist'''
	try:
		config_file = os.path.join(os.environ['DEV_CONFIG_DIR'], CONFIG_FILE_NAME)
	except KeyError:
		config_file = os.path.join(os.path.expanduser('~'), CONFIG_FILE_NAME)
	except:
		print("failed to get environ var")
		sys.exit(1)

	if not os.path.exists(config_file):
		write_configs(Configs("", {}), config_file)
		
	with open(config_file) as json_file:
		data = json.load(json_file, object_hook=object_decoder)

	return data

def switch_users(configs):
	output = subprocess.check_output(["git", "config", "--global", "user.name"])
	print(output)

def gu():
	configs = open_configs()
	
	switch_users(configs)
