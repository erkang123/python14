# from lib import aa
# import importlib
# importlib.import_module('lib.aa')

mod = __import__('lib.aa')
print(mod)
instance = getattr(mod.aa,'C')
obj = instance()
print(obj.name)