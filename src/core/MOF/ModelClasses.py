# -*- coding: utf-8 -*-

##############################################################################
# Copyright 2005 Mikaël Barbero                                              #
# This file is part of Attila The Nun project.                               #
#                                                                            #
# Attila The Nun is free software; you can redistribute it and/or modify     #
# it under the terms of the GNU General Public License as published by       #
# the Free Software Foundation; either version 2 of the License, or          #
# (at your option) any later version.                                        #
#                                                                            #
# Foobar is distributed in the hope that it will be useful,                  #
# but WITHOUT ANY WARRANTY; without even the implied warranty of             #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the              #
# GNU General Public License for more details.                               #
#                                                                            #
# You should have received a copy of the GNU General Public License          #
# along with Foobar; if not, write to the Free Software                      #
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA #
##############################################################################

"""
The MOF provides a set of modeling elements, including the rules for 
their use, with which to construct models. Specifically, the MOF modeling 
elements support development of meta-models. This focus enables the MOF 
to provide a more domain-specific modeling environment for defining 
meta-models instead of a general-purpose modeling environment. 
"""

__revision__  = "$Revision$"
__date__      = "$Date$"
__authors__   = ["Mikaël Barbero <mikael@users.berlios.de>"]

class ModelElement:
	"""
	ModelElement classifies the elementary, atomic constructs of models. 
	ModelElement is the root Class within the MOF Model. 
	"""
	
	def __init__(self):
		# Attributes
		self._name = ""
		self._qualifiedName = []
		self._annotation = ""
		# References
		self._container = None
		self._requiredElement = None
		self._constraint = None
	
	def findRequiredElements(self, kinds, recursive):
		"""
		This operation selects a subset of the ModelElements that this one 
		depends on, based on their dependency categories. The "kinds" 
		argument gives the kinds of dependency of interest to the caller. 
		
		If the "recursive" argument is "false," the operation return the 
		direct dependents only. If it is "true," all dependents in the 
		transitive closure of DependsOn for the specified "kinds" are 
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
			depends on the ModelElement given by "otherElement." If it does, 
			the operation’s result is "true;" otherwise, it is "false." 
			
			If a dependency exists; that is, the result is "true," the operation 
			returns a String in "reason" that categorizes the dependency. 
 
			If the dependency is indirect, IndirectDep is returned. If there 
			are multiple dependencies, any category that applies may be 
			returned in "reason." If no dependencies exist, an empty string 
			is returned in "reason." 
			
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
		"""
		A setter method for the name attribute of this ModelElement. 
		
		return type: none
		parameters:
			name: in String
		"""
		if not self.isFrozen():
			self._name = name
		else:
			pass
	
	def name(self):
		"""
		Return the name of the current ModelElement.
		
		return type: String
		parameters:
			none
		"""
		return self._name
		
	def qualifiedName(self):
		"""
		Return a list of String values consisting of the names of the ModelElement, 
		its container, its container’s container and so on until a non-contained 
		element is reached. The first member of the list is the name of the non-contained 
		element. 

		return type: String (multiplicity one or more; ordered; non-unique)
		"""
		if (self._container != None):
			return self.container().qualifiedName().append(self._name) 
		else: 
			return [self._name] 

	
	def setAnnotation(self, annotation):
		"""
		A setter method for the annotation attribute of this ModelElement.
		
		return type: none
		parameters:
			annotation: in String
		"""
		if not self.isFrozen():
			self._annotation = annotation
		else:
			pass

	def annotation(self):
		"""
		Returns the annotation string of this ModelElement.
		
		return type: String
		parameters:
			none
		"""
		return self._annotation
	
	def container(self):
		"""
		Returns the upper-level container of this ModelElement. Returns None 
		if the current ModelElement is the top-level one.
		
		return type: ModelElement
		parameters:
			none
		"""
		return self._container
	
	def setContainer(self, newValue):
		"""
		Changes the current container of this ModelElement to the newValue.
		
		return type: none
		parameters:
			newValue: in ModelElement
		"""
		self._container = newValue
		
	def unsetContainer(self):
		"""
		Deletes the containment relationship of this ModelElement so that it becomes 
		a top-level ModelElement in the containment hierarchy.
		
		return type: none
		parameters:
			none
		"""
		self._container = None
		
	def constraints(self):
		"""
		Returns constraints set of this ModelElement.
		
		return type: Constraint (multiplicity zero or more; non-ordered; non-unique)
		parameters:
			none
		"""
		pass
	
	def setConstraints(self, newValue):
		"""
		Set constraints set of this ModelElement to newValue. It means that all previous 
		added constraints are removed.
		
		return type: none
		parameters: 
			newValue: in Constraint (multiplicity zero or more; non-ordered; non-unique)
		"""
		pass
	
	def addConstraints(self, newElement):
		"""
		Add a constraint in the constraints set of this ModelElement.
		
		return type: none
		parameters:
			newElement: in Constraint
		"""
		pass
		
	def modifyConstraints(self, oldElement, newElement):
		"""
		Change a previously added constraint in the constraints set of this ModelElement
		to a new one. The old one is discard.
		
		return type: none
		parameters:
			oldElement: in Constraint
			newElement: in Constraint
		"""
		pass
		
	def removeConstraints(self, oldElement):
		"""
		Remove a constraint previously added in this ModelElement's contraints set. 
		
		return type: none
		parameters:
			oldElement: in Constraint
		"""
		pass

class Namespace(ModelElement):
	"""
	The Namespace Class classifies and characterizes ModelElements that can contain 
	other ModelElements. Along with containing the ModelElements, a Namespace 
	defines a namespace, the allowable set of names and the naming constraints, for these 
	elements. 
	
	Subclasses of the Namespace Class have mechanisms for effectively extending their 
	namespace, without actually containing additional ModelElements. Thus Namespace 
	can be viewed in terms of its two roles, as a container and as a namespace mechanism. 
	Because only subclasses extend the namespace, the namespace and contents are 
	coincident in the definition of the Namespace Class. Each Namespace has four 
	collections (the latter three derivable) that are used in the MOF Model’s Constraints. 
	These collections are: 
	
	- The contents (also called the direct contents), which are defined by the contents 
	reference. 
	- All contents, the transitive closure on the contents reference. 
	- The extended namespace (the contents plus elements included by extension), which 
	Namespace subclasses accomplish through generalization and importation. 
	- The extended contents (the transitive closure on the contents reference applied to 
	the extended namespace). 
	"""
	
	def __init__(self):
		ModelElement.__init__(self)

		# References
		self._contents = None
	
	def lookupElement(self, name):
		"""
		Searches for an element contained by this Namespace whose name is precisely 
		equal (as a wide string) to the supplied name. The operation either returns a 
		ModelElement that satisfies the above, or raises the NameNotFound exception.
		
		return type: ModelElement 
		isQuery: yes 
		parameters: 
			name : in String 
		exceptions: NameNotFound 
		"""
		pass
		
	def resolveQualifiedName(self, qualifiedName):
		"""
		Searches for a ModelElement contained within this Namespace that is identified 
		by the supplied qualifiedName. The qualifiedName is interpreted as a "path" 
		starting from this Namespace. 
		
		return type: ModelElement (exactly one). If no element is found, 
			an exception is raised. 
		isQuery: yes 
		parameters: 
			qualifiedName : in String (multiplicity one or more; ordered; not unique) 
		exceptions: NameNotResolved 
		"""
		pass
		
	def findElementsByType(self, ofType, includeSubtypes):
		"""
		Returns a list of the ModelElements contained by this Namespace that match the 
		Class supplied. If ‘includeSubtypes’ is false, this operation returns only those 
		elements whose most-derived Class is ‘ofType’. If ‘includeSubtypes’ is true, the 
		operation also returns instances of subtypes of ‘ofType’. The order of the elements 
		in the returned list is the same as their order in the Namespace. 
		
		For example, "findElementsByType(ModelElement, false)" always returns an 
		empty list, since ModelElement is an abstract Class. On the other hand, 
		"findElementsByType(ModelElement, true)" always returns the contents of the 
		Namespace, since all their Classes are subtypes of ModelElement. 
		
		return type: ModelElement (multiplicity zero or more; ordered; unique)
		isQuery: yes 
		parameters: 
			ofType: in Class 
			includeSubtypes: in Boolean
		"""
		pass
		
	def nameIsValid(self, proposedName):
		"""
		Determines whether the proposedName can be used as the name for a new 
		member ModelElement in this Namespace. Specifically, it checks that the 
		Namespace uniqueness rules would still be satisfied after adding such a name. 
		return type: Boolean 
		isQuery: yes 
		parameters: 
			proposedName: in String 
		"""
		pass

class GeneralizableElement(Namespace):
	"""
	The GeneralizableElement Class classifies and characterizes ModelElements that can 
	be generalized through super typing and specialized through subtyping. A 
	GeneralizableElement inherits the features of each of its supertypes, the features of the 
	supertypes of the immediate supertypes, and so on (in other words all the features of 
	the transitive closure of all the super types of the GeneralizableElement). 

	When a GeneralizableElement inherits a feature, that feature name effectively becomes 
	part ofthe namespace for the GeneralizableElement and the feature is considered part 
	ofthe extended namespace of the Namespace. Therefore, a GeneralizableElement 
	cannot have a superclass if it causes an inherited feature to have a namespace collision 
	with its own features. 
	
	To the degree that a GeneralizableElement is defined by its features, thesuperclass / 
	subclass association defines substitutability. Any instance of a GeneralizableElement 
	can be supplied wherever an instance of a superclass of that GeneralizableElement is 
	expected.
	"""
	
	def __init__(self):
		Namespace.__init__(self)

		# Attributes
		self._isRoot = False
		self._isLeaf = False
		self._isAbstract = False
		self._visibility = "public"
		# References
		self._supertypes = None
	
	def allSuperTypes(self):
		"""
		Returns a list of direct and indirect supertypes of this GeneralizableElement. A 
		direct supertype is a GeneralizableElement that directly generalizes this one. An 
		indirect supertype is defined (recursively) as a supertype of some other direct or 
		indirect supertype of the GeneralizableElement. The order of the list elements is 
		determined by a depth-first traversal of the supertypes with duplicate elements 
		removed. 
		
		return type: GeneralizableElement (multiplicity zero or more, ordered, unique) 
		isQuery: yes 
		parameters: 
			none
		"""
		pass
		
	def lookupElementExtended(self, name):
		"""
		Returns an element whose name matches the supplied "name." Like the 
		"lookupElement" operation on Namespace, this operation searches the contents of 
		the GeneralizableElement. In addition, it tries to match the name in the contents of 
		all direct and indirect supertypes of the GeneralizableElement. For Packages, a 
		subclass of GeneralizableElement, the operation can also match a Namespace 
		associated with an Import objects. NameNotFound is raised if no element matches 
		the name. 

		return type: ModelElement (multiplicity exactly one) 
		isQuery: yes 
		parameters: 
			name: in wstring 
		exceptions: NameNotFound
		"""
		pass
		
	def findElementsByTypeExtended(self, ofType, includeSubtypes):
		"""
		Provides an extension of the findElementsByType defined for Namespace so that 
		contained elements of all superclasses (direct and indirect) of the 
		GeneralizableElement are included in the search. The order of the returned 
		elements is determined by the order of the elements contained in the 
		GeneralizableElements and a depth-first traversal of the superclasses. 
		
		Subclasses can include a larger overall area for the lookup. Package, a subclass of 
		GeneralizableElement, also considers the elements brought into this Namespace 
		through the use of Import. 

		return type: ModelElement (multiplicity zero or more; ordered; unique) 
		isQuery: yes 
		parameters: 
			ofType : in Class 
			includeSubtypes : in Boolean
		"""
		pass
	
class TypedElement(ModelElement):
	"""
	The TypedElement type is an abstraction of ModelElements that require a type as part 
	of their definition. A TypedElement does not itself define a type, but is associated with 
	a Classifier. 
	"""
	
	def __init__(self):
		ModelElement.__init__(self)
	
		# References
		self._type = None
		
	
class Classifier(GeneralizableElement):
	"""
	A classifier provides a classification of instances through a set of Features it contains.
	"""
	
	def __init__(self):
		GeneralizableElement.__init__(self)
	
		pass

class Class(Classifier):
	"""
	A Class defines a classification over a set of object instances by defining the state and 
	behavior they exhibit. This is represented through operations, attributes, references, 
	participation in associations, constants, and constraints. Similar concepts are used in 
	other environments for representing Classes and their implementations. However, in 
	the MOF the class characteristics are modeled in an implementation-independent 
	manner. For instance, an attribute of a Class is specified independently of any code to
	store and manage the attributes value. The implementation simply must insure that its 
	behavior conforms to behavior specified by the chosen technology mapping. The MOF 
	Class construct is more than just an interface specification.
	"""
	
	def __init__(self):
		Classifier.__init__(self)
	
		# Attributes
		self._isSingleton = False

class DataType(Classifier):
	"""
	DataType is the super class of the classes that represent MOF data types and data type 
	constructors as described in Section4.2, "MOFValues," on page 4-2. The DataType 
	class, its subclasses and related classes are depicted in Figure 3-4. 
	"""
	
	def __init__(self):
		Classifier.__init__(self)
	
		pass
		
class PrimitiveType(DataType):
	"""
	Instances of the PrimitiveType class are used to represent primitive data types in a 
	meta-model. The MOF has a small number of built-in primitive datatypes that maybe 
	freely used in any meta-model. These types are defined as instances of PrimitiveType 
	that are contained by the standard "PrimitiveTypes" package. Refer to Section3.10, 
	"The PrimitiveTypes Package," on page 3-114 for details of the PrimitiveTypes 
	package, and to Section 4.2, "MOFValues," on page 4-2 for more details on data type 
	semantics. 
	
	The MOF built-in primitive data types map to different concrete datatypes in the 
	context of each technology mapping. Each technology mapping is expected to support 
	all of the standard built-in primitive datatypes. 
	
	Note - A meta-model may contain PrimitiveType instances other than those defined in 
	the "PrimitiveTypes" package. These instances denote technology specific, vendor 
	specific or user defined primitive datatypes. They should not be used in technology 
	neutral meta-models.
	"""
	
	def __init__(self):
		DataType.__init__(self)
	
		pass

class CollectionType(DataType, TypedElement):
	"""
	The Collection Type class is a type constructor for MOF collection types. A collection 
	type is a data type whose values are finite collections of instances of some base type. 
	The base type for a collection datatype is given by the CollectionType instance’s 
	‘type’ value. The ‘multiplicity’ Attribute gives the collection type’s lower and upper 
	bounds, and its orderedness and uniqueness properties.
	"""
	
	def __init__(self):
		DataType.__init__(self)
		TypedElement.__init__(self)
	
		# Attributes
		self._multiplicity = None
		
class EnumerationType(DataType):
	"""
	The EnumerationType class is a type constructor for MOF enumeration types. An 
	enumeration type is a data type whose values are the elements of a finite set of 
	enumerators. The enumeration type is specified by defining an ordered set of 
	enumerator labels.
	"""

	def __init__(self):
		DataType.__init__(self)
	
		# Attributes
		self._labels = None

class AliasType(DataType, TypedElement):
	"""
	The AliasType class is a type constructor for MOF alias types. An alias type is a 
	subtype of some other MOF class or datatype, given by the ‘type’ value of the 
	AliasType instance; i.e., a subset of the values of the type given by its 'type'. This 
	subset is typically specified by attaching a Constraint to the AliasType instance. An 
	alias type may convey a different "meaning" to that of its base type.
	"""
	
	def __init__(self):
		DataType.__init__(self)
		TypedElement.__init__(self)
	
		pass

class StructureType(DataType):
	"""
	The StructureType class is a type constructor for MOF structure data types. A structure 
	type is a tuple type (i.e., a cartesian product) consisting of one or more fields. The 
	fields are defined by StructureField instances contained by the StructureType instance.
	"""
	
	def __init__(self):
		DataType.__init__(self)
	
		pass
	
class StructureField(TypedElement):
	"""
	The StructureField class is used to specifiy the fields of a StructureType instance.
	"""
	
	def __init__(self):
		TypedElement.__init__(self)
	
		pass
		
class Feature(ModelElement):
	"""
	A Feature defines a characteristic of the ModelElement that contains it. Specifically, 
	Classifiers are defined largely by a composition of Features.
	"""
	
	def __init__(self):
		ModelElement.__init__(self)
	
		# Attributes
		self._scope = None
		self._visibility = "public"
	
class StructuralFeature(Feature, TypedElement):
	"""
	A StructuralFeature defines a static characteristic of the ModelElement that contains it. 
	The attributes and references of a Class define structural properties, which provide for 
	the representation of the state of its instances.
	"""
	
	def __init__(self):
		Feature.__init__(self)
		TypedElement.__init__(self)
	
		# Attributes
		self._multiplicity = None
		self._isChangeable = True # which default value is the good one	
		
class Attribute(StructuralFeature):
	"""
	An Attribute (referred to as a MofAttribute in the mapped IDL) defines a 
	StructuralFeature that contains values for Classifiers or their instances.
	"""
	
	def __init__(self):
		StructuralFeature.__init__(self)
	
		# Attributes
		self._isDerived = True
		
class Reference(StructuralFeature):
	"""
	A Reference defines a Classifier's knowledge of, and access to, links and their 
	instances defined by an Association. Although a Reference derives much of its state 
	from a corresponding AssociationEnd, it provides additional information ; therefore, the 
	MOF cannot adequately represent some meta-models without this mechanism. The 
	inherited attributes defined in StructuralFeature (multiplicity and is_changeable) are 
	constrained to match the values of its corresponding AssociationEnd. However, it has 
	its own visibility, name, and annotation defined.
	
	Note - When creating a Reference, values for the inherited attributes of multiplicity 
	and is_changeable must be supplied. These must be the same as the corresponding 
	attributes on the AssociationEnd to which the Reference will subsequently be linked. 
	"""
	
	def __init__(self):
		StructuralFeature.__init__(self)
	
		# References
		self._exposedEnd = None
		self._referencedEnd = None


class BehavioralFeature(Feature, Namespace):
	"""
	A BehavioralFeature defines a dynamic characteristic of the ModelElement that 
	contains it. Because a BehavioralFeature is partially defined by the Parameters it 
	contains, it is both a Feature and a Namespace.
	"""
		
	def __init__(self):
		Feature.__init__(self)
		Namespace.__init__(self)
	
		pass
		
class Operation(BehavioralFeature):
	"""
	An Operation defines a dynamic feature that offers a service. The behavior of an 
	operation is activated through the invocation of the operation.
	"""
	
	def __init__(self):
		BehavioralFeature.__init__(self)
	
		# Attributes
		self._isQuerry = True
		# References
		self._exceptions = None
		
class Exception(BehavioralFeature):
	"""
	An Exception (referred to as a MofException in the mapped IDL) defines an error or 
	other abnormal condition. The Parameters of an Exception hold a record of an 
	occurrence of the exceptional condition.
	"""
	
	def __init__(self):
		BehavioralFeature.__init__(self)
	
		pass
		
class Association(Classifier):
	"""
	An association defines a classification over a set of links, through a relationship 
	between Classifiers. Each link which is an instance of the association denotes a 
	connection between object instances of the Classifiers of the Association. The MOF 
	restricts associations to binary, restricting each link to two participating objects. This 
	restriction also means that the association is defined between two Classifiers (which 
	may be the same Classifier). The name of the Association is considered directional if it
	provides a clearer or more accurate representation of the association when stated with 
	one participating class first rather than the other. For instance, Operation CanRaise 
	Exception is correct; Exception CanRaise Operation is incorrect. 

	An Association contains precisely two AssociationEnds, each of which has a Class as 
	its "type." A Class has knowledge of its participation in an Association if it contains a 
	Reference that is related to the Association’s Ends, as shown in Figure 3-6. The "type" 
	of a Reference must be the "type" of the AssociationEnd that is the Reference’s 
	"referencedEnd." The "type" of the Reference’s "exposedEnd" must be the Reference’s 
	containing Class, or a supertype of that Class.
	"""
	
	def __init__(self):
		Classifier.__init__(self)
	
		# Attributes
		self._isDerived = None # default boolean
		
class AssociationEnd(TypedElement):
	"""
	An association is composed of two AssociationEnds. Each AssociationEnd defines a 
	Classifier participant in the Association, the role it plays, and constraints on sets of the 
	Classifier instances participating. An instance of an AssociationEnd is a LinkEnd, 
	which defines a relationship between a link, in instance of an Association, and an 
	instance of the AssociationEnd's Classifier, provided in its type attribute.
	"""
	
	def __init__(self):
		TypedElement.__init__(self)
	
		self._isNavigable = True
		self._aggragation = None
		self._multiplicity = None
		self._isChangeable = None
		
	def otherEnd(self):
		"""
		Provides the other AssociationEnd (i.e., not this one) in the enclosing Association.
		return type: AssociationEnd 
		isQuery: yes 
		parameters: 
			none 
		"""
		pass
	
class Package(GeneralizableElement):
	"""
	A Package is a container for a collection of related ModelElements that form a logical 
	meta-model. Packages may be composed and related in the following ways: 
	- A Package can contain nested Packages via the Contains association. 
	- A Package can inherit from other Packages via the Generalizes association. 
	- A Package can import or cluster other Namespaces, including Packages via an 
		Import and the Aliases association.
	"""

	def __init__(self):
		GeneralizableElement.__init__(self)

class Import(ModelElement):
	"""
	An Import allows a Package to make use of ModelElements defined in some other 
	Namespace. An Import object is related to another Namespace via the Aliases 
	association. When a Package contains an Import object, it imports the associated 
	Namespace. This means that ModelElements defined within the imported Namespace 
	are visible in the importing Package. 

	An Import allows the visibility of the imported Package’s contained ModelElements to 
	be further restricted. An Import object represents either Package importing or Package 
	clustering, depending on the "isClustered" attribute.	
	"""	
	
	def __init__(self):
		ModelElement.__init__(self)
	
		# Attributes
		self._visibility = "public"
		self._isClustered = None
		# References
		self._importedNamespace = None
		
class Parameter(TypedElement):
	"""
	A parameter provides a means of communication with operations and other 
	BehavioralFeatures. A parameter passes or communicates values of its defined type.
	"""
	
	def __init__(self):
		TypedElement.__init__(self)
	
		# Attributes
		self._direction = None
		self.multiplicity = None
		
class Constraint(ModelElement):
	"""
	A Constraint defines a rule that restricts the state or behavior of one or more elements 
	in the meta-model. When a Constraint is attached to a ModelElement, the rule it 
	encodes applies to all relevant instances of the ModelElement in a model. 
	
	A Constraint rule, represented by the "expression" attribute, may be encoded in any 
	form. The "language" attribute may be used to denote the language and encoding 
	scheme used
	
	While some Constraints on a model may need to be treated as invariant, it is often 
	convenient for other Constraints to be relaxed, for instance while a model is being 
	edited. While, the "evaluationPolicy" attribute is used to represent these two cases, this 
	information is at best advisory, since the MOF specification does not currently state 
	how and when Constraints should be enforced. 

	Note - A Constraint cannot over-ride structural integrity rules defined by other parts of 
	a meta-model (e.g., multiplicity specifications) or the integrity rules defined by a 
	particular mapping of the meta-model to implementation technology.
	"""
	
	def __init__(self):
		ModelElement.__init__(self)
	
		# Attributes
		self._expression = ""
		self._language = ""
		self._evaluationPolicy = None
		# References
		self._constrainedElements = None
		
class Constant(TypedElement):
	"""
	Constant provides a mechanism for defining constant values for use in meta-models. 
	Constants are limited to values of types defined as PrimitiveType instances
	"""
	
	def __init__(self):
		TypedElement.__init__(self)
	
		# Attributes
		self._value = ""
		
class Tag(ModelElement):
	"""
	Tags provide a light-weight extension mechanism that allows mapping, vendor, and 
	even customer specific information to be added to, or associated with a meta-model. In 
	essence, Tags are arbitrary name / value pairs that can be attached to instances of most 
	ModelElements.
	
	A Tag has an attribute called "tagId" that denotes a category of meaning, and another 
	attribute called "values" that parameterizes that meaning. Each Tag is related to one or 
	more ModelElements by the AttachesTo Association. The Tag need not be contained 
	within the meta-model of the ModelElement it "tags." 
	
	The MOF specification does not generally define the values for the "tagId" or the 
	application specific categories of meaning that they denote. The exception to this is: 
		- Section 5.6, "Standard Tags for the IDL Mapping," on page 5-39 defines some Tags 
			that tailor the IDL produced by the IDLmapping. 
	
	Since "tagId" values are not standardized, there is a risk that different vendors or user 
	organizations will use the same values to denote different categories of meaning. If a 
	"tagId" value is used to mean different things, problems can arise when meta-models 
	using the value are exchanged. 
	
	To avoid such Tag collisions, it is recommended that "tagId" values should use the 
	following scheme based on Java package naming. Each value should start with a prefix 
	formed by reversing the Internet domain name of a "tagId" naming authority. This 
	should be followed by a locally unique component. For instance, this might be a 
	standard or product name followed by a name or names that denotes the meaning. Here 
	are some examples: 
  
  	"org.omg.mof.idl_prefix" 
	  "org.omg.mof.some_tag" 
	  "com.rational.rose.screen_position" 
	  "au.edu.dstc.elvin.event_type" 
	
	It is also recommended that "tagId" values should be spelled in all lower case using the 
	underscore ("_") character as a word separator. 

	Note - In defining new Tag categories, the meta-modeler should take account of the 
	fact that the MOF Model has no Reference for navigating from a ModelElement to its 
	attached Tags. This allows one to attach Tags to elements of a "frozen" meta-model. 
	On the other hand, it makes it harder for a "client" of the meta-model objects to find 
	the Tags for an element. One option is to require relevant Tags to be Contained by the 
	elements they AttachTo, or their parents.
	"""
	
	def __init__(self):
		ModelElement.__init__(self)
	
		# Attributes
		self._tagId = ""
		self._values = ""
		# References
		self._elements = None
		
