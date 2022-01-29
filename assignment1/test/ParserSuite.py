import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    #Test Class decl
    def test_class_decl1(self):
        input = """Class abcXyz {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,200))
    def test_class_decl2(self):
        input = """Class _932dc {}
Class 9021{
    getArea() {
        Return Self.length * Self.width;
    }
}"""
        expect = "Error on line 2 col 6: 9021"
        self.assertTrue(TestParser.test(input,expect,201))

    def test_class_decl3(self):
        input = """Class _932dc {}
Class _:_:9021{
    getArea() {
        Return Self.length * Self.width;
    }
}"""
        expect = "Error on line 2 col 9: :"
        self.assertTrue(TestParser.test(input,expect,202))
    def test_class_decl4(self):
        input = """Class $932dc {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,203))
    def test_class_decl5(self):
        input = """Class Program {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,204))
    def test_class_decl6(self):
        input = """Class _932dc {}
Class _9021{
    getArea() {
        Return Self.length * Self.width;
    }
}
Class Program:_9021{}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,205))
    def test_class_decl7(self):
        input = """Class _932dc:Program {}
Class _9021{
    getArea() {
        Return Self.length * Self.width;
    }
}
Class Program:_9021{}
Class """
        expect = "Error on line 8 col 6: <EOF>"
        self.assertTrue(TestParser.test(input,expect,206))
    def test_class_decl8(self):
        input = """Class _932dc:Program {}
Class __9021{
    getArea() {
        Return Self.length * Self.width;
    }
}
Class Program:__9021{}
Class Abc:Program:__9021"""
        expect = "Error on line 8 col 17: :"
        self.assertTrue(TestParser.test(input,expect,207))
    def test_class_decl9(self):
        input = """Class _932dc:Program {}
Class _9021{
    getArea() {
        Return Self.length * Self.width;
    }
}
Class Program{
    main(){}
    Main(){}
}
Class Abc:Program"""
        expect = "Error on line 11 col 17: <EOF>"
        self.assertTrue(TestParser.test(input,expect,208))
    def test_class_decl10(self):
        input = """Class _932dc:Program {}
Class _9021{
    getArea() {
        Return Self.length * Self.width;
    }
}
Class Program:_9021{
    main(){}
    Main(){}
}
Class Abc{}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,209))

    #Attribute decl
    def test_attr_decl1(self):
        input = """Class _932dc:Program {}
Class _9021{}
Class Program:_9021{
    Val $numOfShape: Int = 0;
    Val immutableAttribute: Int = 0;
    Var length, width: Int;
    Val My1stCons, My2ndCons: Int = 1 + 5, 2;
    Var $x, $y : Int = 0, 0; 
}
Class Abc{}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,210))
    def test_attr_decl2(self):
        input = """
Class Rectangle: Shape {
    Val $numOfShape: Int = 0;
    Val immutableAttribute: Int = 0;
    Var length, width: Int;
    Val My1stCons, My2ndCons: Int = 1 + 5, 2;
    Var $x, $y : Int = 0, 0; 
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,211))
    def test_attr_decl3(self):
        input = """
Class Rectangle: Shape {
    Var My1stCons, My2ndCons: Int = 1 + 5, 2;
    Var $x, $y : Int = 0, 0;
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,212))
    def test_attr_decl4(self):
        input = """
Class Rectangle: Shape {
    Val My1stCons, My2ndCons: Int;
    Var $x, $y : Int;
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,213))
    def test_attr_decl5(self):
        input = """
Class Rectangle: Shape {
    Var My1stCons, My2ndCons: Array[Int, 4] = Array(1, 5, 7, 12);
    Var $x, $y : Array[String, 4] = Array("Kangxi", "Yongzheng", "Qianlong");
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,214))
    def test_attr_decl6(self):
        input = """
Class Rectangle: Shape {
    Var My1stCons, My2ndCons: Array[Array[String, 3], 3] = Array (Array("Volvo", "22", "18"),Array("Saab", "5", "2"),Array("Land Rover", "17", "15"));
    Var $x, $y : Array[String, 4] = Array("Kangxi", "Yongzheng", "Qianlong");
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,215))
    def test_attr_decl7(self):
        input = """
Class Rectangle: Shape {
    Var My1stCons, My2ndCons Array[Array[String, 3], 3] = Array (Array("Volvo", "22", "18"),Array("Saab", "5", "2"),Array("Land Rover", "17", "15"));
    Var $x, $y : Array[String, 4] = Array("Kangxi", "Yongzheng", "Qianlong");
}"""
        expect = "Error on line 3 col 29: Array"
        self.assertTrue(TestParser.test(input,expect,216))
    def test_attr_decl8(self):
        input = """
Class Rectangle: Shape {
    Val My1stCons, My2ndCons: Int =;
    Var $x, $y : Int = 0,0;
}"""
        expect = "Error on line 3 col 35: ;"
        self.assertTrue(TestParser.test(input,expect,217))
    def test_attr_decl9(self):
        input = """
Class Rectangle: Shape {
    Val My1stCons, My2ndCons:;
    Var $x, y : Int;
}"""
        expect = "Error on line 3 col 29: ;"
        self.assertTrue(TestParser.test(input,expect,218))
    def test_attr_decl10(self):
        input = """
Class Rectangle: Shape {
    My1stCons, My2ndCons: Int;
    Var $x, $y : Int;
}"""
        expect = "Error on line 3 col 13: ,"
        self.assertTrue(TestParser.test(input,expect,219))

    #Simple methods decl
    def test_methods_decl1(self):
        input = """
Class Rectangle: Shape {
    getArea() {}
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,220))
    def test_methods_decl2(self):
        input = """
Class Rectangle: Shape {
    :getArea() {}
}"""
        expect = "Error on line 3 col 4: :"
        self.assertTrue(TestParser.test(input,expect,221))
    def test_methods_decl3(self):
        input = """
Class Rectangle: Shape {
    _getArea() {}
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,222))
    def test_methods_decl4(self):
        input = """
Class Rectangle: Shape {
    $_getArea() {}
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,223))
    def test_methods_decl5(self):
        input = """
Class Rectangle: Shape {
    Constructor() {}
    Destructor() {}
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,224))
    def test_methods_decl6(self):
        input = """
Class Rectangle: Shape {
    $Constructor() {}
    Destructor() {}
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,225))
    def test_methods_decl7(self):
        input = """
Class Rectangle: Shape {
    getArea() {}
    $getArea() {}
    Constructor() {}
    Destructor() {}
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,226))
    def test_methods_decl8(self):
        input = """
Class Rectangle: Shape {
    getArea(a,b,c: Int) {}
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,227))
    def test_methods_decl9(self):
        input = """
Class Rectangle: Shape {
    getArea(a,b,c: Int; e,f,g,h: Float; _QWER:Array[Int,3]) {}
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,228))
    def test_methods_decl10(self):
        input = """
Class Rectangle: Shape {
    getArea(a,b,c: Int, e,f,g,h: Float; _QWER:Array[Int,3]) {}
}"""
        expect = "Error on line 3 col 22: ,"
        self.assertTrue(TestParser.test(input,expect,229))

    #Test both simple attrs and methods decl
    def test_mix_decl1(self):
        input = """
Class Rectangle: Shape {
    Val $numOfShape: Int = 0;
    Val immutableAttribute: Int = 0;
    Var length, width: Int;
    Val My1stCons, My2ndCons: Int = 1 + 5, 2;
    Var $x, $y : Int = 0, 0; 
    $getArea() {
        Return Self.length * Self.width;
    }
    getArea(a,b,c: Int) {}
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,230))
    def test_mix_decl2(self):
        input = """
Class Rectangle: Shape {
    Val $numOfShape: Int = 0;
    Val immutableAttribute: Int = 0;
    Var length, width: Int;
    Val My1stCons, My2ndCons: Array[Int, 4] = Array(1, 5, 7, 12);
    Var $x, $y : Array[String, 4] = Array("Kangxi", "Yongzheng", "Qianlong");
    $getArea() {
        Return Self.length * Self.width;
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,231))
    def test_mix_decl3(self):
        input = """
Class Rectangle: Shape {
    Val My1stCons, My2ndCons: Array[Array[String, 3], 3] = Array (Array("Volvo", "22", "18"),Array("Saab", "5", "2"),Array("Land Rover", "17", "15"));
    Var $x, $y : Array[String, 4] = Array("Kangxi", "Yongzheng", "Qianlong");
    $getArea() {
        Return Self.length * Self.width;
    }
    Constructor() {}
    Destructor() {}
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,232))
    def test_mix_decl4(self):
        input = """
Class Rectangle: Shape {
    Val $numOfShape: Int = 0;
    Val immutableAttribute: Int = 0;
    Var length, width: Int;
    Val My1stCons, My2ndCons: Int = 1 + 5, 2;
    Var $x, $y : Int = 0, 0; 
    getArea(a,b,c: Int, e,f,g,h: Float; _QWER:Array[Int,3]) {}
}"""
        expect = "Error on line 8 col 22: ,"
        self.assertTrue(TestParser.test(input,expect,233))
    def test_mix_decl5(self):
        input = """
Class Rectangle: Shape {
    Val My1stCons, My2ndCons: Array[Array[String, 3], 3] = Array (Array("Volvo", "22", "18"),Array("Saab", "5", "2"),Array("Land Rover", "17", "15"));
    Var $x, $y : Array[String, 4] = Array("Kangxi", "Yongzheng", "Qianlong")
    $getArea() {
        Return Self.length * Self.width;
    }
}"""
        expect = "Error on line 5 col 4: $getArea"
        self.assertTrue(TestParser.test(input,expect,234))
    def test_mix_decl6(self):
        input = """
Class Rectangle: Shape {
    Val $numOfShape: Int = 0;
    Val immutableAttribute: Int = 0;
    Var length, width: Int;
    Val My1stCons, My2ndCons: Int = 1 + 5, 2;
    Var $x, $y : Int = 0, 0; 
    $getArea() {
        Return Self.length * Self.width;
    }
    _getArea(a,b,c: Int; e,f,g,h: Float; _QWER:Array[Int,3]) {}
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,235))
    def test_mix_decl7(self):
        input = """
Class Rectangle: Shape {
    Val $numOfShape: Int = 0;
    Val immutableAttribute: Int = 0;
    Var length, width: Int;
    Val My1stCons, My2ndCons: Int = 1 + 5, 2;
    Var $x, $y : Int = 0, 0; 
    $getArea() {
        Return Self.length * Self.width;
    }
    _getArea(a,b,c: Int; e,f,g,h: Float; _QWER:Array[Int,3]; My1stCons, My2ndCons: Array[Array[String, 3], 3]) {}
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,236))
    def test_mix_decl8(self):
        input = """
Class Rectangle: Shape {
    Val $numOfShape: Int = 0;
    Val immutableAttribute: Int = 0;
    Var length, width: Int;
    Val My1stCons, My2ndCons: Int = 1 + 5, 2;
    Var $x, $y : Int = 0, 0;
    Val My1stCons213, __My2ndCons: Array[Array[String, 3], 3] = Array (Array("Volvo", "22", "18"),Array("Saab", "5", "2"),Array("Land Rover", "17", "15"));
    Var $m, $n : Array[String, 4] = Array("Kangxi", "Yongzheng", "Qianlong");
    $getArea() {
        Return Self.length * Self.width;
    }
    _getArea(a,b,c: Int; e,f,g,h: Float; _QWER:Array[Int,3]; My1stCons, My2ndCons: Array[Array[String, 3], 3] = Array (Array("Volvo", "22", "18"),Array("Saab", "5", "2"),Array("Land Rover", "17", "15"))) {}
}"""
        expect = "Error on line 13 col 110: ="
        self.assertTrue(TestParser.test(input,expect,237))
    def test_mix_decl9(self):
        input = """
Class Rectangle: Shape {
    Val My1stCons, My2ndCons: Int;
    Var $x, $y : Int;
    $getArea() {
        Return Self.length * Self.width;
    }
    _getArea(a,b,c: Int; e,f,g,h: Float; _QWER:Array[Int,3]; My1stCons, My2ndCons: Array[Array[String, 3], 3]) {}
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,238))
    def test_mix_decl10(self):
        input = """
Class Program {
    Val $numOfShape: Int = 0;
    Val immutableAttribute: Int = 0;
    Var length, width: Int;
    Val My1stCons, My2ndCons: Int = 1 + 5, 2;
    Var $x, $y : Int = 0, 0; 
    $getArea() {
        Return Self.length * Self.width;
    }
    $getArea() {
        Return Self.length * Self.width;
    }
    _getArea(a,b,c: Int; e,f,g,h: Float; _QWER:Array[Int,3]; My1stCons, My2ndCons: Array[Array[String, 3], 3]) {}
    Constructor(a,b,c: Int; e,f,g,h: Float; _QWER:Array[Int,3]; My1stCons, My2ndCons: Array[Array[String, 3], 3]) {}
    Destructor() {}
    main(){}
    Main(){}
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,239))

    #Test stmts in methods
    def test_stmt1(self):
        input = """
Class Program {
    Val $numOfShape: Int = 0;
    Val immutableAttribute: Int = 0;
    Var length, width: Int;
    Val My1stCons, My2ndCons: Int = 1 + 5, 2;
    Var $x, $y : Int = 0, 0; 
    $getArea() {
        Return Self.length * Self.width;
    }
    $getArea() {
        Return Self.length * Self.width;
    }
    _getArea() {
        Var lit, s: Int;
        lit = 2;
        Var a, b: Array[Int, 5];
        s = lit * lit * Self.myPI;
        a[0] = s;
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,240))
    def test_stmt2(self):
        input = """
Class Program {
    Val $numOfShape: Int = 0;
    Val immutableAttribute: Int = 0;
    Var length, width: Int;
    Val My1stCons, My2ndCons: Int = 1 + 5, 2;
    Var $x, $y : Int = 0, 0; 
    $getArea() {
        Return Self.length * Self.width;
    }
    $getArea() {
        Return Self.length * Self.width;
    }
    Val getArea() {
        Var lit, s: Int;
        lit = 2;
        Var a, b: Array[Int, 5];
        s = lit * lit * Self.myPI;
        a[0] = s;
    }
}"""
        expect = "Error on line 14 col 15: ("
        self.assertTrue(TestParser.test(input,expect,241))
    def test_stmt3(self):
        input = """
Class Program {
    Val $numOfShape: Int = 0;
    Val immutableAttribute: Int = 0;
    Var length, width: Int;
    Val My1stCons, My2ndCons: Int = 1 + 5, 2;
    Var $x, $y : Int = 0, 0; 
    $getArea() {
        Return Self.length * Self.width;
    }
    $getArea() {
        Return Self.length * Self.width;
    }
    _getArea() {
        Var lit, s: Int;
        lit = 2;
        Var a, b: Array[Int, 5];
        s = lit * lit * Self.myPI;
        a[0] = s;
        Break;
        Break;
        Break;
        Continue;
        Break;
        Continue;
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,242))
    def test_stmt4(self):
        input = """
Class Program {
    Val $numOfShape: Int = 0;
    Val immutableAttribute: Int = 0;
    Var length, width: Int;
    Val My1stCons, My2ndCons: Int = 1 + 5, 2;
    Var $x, $y : Int = 0, 0; 
    $getArea() {
        Return Self.length * Self.width;
    }
    $getArea() {
        Break;
        Break;
        Break;
        {
            Continue;
            Break;
            Continue;
        }
        Return Self.length * Self.width;
    }
    _getArea() {
        Var lit, s: Int;
        lit = 2;
        Var a, b: Array[Int, 5];
        s = lit * lit * Self.myPI;
        a[0] = s;
    }
}"""
        expect = "Error on line 15 col 8: {"
        self.assertTrue(TestParser.test(input,expect,243))
    def test_stmt5(self):
        input = """
Class Program {
    Val $numOfShape: Int = 0;
    Val immutableAttribute: Int = 0;
    Var length, width: Int;
    Val My1stCons, My2ndCons: Int = 1 + 5, 2;
    Var $x, $y : Int = 0, 0; 
    $getArea() {
        Return Self.length * Self.width;
    }
    $getArea() {
        Return Self.length * Self.width;
    }
    _getArea() {
        Var lit, s: Int;
        lit = 2;
        Var a, b: Array[Int, 5];
        s = lit * lit * Self.myPI;
        a[0] = s;
        (Break;Break;Break;Continue;Break;Continue;)
    }
}"""
        expect = "Error on line 20 col 9: Break"
        self.assertTrue(TestParser.test(input,expect,244))
    def test_stmt6(self):
        input = """
Class Program {
    Val $numOfShape: Int = 0;
    Val immutableAttribute: Int = 0;
    Var length, width: Int;
    Val My1stCons, My2ndCons: Int = 1 + 5, 2;
    Var $x, $y : Int = 0, 0; 
    $getArea() {
        Return Self.length * Self.width;
    }
    $getArea() {
        Return Self.length * Self.width;
    }
    _getArea() {
        Var lit, s: Int;
        lit = 2;
        Var a, b: Array[Int, 5];
        s = lit * lit * Self.myPI;
        a[0] = s;
        Val My1stCons, My2ndCons: Int = 1 + 5, 2;
        Var $x, $y : Int = 0, 0;
        Val My1stCons213, __My2ndCons: Array[Array[String, 3], 3] = Array (Array("Volvo", "22", "18"),Array("Saab", "5", "2"),Array("Land Rover", "17", "15"));
        Var $m, $n : Array[String, 4] = Array("Kangxi", "Yongzheng", "Qianlong");
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,245))
    def test_stmt7(self):
        input = """
Class Program {
    Val $numOfShape: Int = 0;
    Val immutableAttribute: Int = 0;
    Var length, width: Int;
    Val My1stCons, My2ndCons: Int = 1 + 5, 2;
    Var $x, $y : Int = 0, 0; 
    $getArea() {
        Return Self.length * Self.width;
    }
    $getArea() {
        Return Self.length * Self.width;
    }
    _getArea() {
        Var lit, s: Int;
        lit = 2;
        Var a, b: Array[Int, 5];
        s = lit * lit * Self.myPI;
        a[0] = s;
        New X() = lit * lit * Self.myPI;
        New Arr(a,b,c,e,f,g,h,_QWER, My1stCons,My2ndCons) = X;
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,246))
    def test_stmt8(self):
        input = """
Class Program {
    Val $numOfShape: Int = 0;
    Val immutableAttribute: Int = 0;
    Var length, width: Int;
    Val My1stCons, My2ndCons: Int = 1 + 5, 2;
    Var $x, $y : Int = 0, 0; 
    $getArea() {
        Return Self.length * Self.width;
    }
    $getArea() {
        Return Self.length * Self.width;
    }
    _getArea() {
        Var lit, s: Int;
        lit = 2;
        Var a, b: Array[Int, 5];
        s = lit * lit * Self.myPI;
        a[0] = s;
        Out.printInt(Shape::$numOfShape);
        Out::printInt(Shape.$numOfShape);
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,247))
    def test_stmt9(self):
        input = """
Class Program {
    Val $numOfShape: Int = 0;
    Val immutableAttribute: Int = 0;
    Var length, width: Int;
    Val My1stCons, My2ndCons: Int = 1 + 5, 2;
    Var $x, $y : Int = 0, 0; 
    $getArea() {
        Return Self.length * Self.width;
    }
    $getArea() {
        Return Self.length * Self.width;
    }
    _getArea() {
        Var lit, s: Int;
        lit = 2;
        Var a, b: Array[Int, 5];
        s = lit * lit * Self.myPI;
        a[0] = s;
        New X() = lit * lit * Self.myPI;
        New Arr(a,b,c,e,f,g,h,_QWER, My1stCons,My2ndCons) = X;
        Out.printInt(Shape::$numOfShape);
        Out::printInt(Shape.$numOfShape);
        Break_1 1;
        Continue;
        Return X;
    }
}"""
        expect = "Error on line 24 col 16: 1"
        self.assertTrue(TestParser.test(input,expect,248))
    def test_stmt10(self):
        input = """
Class Program {
    Val $numOfShape: Int = 0;
    Val immutableAttribute: Int = 0;
    Var length, width: Int;
    Val My1stCons, My2ndCons: Int = 1 + 5, 2;
    Var $x, $y : Int = 0, 0; 
    $getArea() {
        Return Self.length * Self.width;
    }
    $getArea() {
        Return Self.length * Self.width;
    }
    _getArea() {
        Var lit, s: Int;
        lit = 2;
        Var a, b: Array[Int, 5];
        s = lit * lit * Self.myPI;
        a[0] = s;
        New X() = lit * lit * Self.myPI;
        New Arr(a,b,c,e,f,g,h,_QWER, My1stCons,My2ndCons) = X;
        Out.printInt(Shape::$numOfShape);
        Out::printInt(Shape.$numOfShape);
        DongNayKoCoYNghiaGiVaNoSeSai; ##Sao no ko sai##
        Continue;
        Return X;
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,249))

    #Test if stmt
    def test_if1(self):
        input = """
Class Shape {
    Val $numOfShape: Int = 0;
    Val immutableAttribute: Int = 0;
    Var length, width: Int;

    $getNumOfShape() {
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
        self.assertTrue(TestParser.test(input,expect,250))
    def test_if2(self):
        input = """
Class Shape {
    Val $numOfShape: Int = 0;
    Val immutableAttribute: Int = 0;
    Var length, width: Int;

    $getNumOfShape() {
        if(A[5] == 5){
            Out.printInt(arr[x]);
        }
    }
}
"""
        expect = "Error on line 8 col 10: ("
        self.assertTrue(TestParser.test(input,expect,251))
    def test_if3(self):
        input = """
Class Shape {
    Val $numOfShape: Int = 0;
    Val immutableAttribute: Int = 0;
    Var length, width: Int;

    $getNumOfShape() {
        If(1){
           If(1){
               If(1){
                   If(1){

                   }
                   Elseif{

                   }
               }
           }
        }
    }
}
"""
        expect = "Error on line 14 col 25: {"
        self.assertTrue(TestParser.test(input,expect,252))
    def test_if4(self):
        input = """
Class Shape {
    Val $numOfShape: Int = 0;
    Val immutableAttribute: Int = 0;
    Var length, width: Int;

    $getNumOfShape() {
        If(1){
           If(1){
               If(1){
                   Elseif(2){
                       
                   }
               }
           }
        }
    }
}
"""
        expect = "Error on line 11 col 19: Elseif"
        self.assertTrue(TestParser.test(input,expect,253))
    def test_if5(self):
        input = """
Class Shape {
    Val $numOfShape: Int = 0;
    Val immutableAttribute: Int = 0;
    Var length, width: Int;

    $getNumOfShape() {
        If(1){
           If(1){
               If(1){
                   If(3){

                   }
                   Elseif(5){
                       
                   }
                   Else{}
               }
               Else{}
           }
           Elseif(4){

           }
           Else{

           }
        }
        Elseif(6){
               
        }
        Else{

        }
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,254))
    def test_if6(self):
        input = """
Class Shape {
    Val $numOfShape: Int = 0;
    Val immutableAttribute: Int = 0;
    Var length, width: Int;

    $getNumOfShape() {
        If(){
            Out.printInt(arr[x]);
        }
    }
}
"""
        expect = "Error on line 8 col 11: )"
        self.assertTrue(TestParser.test(input,expect,255))
    def test_if7(self):
        input = """
Class Shape {
    Val $numOfShape: Int = 0;
    Val immutableAttribute: Int = 0;
    Var length, width: Int;

    $getNumOfShape() {
        If(A[5] == 5){
            Out.printInt(arr[x]);
        }
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,256))
    def test_if8(self):
        input = """
Class Shape {
    HorrorSence() {
        If(You::goDown(floor4)){
            If(You::goDown(floor3)){
                If(You::goDown(floor2)){
                    If(You::goDown(floor1)){
                        If(You::goDown(basement)){
                            Out.print("Hello Annabelle!");
                        }
                        Else{
                            You::goUp();
                        }
                    }
                    Else{
                        You::goUp();
                    }
                }
                Else{
                    You::goUp();
                }
            }
            Else{
                Out.print("You shouldn't go to the basement :)))");
            }
        }
        Else{
            Out.print("Roi mat vl :((");
        }                      
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,257))
    def test_if9(self):
        input = """
Class Shape {
    HorrorSence() {
        If(You::goDown(floor4))
        {
            If(You::goDown(floor3))
            {
                If(You::goDown(floor2))
                {
                    If(You::goDown(floor1))
                    {
                        If(You::goDown(basement))
                        {
                            Out.print("Hello Annabelle!");
                        }
                        Else{
                            You::goUp();
                        }
                    }
                    Else{
                        You::goUp();
                    }
                Else{
                    You::goUp();
                }
            }
            Else{
                Out.print("You shouldn't go to the basement :)))");
            }
        }
        Else{
            Out.print("Thieu thieu cai gi do :v");
        }                      
    }
}"""
        expect = "Error on line 23 col 16: Else"
        self.assertTrue(TestParser.test(input,expect,258))
    def test_if10(self):
        input = """
Class Shape {
    $LetMakeAStair() {
        Self.letMakeAStair(True);
        If(False)
        {
            ##do nothing##
        }
        Elseif(True)
        {
            If((a > b) && (a > c))
            {
                ##do nothing}}}}}}##
            }
            Else
            {
                If((A == B) || (A != C))
                {
                    ##
                    {
                        do nothing
                    }##
                }
                Else{##do nothing##}
            }
                            
        }
        Else
        {
            If((a > b) && (a > c))
            {
                ##do nothing}}}}}}##
            }
            Else
            {
                If((A == B) || (A != C))
                {
                    ##
                    {
                        do nothing
                    }##
                }
                Else{##do nothing##}
            }
        }
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,259))

    #Test loop stmt
    def test_loop1(self):
        input = """
Class Shape {
    $getNumOfShape() {
        Foreach (i In 1 .. 100 By 2) {
            Out.printInt(i);
        }
        Foreach (x In 5 .. 2) {
            Out.printInt(arr[x]);
        }
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,260))
    def test_loop2(self):
        input = """
Class Shape {
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
        self.assertTrue(TestParser.test(input,expect,261))
    def test_loop3(self):
        input = """
Class Shape {
    $getNumOfShape() {
        ForeacH (i In 1 .. 100 By 2) {
            Out.printInt(i);
        }
        Foreach (x In 5 .. 2) {
            Out.printInt(arr[x]);
        }
    }
}
"""
        expect = "Error on line 4 col 16: ("
        self.assertTrue(TestParser.test(input,expect,262))
    def test_loop4(self):
        input = """
Class Shape {
    $getNumOfShape() {
        foreach (i In 1 .. 100 By 2) {
            Out.printInt(i);
        }
        Foreach (x In 5 .. 2) {
            Out.printInt(arr[x]);
        }
    }
}
"""
        expect = "Error on line 4 col 16: ("
        self.assertTrue(TestParser.test(input,expect,263))
    def test_loop5(self):
        input = """
Class Shape {
    $getNumOfShape() {
        Foreach (i in 1 .. 100 By 2) {
            Out.printInt(i);
        }
        Foreach (x In 5 .. 2) {
            Out.printInt(arr[x]);
        }
    }
}
"""
        expect = "Error on line 4 col 19: in"
        self.assertTrue(TestParser.test(input,expect,264))
    def test_loop6(self):
        input = """
Class Shape {
    $getNumOfShape() {
        Foreach (i In 1 .. 100 by 2) {
            Out.printInt(i);
        }
        Foreach (x In 5 .. 2) {
            Out.printInt(arr[x]);
        }
    }
}
"""
        expect = "Error on line 4 col 31: by"
        self.assertTrue(TestParser.test(input,expect,265))
    def test_loop7(self):
        input = """
Class Shape {
    $getNumOfShape() {
        Foreach (i In Array(1,2,3,4,5) .. Array(6,7,8,9,10) By -Array()) {
            Out.printInt(i);
        }
        Foreach (x In 5 .. 2) {
            Out.printInt(arr[x]);
        }
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,266))
    def test_loop8(self):
        input = """
Class Shape {
    $getNumOfShape() {
        Foreach (i,t In 1 .. 100 By 2) {
            Out.printInt(i);
        }
        Foreach (x In 5 .. 2) {
            Out.printInt(arr[x]);
        }
    }
}
"""
        expect = "Error on line 4 col 18: ,"
        self.assertTrue(TestParser.test(input,expect,267))
    def test_loop9(self):
        input = """
Class Shape {
    $getNumOfShape() {
        Foreach (i In 1 .. 100 By 2) {
            Out.printInt(i);
        }
        Foreach (x In 5 ... 2) {
            Out.printInt(arr[x]);
        }
    }
}
"""
        expect = "Error on line 7 col 26: ."
        self.assertTrue(TestParser.test(input,expect,268))
    def test_loop10(self):
        input = """
Class Shape {
    $getNumOfShape() {
        Foreach (i In 1 .. 100 By 2) {
            Out.printInt(i);
            Foreach (x In 5 .. 2) {
                Out.printInt(arr[x]);
                Foreach (x In 5 .. 2) {
                    Out.printInt(arr[x]);
                    Foreach (i In 1 .. 100 By 2) {
                        Out.printInt(i);
                        Foreach (x In 5 .. 2) {
                            Out.printInt(arr[x]);
                            Foreach (x In 5 .. 2) {
                                Out.printInt(arr[x]);
                            } 
                        }
                    }
                }
            }
        }
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,269))

    #Test expressions
    def test_expr1(self):
        input = """
Class Shape {
    Val $numOfShape: Int = 0;
    Val immutableAttribute: Int = 0;
    Var length, width: Int;

    $getNumOfShape() {
        length = 5000_324234_3312 + -4.0E-15 * 4.14567 / 0xABCD1234 - 01234567 % 0b101010101;
        If(A[5] != 5){}
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,270))
    def test_expr2(self):
        input = """
Class Shape {
    $getNumOfShape() {
        length = Self.Something == Self.Nothing();
        length = Self.Something != Self.Nothing();
        length = Self.Something > Self.Nothing();
        length = Self.Something < Self.Nothing();
        length = Self.Something >= Self.Nothing();
        length = Self.Something <= Self.Nothing();
        If(A[5] != 5){}
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,271))
    def test_expr3(self):
        input = """
Class Shape {
    $getNumOfShape() {
        length = "Self.Something" +. "Self.Nothing()";
        length = "Self.Something" ==. "Self.Nothing()";
        If(A[5] != 5){}
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,272))
    def test_expr4(self):
        input = """
Class Shape {
    $getNumOfShape() {
        length = Self.Something || Self.Nothing() + A[Self::Athing()];
        length = Self.Something && Self.Nothing() % -Self::Athing();
        length = !Self.Something;
        length = !Self.Something && !Self.Nothing() * !Self::Athing();
        If(A[5] != 5){}
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,273))
    def test_expr5(self):
        input = """
Class Shape {
    $getNumOfShape() {
        length = Self.Something > Self.Nothing() || Self.Nothing() > Self::Athing();
        length = Self.Something > Self.Nothing() && Self.Nothing() > Self::Athing();
        If(A[5] != 5){}
    }
}
"""
        expect = "Error on line 4 col 67: >"
        self.assertTrue(TestParser.test(input,expect,274))
    def test_expr6(self):
        input = """
Class Shape {
    $getNumOfShape() {
        length = 50 + -4 * 4 / 4 - 1 % 7 || !Self.Nothing() % -Self.Something;
        If(A[5] != 5){}
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,275))
    def test_expr7(self):
        input = """
Class Shape {
    $getNumOfShape() {
        New X("50 + -4 * 4 / 4 - 1 % 7" || !Self.Nothing() % -Self.Something, Self.Something || Self.Nothing() + A[Self::Athing()], "Self.Something" +. "Self.Nothing()");
        If(A[5] != 5){}
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,276))
    def test_expr8(self):
        input = """
Class Shape {
    $getNumOfShape() {
        If(A[50 + -4 * 4 / 4 - 1 % 7] != Self.Nothing() +. A[Self::Athing()]){}
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,277))
    def test_expr9(self):
        input = """
Class Shape {
    $getNumOfShape() {
        length = Self.Something == Self.Nothing();
        length = Self.Something != Self.Nothing();
        length = Self.Something > Self.Nothing();
        length = Self.Something < Self.Nothing();
        length = Self.Something >= Self.Nothing();
        length = Self::Something <= Self.Nothing() == Self.Athing();
    }
}
"""
        expect = "Error on line 9 col 51: =="
        self.assertTrue(TestParser.test(input,expect,278))
    def test_expr10(self):
        input = """
Class Shape {
    $getNumOfShape() {
        If(A[A[A[Self1.Self2.AnotherSelf::$A[New X(5000_324234_3312 + -4.0E-15 * 4.14567 / 0xABCD1234 - 01234567 % 0b101010101 || !Self.Nothing() % -Self.Something, Self.Something || Self.Nothing() + A[Self::Athing()], "Self.Something" +. "Self.Nothing()")]]]] != 5){}
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,279))

    #Now Test everything
    def test_all1(self):
        input = """
Class Shape:Program {
    Val $numOfShape: Int = 0;
    Val immutableAttribute: Int = 0;
    Var length, width: Int;

    $getNumOfShape() {
        Foreach (i In 1 .. 100 By 2) {
            Out.printInt(i);
            Foreach (x In 5 .. 2) {
                Out.printInt(arr[x]);
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
    }
}
Class Program{
    Constructor(){
        Foreach (i In 1 .. 100 By 2) {
            Out.printInt(i);
            Foreach (x In 5 .. 2) {
                Out.printInt(arr[x]);
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
    }
    Main(){
        If(A[A[A[Self1.Self2.AnotherSelf::A[New X(5000_324234_3312 + -4.0E-15 * 4.14567 / 0xABCD1234 - 01234567 % 0b101010101 || !Self.Nothing() % -Self.Something, Self.Something || Self.Nothing() + A[Self::Athing()], "Self.Something" +. "Self.Nothing()")]]]] != 5){}
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,280))
    def test_all2(self):
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
        self.assertTrue(TestParser.test(input,expect,281))
    def test_all3(self):
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
            Return a / b * c - d + e != True;
        }
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,282))
    def test_all4(self):
        input = """
Class Shape {
    Val $numOfShape: Int = 0;
    Val immutableAttribute: Int = 0;
    Var length, width: Int;

    $getNumOfShape() {
        Return a[Program::$foo(a[b&&c],"test",True)];
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,283))
    def test_all5(self):
        input = """
Class Shape {
    Val $numOfShape: Int = 0;
    Val immutableAttribute: Int = 0;
    Var length, width: Int;

    $getNumOfShape() {
        If(Luoi.Lam.Roi(Toi) == True){
            Out::Print("Nghi thoi ko lam nua");
        }
        Else{
            Return "Co not cho xong vay";
        }
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,284))
    def test_all6(self):
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
        self.assertTrue(TestParser.test(input,expect,285))
    def test_all7(self):
        input = """
Class Shape {
    Val $numOfShape: Int = 0;
    Val immutableAttribute: Int = 0;
    Var length, width: Int;

    $getNumOfShape() {
        Foreach (i In 1 .. 100 By 2) {
            If(a >= b) {
                Break;
            } Else {
                Continue;
            }
        }
        Foreach (x In 5 .. 2) {
            Out.printInt(arr["Con vai test nua thoi nhi"]);
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
        self.assertTrue(TestParser.test(input,expect,286))
    def test_all8(self):
        input = """
Class Character {
    Val Name: String;
    Val HP, MP: Int = 100, 100;
    Val Atk, Def: Float = weapon_atk+base_atk, base_def+bonus_def;
    Var $luck, critical_dmg: Int = 5, 50;

    Constrctor(Name: Character){
        Self.Name = Name;
    }

    $getSpecialAbility(SkillName, Effect: String; Stat: Float; Cost: Int){
        Self.SkillName = SkillName;
        Self.Effect = Effect;
        Self.Stat = Stat;
        Self.Cost = Cost;
        Return Self.Name::PerformSkill(Self.Stat, Self.Cost);
    }

    PerformSkill(Dmg: Float; Cost: Int){
        Self.MP = Self.MP - Cost;
        Return Dmg;
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,287))
    def test_all9(self):
        input = """
Class Character {
    Val Name: String;
    Val HP, MP: Int = 100, 100;
    Val Atk, Def: Float = weapon_atk+base_atk, base_def+bonus_def;
    Var $luck, critical_dmg: Int = 5, 50;

    Constrctor(Name: Character){
        Self.Name = Name::Name;
    }

    $getSpecialAbility(SkillName, Effect: String; Stat: Float; Cost: Int){
        Self.SkillName = SkillName;
        Self.Effect = Effect;
        Self.Stat = Stat;
        Self.Cost = Cost;
        Return Self.Name::PerformSkill(Self.Stat, Self.Cost);
    }

    PerformSkill(Dmg: Float; Cost: Int){
        Self.MP = Self.MP - Cost;
        Return Dmg;
    }
}
Class Cloud_Strife:Charracter{
    Val Name: String; 
    Constrctor(){
        Self.Name = "Cloud";
        Self.SkillName = "Counter Attack";
        Self.Effect = "Yolo I don't know OK!!!";
        Self.Dmg = 20;
        Self.Cost = 10;
        Cloud_Strife.getSpecialAbility(Self.SkillName, Self.SkillName, Self.Effect, Self.Dmg, Self.Cost);
    }
}
Class Tifa_Lockhart:Charracter{
    Val Name: String; 
    Constrctor(){
        Self.Name = "Tifa";
        Self.SkillName = "Dance of Warth";
        Self.Effect = "Judgement Cut + Fiora's ulti???";
        Self.Dmg = 10 * 5;
        Self.Cost = 7 * 5;
        Tifa_Lockhart.getSpecialAbility(Self.SkillName, Self.SkillName, Self.Effect, Self.Dmg, Self.Cost);
    }
}
Class Aerith_Gainsborough:Charracter{
    Val Name: String; 
    Constrctor(){
        Self.Name = "Aerith";
        Self.SkillName = "Rays of judgement";
        Self.Effect = "Lux's ulti in URF";
        Self.Dmg = 45;
        Self.Cost = 45;
        Aerith_Gainsborough.getSpecialAbility(Self.SkillName, Self.SkillName, Self.Effect, Self.Dmg, Self.Cost);
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,288))
    def test_all10(self):
        input = """
Class Character {
    Val Name: String;
    Val HP, MP: Int = 100, 100;
    Val Atk, Def: Float = weapon_atk+base_atk, base_def+bonus_def;
    Var $luck, critical_dmg: Int = 5, 50;

    Constrctor(Name: Character){
        Self.Name = Name::Name;
    }

    $getSpecialAbility(SkillName, Effect: String; Stat: Float; Cost: Int){
        Self.SkillName = SkillName;
        Self.Effect = Effect;
        Self.Stat = Stat;
        Self.Cost = Cost;
        Return Self.Name::PerformSkill(Self.Stat, Self.Cost);
    }

    PerformSkill(Dmg: Float; Cost: Int){
        Self.MP = Self.MP - Cost;
        Return Dmg;
    }
}
Class Cloud_Strife:Charracter{
    Val Name: String; 
    Constrctor(){
        Self.Name = "Cloud";
        Self.SkillName = "Counter Attack";
        Self.Effect = "Yolo I don't know OK!!!";
        Self.Dmg = 20;
        Self.Cost = 10;
    }
}
Class Tifa_Lockhart:Charracter{
    Val Name: String; 
    Constrctor(){
        Self.Name = "Tifa";
        Self.SkillName = "Dance of Warth";
        Self.Effect = "Judgement Cut + Fiora's ulti???";
        Self.Dmg = 10 * 5;
        Self.Cost = 7 * 5;
    }
}
Class Aerith_Gainsborough:Charracter{
    Val Name: String; 
    Constrctor(){
        Self.Name = "Aerith";
        Self.SkillName = "Rays of judgement";
        Self.Effect = "Lux's ulti in URF";
        Self.Dmg = 45;
        Self.Cost = 45;
    }
}
Class Program{
    Main(){
        PhoeniS = New Tifa_Lockhart();
        PhoeniS.getSpecialAbility(PhoeniS.SkillName, PhoeniS.Effect, PhoeniS.Dmg, PhoeniS.Cost);
        Out.print(PhoeniS.Name, PhoeniS.SkillName, PhoeniS.MP);
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,289))

    #Test examples in pdf and bkel
    def test_simple_program1(self):
        input = """
Class main {}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,290))

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
        self.assertTrue(TestParser.test(input,expect,291))

    def test_simple_program3(self):
        input = """
Class Program {
    main() {
        Out.printInt(Shape::$numOfShape);
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,292))

    def test_simple_program4(self):
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
        self.assertTrue(TestParser.test(input,expect,293))
    
    def test_simple_program5(self):
        """Miss ( {"""
        input = """
Class Shape {
    $getNumOfShape( {
        Return Self.length * Self.width;
    }
}
"""
        expect = "Error on line 3 col 20: {"
        self.assertTrue(TestParser.test(input,expect,294))

    def test_more_complex_program1(self):
        input = """
Class Shape {
    Val $numOfShape: Int = 0;
    Val immutableAttribute: Int = 0;
    Var length, width: Int;
    Val My1stCons, My2ndCons: Int = 1 + 5, 2;
    Var $x, $y : Int = 0, 0;


    $getNumOfShape() {
        Return $numOfShape;
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,295))

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
        self.assertTrue(TestParser.test(input,expect,296))

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
        self.assertTrue(TestParser.test(input,expect,297))

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
        self.assertTrue(TestParser.test(input,expect,298))

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
        self.assertTrue(TestParser.test(input,expect,299))

    

    