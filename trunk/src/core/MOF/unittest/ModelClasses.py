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

import MOFModel
import unittest

"""
Module Doc String
"""

__revision__  = "$Revision$"
__date__      = "$Date$"
__authors__   = ["Mikaël Barbero <mikael@users.berlios.de>"]

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
