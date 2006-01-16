from metamodels import emof
from metamodels import KM3
from metamodels import PyTl
from Repository import *

source_km3 = Repository(metamodel=KM3)
source_km3.read_from_file("./data/dot.km3")
source_km3.save_to_file("./data/dot-bis.km3")

#target_emof = Repository(metamodel=emof)
#target_emof.create_empty_model()

#transfo = Repository(metamodel=PyTl)
#transfo.read_from_file("./transformations/Class2Package-emof.py")
#transfo.model[0].transform(source_emof,target_emof)
#target_emof.save_to_file("./data/test2.xmi")
