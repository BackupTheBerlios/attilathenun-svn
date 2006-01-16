from metamodels import emof
from metamodels import PyTl
from Repository import *

source_emof = Repository(metamodel=emof)
source_emof.read_from_file("./data/test.xmi")

transfo = Repository(metamodel=PyTl)
transfo.read_from_file("./transformations/Class2PythonSource.py")
transfo.model[0].transform(source_emof,"./output/")
