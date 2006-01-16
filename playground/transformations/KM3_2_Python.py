""" transform a KM3 to classical python classes """
def source_metamodels():
  return ['KM3']

def target_metamodels():
  return ['Python']

import imp

from new import classobj



class FromKM3Class(type):
     def __new__(cls, km3class):
         name = km3class.name
         bases = tuple()
         #for attr in km3class.structuralFeatures:
         #  pass
         dct = dict()
         return type.__new__(cls, name, bases, dct)

     def __init__(cls, km3class):
         name = km3class.name
         bases = tuple()
         dct = dict()
         cls.machin = km3class
         super(FromKM3Class, cls).__init__(name, bases, dct)

def Classe2Class(source,target):
  for c in source.get_all_of_kind('Class'):
    toto = classobj(c.name,tuple(),dict())
    print toto().machin



def transform(km3,py):
  #first create a python module
  for m in km3.get_all_of_kind('Package'):
    module = imp.new_module(m.name)
    #first create all dummy the classes
    for c in m.contents:
      #preparing attributes
      module.__setattr__(c.name,FromKM3Class(c))
      print module.Book.machin 
      aa = module.Book()
      bb = module.Book()
      aa.machin = c
      print aa.machin
      print bb.machin
    # then transform km3 classes to python classes
  
  # dont forget the classes attributes
  

  # then transform references to special lists
  pass
