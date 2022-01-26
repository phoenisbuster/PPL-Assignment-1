import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_lowercase_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("abc","abc,<EOF>",101))
    def test_lower_upper_id(self):
        self.assertTrue(TestLexer.test("Break","Break,<EOF>",102))
    def test_mixed_id(self):
        self.assertTrue(TestLexer.test("aAsVN3","aAsVN3,<EOF>",103))
    def test_integer(self):
        """test integers"""
        input = """ "abc\\h def"  """
        expect = "Illegal Escape In String: abc\h"
        self.assertTrue(TestLexer.test(input,expect,104))
    def test_string(self):
        """test string"""
        self.assertTrue(TestLexer.test("ab?svn","ab,Error Token ?",105))

    def test_another_integer(self):
        """test another integer"""
        input = """ "abc def  """
        expect = "Unclosed String: abc def  "
        self.assertTrue(TestLexer.test(input,expect,106))

    def test_another_integer7(self):
        """test another integer"""
        input = "0123"
        expect = "0123,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,107))

    def test_another_integer8(self):
        """test another integer"""
        input = "0x1A"
        expect = "0x1A,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,108))

    def test_another_integer9(self):
        """test another integer"""
        input = "0b11111111"
        expect = "0b11111111,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,109))

    def test_another_integer10(self):
        """test another integer"""
        input = "1_234_567"
        expect = "1234567,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,110))

    def test_another_integer11(self):
        """test another integer"""
        input = "1234"
        expect = "1234,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,111))

    def test_another_float1(self):
        """test another float"""
        input = "1.234"
        expect = "1.234,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,112))

    def test_another_float2(self):
        """test another float"""
        input = "1.2e3"
        expect = "1.2e3,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,113))

    def test_another_float3(self):
        """test another float"""
        input = "7E-10"
        expect = "7E-10,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,114))

    def test_another_float4(self):
        """test another float"""
        input = "1_234.567"
        expect = "1234.567,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,115))

    def test_another_float5(self):
        """test another float"""
        input = "1_234.5_67"
        expect = "1234.567,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,116))

    def test_another_string1(self):
        """test another string"""
        input = """ "This is a string containing tab \t" """
        expect = """"This is a string containing tab 	",<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,117))

    def test_another_string2(self):
        """test another string"""
        input = """ "He asked me: '"Where is John?'"" """
        expect = """"He asked me: '"Where is John?'"",<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,118))

    def test_another_array1(self):
        """test another array"""
        input = "Array(1, 5, 7, 12)"
        expect = "Array(1, 5, 7, 12),<EOF>"
        self.assertTrue(TestLexer.test(input,expect,119))

    def test_another_array2(self):
        """test another array"""
        input = """Array("Kangxi", "Yongzheng", "Qianlong")"""
        expect = """Array("Kangxi", "Yongzheng", "Qianlong"),<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,120))

    def test_another_bool1(self):
        """test another bool"""
        input = "True"
        expect = "True,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,121))

    def test_another_bool2(self):
        """test another bool"""
        input = "False"
        expect = "False,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,122))