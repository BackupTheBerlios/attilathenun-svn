from metamodels import KM3
from metamodels import Python
from metamodels import PyTl
from Repository import *

source_km3 = Repository(KM3)
source_km3.read_from_file("data/Book2Publication/Book/Book.km3")

transfo = Repository(metamodel=PyTl)
transfo.read_from_file("./transformations/KM3_2_Python.py")

target_py = Repository(metamodel=Python)
target_py.create_empty_model()

transfo.model[0].transform(source_km3,target_py)
