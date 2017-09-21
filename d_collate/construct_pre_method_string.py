def _(methods, address, class_name):
    ret = ''

    if 'using.cs' in methods:
        ret += '\n'.join(methods['using.cs']) + '\n\n'
        del(methods['using.cs'])

    ret += 'namespace ' + '.'.join(address) + '\n{'
    if 'test' in class_name:
        ret += "\n    using NUnit.Framework;"
        ret += "\n"
        ret += "\n    [TestFixture]"
    ret += "\n    [Serializable]"


    if '_.cs' in methods:
        ret += '\n    ' + '\n    '.join(methods['_.cs'][:-1]) + '\n'
        del(methods['_.cs'])
    else:
        ret += "\n    public class " + class_name
        ret += "\n    {"

    return ret
