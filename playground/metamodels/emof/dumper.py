#
# dumper.py
#
# generated by pyemof v0.7.0 on [Fri Sep 16 13:40:03 2005] 
#
# Copyright (C) 2003, 2004, 2005 Raphael Marvie 
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA
# 02111-1307, USA.
# http://www.fsf.org/licensing/licenses/gpl.html
#
# Author contact: raphael.marvie@lifl.fr
#

from xml.dom import minidom

import core 

class DumpElement (object):
    def __init__ (self, doc):
        super(DumpElement, self).__init__()
        self._doc = doc
    def process(self, obj, elt):
        elt.setAttributeNS('xmi', 'xmi:id', obj._xmi_id)
    def __call__(self, obj, nodename):
        elt = self._doc.createElement(nodename)
        self.process(obj, elt)
        return elt


class Element (DumpElement):

    def __init__(self, doc):
        super(Element, self).__init__(doc)

    def process(self, obj, elt):
        super(Element, self).process(obj, elt)
        if elt.nodeName == 'emof:Element':
            elt.removeAttributeNS('xsi', 'type')
        else:
            elt.setAttributeNS('xsi', 'xsi:type', 'emof:Element')


class Object (Element):

    def __init__(self, doc):
        super(Object, self).__init__(doc)

    def process(self, obj, elt):
        super(Object, self).process(obj, elt)
        if elt.nodeName == 'emof:Object':
            elt.removeAttributeNS('xsi', 'type')
        else:
            elt.setAttributeNS('xsi', 'xsi:type', 'emof:Object')


class NamedElement (Object):

    def __init__(self, doc):
        super(NamedElement, self).__init__(doc)

    def process(self, obj, elt):
        super(NamedElement, self).process(obj, elt)
        if elt.nodeName == 'emof:NamedElement':
            elt.removeAttributeNS('xsi', 'type')
        else:
            elt.setAttributeNS('xsi', 'xsi:type', 'emof:NamedElement')
        if obj.name:
            elt.setAttributeNS(None, 'name', str(obj.name))


class Tag (Object):

    def __init__(self, doc):
        super(Tag, self).__init__(doc)

    def process(self, obj, elt):
        super(Tag, self).process(obj, elt)
        if elt.nodeName == 'emof:Tag':
            elt.removeAttributeNS('xsi', 'type')
        else:
            elt.setAttributeNS('xsi', 'xsi:type', 'emof:Tag')
        if obj.name:
            elt.setAttributeNS(None, 'name', str(obj.name))
        if obj.value:
            elt.setAttributeNS(None, 'value', str(obj.value))
        for o in obj.element:
            child = self._doc.createElement('element')
            value = self._doc.createTextNode(o._xmi_id)
            child.appendChild(value)
            elt.appendChild(child)


class Package (NamedElement):

    def __init__(self, doc):
        super(Package, self).__init__(doc)

    def process(self, obj, elt):
        super(Package, self).process(obj, elt)
        if elt.nodeName == 'emof:Package':
            elt.removeAttributeNS('xsi', 'type')
        else:
            elt.setAttributeNS('xsi', 'xsi:type', 'emof:Package')
        if obj.uri:
            elt.setAttributeNS(None, 'uri', str(obj.uri))
        for o in obj.nestedPackage:
            clss = dumpers[type(o)]
            child = clss(self._doc)(o, 'nestedPackage')
            elt.appendChild(child)
        if obj.nestingPackage:
            elt.setAttributeNS(None, 'nestingPackage', obj.nestingPackage._xmi_id)
        for o in obj.ownedType:
            clss = dumpers[type(o)]
            child = clss(self._doc)(o, 'ownedType')
            elt.appendChild(child)


class TypedElement (NamedElement):

    def __init__(self, doc):
        super(TypedElement, self).__init__(doc)

    def process(self, obj, elt):
        super(TypedElement, self).process(obj, elt)
        if elt.nodeName == 'emof:TypedElement':
            elt.removeAttributeNS('xsi', 'type')
        else:
            elt.setAttributeNS('xsi', 'xsi:type', 'emof:TypedElement')
        if obj.type:
            elt.setAttributeNS(None, 'type', obj.type._xmi_id)


class EnumerationLiteral (NamedElement):

    def __init__(self, doc):
        super(EnumerationLiteral, self).__init__(doc)

    def process(self, obj, elt):
        super(EnumerationLiteral, self).process(obj, elt)
        if elt.nodeName == 'emof:EnumerationLiteral':
            elt.removeAttributeNS('xsi', 'type')
        else:
            elt.setAttributeNS('xsi', 'xsi:type', 'emof:EnumerationLiteral')
        if obj.enumeration:
            elt.setAttributeNS(None, 'enumeration', obj.enumeration._xmi_id)


class Type (NamedElement):

    def __init__(self, doc):
        super(Type, self).__init__(doc)

    def process(self, obj, elt):
        super(Type, self).process(obj, elt)
        if elt.nodeName == 'emof:Type':
            elt.removeAttributeNS('xsi', 'type')
        else:
            elt.setAttributeNS('xsi', 'xsi:type', 'emof:Type')


class MultiplicityElement (TypedElement):

    def __init__(self, doc):
        super(MultiplicityElement, self).__init__(doc)

    def process(self, obj, elt):
        super(MultiplicityElement, self).process(obj, elt)
        if elt.nodeName == 'emof:MultiplicityElement':
            elt.removeAttributeNS('xsi', 'type')
        else:
            elt.setAttributeNS('xsi', 'xsi:type', 'emof:MultiplicityElement')
        if obj.isOrdered:
            elt.setAttributeNS(None, 'isOrdered', str(obj.isOrdered))
        if obj.isUnique:
            elt.setAttributeNS(None, 'isUnique', str(obj.isUnique))
        if obj.lower:
            elt.setAttributeNS(None, 'lower', str(obj.lower))
        if obj.upper:
            elt.setAttributeNS(None, 'upper', str(obj.upper))


class DataType (Type):

    def __init__(self, doc):
        super(DataType, self).__init__(doc)

    def process(self, obj, elt):
        super(DataType, self).process(obj, elt)
        if elt.nodeName == 'emof:DataType':
            elt.removeAttributeNS('xsi', 'type')
        else:
            elt.setAttributeNS('xsi', 'xsi:type', 'emof:DataType')
        if obj.serializable:
            elt.setAttributeNS(None, 'serializable', str(obj.serializable))
        if obj.defaultValue:
            elt.setAttributeNS(None, 'defaultValue', str(obj.defaultValue))
        if obj.allowNull:
            elt.setAttributeNS(None, 'allowNull', str(obj.allowNull))


class Class (Type):

    def __init__(self, doc):
        super(Class, self).__init__(doc)

    def process(self, obj, elt):
        super(Class, self).process(obj, elt)
        if elt.nodeName == 'emof:Class':
            elt.removeAttributeNS('xsi', 'type')
        else:
            elt.setAttributeNS('xsi', 'xsi:type', 'emof:Class')
        if obj.isAbstract:
            elt.setAttributeNS(None, 'isAbstract', str(obj.isAbstract))
        for o in obj.ownedAttribute:
            clss = dumpers[type(o)]
            child = clss(self._doc)(o, 'ownedAttribute')
            elt.appendChild(child)
        for o in obj.ownedOperation:
            clss = dumpers[type(o)]
            child = clss(self._doc)(o, 'ownedOperation')
            elt.appendChild(child)
        for o in obj.superClass:
            child = self._doc.createElement('superClass')
            value = self._doc.createTextNode(o._xmi_id)
            child.appendChild(value)
            elt.appendChild(child)


class Operation (MultiplicityElement):

    def __init__(self, doc):
        super(Operation, self).__init__(doc)

    def process(self, obj, elt):
        super(Operation, self).process(obj, elt)
        if elt.nodeName == 'emof:Operation':
            elt.removeAttributeNS('xsi', 'type')
        else:
            elt.setAttributeNS('xsi', 'xsi:type', 'emof:Operation')
        for o in obj.raisedException:
            child = self._doc.createElement('raisedException')
            value = self._doc.createTextNode(o._xmi_id)
            child.appendChild(value)
            elt.appendChild(child)
        for o in obj.ownedParameter:
            clss = dumpers[type(o)]
            child = clss(self._doc)(o, 'ownedParameter')
            elt.appendChild(child)
        if obj.class_:
            elt.setAttributeNS(None, 'class', obj.class_._xmi_id)


class Parameter (MultiplicityElement):

    def __init__(self, doc):
        super(Parameter, self).__init__(doc)

    def process(self, obj, elt):
        super(Parameter, self).process(obj, elt)
        if elt.nodeName == 'emof:Parameter':
            elt.removeAttributeNS('xsi', 'type')
        else:
            elt.setAttributeNS('xsi', 'xsi:type', 'emof:Parameter')
        for o in obj.operation:
            child = self._doc.createElement('operation')
            value = self._doc.createTextNode(o._xmi_id)
            child.appendChild(value)
            elt.appendChild(child)


class Property (MultiplicityElement):

    def __init__(self, doc):
        super(Property, self).__init__(doc)

    def process(self, obj, elt):
        super(Property, self).process(obj, elt)
        if elt.nodeName == 'emof:Property':
            elt.removeAttributeNS('xsi', 'type')
        else:
            elt.setAttributeNS('xsi', 'xsi:type', 'emof:Property')
        if obj.isReadOnly:
            elt.setAttributeNS(None, 'isReadOnly', str(obj.isReadOnly))
        if obj.default:
            elt.setAttributeNS(None, 'default', str(obj.default))
        if obj.isComposite:
            elt.setAttributeNS(None, 'isComposite', str(obj.isComposite))
        if obj.isDerived:
            elt.setAttributeNS(None, 'isDerived', str(obj.isDerived))
        if obj.isId:
            elt.setAttributeNS(None, 'isId', str(obj.isId))
        if obj.opposite:
            elt.setAttributeNS(None, 'opposite', obj.opposite._xmi_id)
        if obj.class_:
            elt.setAttributeNS(None, 'class', obj.class_._xmi_id)


class Enumeration (DataType):

    def __init__(self, doc):
        super(Enumeration, self).__init__(doc)

    def process(self, obj, elt):
        super(Enumeration, self).process(obj, elt)
        if elt.nodeName == 'emof:Enumeration':
            elt.removeAttributeNS('xsi', 'type')
        else:
            elt.setAttributeNS('xsi', 'xsi:type', 'emof:Enumeration')
        for o in obj.ownedLiteral:
            clss = dumpers[type(o)]
            child = clss(self._doc)(o, 'ownedLiteral')
            elt.appendChild(child)


class PrimitiveType (DataType):

    def __init__(self, doc):
        super(PrimitiveType, self).__init__(doc)

    def process(self, obj, elt):
        super(PrimitiveType, self).process(obj, elt)
        if elt.nodeName == 'emof:PrimitiveType':
            elt.removeAttributeNS('xsi', 'type')
        else:
            elt.setAttributeNS('xsi', 'xsi:type', 'emof:PrimitiveType')


class Integer (DumpElement):

    def __init__(self, doc):
        super(Integer, self).__init__(doc)

    def process(self, obj, elt):
        super(Integer, self).process(obj, elt)
        if elt.nodeName == 'emof:Integer':
            elt.removeAttributeNS('xsi', 'type')
        else:
            elt.setAttributeNS('xsi', 'xsi:type', 'emof:Integer')


class Boolean (DumpElement):

    def __init__(self, doc):
        super(Boolean, self).__init__(doc)

    def process(self, obj, elt):
        super(Boolean, self).process(obj, elt)
        if elt.nodeName == 'emof:Boolean':
            elt.removeAttributeNS('xsi', 'type')
        else:
            elt.setAttributeNS('xsi', 'xsi:type', 'emof:Boolean')


class String (DumpElement):

    def __init__(self, doc):
        super(String, self).__init__(doc)

    def process(self, obj, elt):
        super(String, self).process(obj, elt)
        if elt.nodeName == 'emof:String':
            elt.removeAttributeNS('xsi', 'type')
        else:
            elt.setAttributeNS('xsi', 'xsi:type', 'emof:String')

dumpers = {
    core.Element: Element,
    core.Object: Object,
    core.NamedElement: NamedElement,
    core.Tag: Tag,
    core.Package: Package,
    core.TypedElement: TypedElement,
    core.EnumerationLiteral: EnumerationLiteral,
    core.Type: Type,
    core.MultiplicityElement: MultiplicityElement,
    core.DataType: DataType,
    core.Class: Class,
    core.Operation: Operation,
    core.Parameter: Parameter,
    core.Property: Property,
    core.Enumeration: Enumeration,
    core.PrimitiveType: PrimitiveType,
    core.Integer: Integer,
    core.Boolean: Boolean,
    core.String: String    
}

class Dumper (object):
    '''emof model dumper to an XMI file.'''

    def __init__(self):
        super(Dumper, self).__init__()
        self._doc = minidom.Document()
        root = self._doc.createElement('xmi:XMI')
        root.setAttribute('xmi:version', '2.0')
        root.setAttribute('xmlns:xmi', 'http://www.omg.org/XMI')
        root.setAttribute('xmlns:xsi',
                          'http://www.w3.org/2001/XMLSchema-instance' )
        root.setAttribute('xmlns:emof',
                          'http://nowhere/emof.xmi')
        self._doc.appendChild(root)

    def dump(self, rep, filename='out.xmi'):
        for x in rep.Element:
            elt = Element(self._doc)(x, 'emof:Element')
            self._doc.documentElement.appendChild(elt)
        for x in rep.Object:
            elt = Object(self._doc)(x, 'emof:Object')
            self._doc.documentElement.appendChild(elt)
        for x in rep.NamedElement:
            elt = NamedElement(self._doc)(x, 'emof:NamedElement')
            self._doc.documentElement.appendChild(elt)
        for x in rep.Tag:
            elt = Tag(self._doc)(x, 'emof:Tag')
            self._doc.documentElement.appendChild(elt)
        for x in rep.Package:
            elt = Package(self._doc)(x, 'emof:Package')
            self._doc.documentElement.appendChild(elt)
        for x in rep.TypedElement:
            elt = TypedElement(self._doc)(x, 'emof:TypedElement')
            self._doc.documentElement.appendChild(elt)
        for x in rep.EnumerationLiteral:
            elt = EnumerationLiteral(self._doc)(x, 'emof:EnumerationLiteral')
            self._doc.documentElement.appendChild(elt)
        for x in rep.Type:
            elt = Type(self._doc)(x, 'emof:Type')
            self._doc.documentElement.appendChild(elt)
        for x in rep.MultiplicityElement:
            elt = MultiplicityElement(self._doc)(x, 'emof:MultiplicityElement')
            self._doc.documentElement.appendChild(elt)
        for x in rep.DataType:
            elt = DataType(self._doc)(x, 'emof:DataType')
            self._doc.documentElement.appendChild(elt)
        for x in rep.Class:
            elt = Class(self._doc)(x, 'emof:Class')
            self._doc.documentElement.appendChild(elt)
        for x in rep.Operation:
            elt = Operation(self._doc)(x, 'emof:Operation')
            self._doc.documentElement.appendChild(elt)
        for x in rep.Parameter:
            elt = Parameter(self._doc)(x, 'emof:Parameter')
            self._doc.documentElement.appendChild(elt)
        for x in rep.Property:
            elt = Property(self._doc)(x, 'emof:Property')
            self._doc.documentElement.appendChild(elt)
        for x in rep.Enumeration:
            elt = Enumeration(self._doc)(x, 'emof:Enumeration')
            self._doc.documentElement.appendChild(elt)
        for x in rep.PrimitiveType:
            elt = PrimitiveType(self._doc)(x, 'emof:PrimitiveType')
            self._doc.documentElement.appendChild(elt)
        for x in rep.Integer:
            elt = Integer(self._doc)(x, 'emof:Integer')
            self._doc.documentElement.appendChild(elt)
        for x in rep.Boolean:
            elt = Boolean(self._doc)(x, 'emof:Boolean')
            self._doc.documentElement.appendChild(elt)
        for x in rep.String:
            elt = String(self._doc)(x, 'emof:String')
            self._doc.documentElement.appendChild(elt)
        o = file(filename, 'w')
        o.write(self._doc.toprettyxml())
        o.close()

# eof
