import argparse





parser = argparse.ArgumentParser(description='My example explanation')
parser.add_argument('--my_optional',type=int,default=2,help='provide an integer (default: 2)')
my_namespace = parser.parse_args()

print(my_namespace.my_optional)