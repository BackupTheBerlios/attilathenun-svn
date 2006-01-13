# -*- coding: utf-8 -*-

##############################################################################
# Copyright 2005, 2006 Attila The Nun Project                                #
# This file is part of Attila The Nun project.                               #
#                                                                            #
# Attila The Nun is free software; you can redistribute it and/or modify     #
# it under the terms of the GNU General Public License as published by       #
# the Free Software Foundation; either version 2 of the License, or          #
# (at your option) any later version.                                        #
#                                                                            #
# Attila The Nun is distributed in the hope that it will be useful,          #
# but WITHOUT ANY WARRANTY; without even the implied warranty of             #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the              #
# GNU General Public License for more details.                               #
#                                                                            #
# You should have received a copy of the GNU General Public License          #
# along with Attila The Nun; if not, write to the Free Software              #
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA #
##############################################################################

"""
This module contains all classes which refers to Ecore models elements.
"""

__revision__  = "$Revision$"
__date__      = "$Date$"
__authors__   = ["Mikaël Barbero <mikael@users.berlios.de>"]

class EObject:
	"""
	A representation of the model object 'EObject'.
		
	EObject is the root of all modeled objects so all the method names start 
	with "e" to distinguish the EMF methods from the client methods. It provides 
	support for the behaviors and features common to all modeled objects.
	"""
	
	def __init__(self):
		pass
		
	def eAllContent(self):
		pass
		
	def eClass(self):
		pass
		
	def eContainer(self):
		pass
		
	def eContainingFeature(self):
		pass
		
	def eContainmentFeature(self):
		pass
		
	def eContents(self):
		pass
	
	def eCrossReferences(self):
		pass
		
	def eGet(self, feature, resolve=True):
		pass
		
	def eIsProxy(self):
		pass
		
	def eIsSet(sefl, feature):
		pass
		
	def eResource(self):
		pass
		
	def eSet(self, feature, newValue):
		pass
		
	def eUnset(self, feature):
		pass
	
class EModelElement(EObject):
	def __init__(self):
		pass
		
	def getEAnnotations(source=""):	
		pass
	
class EFactory(EModelElement):
	def __init__(self):
		pass
		
	def convertToString(self, eDataType, instanceValue):
		pass
	
	def create(self, eClass):
		pass
		
	def createFromString(self, eDataType, literalValue):
		pass
		
	def getEPackage(self):
		pass
		
	def setEPackage(self, value):
		pass
	
class ENamedElement(EModelElement):
	def __init__(self):
		pass
		
	def getName(self):
		pass
		
	def setName(self, value):
		pass
	
class EAnnotation(EModelElement):
	def __init__(self):
		pass
		
	def getContents(self):
		pass
		
	def getDetails(self):
		pass
		
	def getEModelElement(self):
		pass
		
	def getReferences(self):
		pass
		
	def getSource(self):
		pass
		
	def setEModelElement(self, value):
		pass
		
	def setSource(self, value):
		pass
	
class EPackage(ENamedElement):
	def __init__(self):
		pass
	
class EClassifier(ENamedElement):
	def __init__(self):
		pass
	
class EEnumLiteral(ENamedElement):
	def __init__(self):
		pass
	
class ETypedElement(ENamedElement):
	def __init__(self):
		pass
	
class EClass(EClassifier):
	def __init__(self):
		pass
	
class EDataType(EClassifier):
	def __init__(self):
		pass
	
class EStructuralFeature(ETypedElement):
	def __init__(self):
		pass
	
class EOperation(ETypedElement):
	def __init__(self):
		pass
	
class EParameter(ETypedElement):
	def __init__(self):
		pass
	
class EEnum(EDataType):
	def __init__(self):
		pass
	
class EAttribute(EStructuralFeature):
	def __init__(self):
		pass
	
class EReference(EStructuralFeature):
	def __init__(self):
		pass