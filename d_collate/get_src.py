import os
import read_files

def _(path, namespace_depth):
    top = {'namespaces': {}, 'classes': {}}

    for root, dirs, files in os.walk(path):
        if (len(files) == 0):
            continue
        address = root.split(os.sep)
        class_name = address.pop()

        parent = top
        for namespace in address:
            if (namespace not in parent['namespaces']):
                parent['namespaces'][namespace] = {
                    'namespaces': {},
                    'classes': {}}
            parent = parent['namespaces'][namespace]
        class_string = read_files._(address, class_name, files, namespace_depth)
        parent['classes'][class_name] = class_string

    return top
