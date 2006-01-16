def source_metamodels():
  return ['emof']

def target_metamodels():
  return ['python']

from extractors.PyGenerator  import *
import os


def Class2PythonCode(source,target):
  for c in source.get_all_of_kind('Class'):
    filename = target + c.name + ".py"
    template = File()
    template.read_from_file('./templates/PythonClass.tpl')
    print "Generating code for class %s " % filename
    if not os.access(filename,os.W_OK):
      print "NEW"
      template.write_to_file(filename,{"theclass":c})
    generated = File()
    generated.read_from_file(filename)
    generated.add_template_sections(template.sections)
    generated.write_to_file(filename,{"theclass":c})

     
     


def transform(source_model,target_path):
   print "Generating to %s" % target_path
   Class2PythonCode(source_model,target_path)

