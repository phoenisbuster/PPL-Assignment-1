import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: Class main() {} """
        input = """Class main {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    def test_more_complex_program(self):
        """More complex program"""
        input = """
Class Rectangle: Shape {
    getArea() {
        Return Self.length * Self.width;
    }
}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,202))
    
    def test_wrong_miss_close(self):
        """Miss ( {"""
        input = """
Class Shape {
    $getNumOfShape
        Return Self.length * Self.width;
    }
}
        """
        expect = "Error on line 3 col 24: {"
        self.assertTrue(TestParser.test(input,expect,203))