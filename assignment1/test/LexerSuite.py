import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    
    #test id
    def test_id(self):
        self.assertTrue(TestLexer.test("Array_[_Array_]","Array_,[,_Array_,],<EOF>",100))
    def test_lowercase_id(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("abc","abc,<EOF>",101))
    def test_lower_upper_id(self):
        self.assertTrue(TestLexer.test("Beach","Beach,<EOF>",102))
    def test_mixed_id(self):
        self.assertTrue(TestLexer.test("aAsVN3","aAsVN3,<EOF>",103))
    def test_id1(self):
        """test identifiers"""
        input = "WriteLn"
        expect = "WriteLn,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,104))
    def test_id2(self):
        """test identifiers"""
        input = "writeln"
        expect = "writeln,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,105))
    def test_id3(self):
        """test identifiers"""
        input = "WRITELN"
        expect = "WRITELN,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,106))
    def test_id4(self):
        """test identifiers"""
        input = "_abc"
        expect = "_abc,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,107))
    def test_id5(self):
        """test identifiers"""
        input = "_Abc"
        expect = "_Abc,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,108))
    def test_id6(self):
        """test identifiers"""
        input = "0ZU"
        expect = "0,ZU,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,109))
    def test_id7(self):
        """test identifiers"""
        input = "_AbcDef_"
        expect = "_AbcDef_,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,110))
    def test_id8(self):
        """test identifiers"""
        input = "_AbcDef_190_"
        expect = "_AbcDef_190_,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,111))
    def test_id9(self):
        """test identifiers"""
        input = "9_opAHCB"
        expect = "9,_opAHCB,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,112))
    def test_id10(self):
        """test identifiers"""
        input = "$abc__123"
        expect = "$abc__123,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,113))
    def test_id11(self):
        """test wrong id"""
        self.assertTrue(TestLexer.test("ab?svn","ab,Error Token ?",114))

    #Test string
    def test_string1(self):
        """test another string"""
        input = """ "This is a string containing NOTHING" """
        expect = """This is a string containing NOTHING,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,115))
    def test_string2(self):
        """test another string"""
        input = """ "This is a random string" """
        expect = """This is a random string,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,116))
    def test_string3(self):
        """test another string"""
        input = """ "_YUVjhvdjsvcweh34uuwcejjcwvvwrebvwrb   rgewrverbrh fefegeg geregeg" """
        expect = """_YUVjhvdjsvcweh34uuwcejjcwvvwrebvwrb   rgewrverbrh fefegeg geregeg,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,117))
    def test_another_string1(self):
        """test another string"""
        input = """ "This is a string containing tab \t" """
        expect = """This is a string containing tab 	,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,118))
    def test_another_string2(self):
        """test another string"""
        input = """ "This is a string containing backspace \b" """
        expect = """This is a string containing backspace ,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,119))
    def test_another_string3(self):
        """test another string"""
        input = """ "This is a string containing form feed \f" """
        expect = """This is a string containing form feed ,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,120))
    def test_another_string4(self):
        """test another string"""
        input = """ "This is a string containing carriage return \r" """
        expect = """This is a string containing carriage return 
,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,121))
    def test_another_string5(self):
        """test another string"""
        input = """ "This is a string containing newline \n" """
        expect = """This is a string containing newline 

,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,122))
    def test_another_string6(self):
        """test another string"""
        input = """ "''This is a string'' containing single quotes '''''''''''" """
        expect = """''This is a string'' containing single quotes ''''''''''',<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,123))
    def test_another_string7(self):
        """test another string"""
        input = """ "This is a string containing backslash \\\\\\\\\ao that day " """
        expect = """Illegal Escape In String: This is a string containing backslash \\\\\\\\"""
        self.assertTrue(TestLexer.test(input,expect,124))
    def test_another_string8(self):
        """test another string"""
        input = """ "This is a string containing backslash \\\\\\\\\" """
        expect = """This is a string containing backslash \\\\\\\\,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,125))
    def test_another_string9(self):
        """test another string"""
        input = """ "He asked me: '"Where is John?'"" """
        expect = """He asked me: '"Where is John?'",<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,126))
    def test_illegal_Escape(self):
        """Illegal Escape"""
        input = """ "abc\\h def"  """
        expect = "Illegal Escape In String: abc\h"
        self.assertTrue(TestLexer.test(input,expect,127))
    def test_unclosed_String(self):
        """Unclosed String"""
        input = """ "abc def  """
        expect = "Unclosed String: abc def  "
        self.assertTrue(TestLexer.test(input,expect,128))

    #Test BRACKET
    def test_bracket_1(self):
        self.assertTrue(TestLexer.test("schedule(an_expression, sc_time [, sc_cycle]) (sc)","schedule,(,an_expression,,,sc_time,[,,,sc_cycle,],),(,sc,),<EOF>",129))
    def test_bracket_2(self):
        self.assertTrue(TestLexer.test("ABC (ABC1){ABCzyz();}","ABC,(,ABC1,),{,ABCzyz,(,),;,},<EOF>",130))
    def test_bracket_3(self):
        self.assertTrue(TestLexer.test("if ((a == 1)) {if ((b == 3)) {c = 4;}d = 5;}","if,(,(,a,==,1,),),{,if,(,(,b,==,3,),),{,c,=,4,;,},d,=,5,;,},<EOF>",131))
    def test_bracket_4(self):
        self.assertTrue(TestLexer.test("do a+b; while(a>1)","do,a,+,b,;,while,(,a,>,1,),<EOF>",132))
    def test_bracket_5(self):
        self.assertTrue(TestLexer.test("foo(foo(foo(foo(foo(foo())))))","foo,(,foo,(,foo,(,foo,(,foo,(,foo,(,),),),),),),<EOF>",133))

    #Test OP
    def test_op_1(self):
        self.assertTrue(TestLexer.test("a||b+b!=c","a,||,b,+,b,!=,c,<EOF>",134))
    def test_op_2(self):
        self.assertTrue(TestLexer.test("a>c>=&&*!c","a,>,c,>=,&&,*,!,c,<EOF>",135))
    def test_op_3(self):
        self.assertTrue(TestLexer.test("!a!d=abc>c=d==e","!,a,!,d,=,abc,>,c,=,d,==,e,<EOF>",136))
    def test_op_4(self):
        self.assertTrue(TestLexer.test("a+b-c/*d","a,+,b,-,c,/,*,d,<EOF>",137))
    def test_op_5(self):
        self.assertTrue(TestLexer.test("!a&&b+(a||c)+d","!,a,&&,b,+,(,a,||,c,),+,d,<EOF>",138))
    def test_op_6(self):
        self.assertTrue(TestLexer.test("a<=c+d % d","a,<=,c,+,d,%,d,<EOF>",139))
    def test_op_7(self):
        self.assertTrue(TestLexer.test("a-b-c+e%f","a,-,b,-,c,+,e,%,f,<EOF>",140))
    def test_op_8(self):
        self.assertTrue(TestLexer.test("a||c>d+e--f","a,||,c,>,d,+,e,-,-,f,<EOF>",141))
    def test_op_9(self):
        self.assertTrue(TestLexer.test("a++++++++++","a,+,+,+,+,+,+,+,+,+,+,<EOF>",142))
    def test_op_10(self):
        self.assertTrue(TestLexer.test(">>===abc",">,>=,==,abc,<EOF>",143))

    #MIX1
    def test_mix_1(self):
        self.assertTrue(TestLexer.test(" Array[j] = Array[j] * 10 + (str[i] - 48);","Array,[,j,],=,Array,[,j,],*,10,+,(,str,[,i,],-,48,),;,<EOF>",144))
    def test_mix_2(self):
        self.assertTrue(TestLexer.test(" FILE *file_o = fopen ( filename_o, w );","FILE,*,file_o,=,fopen,(,filename_o,,,w,),;,<EOF>",145))
    def test_mix_3(self):
        self.assertTrue(TestLexer.test(" int str_length = strlen(str);","int,str_length,=,strlen,(,str,),;,<EOF>",146))
    def test_mix_4(self):
        self.assertTrue(TestLexer.test("i = 0; str[i] != 0; i++","i,=,0,;,str,[,i,],!=,0,;,i,+,+,<EOF>",147))

    #Test Comment
    def test_cmt_1(self):
        self.assertTrue(TestLexer.test("##_122/*/*/./*/*/*/*/*/#","Error Token #",148))
    def test_cmt_2(self):
        input = """ ## This is a
        dcwevwevw\\\<?>:::">>:L::@$%^&*())(&%$#!~)
        ({}|)
multi-line
comment.
## """
        expect = """<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,149))
    def test_cmt_3(self):
        input = """
        ##_fe4io8whoigo34eghio34??L::<:;';~~~\\\\|||****&^^^&&%^^%$#@#$%%^&%&&%||||////###
        """ 
        expect = "Error Token #"
        self.assertTrue(TestLexer.test(input,expect,150))
    def test_cmt_4(self):
        input = """##_fe4io8whoigo34eghio34??L::<:;';~~~\\\\|||****&^^^&&%^^%$#@#$%%^&%&&%||||////##""" 
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input,expect,151))
  
    #Test int
    def test_another_integer7(self):
        """test another integer"""
        input = "0123"
        expect = "0123,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,152))
    def test_another_integer8(self):
        """test another integer"""
        input = "0x1A"
        expect = "0x1A,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,153))
    def test_another_integer9(self):
        """test another integer"""
        input = "0b11111111"
        expect = "0b11111111,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,154))
    def test_another_integer10(self):
        """test another integer"""
        input = "1_234_567"
        expect = "1234567,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,155))
    def test_another_integer11(self):
        """test another integer"""
        input = "1234"
        expect = "1234,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,156))
    def test_another_integer12(self):
        """test another integer"""
        input = "0"
        expect = "0,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,157))
    def test_another_integer13(self):
        """test another integer"""
        input = "0989898"
        expect = "0,989898,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,158))
    def test_another_integer14(self):
        """test another integer"""
        input = "1___234_567_"
        expect = "1,___234_567_,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,159))

    #Test float
    def test_another_float1(self):
        """test another float"""
        input = "1.0"
        expect = "1.0,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,160))
    def test_another_float2(self):
        """test another float"""
        input = "1.2e3"
        expect = "1.2e3,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,161))
    def test_another_float3(self):
        """test another float"""
        input = "7E-10"
        expect = "7E-10,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,162))
    def test_another_float4(self):
        """test another float"""
        input = "1_234.567"
        expect = "1234.567,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,163))
    def test_another_float5(self):
        """test another float"""
        input = ".0e12,0.e13,,.0E-0"
        expect = ".,0e12,,,0,.,e13,,,,,.,0E-0,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,164))
    def test_another_float6(self):
        """test another float"""
        input = " e= 0.33E-3 e=128e-42"
        expect = "e,=,0.33E-3,e,=,128e-42,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,165))
    def test_another_float7(self):
        """test another float"""
        input = "33E-33.33E-33.33"
        expect = "33E-33,.,33E-33,.,33,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,166))
    def test_another_float8(self):
        """test another float"""
        input = "13.4e+-3.5 hm"
        expect = "13.4,e,+,-,3.5,hm,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,167))
    def test_another_float9(self):
        """test another float"""
        input = "325.432e---3"
        expect = "325.432,e,-,-,-,3,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,168))
    def test_another_float10(self):
        """test another float"""
        input = "1e1.2E2.3e3.4E4.5e5.6E6.7e7.8E8.9e9.Ezzz"
        expect = "1e1,.,2E2,.,3e3,.,4E4,.,5e5,.,6E6,.,7e7,.,8E8,.,9e9,.,Ezzz,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,169))
    def test_another_float11(self):
        """test another float"""
        input = "a=1.2 a=1. a=.1 a=1ecde2 a=1.2E-2 e=1.2e-2 c=e-42"
        expect = "a,=,1.2,a,=,1,.,a,=,.,1,a,=,1,ecde2,a,=,1.2E-2,e,=,1.2e-2,c,=,e,-,42,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,170))
    
    #UNCLOSED
    def test_unclose_string_1(self):
        self.assertTrue(TestLexer.test(""" "123a\\n123 ""","Unclosed String: 123a\\n123 ",171))
    def test_unclose_string_2(self):
        self.assertTrue(TestLexer.test(""" "123a\n\n ""","""Unclosed String: 123a



 """,172))
    def test_unclose_string_3(self):
        self.assertTrue(TestLexer.test(""" "a" "aa" "" " ""","a,aa,,Unclosed String:  ",173))
    def test_unclose_string_4(self):
        self.assertTrue(TestLexer.test(""" "\\123a\\n123 ""","Illegal Escape In String: \\123",174))
    def test_unclose_string_5(self):
        self.assertTrue(TestLexer.test(""" "abc"xyz"mnl ""","abc,xyz,Unclosed String: mnl ",175))
    def test_unclose_string_6(self):
        self.assertTrue(TestLexer.test(""" print("div none,a[13]); ""","print,(,Unclosed String: div none,a[13]); ",176))
    def test_unclose_string_7(self):
        self.assertTrue(TestLexer.test(""" scanf("abc,); ""","scanf,(,Unclosed String: abc,); ",177))
    def test_unclose_string_8(self):
        self.assertTrue(TestLexer.test(""" _abc="//abcd ""","_abc,=,Unclosed String: //abcd ",178))
        
    #ILLEGAL ESCAPE
    def test_illegal_escape_1(self):
        self.assertTrue(TestLexer.test(""" 123 "123a\\m123" ""","123,Illegal Escape In String: 123a\\m",179))
    def test_illegal_escape_2(self):
        self.assertTrue(TestLexer.test(""" 123 "123a\\\\\\m123" ""","123,Illegal Escape In String: 123a\\\\\\m",180))
    def test_illegal_escape_3(self):
        self.assertTrue(TestLexer.test(""" "123a\\m123""\\a" ""","Illegal Escape In String: 123a\\m",181))
    def test_illegal_escape_4(self):
        self.assertTrue(TestLexer.test(""" "123a\\am123" ""","Illegal Escape In String: 123a\\a",182))
    def test_illegal_escape_5(self):
        self.assertTrue(TestLexer.test(""" "\\\a // 123a\\m123" ""","Illegal Escape In String: \",183))
    def test_illegal_escape_6(self):
        self.assertTrue(TestLexer.test(""" "\\!" "123a\\m123" ""","Illegal Escape In String: \\!",184))
    def test_illegal_escape_7(self):
        self.assertTrue(TestLexer.test("""  "123""a\\****m123" ""","123,Illegal Escape In String: a\\*",185))
    def test_illegal_escape_8(self):
        self.assertTrue(TestLexer.test(""" "123a\\_sncxyz123" ""","Illegal Escape In String: 123a\\_",186))

    #ERROR CHAR
    def test_error_char_1(self):
        self.assertTrue(TestLexer.test(""" ""??"" """,",Error Token ?",187))
    def test_error_char_2(self):
        self.assertTrue(TestLexer.test(" print('error?');  ","print,(,Error Token '",188))
    def test_error_char_3(self):
        self.assertTrue(TestLexer.test(" _@abc=xyz ","_,Error Token @",189))
    def test_error_char_4(self):
        self.assertTrue(TestLexer.test(" 12..12*.e-6 ","12,..,12,*,.,e,-,6,<EOF>",190))
    def test_error_char_5(self):
        self.assertTrue(TestLexer.test(" _abc/? ","_abc,/,Error Token ?",191))
    def test_error_char_6(self):
        self.assertTrue(TestLexer.test(" a&b=true","a,Error Token &",192))
    def test_error_char_7(self):
        self.assertTrue(TestLexer.test("_#######Test ","_,Error Token #",193)) ##Block cmt

    #MIX2
    def test_overall24(self):
        self.assertTrue(TestLexer.test("3.4e-2*35(abc[5],AV)","3.4e-2,*,35,(,abc,[,5,],,,AV,),<EOF>",194))
    def test_overall25(self):
        self.assertTrue(TestLexer.test("\"Teacher1: \",\"\\b\\f\\rMy students are too lazy\"","Teacher1: ,,,\\b\\f\\rMy students are too lazy,<EOF>",195))
    def test_overall26(self):
        self.assertTrue(TestLexer.test("\"Teacher2: \",\"Just be harder!, like this: \\\\\\\\\\b\\f\\r\\\\\\\\\"","Teacher2: ,,,Just be harder!, like this: \\\\\\\\\\b\\f\\r\\\\\\\\,<EOF>",196))

    #Test some keyword, op, se
    def test_keyword(self):
        """test another bool"""
        input = """
Break Continue If Elseif Else
Foreach True False Array In
Int Float Boolean String Return
Null Class Val Var Self
Constructor Destructor New By
"""
        expect = "Break,Continue,If,Elseif,Else,Foreach,True,False,Array,In,Int,Float,Boolean,String,Return,Null,Class,Val,Var,Self,Constructor,Destructor,New,By,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,197))
    def test_operator_notation(self):
        """test another bool"""
        input = """
+ - * / %
! && || == =
!= < <= > >=
==. +. . :: New
"""
        expect = "+,-,*,/,%,!,&&,||,==,=,!=,<,<=,>,>=,==.,+.,.,::,New,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,198))
    def test_seperators(self):
        """test another bool"""
        input = """
( ) [ ] . , ; : { }
"""
        expect = "(,),[,],.,,,;,:,{,},<EOF>"
        self.assertTrue(TestLexer.test(input,expect,199))