"""Test module"""


class Number:
    """Test class"""

    def __init__(self, n):
        """init"""
        self.value = n

    def val(self):
        """val"""
        return self.value

    def add(self, n2):
        """add"""
        self.value += n2.val()

    def __add__(self, n2):
        """add"""
        return self.__class__(self.value + n2.val())

    def __str__(self):
        """str"""
        return str(self.val())

    @classmethod
    def addall(cls, number_obj_iter):
        """addall"""
        cls(sum(n.val() for n in number_obj_iter))
