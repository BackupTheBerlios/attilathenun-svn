from syck import *

""" a simple website metamodel, for educationnal concerns only 

"""

def get_info():
  return {'name':'SimpleWeb', 'description':'A simple website metamodel'}

def read_from_file(path):
   file = open(path,'r')
   obj = load(file.read())
   file.close()
   return obj


def save_to_file(model,path):
   file = open(path,'r')
   file.write(dump(model))
   file.close()


def create_empty_model():
   return WebSite()

from xml.dom import minidom 
class WebSite:
  def __init__(self):
   self.pages = []

class Page:
  def __init__(self):
   self.title = "Blank"
   self.sections = [] # reference to sections
   self.page_object  = None
   self.outputFile  = "default_output.html"

  def instantiate(self):
     pass


class Section:
  def __init__(self):
    pass



class TemplatePart(Section):
  def __init__(self):
    Section.__init__(self)
    self.template_file =""
    self.node_id =""
    self.domTree = None


  def load_template(self):
    self.domTree = minidom.parse(self.template_file)
    self.domTree = self.domTree.getElementById('truc')
    print self.domTree

  def instantiate(self,object):
     pass

if __name__=="__main__":
  print "starting"
  template = TemplatePart()
  template.template_file = "test.xml"
  template.node_id="truc"
  template.load_template()
