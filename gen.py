import argparse


# FLAGS
DEBUG = True

# CONSTANTS


# FUNCTIONS
def dprint(text):
    if DEBUG:
        print "DEBUG:", text

parser = argparse.ArgumentParser()
subparser = parser.add_subparsers(dest="cmd")
p_new    = subparser.add_parser('new')
p_new .add_argument('--class','-c', dest='cl', help = "specify to create class header")
p_new .add_argument('--namespace','-n', dest='ns', help = "list of namespaces", nargs='+')
args = parser.parse_args()
dprint(args)

