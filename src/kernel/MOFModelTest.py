# -*- coding: utf-8 -*-

import MOFModel
import unittest

__version__ = "1.4"
__date__    = ""
__author__  = "Barbero Mikaël"

class ModelElementTestCase(unittest.TestCase):
	badTestSet = (MOFModel.ModelElement("elementName"),
	MOFModel.Namespace(),
	MOFModel.GeneralizableElement(),
	MOFModel.Classifier(),
	MOFModel.Package(),
	MOFModel.TypedElement()
	)

	goodTestSet = ()

	def testIsBad(self):
		for me in self.badTestSet:
			self.assertRaises(MOFModel.UncheckedConstraint, me.checkConstraints)
			
	def testIsGood(self):
		for me in self.goodTestSet:
			self.assertEqual(me.checkConstraints, True)
	

		
if __name__ == "__main__":
	unittest.main()   