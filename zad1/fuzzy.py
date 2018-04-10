class Fuzzy:

    TRUTH_TRESHOLD=0.5
    EPSILON=0.0001

    def __init__(self, v):
        if v > 1.0:
            self.v = 1.0
        elif v < 0.0:
            self.v = 0.0
        else:
            self.v = v

    # To string
    def __str__(self):
        return '{:.3f}'.format(self.v)

    # Equal
    def __eq__(self,o):
        if isinstance(o,Fuzzy):
            return self.v-o.v<Fuzzy.EPSILON
        else:
            return self.v-o<Fuzzy.EPSILON

    # Greater
    def __gt__(self,o):
        if isinstance(o,Fuzzy):
            return self.v>o.v
        else:
            return self.v>o

    # Not equal
    def __ne__(self,o):
        return not self==o

    # Back to classic logic
    def __bool__(self):
        return True if self.v >= Fuzzy.TRUTH_TRESHOLD else False

    # Negation
    def __neg__(self):
        return Fuzzy(1.0 - self.v)

    # Alternative
    def __or__(self, other):
        return Fuzzy(max(self.v, other.v))

    # Conjunction
    def __and__(self, other):
        return Fuzzy(min(self.v, other.v))

    # Sets truth value
    def set_value(self,v):
        self.v = v

    # Sets parameter for conversion to classic logic
    @staticmethod
    def set_truth_threshold(t):
        if t > 1:
            Fuzzy.TRUTH_TRESHOLD = 1
        elif t < 0:
            Fuzzy.TRUTH_TRESHOLD = 0
        else:
            Fuzzy.TRUTH_TRESHOLD = t
