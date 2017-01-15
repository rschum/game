#! /usr/bin/python2.7

from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from source.abstract.base_object.model import model

class Foo(model.Model):
    def __init__(self, parent = None):
        model.Model.__init__(self, parent)
        pass

if __name__ == "__main__":
    foo0 = Foo()
    print foo0.get_seed()
    
    bar0 = Foo(foo0)
    print bar0.get_seed()

    bar1 = Foo(foo0)
    print bar1.get_seed()

    baz0 = Foo(bar0)
    print baz0.get_seed()

    baz1 = Foo(bar0)
    print baz1.get_seed()

    print("")
    print foo0.get_seed()
    print bar0.get_seed()
    print bar1.get_seed()
    print baz0.get_seed()
    print baz1.get_seed()
    """
    print("")
    print baz0.parent.get_seed()
    baz0.parent_to(foo0)
    print baz0.parent.get_seed()
    """
    print("")
    print(len(foo0.children))
    print(len(bar0.children))
    baz1.parent_to(foo0)
    print(len(foo0.children))
    print(len(bar0.children))
