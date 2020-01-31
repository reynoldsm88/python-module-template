import unittest
from stuff.classes import MyClass


class MyClassTest( unittest.TestCase ):

    def test_do_work( self ):
        my_class = MyClass( 1 )
        self.assertEqual( 1, my_class.do_work() )