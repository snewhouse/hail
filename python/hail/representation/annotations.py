class Struct(object):
    """
    Nested annotation structure.

    Struct elements are treated as both 'items' and 'attributes', which
    allows either syntax for accessing the element "foo" of struct "bar":

    >>> bar.foo
    >>> bar['foo']

    Note that it is possible to use Hail to define struct fields inside
    of a key table or variant dataset that do not match python syntax.
    The name "1kg", for example, will not parse to python because it
    begins with an integer, which is not an acceptable leading character
    for an identifier.  There are two ways to access this field:

    >>> getattr(bar, '1kg')
    >>> bar['1kg']

    :param dict attributes: struct members.
    """

    def __init__(self, attributes):

        self._attrs = attributes

    def __getattr__(self, item):
        assert (self._attrs)
        if item not in self._attrs:
            raise AttributeError("Struct instance has no attribute '%s'" % item)
        return self._attrs[item]

    def __contains__(self, item):
        return item in self._attrs

    def __getitem__(self, item):
        return self.__getattr__(item)

    def __len__(self):
        return len(self._attrs)

    def __str__(self):
        return 'Struct' + str(self._attrs)

    def __repr__(self):
        return 'Struct' + repr(self._attrs)

    def __eq__(self, other):
        return self._attrs == other._attrs
