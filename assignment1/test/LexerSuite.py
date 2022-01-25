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