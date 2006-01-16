
# needed for checking sources and destinations, and for auto-converts
def source_metamodels():
  return ['Book']

def target_metamodels():
  return ['Publication']



def getNbPages(book):
  sum = 0
  for c in book.chapters:
     sum += c.nb_pages
  return sum

def book2publication(source,target):
  for b in source.get_all_of_kind('Book'):
    pub = target.add_instance('Publication')
    pub.title = b.title
    pub.nb_pages = getNbPages(b)
      

def transform(source_model,target_model):
  book2publication(source_model,target_model)
