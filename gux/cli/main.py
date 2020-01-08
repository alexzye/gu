from .gux import gux
import argparse

parser = argparse.ArgumentParser(description='Configure git users')

parser.add_argument('cmd', nargs='*', help='starting ID to use as ballot ID')
parser.add_argument('-g', '--global', action='store_true', help='applies setting globally', dest='glob')

def main():
	gux(parser)