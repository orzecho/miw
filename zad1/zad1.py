class TylkoParzyste:

    def __init__(self, name, v):
        self.name = name
        if isinstance(v, int):
            self.v = v if v % 2 == 0 else v + 1
        else:
            self.v = 0

    def __str__(self):
        return '{} = {}'.format(self.name, self.v)

    def __add__(self, o):
        name = ''
        v = 0
        if isinstance(o, TylkoParzyste):
            name = '{}+{}'.format(self.name, o.name)
            v = self.v + o.v
        elif isinstance(o, int):
            name = '{}+?'.format(self.name)
            v = self.v + o
        else:
            raise ValueError('Trying to add non int or non TylkoParzyste.')

        return TylkoParzyste(name, v)

a = TylkoParzyste('A', 13) + 2
print(a)