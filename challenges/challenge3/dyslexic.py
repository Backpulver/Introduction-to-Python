import inspect
from itertools import permutations

class Dyslexic:
    def __init__(self, obj):
        self.passed_object = obj
        self.obj_attributes_list = []
        self.newAttributeNames = []

    def __enter__(self):
        for i in inspect.getmembers(self.passed_object):
            if not i[0].startswith("_"):
                if not inspect.ismethod(i[1]):
                    self.obj_attributes_list.append(i)
        
        for tuple_in_list in self.obj_attributes_list:
            perms_set = [''.join(p) for p in permutations(tuple_in_list[0])]
            perms_set = set(perms_set)
            for item in perms_set:
                self.newAttributeNames.append(item)
                self.__setattr__(item, tuple_in_list[1])


    def __exit__(self, type, value, traceback):  
      for elem in self.newAttributeNames:
            delattr(self, elem)


class Baba:
    abc = 5


baba = Baba()

with Dyslexic(baba) as dyslexic_baba:
    print(dyslexic_baba.abc)  # 5
    print(dyslexic_baba.bac)  # 5
    print(dyslexic_baba.cab)  # 5     
    # print(dyslexic_baba.notreal) # AttributeError: Baba object has no dyslexic attributes notreal


# import itertools

# class Dyslexic:
    
#     def __init__(self, obj):
#         self._object = obj

#     def __enter__(self):
#         return self

#     def __exit__(self, exc_type, value, traceback):
#         pass
    
#     def __getattr__(self, name):
#         for permutation in itertools.permutations(name):
#             try:
#                 return getattr(self._object, ''.join(permutation))
#             except AttributeError:
#                 continue # Try another one
#         raise AttributeError(f'{self._object.__class__.__name__} object has no dyslexic attributes {name}')