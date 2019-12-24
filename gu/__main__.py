from gu import gu
import argparse

parser = argparse.ArgumentParser(description='Configure git users')

parser.add_argument('cmd', nargs='*', help='starting ID to use as ballot ID')
parser.add_argument('-v', '--verbose', action='store_true', help='verbose printing')

args = parser.parse_args()

print(args.verbose)
print(args.cmd)
if __name__ == "__main__":
	gu.gu() # ga ga