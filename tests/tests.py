import sys
from overload import overload


@overload
def test_fun(a: str, b: str):
    print('Test. with a function. Parameters types: str and str')

def watiztest():
    print(test_fun)

watiztest()

@overload
def test_fun(a: int, b: int):
    print('Test. with a function. Parameters types: int and int')

watiztest()

@overload
def test_fun(a: int, b: str):
    print('Test. with a function. Parameters types: int and str')

watiztest()

@overload
def test_fun(a: str, b: int):
    print('Test. with a function. Parameters types: str and int')

watiztest()


class Test:
    
    def __init__(self):
        self.coucou = 'coucou'

    @overload
    def test_method(self: object, a: str, b: str):
        print('Test. with an object method. Parameters types: str and str')

    @overload
    def test_method(self: object, a: int, b: int):
        print('Test. with an object method. Parameters types: int and int')

    @overload
    def test_method(self: object, a: int, b: str):
        print('Test. with an object method. Parameters types: int and str')

    @overload
    def test_method(self: object, a: str, b: int):
        print('Test. with an object method. Parameters types: str and int')

    def watiztest(self):
        print(self.test)

try:
    t = Test()
    t.test_method('IJustLost', 'TheGame')
    t.test_method(42, 1337)
    t.test_method(666, 'Test.')
    t.test_method('Votai Test.', 42)
    t.watiztest()
except Exception as e:
    print('overload does not handle class methods for the moment')
    print(sys.exc_info()[0])
    print(e)
finally:
    test_fun('IJustLost', 'TheGame')
    test_fun(42, 1337)
    test_fun(666, 'Test.')
    test_fun('Votai Test.', 42)
