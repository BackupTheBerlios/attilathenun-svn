
class ClassNotFound:
  pass


class Repository:
  def __init__(self,metamodel):
     self.model = []
     self.metamodel = metamodel
     self.tag2elements = {}
     self.element2tags = {}
     self.links = []

  def __add_to_dictlist(self,dictlist,key,item):
     if key in dictlist.keys():
        # then we should add the item in the list
        dictlist[key].append(item)
     else:
        #we should create the list
        dictlist[key] = [item]

  def __remove_to_dictlist(self,dictlist,key,item):
     if key in dictlist.keys():
        # then we should add the item in the list
        dictlist[key].remove(item)


  def get_class(self,name,object = None,already_done = []):
     """ return the class of the given name (looking in the metamodel)"""
     if not object : 
       object = self.metamodel
     if object in already_done : 
       return ClassNotFound
     for classe in  self.metamodel.__dict__.items():
        if name == "%s" % classe[0]:
            #print "trouvé %s en tant que %s" % (classe[0],classe[1])            
            return classe[1]
        #else: 
        #    print "pas bon : %s" % classe[0]
     already_done.append(object)
     #not found here
     for classe in  self.metamodel.__dict__.items():
         return  self.get_class(name,object = classe,already_done = already_done)
     print "class %s not found" % name
     return ClassNotFound
        

  def create_instance(self,name):
     """ create an instance of the "name" type and return it"""
     print "INFO : new %s" % name
     return self.get_class(name)()

  def add_instance(self,name):
     """ create an instance of the "name" type, add it into the repository and return it"""
     new = self.create_instance(name)
     self.model.append(new)
     return new


  def get_all_of_kind(self,name,current_object = None,already_done = None):
     """ return a list filled with all the instances of the model which class is or is subclassed from 'name' """
     #print "get_all_of_kind %s " % name
     resultat = []
     if already_done == None : already_done = []
     classe = self.get_class(name)
     if current_object in already_done:
       return []
     else:
       if current_object== None : current_object = self.model
       already_done.append(current_object)
       if issubclass(current_object.__class__,classe) or isinstance(current_object,classe) or current_object.__class__ == classe:
        resultat.append(current_object)
       else:
         pass
         #print "apas : %s != %s " % (classe,current_object.__class__)
       if hasattr(current_object,'__dict__'):
           for truc in current_object.__dict__.items():
             resultat += self.get_all_of_kind(name,current_object = truc,already_done = already_done)
       if isinstance(current_object,list):
           for truc in current_object:
             resultat += self.get_all_of_kind(name,current_object = truc,already_done = already_done)
       if isinstance(current_object,tuple):
           for truc in current_object:
             resultat += self.get_all_of_kind(name,current_object = truc,already_done = already_done)
     return resultat

  def display_all(self,current_object = None,already_done = [],depth = 0):
     """ return a list filled with all the instances of the model which class is or is subclassed from 'name' """
     #FIXME : infinite loops are possible
     if current_object in already_done:
       return
     else:
       if current_object== None : current_object = self.model
       already_done.append(current_object)
       print '-'*depth + '>' + str(current_object)
       if hasattr(current_object,'__dict__'):
           for truc in current_object.__dict__.items():
             self.display_all(current_object = truc,already_done = already_done,depth = depth + 1)
       if isinstance(current_object,list):
           for truc in current_object:
             self.display_all(current_object = truc,already_done = already_done,depth = depth + 1)
       if isinstance(current_object,tuple):
           for truc in current_object:
             self.display_all(current_object = truc,already_done = already_done,depth = depth + 1)
     
  def create_empty_model(self):
    self.model.append(self.metamodel.create_empty_model())

  def read_from_file(self,path):
    #here we could use scenarios for "auto-convert" stuffs
    self.model.append(self.metamodel.read_from_file(path))


  def save_to_file(self,path):
    #here we could use scenarios for "auto-convert" stuffs
    if len(self.model) != 0: 
       self.metamodel.save_to_file(self.model[0],path)
    else: 
       print "WARNING : nothing to save! "
       self.metamodel.save_to_file(None,path)
   
  # tags management

  def tag_element(self,tag_name,element):
    """ add a tag on this element."""
    self.__add_to_dictlist(self.element2tags,tag_name,element)
    self.__add_to_dictlist(self.tag2elements,element,tag_name)

  def untag_element(self,tag_name,element):
    """ remove a tag on this element."""
    pass

  def is_tagged(self,tag_name,element):
    """ return true if the element is tagged with this tag_name."""
    return (tag_name in self.tag2elements.keys()) and (element in self.tag2elements[tag_name])

  def get_all_tagged(self,tag_name):
    """ return a list with all the objects tagged with this tagname."""
    return self.tag2elements[tag_name]

  def get_tags(self,element):
    """ return a list with all the tags of this object."""
    if element in self.element2tags.keys():
      return self.element2tags[element]
    return []


  # link management
  def link(self,linkName,element1,element2):
    if id(element1) > id(element2):
     self.links.append((linkName,element1,element2))
    else:
     self.links.append((linkName,element2,element1))

  def get_linkend(self,linkName,element):
    for link in self.links:
       if linkName == link[0]:
         if element == link[1]:
           return link[2]
         if element == link[2]:
           return link[1]
    return None

