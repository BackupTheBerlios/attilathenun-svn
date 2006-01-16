

On a un mapping trivial Elements->Elements

Quid de la structure ? ici le mapping est évident également..
La structure peut ê representée par les liens (références)

exemple : 
nomAssociation : Class -> Class
 
on veut la transformer en 
AutreAssociation Element->Element

Class <-> Class
Class.truc <-> Class.bidule
Class.association


si on veut de KM3 -> emof

On récupère les classes instanciées
 pour chaque classe, on en crée une autre.
 on prend les attributs mappés depuis Classe et on met à jour les autres


transform :
 mapElement(KM3.Class,MOF.Class)
 mapAttribute(KM3.Class.name,MOF.Class.name)
 mapAttribute(KM3.Class.truc,MOF.Class.bidule)
 mapCollection(KM3.Class.subclasses,MOF.Class.autreSubClasse)
 
 #ici c'est unidirectionnel
 for otherclass in KM3.Class.subclasses
    MOF.Class.autreSubclasse += mappedObject(otherclass)
 

#=> on veut donc les liens de transformations !!  
