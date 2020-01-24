from .gux import gux
import argparse

parser = argparse.ArgumentParser(description='Git user switcher')

parser.add_argument('cmd', nargs='*', help="use [user], add, list, ls, rm [user]")
parser.add_argument('-g', '--global', action='store_true', help='applies setting globally', dest='glob')

def main():
	gux(parser)