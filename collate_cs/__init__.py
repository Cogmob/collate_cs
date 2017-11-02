import _
import sys

if len(sys.argv) < 4:
    print('usage:')
    print('collate before_path after_path depth')
    exit()

_._(sys.argv[1], sys.argv[2], int(sys.argv[3]))
