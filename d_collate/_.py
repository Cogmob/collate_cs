import os
import sys
import get_src
import write_src

if len(sys.argv) < 3:
    print('usage:')
    print('collate before_path after_path depth')
    exit()

def _(before_path, after_path, namespace_depth):
    src = get_src._(before_path, namespace_depth)
    write_src._(src, after_path, namespace_depth)

_(sys.argv[0], sys.argv[1], sys.argv[2])
