import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    #Test examples in pdf and bkel
    def test_simple_program1(self):
        """Simple program: Class main() {} """
        input = """Class main {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,200))

    def test_simple_program1(self):
        """Simple program: Class main() {} """
        input = """CLass main {}"""
        expect = "Error on line 1 col 0: CLass"
        self.assertTrue(TestParser.test(input,expect,201))

    def test_simple_program2(self):
        """Miss ( {"""
        input = """
Class Rectangle: Shape {
    getArea() {
        Return Self.length * Self.width;
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,202))

    def test_simple_program3(self):
        input = """
Class Program {
    main() {
        Out.printInt(Shape::$numOfShape);
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,203))

    def test_simple_program4(self):
        """Miss ( {"""
        input = """
Class Rectangle: Shape {
    getArea() {
        Var lit, s: Int;
        lit = 2;
        Var a, b: Array[Int, 5];
        s = lit * lit * Self.myPI;
        a[0] = s;
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,204))
    
    def test_wrong_miss_close(self):
        """Miss ( {"""
        input = """
Class Shape {
    $getNumOfShape( {
        Return Self.length * Self.width;
    }
}
"""
        expect = "Error on line 3 col 20: {"
        self.assertTrue(TestParser.test(input,expect,205))

    def test_more_complex_program1(self):
        input = """
Class Shape {
    Val $numOfShape: Int = 0;
    Val immutableAttribute: Int = 0;
    Var length, width: Int;

    $getNumOfShape() {
        Return $numOfShape;
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,206))

    def test_more_complex_program2(self):
        input = """
Class Shape {
    Val $numOfShape: Int = 0;
    Val immutableAttribute: Int = 0;
    Var length, width: Int;

    $getNumOfShape() {
        Return $numOfShape;
    }
}

Class Rectangle: Shape {
    getArea() {
        Return Self.length * Self.width;
    }
}

Class Program {
    main() {
        Out.printInt(Shape::$numOfShape);
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,207))

    def test_more_complex_program3(self):
        input = """
Class Shape {
    Val $numOfShape: Int = 0;
    Val immutableAttribute: Int = 0;
    Var length, width: Int;

    $getNumOfShape() {
        Foreach (i In 1 .. 100 By 2) {
            Out.printInt(i);
        }
        Foreach (x In 5 .. 2) {
            Out.printInt(arr[x]);
        }
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,208))

    def test_more_complex_program4(self):
        input = """
Class Shape {
    Val $numOfShape: Int = 0;
    Val immutableAttribute: Int = 0;
    Var length, width: Int;

    $getNumOfShape() {
        Foreach (i In 1 .. 100 By 2) {
            Out.printInt(i);
        }
        Foreach (x In 5 .. 2) {
            Out.printInt(arr[x]);
        }
        If(A[5] == 5){
            Out.printInt(arr[x]);
        }
        Elseif(a*6 > b+4){
            Out.printInt(Shape::$numOfShape);
        }
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,209))

    def test_more_complex_program5(self):
        input = """
Class Shape {
    Val $numOfShape: Int = 0;
    Val immutableAttribute: Int = 0;
    Var length, width: Int;

    $getNumOfShape() {
        Foreach (i In 1 .. 100 By 2) {
            Out.printInt(i);
        }
        Foreach (x In 5 .. 2) {
            Out.printInt(arr[x]);
        }
        If(A[5] == 5){
            Out.printInt(arr[x]);
        }
        Elseif(a*6 > b+4){
            Out.printInt(Shape::$numOfShape);
        }
        Else{
            Out.printInt(Shape.$numOfShape);
        }
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,210))