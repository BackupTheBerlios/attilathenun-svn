#Metamodel management



"""
KM3 metamodel

Work in progress - 
TODO : 
	comments management
        Enumerations management

"""

from core import *
from km3_parsing import *

def get_info():
  return {'name':'KM3', 'description':'Kernel MetaMetaModel from the ATLAS Team'}

def save_to_file(model,path):
   file = open(path,'w')
   file.write(model.__write__())
   file.close()

def create_empty_model():
   return Metamodel()

def navigate(km3obj):
  """ a Model navigator should return the linked elements for a given one """
  result = []
  if isinstance(km3obj,Metamodel):
     result += km3obj.contents

  if isinstance(km3obj,Enumeration):
     result += km3obj.literals

  if isinstance(km3obj,Class):
     result += km3obj.supertypes
     result += km3obj.structuralFeatures

  if isinstance(km3obj,TypedElement):
     result += [km3obj.type]

  if isinstance(km3obj,StructuralFeature):
     result += [km3obj.owner]

  if isinstance(km3obj,Reference):
     if km3obj.opposite:
       result += [km3obj.opposite]

  if isinstance(km3obj,Package):
     result +=  km3obj.contents
     result += [km3obj.metamodel]

  return result





