from gu import gu
import argparse

# class FooAction(argparse.Action):
# 	def __init__(self, option_strings, dest, nargs=None, **kwargs):
# 	if nargs is not None:
# 	raise ValueError("nargs not allowed")
# 	super(FooAction, self).__init__(option_strings, dest, **kwargs)
# 	def __call__(self, parser, namespace, values, option_string=None):
# 	print('%r %r %r' % (namespace, values, option_string))
# 	setattr(namespace, self.dest, values)


parser = argparse.ArgumentParser(description='Configure git users')

parser.add_argument('cmd', nargs='*', help='starting ID to use as ballot ID')
parser.add_argument('-v', '--verbose', action='store_true', help='verbose printing')

args = parser.parse_args()

print(args.verbose)
print(args.cmd)
if __name__ == "__main__":
	gu.gu() # ga ga