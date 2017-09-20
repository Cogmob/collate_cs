import os
import get_src
import write_src

before_path = 'before'
after_path = 'after'
namespace_depth = 1

def _(before_path, after_path, namespace_depth):
    src = get_src._(before_path, namespace_depth)
    write_src._(src, after_path, namespace_depth)

_(before_path, after_path, namespace_depth)
