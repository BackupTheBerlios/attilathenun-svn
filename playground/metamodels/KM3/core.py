
##Behavior classes ###

# Python seems limitated in one way : cardinalities and oppositeOf references. 
#      this base class use introspection to fill these requirements
#
#


class KM3Base:
  __metaclass__ = type
  def __init__(self):
     self._pv_oppositeOf = {} #this is filled with couples ("my attribute name" -> "the other class attribute name")
     self._pv_cardinalities = {} #this is filled with couples ("my attribute name" -> ("maxvalue","minvalue"))

  #this method is called each time somebody wants to define an attribute

  def __setattr__(self,attr,value):
     if attr.startswith('_pv_'):
       self.__dict__[attr] = value
     else:
       self.__dict__[attr] = value
 

## Structural classes ###
class LocatedElement(KM3Base):
  def __init__(self):
     KM3Base.__init__(self)
     self.location = ""

class ModelElement(LocatedElement):
  def __init__(self):
     LocatedElement.__init__(self)
     self.name = ""

class Classifier(ModelElement):
  def __init__(self):
     ModelElement.__init__(self)
     
class DataType(Classifier):
  def __init__(self):
     Classifier.__init__(self)

  def __repr__(self):
     return "DataType %s " % self.name

  def __write__(self):
     return "datatype %s" % self.name

class Enumeration(Classifier):
  def __init__(self):
     Classifier.__init__(self)
     self.literals = [] # list of EnumLiterals


class EnumLiteral(ModelElement):
  def __init__(self):
     ModelElement.__init__(self)
     self.enum = None  #this parent enumeration oposite of literals


class Class(Classifier):
  def __init__(self):
     Classifier.__init__(self)
     self.isAbstract  = False
     self.supertypes = [] # list of classes
     self.structuralFeatures =[] #list of structural features
  
  def __repr__(self):
     result =  "Class %s " % self.name
     if len(self.supertypes) > 0:
       result += " %s superclasses : " % len(self.supertypes)
       for super in self.supertypes:
           result += " %s" % super.name
     for p in self.structuralFeatures:
        result += "\n    %s" % p       
     return result

  def __write__(self):
     result = ""
     if self.isAbstract:result += " abstract "
     result += " class %s  " % self.name
     for super in self.supertypes:
       result += "extends %s " % super.name
     result += "\n  {\n"
     for p in self.structuralFeatures:
       result += "\n     %s" % p.__write__()
     result += "\n  }\n"
     return result

class TypedElement(ModelElement):
  def __init__(self):
     ModelElement.__init__(self)
     self.lower = 1
     self.higher = 1
     self.isOrdered = False
     self.isUnique = True
     self.type = None #reference vers un Classifier


class StructuralFeature(TypedElement):
  def __init__(self):
     TypedElement.__init__(self)
     self.owner = None #reference to  Class opposite of structuralfeatures

class Attribute(StructuralFeature):
  def __init__(self):
     StructuralFeature.__init__(self)

  def __repr__(self):
     result = "attribute %s : %s ;" % (self.name,self.type.name)
     return result
     
  def __write__(self):
     mult = ""
     if (self.lower,self.higher) != (1,1):
       if self.lower == self.higher == -1 :
           mult += "[*]"
       else:
           mult += "["
           if self.lower == -1:
              mult += "*"
           else:
              mult += str(self.lower)
           result += '-'
           if self.higher == -1:
              mult += "*"
           else:
              mult += str(self.higher)
           mult += "]"
     result = "attribute %s%s : %s ;" % (self.name,mult,self.type.name)
     return result

class Reference(StructuralFeature):
  def __init__(self):
     StructuralFeature.__init__(self)
     self.isContainer = False
     self.opposite = None #reference to Reference [0-1]


  def __repr__(self):
     #result = "Reference %s : %s" % (self.name,self.type.name)
     result = "reference %s " % self.name
     if self.isOrdered:
       result += " ordered "
     if self.isContainer:
       result += " container "
     result += ": %s " % self.type.name
     if self.opposite:
       result += " oppositeOf %s " % self.opposite.name
     result += ';'
     return result

  def __write__(self):
     result = "reference %s" % self.name
     # now we should check multiplicity
     if (self.lower,self.higher) != (1,1):
       if self.lower == self.higher == -1 :
           result += "[*]"
       else:
           result += "["
           if self.lower == -1:
              result += "*"
           else:
              result += str(self.lower)
           result += '-'
           if self.higher == -1:
              result += "*"
           else:
              result += str(self.higher)
           result += "]"
     if self.isOrdered:
       result += " ordered "
     if self.isContainer:
       result += " container "
     result += ": %s " % self.type.name
     if self.opposite:
       result += " oppositeOf %s " % self.opposite.name
     result += ';'
     return result

class Package(ModelElement):
  def __init__(self):
     ModelElement.__init__(self)
     self.contents = [] # reference to ModelElement opposite of package
     self.metamodel = None # reference to a MetaModel opposite of content

  def __repr__(self):
     result = "Package with %s classifiers" % len(self.contents)
     for p in self.contents:
       result += "\n      + %s" % str(p)
     return result

  def __write__(self):
     result = "package %s { " % self.name
     for p in self.contents:
       result += "\n%s" % p.__write__()
     result += "\n}"
     return result


class Metamodel(LocatedElement):
  def __init__(self):
     LocatedElement.__init__(self)
     self.contents = [] # reference to Packages opposite of metamodel

  def __repr__(self):
     result = "Metamodel with %s packages" % len(self.contents)
     for p in self.contents:
       result += "\n   + %s" % str(p)
     return result
     
  def __write__(self):
     result = ""
     for p in self.contents:
       result += "\n%s\n" % p.__write__()
     return result

    

