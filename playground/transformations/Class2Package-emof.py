def source_metamodels():
  return ['emof']

def target_metamodels():
  return ['emof']


def Class2Package(source,target):
  for c in source.get_all_of_kind('Class'):
    nouv = target.create_instance('Package')
    nouv.name = c.name
    target.model[0].add_Package(nouv) #FIXME : should be something like : target.add_Package("destination",nouv)


def transform(source_model,target_model):
  Class2Package(source_model,target_model)

