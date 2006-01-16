from metamodels import Publication
from metamodels import Book
from metamodels import KM3
from metamodels import PyTl
from Repository import *

mmm = KM3.read_from_file("data/Book2Publication/Book/Book.km3")
print KM3.navigate(mmm)


book = Repository(metamodel=Book)
livre = book.create_instance("Book")
livre.title = "titre du livre"
chap1 = book.create_instance("Chapter")
chap1.title = "titre du chap1"
chap1.nb_pages = 10
chap2 = book.create_instance("Chapter")
chap2.title = "titre du chap2"
chap2.nb_pages = 1
chap3 = book.create_instance("Chapter")
chap3.title = "titre du chap3"
chap3.nb_pages = 20
chap4 = book.create_instance("Chapter")
chap4.title = "titre du chap4"
chap4.nb_pages = 11
livre.chapters = [chap1,chap2,chap3,chap4]
book.model = livre


pub = Repository(metamodel=Publication)
transfo = Repository(metamodel=PyTl)
transfo.read_from_file("./transformations/Book2Publication.py")
transfo.model[0].transform(book,pub)
print pub.model[0]
