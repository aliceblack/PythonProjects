import sys

print ('Program and arguments:', str(sys.argv))
if len(sys.argv) > 1:
    if sys.argv[1] == 'debug':
        print('Starting in debug mode...')
