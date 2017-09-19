import os
import process_file

def _(address, class_name, files, namespace_depth):
    methods = {}
    for filename in files:
        path = os.sep.join(address) + '/' + class_name + '/' + filename
        with open(path, 'r') as f:
            methods[filename] = process_file._(f.read())

    ret = 'namespace ' + '.'.join(address[namespace_depth:])
    ret += "\n{"

    if 'test' in class_name:
        ret += "\n    using NUnit.Framework;"
        ret += "\n"
        ret += "\n    [TestFixture]"
    ret += "\n    public class " + class_name
    ret += "\n    {"

    string_methods = []
    for name, body in methods.items():
        string_method = ''
        if 'test' in class_name:
            string_method += "\n        [Test]"
        string_method += '\n        '+ '\n        '.join(body)
        string_methods.append(string_method)
    ret += '\n'.join(string_methods) + '\n    }\n}'
    return ret
