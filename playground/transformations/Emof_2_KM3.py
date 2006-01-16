def source_metamodels():
  return ['emof']

def target_metamodels():
  return ['KM3']

def mappedObject(mm,element):
  return  mm.get_linkend("mappedTo",element)

def mapAttribute(mm1,element1,attr1,mm2,element2,attr2):
  #first get the elements concerned
  for i in mm1.get_all_of_kind(element1):
     #then get the list
     o = mm2.add_instance(element2)
     #now we should link i and o
     mm1.link("mappedTo",i,o)

def mapCollection(mm1,element1,col1,col2):
  #first get the elements concerned
  for i in mm1.get_all_of_kind(element1):
     #then get the list
     collection = i.__dict__[col1]
     destination = mappedObject(mm1,element1)
     print "on récupère la liste %s et la destination %s " % (collection,destination)
     for c in collection:
       #pour chaque element, on  récupère celui qui est déjà mappé et on l'ajoute dans la liste destination
       pass

def mapElement(mm1,element1,mm2,element2):
 #for each element1 from mm1, create an element2
 for i in mm1.get_all_of_kind(element1):
     o = mm2.add_instance(element2)
     #now we should link i and o
     mm1.link("mappedTo",i,o)
 


def from_mof_to_km3(emof,km3):
  mapElement(emof,"Class",km3,"Class")
  mapAttribute(emof,"Class","name",km3,"Class","name")
  mapAttribute(emof,"Class","bidule",km3,"Class","machin")

  mapElement(emof,"Package",km3,"Package")
  mapAttribute(emof,"Package","name",km3,"Package","name")
  mapAttribute(emof,"Class","bidule",km3,"Class","machin")
  mapCollection(emof,"Class","_superClass","superClass")
  #mapCollection(emof,"Class","subClasses")
  
from Browser import * 

def transform(source_model,target_model):
  repos2 = source_model.get_all_of_kind("Repository")[0]
  classe = source_model.get_all_of_kind("Package")
  print source_model.get_all_of_kind("Class")
  from_mof_to_km3(source_model,target_model)
  for i in source_model.get_all_of_kind("Class"):
     print "%s   <---->   %s" % (mappedObject(source_model,i),i)
 
  #browse(target_model.model)
  

