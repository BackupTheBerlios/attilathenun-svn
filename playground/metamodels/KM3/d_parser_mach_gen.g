 km3 : package*;
${action}
 package :  "package" name "{"  abs_class* types_decl* class* "}";
${action}
types_decl : 'datatype' name ';';
${action}
 name : "[a-zA-Z]+([0-9a-zA-Z])*"  | quotedname;
${action}
 anything : "[a-zA-Z]*([0-9a-zA-Z])*" ;
${action}
 quotedname : '"' name '"' ;
${action}
 abs_class : 'abstract class' name superclasses* '{'  class_content* '}';
${action}
 class : 'class' name superclasses* '{' class_content* '}';
${action}
 superclasses : 'extends' name* ;
${action}
 comment : '--' anything* ;
${action}
 class_content : attribute | reference | comment ;
${action}
 attribute : 'attribute' name ':' name  ';';
${action}
 number : "[0-9]+" ;
${action}
 bimult : '[' number '-' number ']' ;
${action}
 monomult : '[' number ']';
${action}
 infini : '[' '*' ']' ;
${action}
 multiplicity :  bimult | monomult | infini ;
${action}
 reference : 'reference' name multiplicity* ordered* ':' name opposite*   ';' ;
${action}
 opposite : 'oppositeOf' name ;
${action}
 ordered : 'ordered container' ;
${action}
