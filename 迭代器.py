class Classmate (object):
    def __init__(self):
        self.names = list()

    def Add (self, name):
        self.names.append(name)

    def __iter__(self):
        return Classitrator(self)

class Classitrator (object):
    def __init__(self, obj):
        self.obj = obj

    def __iter__(self):
        pass
    def __next__(self):
        for i in range(1):
            return self.obj.names[i]

classmate = Classmate()
classmate.Add('cq')
classmate.Add('hh')

for name in classmate:
    print(name)
