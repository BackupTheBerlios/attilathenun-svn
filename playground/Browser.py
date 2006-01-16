


from Tkinter import *
from editobj.treewidget import *
import os, os.path, sys, string, imp


def str_beautifull(thing):
   """ should return a nice view of the thing.."""
   origin = str(thing.__class__)
   origin = origin.split('.').pop()
   if isinstance(thing,list) or isinstance(thing,tuple):
     origin = "[...]"
   return origin

class BigNode(Node):
  def __init__(self, parent, model,name = ""):
    self.model = model
    self.name = name
    if self.name == "": self.name = str_beautifull(self.model)
    Node.__init__(self, parent)

  def __str__(self): return self.name
    
  def iseditable(self): return 0
  def isexpandable(self): 
    if hasattr(self.model,"__dict__"):
      return len(self.model.__dict__.items())
    if isinstance(self.model,list) or isinstance(self.model,tuple):
      return len(self.model)
    return 0

  def filter(self,obj):
    return True

  def createchildren(self, oldchildren = None):
    result = []
    if hasattr(self.model,"__dict__"):
      for o in self.model.__dict__.keys():
        if not o.startswith('_') :
         result.append(BigNode(self,self.model.__dict__[o],name=o))
    if isinstance(self.model,list) or isinstance(self.model,tuple):
      for o in self.model:
        result.append(BigNode(self,o))
    return result
 

def browse(my_obj):
   root = Tk()
   tree = Tree(root)
   tree.frame.pack(expand=1, fill="both")
   node = BigNode(tree,my_obj)
   root.mainloop()
