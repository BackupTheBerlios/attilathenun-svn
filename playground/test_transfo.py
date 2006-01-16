from metamodels import emof
from metamodels import KM3
from metamodels import PyTl
from Repository import *

import Browser


source_emof = Repository(metamodel=emof)
source_emof.read_from_file("./data/test.xmi")
#print source_emof.display_all()
#Browser.browse(KM3)

target_km3 = Repository(metamodel=KM3)
target_km3.create_empty_model()


transfo = Repository(metamodel=PyTl)
transfo.read_from_file("./transformations/Emof_2_KM3.py")

transfo.model[0].transform(source_emof,target_km3)
#Browser.browse(target_km3)

target_km3.save_to_file("./data/Emof_2_KM3.xmi")
