import os

def _(src, path):
    for name, namespace in src['namespaces'].items():
        _(namespace, path + os.sep + name)

    for name, body in src['classes'].items():
        if not os.path.exists(path):
            os.makedirs(path)

        with open(path + os.sep + name + '.csh', 'w') as f:
            f.write(body)
