# -*- coding: utf-8 -*-

"""
The MOF provides a set of modeling elements, including the rules for 
their use, with which to construct models. Specifically, the MOF modeling 
elements support development of meta-models. This focus enables the MOF 
to provide a more domain-specific modeling environment for defining 
meta-models instead of a general-purpose modeling environment. 
"""

__version__ = "1.4"
__date__    = ""
__author__  = "Barbero Mikaël"

class UncheckedConstraint(Exception): pass

class ModelElement:
	"""
	ModelElement classifies the elementary, atomic constructs of models. 
	ModelElement is the root Class within the MOF Model. 
	"""
	def __init__(self, name, annotation=""):
		# Attributes
		self._name = name
		self._qualifiedName = []
		self._annotation = annotation
		# References
		self._container = None
		self._requiredElement = None
		self._constraint = None
	
	def findRequiredElements(self, kinds, recursive):
		"""
		This operation selects a subset of the ModelElements that this one 
		depends on, based on their dependency categories. The “kinds” 
		argument gives the kinds of dependency of interest to the caller. 
		
		String constants for the standard dependency categories are given 
		in Section 3.8, “MOF Model Constants,” on page 3-82 and their 
		meanings are defined in Section 3.5.9, “DependsOn,” on page 3-75. 
		In this context, the AllDep pseudocategory (i.e., “all”) is 
		equivalent to passing all of the standard categories, and the 
		IndirectDep pseudo-category (i.e., “indirect”) is ignored. 
		
		If the “recursive” argument is “false,” the operation return the 
		direct dependents only. If it is “true,” all dependents in the 
		transitive closure of DependsOn for the specified “kinds” are 
		returned. 
		
		return type: ModelElement (multiplicity: zero or more; unordered, unique) 
		isQuery: yes 
		parameters: 
			kinds: in String (multiplicity: one or more; unordered; unique) 
			recursive: in Boolean 
		"""
		pass
		
	def isRequiredBecause(self, otherElement, reason):
		"""
		This operation performs two functions: 
			It checks whether this ModelElement directly or indirectly 
			depends on the ModelElement given by “otherElement.” If it does, 
			the operation’s result is “true;” otherwise, it is “false.” 
			
			If a dependency exists; that is, the result is “true,” the operation 
			returns a String in “reason” that categorizes the dependency. 
			String constants for the dependency kind categories are given 
			in Section 3.8, “MOF Model Constants,” on page 3-82 and their 
			meanings are defined in Section 3.5.9, “DependsOn,” on page 3-75. 
			If the dependency is indirect, IndirectDep is returned. If there 
			are multiple dependencies, any category that applies may be 
			returned in “reason.” If no dependencies exist, an empty string 
			is returned in “reason.” 
			
		return type: Boolean 
		isQuery: yes 
		parameters: 
			otherElement: in ModelElement 
			reason: out String 
		"""
		pass
		
	def isFrozen(self):
		"""
		Reports the freeze status of a ModelElement. A ModelElement, at 
		anyparticular time, is either frozen or not frozen. All ModelElements 
		of a published model are permanently frozen. 
		
		return type: Boolean 
		isQuery: yes 
		"""
		pass
		
	def isVisible(self, otherElement):
		"""
		Returns true. This operation is reserved for future use when the 
		MOF visibility rules have stabilized. Then it will determine whether
		the supplied otherElement is visible to this ModelElement. 
		
		return type: Boolean 
		isQuery: yes 
		parameters: 
			otherElement: in ModelElement 
		"""
		return True
		
	def setName(self, name):
		if not self.isFrozen():
			self._name = name
		else:
			raise UncheckedConstraint("The attribute values of a ModelElement which is frozen cannot be changed. [C-2]")
	
	def name(self):
		return self._name
		
	def qualifiedName(self):
		if (self._container != None):
			return self._container.qualifiedName().append(self._name) 
		else: 
			return [self._name] 

	
	def setAnnotation(self, annotation):
		if not self.isFrozen():
			self._annotation = annotation
		else :
			raise UncheckedConstraint("The attribute values of a ModelElement which is frozen cannot be changed. [C-2]")

	def annotation(self):
		return self._annotation
	
	def container(self):
		return self._container
	
	def setContainer(self, newValue):
		self._container = newValue
		
	def unsetContainer(self):
		self._container = None
		
	def constraints(self):
		pass
		
	def addConstraints(self, newElement):
		pass
		
	def modifyConstraints(self, oldElement, newElement):
		pass
		
	def removeConstraints(self, oldElement):
		pass

	def checkConstraints(self):
		if (self.__class__.__name__ != "Package"):
			if (self.container() == None):
				raise UncheckedConstraint("A ModelElement that is not a Package must have a container. [C-1]")
		

class Namespace(ModelElement):
	"""
	This is the base Class for all M3-level Classes that need to act as 
	containers in the MOF Model
	"""
	
	def __init__(self):
		pass
	
	def lookupElement(self):
		pass
	def resolveQualifyName(self):
		pass
	def findElementByType(self):
		pass
	def nameIsValid(self):
		pass

class GeneralizableElement(Namespace):
	"""
	This is the base Class for all M3-level Classes that support 
	"generalization" (i.e., inheritance)
	"""
	def __init__(self):
		self._isRoot = False
		self._isLeaf = False
		self._isAbstract = False
		self._visibility = "public"
	
	def allSuperTypes(self):
		pass
	def lookupElementExtended(self):
		pass
	def findElementsByTypeExtended(self):
		pass
	
class Classifier(GeneralizableElement):
	def __init__(self):
		pass

class Package(GeneralizableElement):
	def __init__(self):
		pass
	
class TypedElement:
	def __init__(self):
		pass
