
def get_info():
  return {'name':'Publication'}


class Publication:
  def __init__(self):
     title = ""
     nb_pages = 0
  def __str__(self):
     return "Publication - title : '%s' and nb pages='%s'" % (self.title,self.nb_pages)

