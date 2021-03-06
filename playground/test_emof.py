from metamodels import emof
from metamodels import PyTl
from Repository import *

source_emof = Repository(metamodel=emof)
source_emof.read_from_file("./data/test.xmi")


target_emof = Repository(metamodel=emof)
target_emof.create_empty_model()

transfo = Repository(metamodel=PyTl)
transfo.read_from_file("./transformations/Class2Package-emof.py")
transfo.model[0].transform(source_emof,target_emof)
target_emof.save_to_file("./data/test2.xmi")
