from core import *
import loader
import dumper

def read_from_file(path):
   return loader.Loader().load(path)

def save_to_file(model,path):
   if model == None:
     model = Repository()
   dumper.Dumper().dump(model,path)

def create_empty_model():
   return Repository()
   

def get_info():
  return {'name':'emof'}
