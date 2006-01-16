from dparser import Parser
from core import *
import sys, StringIO


all_objects = []

def d_km3(t,s):
  ' km3 : package*'
  result = Metamodel()
  for pack in (t[0]):
   if pack:
     pack.metamodel = result
     result.contents.append(pack)
  all_objects.append(result)
  return result

def d_package(t,s):
  ' package :  "package" name "{"  types_decl* class* comment*"}"'
  result = Package()
  result.name = t[1]
  for a_class in (t[3] + t[4] + t[5]):
     if a_class:
       result.contents.append(a_class)
       a_class.owner = result
  all_objects.append(result)
  return result

def d_types_decl(t,s):
  """types_decl : 'datatype' name ';'"""
  result = DataType()
  result.name = t[1]
  all_objects.append(result)
  return result

def d_name(t,s):
  """ name : "[a-zA-Z]+([0-9a-zA-Z_])*"  | quotedname"""
  return t[0]

def d_anything(t,s):
  """ anything : "[a-zA-Z]*([0-9a-zA-Z|_()!.])*.*" """
  return t[0]

def d_quotedname(t,s):
  """ quotedname : '"' name '"' """
  return t[1]

def d_class(t,s):
  """ class : 'abstract'* 'class' name superclasses* '{' class_content* '}'"""
  result = Class()
  result.name = t[2]
  result.supertypes = t[3]#FIXME : resolve the names -done
  result.structuralFeatures = [ x for x in t[5] if x != None ] # to remove comments
  for attr in result.structuralFeatures:
    attr.owner = result
  if len(t[0]) > 0:
   result.isAbstract = True 
  all_objects.append(result)
  return result

def d_superclasses(t,s):
  """ superclasses : 'extends' name* """
  return t[1]

def d_number(t):
    ' number : "[0-9]+" '            # match a positive integer
    return int(t[0])             # turn the matched string into an intege

def d_comment(t,s):
  """ comment : '--' anything* """
  return t[1]
 
def d_class_content(t,s):
  """ class_content : attribute | reference | comment """
  result = None
  if t[0]:result =  t[0]
  if len(t) > 1 and  t[1]:result = t[1]
  #if len(t) > 2  and t[2]:result = t[2]
  if isinstance(result,list): return None
  all_objects.append(result)
  return result

def d_attribute(t,s):
   """ attribute : 'attribute' name  multiplicity*  ':' name  ';'"""
   result = Attribute() #FIXME : use multiplicity
   result.name = t[1]
   result.type = t[4]
   return result

def d_number(t):
    ' number : "[0-9*]+" '            # match a positive integer
    if t[0] == "*": return -1 
    return int(t[0])  

def d_bimultiplicity(t,s):
  """ bimult : '[' number '-' number ']' """
  return ( t[1] , t[3] )

def d_monomultiplicity(t,s):
  """ monomult : '[' number ']'"""
  return ( 0 , t[1] )

def d_infini(t,s):
  """ infini : '[' '*' ']' """
  return ( -1 , -1 )
  

def d_multiplicity(t,s):
   """ multiplicity :  bimult | monomult | infini """
   return t[0]

def d_reference(t,s):
   """ reference : 'reference' name multiplicity* ordered* container* ':' name opposite*   ';' """
   result = Reference()
   result.name = t[1]
   if len(t[7]) > 0:
     result.opposite = t[7][0]#FIXME : resolve the names  - done
   result.type = t[6]#FIXME : resolve the names - done
   #now multiplicity
   if len(t[2]) > 0:
     result.lower = t[2][0][0]
     result.higher = t[2][0][1]
     result.isContainer = True
   if len(t[3]) > 0:
     result.isOrdered = True
   return result

def d_opposite(t,s):
   """ opposite : 'oppositeOf' name """
   return t[1]

def d_ordered(t,s):
   """ ordered : 'ordered' """
   return True

def d_container(t,s):
   """ container : 'container' """
   return True

#def read_from_file(self,path):
#  pass

class  KM3Class(type):
     def __new__(cls , km3class):
        name = km3class.name
        bases = tuple([Class])
        dct = dict()
        dct = {"machin":None}
        return type.__new__(cls, name, bases, dct)

     def __init__(cls, km3class):
        name = km3class.name
        bases = tuple([Class])
        dct = {"machin":None}
        super(KM3Class, cls).__init__(name, bases, dct)

classes_done = dict()

def from_km3_to_python(model):
   #first create classes for all the "no superclasses classes"
   for klass in all_objects:
      if klass.__class__ == Class and klass.supertypes == []:
        classes_done[klass.name] = KM3Class(klass)
        print classes_done[klass.name].machin
   #then iterate in the list as long as something is inside.
   # choose a new class to instantiate if all the superclasses are already dones
   return model


def read_from_file(path):
  print "Parsing %s" % path
  metamodel = Parser().parse(open(path,'r').read())
  #resolving lazy references
  for obj in all_objects:
   if obj.__class__ == Class:
     #we should create links to superclasses
     old = obj.supertypes
     obj.supertypes = []
     for name in old:
       for obis in all_objects:
        if hasattr(obis,'name') and obis.name == name[0]:
          obj.supertypes.append(obis)
        #else:
        #  if hasattr(obis,'name'): print "%s != %s" %(obis.name,name[0])
   if obj.__class__ == Reference or obj.__class__ == Attribute:
     #we should create links to associated classes
     name = obj.type
     for obis in all_objects:
        if hasattr(obis,'name') and obis.name == name:
          obj.type = obis
        #else:
        #  if hasattr(obis,'name'): print "%s != %s" %(obis.name,name)
   if obj.__class__ == Reference:
     name = obj.opposite
     for obis in all_objects:
        if hasattr(obis,'name') and obis.name == name:
          obj.opposite = obis
  return from_km3_to_python(metamodel)

if __name__=="__main__":
  print read_from_file(sys.argv[1])

