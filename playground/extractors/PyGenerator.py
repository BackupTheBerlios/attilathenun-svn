
import os,re,time,md5,compiler
from copy import copy

class Section:
  def __init__(self,data=""):
    self.data = data
  
  def instantiate(self,parent,context_dict = None):
    return self.data

class StaticSection(Section):
  def __init__(self,data=""):
    Section.__init__(self,data=data)

class GenerativeSection(Section):
  def __init__(self,data=""):
    Section.__init__(self,data=data)

  def get_hash_key(self):
    """ Should return a code"""
    if self.is_linked_section():
       return "RIENDUTOUT"
    return str(hex(self.data.__hash__())[2:]) + " " 

  def __repr__(self):
    return "Generative section hash=%s" % self.get_hash_key()
  
  def is_linked_section(self):
    toto = re.search("key=(-*.* )",self.data)
    return toto != None

  def get_linked_key(self):
    toto = re.search("key=(-*.* )",self.data)
    if toto:
      return toto.groups()[0]
    else:
      print "WARNING: Rien trouvé dans %s" % self.data
    

  def instantiate(self,parent,context_dict = None):
    if context_dict == None: 
       context_dict = dict()
    if self.is_linked_section():
      result = ""
      result +=  parent.find_section(self.get_linked_key()).instantiate(parent,context_dict)
      return result
    else:
      out = Outputer()
      last_line = self.data.split('\n')[-1]
      code = compiler.compile(self.data,filename="In-template code", mode='exec')
      eval(code,locals(),context_dict)
      result = "[-key=%s\n%s\n%s-]" % (self.get_hash_key(),out,last_line) 
      return result


class Outputer:
  def __init__(self):
    self.data = ""

  def add(self,newdata):
    self.data += newdata

  def __append__(self,newdata):
    self.data += newdata

  def __repr__(self):
    return str(self.data)



class File:
  def __init__(self):
    self.sections = []
    self.tpl_sections = []
    self.begin_str = "[-"
    self.end_str="-]"

  def add_template_sections(self,sections):
    self.tpl_sections += sections

  def find_section(self,key):
    for s in self.tpl_sections:
     if hasattr(s,'get_hash_key'):
       if s.get_hash_key() == key:
        return s
    print "Did not find key=%s in %s" % (key,self.tpl_sections)

  def has_end_separator(self,line):
    if self.end_str in line:
      return True
    return False

  def has_begin_separator(self,line):
    if self.begin_str in line:
      return True
    return False

  def read_from_file(self,filename):
     """ here we fill all the sections with the file content"""
     fd = open(filename)
     data = ""
     line = fd.readline()
     while line:
        if self.has_begin_separator(line):
           #now it's a generative section
           #first finish the static section with the beginning 
           data += line.split(self.begin_str)[0]
           self.sections.append(StaticSection(data=data))
           line = line.split(self.begin_str)[1]
           #then create the new generative section and put data inside
           data = ""
           while not self.has_end_separator(line):
              data += line
              line=fd.readline()
           data += line.split(self.end_str)[0]
           self.sections.append(GenerativeSection(data=data))
           line = line.split(self.end_str)[1]
           data = ""
        data += line
        line=fd.readline()
     #print "nouvelles STatique #{%s}#" %  data
     self.sections.append(StaticSection(data=data))
     fd.close()
   
  
  def write_to_file(self,filename,context_dict=None):
      fd = open(filename,'w')
      for sec in self.sections:
        fd.write(sec.instantiate(self,context_dict = context_dict))
      fd.close()

  def add_sections(self,sec):
     self.sections += sec


if __name__=="__main__":
  template = File()
  template.read_from_file("templates/stupid_template")
  #template.write_to_file("templates/generated_stupid_template")
  generated = File()
  generated.read_from_file("templates/generated_stupid_template")
  generated.add_sections(template.sections)
  print "################# DEUXIEMME TEMPLATE ######################"
  generated.write_to_file("templates/generated_stupid_template_bis")
