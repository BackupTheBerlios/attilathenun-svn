
def my_import(name):
    mod = __import__(name)
    components = name.split('.')
    for comp in components[1:]:
        mod = getattr(mod, comp)
    return mod


def read_from_file(path):
 path = path.replace('./','')
 path = path.replace('.py','')
 path = path.replace('/','.')
 return  my_import(path)

