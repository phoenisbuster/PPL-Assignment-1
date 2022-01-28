# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2S")
        buf.write("\u02d5\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\t")
        buf.write("U\4V\tV\4W\tW\4X\tX\4Y\tY\4Z\tZ\4[\t[\4\\\t\\\4]\t]\4")
        buf.write("^\t^\4_\t_\4`\t`\4a\ta\4b\tb\3\2\3\2\3\3\3\3\3\3\3\4\3")
        buf.write("\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13")
        buf.write("\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20\3")
        buf.write("\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\24\3\24\7\24")
        buf.write("\u00ef\n\24\f\24\16\24\u00f2\13\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\25\3\25\5\25\u00fb\n\25\3\26\3\26\7\26\u00ff\n")
        buf.write("\26\f\26\16\26\u0102\13\26\3\27\3\27\6\27\u0106\n\27\r")
        buf.write("\27\16\27\u0107\3\30\3\30\3\30\3\30\5\30\u010e\n\30\3")
        buf.write("\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\5\31\u0118\n\31")
        buf.write("\3\31\3\31\3\32\3\32\3\33\3\33\5\33\u0120\n\33\3\33\6")
        buf.write("\33\u0123\n\33\r\33\16\33\u0124\3\34\3\34\7\34\u0129\n")
        buf.write("\34\f\34\16\34\u012c\13\34\3\35\3\35\3\35\7\35\u0131\n")
        buf.write("\35\f\35\16\35\u0134\13\35\3\35\5\35\u0137\n\35\3\35\6")
        buf.write("\35\u013a\n\35\r\35\16\35\u013b\7\35\u013e\n\35\f\35\16")
        buf.write("\35\u0141\13\35\5\35\u0143\n\35\3\36\3\36\3\36\7\36\u0148")
        buf.write("\n\36\f\36\16\36\u014b\13\36\3\37\3\37\3\37\3\37\7\37")
        buf.write("\u0151\n\37\f\37\16\37\u0154\13\37\3 \3 \3 \3 \7 \u015a")
        buf.write("\n \f \16 \u015d\13 \3!\3!\5!\u0161\n!\3\"\3\"\3\"\7\"")
        buf.write("\u0166\n\"\f\"\16\"\u0169\13\"\3\"\3\"\3\"\3\"\7\"\u016f")
        buf.write("\n\"\f\"\16\"\u0172\13\"\3\"\3\"\7\"\u0176\n\"\f\"\16")
        buf.write("\"\u0179\13\"\3\"\3\"\3\"\3#\3#\3#\7#\u0181\n#\f#\16#")
        buf.write("\u0184\13#\3#\3#\7#\u0188\n#\f#\16#\u018b\13#\3#\3#\7")
        buf.write("#\u018f\n#\f#\16#\u0192\13#\3#\3#\3$\3$\3$\7$\u0199\n")
        buf.write("$\f$\16$\u019c\13$\3$\3$\3$\3$\7$\u01a2\n$\f$\16$\u01a5")
        buf.write("\13$\3$\3$\7$\u01a9\n$\f$\16$\u01ac\13$\3$\3$\3$\3%\3")
        buf.write("%\3%\3&\3&\3&\3&\3&\5&\u01b9\n&\3\'\3\'\3\'\3\'\3\'\3")
        buf.write("\'\3\'\3\'\3\'\5\'\u01c4\n\'\3(\3(\3(\3(\3(\3(\3(\3)\3")
        buf.write(")\3*\3*\3*\3+\3+\3+\3+\3+\3+\3+\3+\3,\3,\3,\3,\3,\3-\3")
        buf.write("-\3-\3-\3-\3-\3.\3.\3.\3.\3.\3.\3.\3.\3.\3/\3/\3/\3\60")
        buf.write("\3\60\3\60\3\60\3\60\3\60\3\60\3\61\3\61\3\61\3\61\3\61")
        buf.write("\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\63\3\63\3\63")
        buf.write("\3\63\3\63\3\64\3\64\3\64\3\64\3\64\3\64\3\65\3\65\3\65")
        buf.write("\3\65\3\65\3\65\3\66\3\66\3\66\3\67\3\67\3\67\3\67\38")
        buf.write("\38\38\38\38\38\39\39\39\39\39\39\39\39\3:\3:\3:\3:\3")
        buf.write(":\3:\3:\3;\3;\3;\3;\3;\3;\3;\3<\3<\3<\3<\3<\3<\3=\3=\3")
        buf.write("=\3=\3=\3>\3>\3>\3>\3?\3?\3?\3?\3@\3@\3@\3@\3@\3A\3A\3")
        buf.write("A\3A\3A\3A\3A\3A\3A\3A\3A\3A\3B\3B\3B\3B\3B\3B\3B\3B\3")
        buf.write("B\3B\3B\3C\3C\3C\3C\3D\3D\3D\3E\3E\3E\3E\3E\3E\3E\3E\3")
        buf.write("E\3E\3E\3E\3E\3E\3E\3E\3E\3E\3E\3E\3E\3E\3E\3E\3E\3E\3")
        buf.write("E\5E\u028a\nE\3F\3F\3G\3G\3H\3H\3I\3I\3J\3J\3K\3K\3L\3")
        buf.write("L\3L\3M\3M\3M\3N\3N\3N\3O\3O\3O\3P\3P\3Q\3Q\3R\3R\3S\3")
        buf.write("S\3S\3T\3T\3T\3U\3U\3U\3U\3V\3V\3V\3W\3W\3W\3X\3X\3Y\3")
        buf.write("Y\3Z\3Z\3[\3[\3\\\3\\\3]\3]\3^\3^\3_\3_\3`\3`\3a\6a\u02cd")
        buf.write("\na\ra\16a\u02ce\3a\3a\3b\3b\3b\3\u00f0\2c\3\3\5\4\7\5")
        buf.write("\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35")
        buf.write("\20\37\21!\22#\23%\24\'\25)\26+\2-\2/\27\61\30\63\2\65")
        buf.write("\2\67\29\2;\2=\2?\2A\31C\32E\33G\34I\2K\2M\2O\2Q\2S\2")
        buf.write("U\35W\36Y\37[ ]!_\"a#c$e%g&i\'k(m)o*q+s,u-w.y/{\60}\61")
        buf.write("\177\62\u0081\63\u0083\64\u0085\65\u0087\66\u0089\2\u008b")
        buf.write("\67\u008d8\u008f9\u0091:\u0093;\u0095<\u0097=\u0099>\u009b")
        buf.write("?\u009d@\u009fA\u00a1B\u00a3C\u00a5D\u00a7E\u00a9F\u00ab")
        buf.write("G\u00adH\u00afI\u00b1J\u00b3K\u00b5L\u00b7M\u00b9N\u00bb")
        buf.write("O\u00bdP\u00bfQ\u00c1R\u00c3S\3\2\25\5\2C\\aac|\6\2\62")
        buf.write(";C\\aac|\4\2GGgg\4\2--//\3\2\62;\3\2\63;\3\2\629\4\2\62")
        buf.write("9aa\4\2ZZzz\4\2\62;CH\5\2\62;CHaa\4\2DDdd\3\2\62\63\4")
        buf.write("\2\62\63aa\3\2$$\4\2$$^^\t\2))^^ddhhppttvv\5\2\62;CHc")
        buf.write("h\5\2\n\f\16\17\"\"\2\u0307\2\3\3\2\2\2\2\5\3\2\2\2\2")
        buf.write("\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3")
        buf.write("\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2")
        buf.write("\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2")
        buf.write("\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2")
        buf.write("\2\2\2/\3\2\2\2\2\61\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E")
        buf.write("\3\2\2\2\2G\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2")
        buf.write("[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2")
        buf.write("\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2")
        buf.write("\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2")
        buf.write("\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2")
        buf.write("\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087")
        buf.write("\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2")
        buf.write("\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u0097")
        buf.write("\3\2\2\2\2\u0099\3\2\2\2\2\u009b\3\2\2\2\2\u009d\3\2\2")
        buf.write("\2\2\u009f\3\2\2\2\2\u00a1\3\2\2\2\2\u00a3\3\2\2\2\2\u00a5")
        buf.write("\3\2\2\2\2\u00a7\3\2\2\2\2\u00a9\3\2\2\2\2\u00ab\3\2\2")
        buf.write("\2\2\u00ad\3\2\2\2\2\u00af\3\2\2\2\2\u00b1\3\2\2\2\2\u00b3")
        buf.write("\3\2\2\2\2\u00b5\3\2\2\2\2\u00b7\3\2\2\2\2\u00b9\3\2\2")
        buf.write("\2\2\u00bb\3\2\2\2\2\u00bd\3\2\2\2\2\u00bf\3\2\2\2\2\u00c1")
        buf.write("\3\2\2\2\2\u00c3\3\2\2\2\3\u00c5\3\2\2\2\5\u00c7\3\2\2")
        buf.write("\2\7\u00ca\3\2\2\2\t\u00cc\3\2\2\2\13\u00ce\3\2\2\2\r")
        buf.write("\u00d0\3\2\2\2\17\u00d2\3\2\2\2\21\u00d4\3\2\2\2\23\u00d6")
        buf.write("\3\2\2\2\25\u00d8\3\2\2\2\27\u00da\3\2\2\2\31\u00dc\3")
        buf.write("\2\2\2\33\u00de\3\2\2\2\35\u00e0\3\2\2\2\37\u00e2\3\2")
        buf.write("\2\2!\u00e4\3\2\2\2#\u00e6\3\2\2\2%\u00e8\3\2\2\2\'\u00ea")
        buf.write("\3\2\2\2)\u00fa\3\2\2\2+\u00fc\3\2\2\2-\u0103\3\2\2\2")
        buf.write("/\u010d\3\2\2\2\61\u0111\3\2\2\2\63\u011b\3\2\2\2\65\u011d")
        buf.write("\3\2\2\2\67\u0126\3\2\2\29\u0142\3\2\2\2;\u0144\3\2\2")
        buf.write("\2=\u014c\3\2\2\2?\u0155\3\2\2\2A\u0160\3\2\2\2C\u0162")
        buf.write("\3\2\2\2E\u017d\3\2\2\2G\u0195\3\2\2\2I\u01b0\3\2\2\2")
        buf.write("K\u01b8\3\2\2\2M\u01c3\3\2\2\2O\u01c5\3\2\2\2Q\u01cc\3")
        buf.write("\2\2\2S\u01ce\3\2\2\2U\u01d1\3\2\2\2W\u01d9\3\2\2\2Y\u01de")
        buf.write("\3\2\2\2[\u01e4\3\2\2\2]\u01ed\3\2\2\2_\u01f0\3\2\2\2")
        buf.write("a\u01f7\3\2\2\2c\u01fc\3\2\2\2e\u0204\3\2\2\2g\u0209\3")
        buf.write("\2\2\2i\u020f\3\2\2\2k\u0215\3\2\2\2m\u0218\3\2\2\2o\u021c")
        buf.write("\3\2\2\2q\u0222\3\2\2\2s\u022a\3\2\2\2u\u0231\3\2\2\2")
        buf.write("w\u0238\3\2\2\2y\u023e\3\2\2\2{\u0243\3\2\2\2}\u0247\3")
        buf.write("\2\2\2\177\u024b\3\2\2\2\u0081\u0250\3\2\2\2\u0083\u025c")
        buf.write("\3\2\2\2\u0085\u0267\3\2\2\2\u0087\u026b\3\2\2\2\u0089")
        buf.write("\u0289\3\2\2\2\u008b\u028b\3\2\2\2\u008d\u028d\3\2\2\2")
        buf.write("\u008f\u028f\3\2\2\2\u0091\u0291\3\2\2\2\u0093\u0293\3")
        buf.write("\2\2\2\u0095\u0295\3\2\2\2\u0097\u0297\3\2\2\2\u0099\u029a")
        buf.write("\3\2\2\2\u009b\u029d\3\2\2\2\u009d\u02a0\3\2\2\2\u009f")
        buf.write("\u02a3\3\2\2\2\u00a1\u02a5\3\2\2\2\u00a3\u02a7\3\2\2\2")
        buf.write("\u00a5\u02a9\3\2\2\2\u00a7\u02ac\3\2\2\2\u00a9\u02af\3")
        buf.write("\2\2\2\u00ab\u02b3\3\2\2\2\u00ad\u02b6\3\2\2\2\u00af\u02b9")
        buf.write("\3\2\2\2\u00b1\u02bb\3\2\2\2\u00b3\u02bd\3\2\2\2\u00b5")
        buf.write("\u02bf\3\2\2\2\u00b7\u02c1\3\2\2\2\u00b9\u02c3\3\2\2\2")
        buf.write("\u00bb\u02c5\3\2\2\2\u00bd\u02c7\3\2\2\2\u00bf\u02c9\3")
        buf.write("\2\2\2\u00c1\u02cc\3\2\2\2\u00c3\u02d2\3\2\2\2\u00c5\u00c6")
        buf.write("\7<\2\2\u00c6\4\3\2\2\2\u00c7\u00c8\7\60\2\2\u00c8\u00c9")
        buf.write("\7\60\2\2\u00c9\6\3\2\2\2\u00ca\u00cb\5w<\2\u00cb\b\3")
        buf.write("\2\2\2\u00cc\u00cd\5q9\2\u00cd\n\3\2\2\2\u00ce\u00cf\5")
        buf.write("m\67\2\u00cf\f\3\2\2\2\u00d0\u00d1\5o8\2\u00d1\16\3\2")
        buf.write("\2\2\u00d2\u00d3\5s:\2\u00d3\20\3\2\2\2\u00d4\u00d5\5")
        buf.write("i\65\2\u00d5\22\3\2\2\2\u00d6\u00d7\5}?\2\u00d7\24\3\2")
        buf.write("\2\2\u00d8\u00d9\5{>\2\u00d9\26\3\2\2\2\u00da\u00db\5")
        buf.write("]/\2\u00db\30\3\2\2\2\u00dc\u00dd\5a\61\2\u00dd\32\3\2")
        buf.write("\2\2\u00de\u00df\5_\60\2\u00df\34\3\2\2\2\u00e0\u00e1")
        buf.write("\5c\62\2\u00e1\36\3\2\2\2\u00e2\u00e3\5k\66\2\u00e3 \3")
        buf.write("\2\2\2\u00e4\u00e5\5\u0087D\2\u00e5\"\3\2\2\2\u00e6\u00e7")
        buf.write("\5u;\2\u00e7$\3\2\2\2\u00e8\u00e9\5\u0085C\2\u00e9&\3")
        buf.write("\2\2\2\u00ea\u00eb\7%\2\2\u00eb\u00ec\7%\2\2\u00ec\u00f0")
        buf.write("\3\2\2\2\u00ed\u00ef\13\2\2\2\u00ee\u00ed\3\2\2\2\u00ef")
        buf.write("\u00f2\3\2\2\2\u00f0\u00f1\3\2\2\2\u00f0\u00ee\3\2\2\2")
        buf.write("\u00f1\u00f3\3\2\2\2\u00f2\u00f0\3\2\2\2\u00f3\u00f4\7")
        buf.write("%\2\2\u00f4\u00f5\7%\2\2\u00f5\u00f6\3\2\2\2\u00f6\u00f7")
        buf.write("\b\24\2\2\u00f7(\3\2\2\2\u00f8\u00fb\5+\26\2\u00f9\u00fb")
        buf.write("\5-\27\2\u00fa\u00f8\3\2\2\2\u00fa\u00f9\3\2\2\2\u00fb")
        buf.write("*\3\2\2\2\u00fc\u0100\t\2\2\2\u00fd\u00ff\t\3\2\2\u00fe")
        buf.write("\u00fd\3\2\2\2\u00ff\u0102\3\2\2\2\u0100\u00fe\3\2\2\2")
        buf.write("\u0100\u0101\3\2\2\2\u0101,\3\2\2\2\u0102\u0100\3\2\2")
        buf.write("\2\u0103\u0105\7&\2\2\u0104\u0106\t\3\2\2\u0105\u0104")
        buf.write("\3\2\2\2\u0106\u0107\3\2\2\2\u0107\u0105\3\2\2\2\u0107")
        buf.write("\u0108\3\2\2\2\u0108.\3\2\2\2\u0109\u010e\59\35\2\u010a")
        buf.write("\u010e\5;\36\2\u010b\u010e\5=\37\2\u010c\u010e\5? \2\u010d")
        buf.write("\u0109\3\2\2\2\u010d\u010a\3\2\2\2\u010d\u010b\3\2\2\2")
        buf.write("\u010d\u010c\3\2\2\2\u010e\u010f\3\2\2\2\u010f\u0110\b")
        buf.write("\30\3\2\u0110\60\3\2\2\2\u0111\u0117\5\63\32\2\u0112\u0118")
        buf.write("\5\67\34\2\u0113\u0118\5\65\33\2\u0114\u0115\5\67\34\2")
        buf.write("\u0115\u0116\5\65\33\2\u0116\u0118\3\2\2\2\u0117\u0112")
        buf.write("\3\2\2\2\u0117\u0113\3\2\2\2\u0117\u0114\3\2\2\2\u0118")
        buf.write("\u0119\3\2\2\2\u0119\u011a\b\31\4\2\u011a\62\3\2\2\2\u011b")
        buf.write("\u011c\59\35\2\u011c\64\3\2\2\2\u011d\u011f\t\4\2\2\u011e")
        buf.write("\u0120\t\5\2\2\u011f\u011e\3\2\2\2\u011f\u0120\3\2\2\2")
        buf.write("\u0120\u0122\3\2\2\2\u0121\u0123\t\6\2\2\u0122\u0121\3")
        buf.write("\2\2\2\u0123\u0124\3\2\2\2\u0124\u0122\3\2\2\2\u0124\u0125")
        buf.write("\3\2\2\2\u0125\66\3\2\2\2\u0126\u012a\5\u00bd_\2\u0127")
        buf.write("\u0129\t\6\2\2\u0128\u0127\3\2\2\2\u0129\u012c\3\2\2\2")
        buf.write("\u012a\u0128\3\2\2\2\u012a\u012b\3\2\2\2\u012b8\3\2\2")
        buf.write("\2\u012c\u012a\3\2\2\2\u012d\u0143\7\62\2\2\u012e\u013f")
        buf.write("\t\7\2\2\u012f\u0131\t\6\2\2\u0130\u012f\3\2\2\2\u0131")
        buf.write("\u0134\3\2\2\2\u0132\u0130\3\2\2\2\u0132\u0133\3\2\2\2")
        buf.write("\u0133\u0136\3\2\2\2\u0134\u0132\3\2\2\2\u0135\u0137\7")
        buf.write("a\2\2\u0136\u0135\3\2\2\2\u0136\u0137\3\2\2\2\u0137\u0139")
        buf.write("\3\2\2\2\u0138\u013a\t\6\2\2\u0139\u0138\3\2\2\2\u013a")
        buf.write("\u013b\3\2\2\2\u013b\u0139\3\2\2\2\u013b\u013c\3\2\2\2")
        buf.write("\u013c\u013e\3\2\2\2\u013d\u0132\3\2\2\2\u013e\u0141\3")
        buf.write("\2\2\2\u013f\u013d\3\2\2\2\u013f\u0140\3\2\2\2\u0140\u0143")
        buf.write("\3\2\2\2\u0141\u013f\3\2\2\2\u0142\u012d\3\2\2\2\u0142")
        buf.write("\u012e\3\2\2\2\u0143:\3\2\2\2\u0144\u0145\7\62\2\2\u0145")
        buf.write("\u0149\t\b\2\2\u0146\u0148\t\t\2\2\u0147\u0146\3\2\2\2")
        buf.write("\u0148\u014b\3\2\2\2\u0149\u0147\3\2\2\2\u0149\u014a\3")
        buf.write("\2\2\2\u014a<\3\2\2\2\u014b\u0149\3\2\2\2\u014c\u014d")
        buf.write("\7\62\2\2\u014d\u014e\t\n\2\2\u014e\u0152\t\13\2\2\u014f")
        buf.write("\u0151\t\f\2\2\u0150\u014f\3\2\2\2\u0151\u0154\3\2\2\2")
        buf.write("\u0152\u0150\3\2\2\2\u0152\u0153\3\2\2\2\u0153>\3\2\2")
        buf.write("\2\u0154\u0152\3\2\2\2\u0155\u0156\7\62\2\2\u0156\u0157")
        buf.write("\t\r\2\2\u0157\u015b\t\16\2\2\u0158\u015a\t\17\2\2\u0159")
        buf.write("\u0158\3\2\2\2\u015a\u015d\3\2\2\2\u015b\u0159\3\2\2\2")
        buf.write("\u015b\u015c\3\2\2\2\u015c@\3\2\2\2\u015d\u015b\3\2\2")
        buf.write("\2\u015e\u0161\5e\63\2\u015f\u0161\5g\64\2\u0160\u015e")
        buf.write("\3\2\2\2\u0160\u015f\3\2\2\2\u0161B\3\2\2\2\u0162\u0167")
        buf.write("\7$\2\2\u0163\u0164\7)\2\2\u0164\u0166\7$\2\2\u0165\u0163")
        buf.write("\3\2\2\2\u0166\u0169\3\2\2\2\u0167\u0165\3\2\2\2\u0167")
        buf.write("\u0168\3\2\2\2\u0168\u0170\3\2\2\2\u0169\u0167\3\2\2\2")
        buf.write("\u016a\u016f\5I%\2\u016b\u016f\n\20\2\2\u016c\u016d\7")
        buf.write(")\2\2\u016d\u016f\7$\2\2\u016e\u016a\3\2\2\2\u016e\u016b")
        buf.write("\3\2\2\2\u016e\u016c\3\2\2\2\u016f\u0172\3\2\2\2\u0170")
        buf.write("\u016e\3\2\2\2\u0170\u0171\3\2\2\2\u0171\u0177\3\2\2\2")
        buf.write("\u0172\u0170\3\2\2\2\u0173\u0174\7)\2\2\u0174\u0176\7")
        buf.write("$\2\2\u0175\u0173\3\2\2\2\u0176\u0179\3\2\2\2\u0177\u0175")
        buf.write("\3\2\2\2\u0177\u0178\3\2\2\2\u0178\u017a\3\2\2\2\u0179")
        buf.write("\u0177\3\2\2\2\u017a\u017b\7$\2\2\u017b\u017c\b\"\5\2")
        buf.write("\u017cD\3\2\2\2\u017d\u0182\7$\2\2\u017e\u017f\7)\2\2")
        buf.write("\u017f\u0181\7$\2\2\u0180\u017e\3\2\2\2\u0181\u0184\3")
        buf.write("\2\2\2\u0182\u0180\3\2\2\2\u0182\u0183\3\2\2\2\u0183\u0189")
        buf.write("\3\2\2\2\u0184\u0182\3\2\2\2\u0185\u0188\5I%\2\u0186\u0188")
        buf.write("\n\21\2\2\u0187\u0185\3\2\2\2\u0187\u0186\3\2\2\2\u0188")
        buf.write("\u018b\3\2\2\2\u0189\u0187\3\2\2\2\u0189\u018a\3\2\2\2")
        buf.write("\u018a\u0190\3\2\2\2\u018b\u0189\3\2\2\2\u018c\u018d\7")
        buf.write(")\2\2\u018d\u018f\7$\2\2\u018e\u018c\3\2\2\2\u018f\u0192")
        buf.write("\3\2\2\2\u0190\u018e\3\2\2\2\u0190\u0191\3\2\2\2\u0191")
        buf.write("\u0193\3\2\2\2\u0192\u0190\3\2\2\2\u0193\u0194\b#\6\2")
        buf.write("\u0194F\3\2\2\2\u0195\u019a\7$\2\2\u0196\u0197\7)\2\2")
        buf.write("\u0197\u0199\7$\2\2\u0198\u0196\3\2\2\2\u0199\u019c\3")
        buf.write("\2\2\2\u019a\u0198\3\2\2\2\u019a\u019b\3\2\2\2\u019b\u01a3")
        buf.write("\3\2\2\2\u019c\u019a\3\2\2\2\u019d\u01a2\n\21\2\2\u019e")
        buf.write("\u01a2\5I%\2\u019f\u01a0\7)\2\2\u01a0\u01a2\7$\2\2\u01a1")
        buf.write("\u019d\3\2\2\2\u01a1\u019e\3\2\2\2\u01a1\u019f\3\2\2\2")
        buf.write("\u01a2\u01a5\3\2\2\2\u01a3\u01a1\3\2\2\2\u01a3\u01a4\3")
        buf.write("\2\2\2\u01a4\u01aa\3\2\2\2\u01a5\u01a3\3\2\2\2\u01a6\u01a7")
        buf.write("\7)\2\2\u01a7\u01a9\7$\2\2\u01a8\u01a6\3\2\2\2\u01a9\u01ac")
        buf.write("\3\2\2\2\u01aa\u01a8\3\2\2\2\u01aa\u01ab\3\2\2\2\u01ab")
        buf.write("\u01ad\3\2\2\2\u01ac\u01aa\3\2\2\2\u01ad\u01ae\5K&\2\u01ae")
        buf.write("\u01af\b$\7\2\u01afH\3\2\2\2\u01b0\u01b1\7^\2\2\u01b1")
        buf.write("\u01b2\t\22\2\2\u01b2J\3\2\2\2\u01b3\u01b4\7^\2\2\u01b4")
        buf.write("\u01b9\n\22\2\2\u01b5\u01b9\5O(\2\u01b6\u01b9\5M\'\2\u01b7")
        buf.write("\u01b9\5S*\2\u01b8\u01b3\3\2\2\2\u01b8\u01b5\3\2\2\2\u01b8")
        buf.write("\u01b6\3\2\2\2\u01b8\u01b7\3\2\2\2\u01b9L\3\2\2\2\u01ba")
        buf.write("\u01bb\7^\2\2\u01bb\u01bc\4\62\65\2\u01bc\u01bd\4\629")
        buf.write("\2\u01bd\u01c4\4\629\2\u01be\u01bf\7^\2\2\u01bf\u01c0")
        buf.write("\4\629\2\u01c0\u01c4\4\629\2\u01c1\u01c2\7^\2\2\u01c2")
        buf.write("\u01c4\4\629\2\u01c3\u01ba\3\2\2\2\u01c3\u01be\3\2\2\2")
        buf.write("\u01c3\u01c1\3\2\2\2\u01c4N\3\2\2\2\u01c5\u01c6\7^\2\2")
        buf.write("\u01c6\u01c7\7w\2\2\u01c7\u01c8\5Q)\2\u01c8\u01c9\5Q)")
        buf.write("\2\u01c9\u01ca\5Q)\2\u01ca\u01cb\5Q)\2\u01cbP\3\2\2\2")
        buf.write("\u01cc\u01cd\t\23\2\2\u01cdR\3\2\2\2\u01ce\u01cf\7^\2")
        buf.write("\2\u01cf\u01d0\7j\2\2\u01d0T\3\2\2\2\u01d1\u01d2\7R\2")
        buf.write("\2\u01d2\u01d3\7t\2\2\u01d3\u01d4\7q\2\2\u01d4\u01d5\7")
        buf.write("i\2\2\u01d5\u01d6\7t\2\2\u01d6\u01d7\7c\2\2\u01d7\u01d8")
        buf.write("\7o\2\2\u01d8V\3\2\2\2\u01d9\u01da\7o\2\2\u01da\u01db")
        buf.write("\7c\2\2\u01db\u01dc\7k\2\2\u01dc\u01dd\7p\2\2\u01ddX\3")
        buf.write("\2\2\2\u01de\u01df\7D\2\2\u01df\u01e0\7t\2\2\u01e0\u01e1")
        buf.write("\7g\2\2\u01e1\u01e2\7c\2\2\u01e2\u01e3\7m\2\2\u01e3Z\3")
        buf.write("\2\2\2\u01e4\u01e5\7E\2\2\u01e5\u01e6\7q\2\2\u01e6\u01e7")
        buf.write("\7p\2\2\u01e7\u01e8\7v\2\2\u01e8\u01e9\7k\2\2\u01e9\u01ea")
        buf.write("\7p\2\2\u01ea\u01eb\7w\2\2\u01eb\u01ec\7g\2\2\u01ec\\")
        buf.write("\3\2\2\2\u01ed\u01ee\7K\2\2\u01ee\u01ef\7h\2\2\u01ef^")
        buf.write("\3\2\2\2\u01f0\u01f1\7G\2\2\u01f1\u01f2\7n\2\2\u01f2\u01f3")
        buf.write("\7u\2\2\u01f3\u01f4\7g\2\2\u01f4\u01f5\7k\2\2\u01f5\u01f6")
        buf.write("\7h\2\2\u01f6`\3\2\2\2\u01f7\u01f8\7G\2\2\u01f8\u01f9")
        buf.write("\7n\2\2\u01f9\u01fa\7u\2\2\u01fa\u01fb\7g\2\2\u01fbb\3")
        buf.write("\2\2\2\u01fc\u01fd\7H\2\2\u01fd\u01fe\7q\2\2\u01fe\u01ff")
        buf.write("\7t\2\2\u01ff\u0200\7g\2\2\u0200\u0201\7c\2\2\u0201\u0202")
        buf.write("\7e\2\2\u0202\u0203\7j\2\2\u0203d\3\2\2\2\u0204\u0205")
        buf.write("\7V\2\2\u0205\u0206\7t\2\2\u0206\u0207\7w\2\2\u0207\u0208")
        buf.write("\7g\2\2\u0208f\3\2\2\2\u0209\u020a\7H\2\2\u020a\u020b")
        buf.write("\7c\2\2\u020b\u020c\7n\2\2\u020c\u020d\7u\2\2\u020d\u020e")
        buf.write("\7g\2\2\u020eh\3\2\2\2\u020f\u0210\7C\2\2\u0210\u0211")
        buf.write("\7t\2\2\u0211\u0212\7t\2\2\u0212\u0213\7c\2\2\u0213\u0214")
        buf.write("\7{\2\2\u0214j\3\2\2\2\u0215\u0216\7K\2\2\u0216\u0217")
        buf.write("\7p\2\2\u0217l\3\2\2\2\u0218\u0219\7K\2\2\u0219\u021a")
        buf.write("\7p\2\2\u021a\u021b\7v\2\2\u021bn\3\2\2\2\u021c\u021d")
        buf.write("\7H\2\2\u021d\u021e\7n\2\2\u021e\u021f\7q\2\2\u021f\u0220")
        buf.write("\7c\2\2\u0220\u0221\7v\2\2\u0221p\3\2\2\2\u0222\u0223")
        buf.write("\7D\2\2\u0223\u0224\7q\2\2\u0224\u0225\7q\2\2\u0225\u0226")
        buf.write("\7n\2\2\u0226\u0227\7g\2\2\u0227\u0228\7c\2\2\u0228\u0229")
        buf.write("\7p\2\2\u0229r\3\2\2\2\u022a\u022b\7U\2\2\u022b\u022c")
        buf.write("\7v\2\2\u022c\u022d\7t\2\2\u022d\u022e\7k\2\2\u022e\u022f")
        buf.write("\7p\2\2\u022f\u0230\7i\2\2\u0230t\3\2\2\2\u0231\u0232")
        buf.write("\7T\2\2\u0232\u0233\7g\2\2\u0233\u0234\7v\2\2\u0234\u0235")
        buf.write("\7w\2\2\u0235\u0236\7t\2\2\u0236\u0237\7p\2\2\u0237v\3")
        buf.write("\2\2\2\u0238\u0239\7E\2\2\u0239\u023a\7n\2\2\u023a\u023b")
        buf.write("\7c\2\2\u023b\u023c\7u\2\2\u023c\u023d\7u\2\2\u023dx\3")
        buf.write("\2\2\2\u023e\u023f\7P\2\2\u023f\u0240\7w\2\2\u0240\u0241")
        buf.write("\7n\2\2\u0241\u0242\7n\2\2\u0242z\3\2\2\2\u0243\u0244")
        buf.write("\7X\2\2\u0244\u0245\7c\2\2\u0245\u0246\7n\2\2\u0246|\3")
        buf.write("\2\2\2\u0247\u0248\7X\2\2\u0248\u0249\7c\2\2\u0249\u024a")
        buf.write("\7t\2\2\u024a~\3\2\2\2\u024b\u024c\7U\2\2\u024c\u024d")
        buf.write("\7g\2\2\u024d\u024e\7n\2\2\u024e\u024f\7h\2\2\u024f\u0080")
        buf.write("\3\2\2\2\u0250\u0251\7E\2\2\u0251\u0252\7q\2\2\u0252\u0253")
        buf.write("\7p\2\2\u0253\u0254\7u\2\2\u0254\u0255\7v\2\2\u0255\u0256")
        buf.write("\7t\2\2\u0256\u0257\7w\2\2\u0257\u0258\7e\2\2\u0258\u0259")
        buf.write("\7v\2\2\u0259\u025a\7q\2\2\u025a\u025b\7t\2\2\u025b\u0082")
        buf.write("\3\2\2\2\u025c\u025d\7F\2\2\u025d\u025e\7g\2\2\u025e\u025f")
        buf.write("\7u\2\2\u025f\u0260\7v\2\2\u0260\u0261\7t\2\2\u0261\u0262")
        buf.write("\7w\2\2\u0262\u0263\7e\2\2\u0263\u0264\7v\2\2\u0264\u0265")
        buf.write("\7q\2\2\u0265\u0266\7t\2\2\u0266\u0084\3\2\2\2\u0267\u0268")
        buf.write("\7P\2\2\u0268\u0269\7g\2\2\u0269\u026a\7y\2\2\u026a\u0086")
        buf.write("\3\2\2\2\u026b\u026c\7D\2\2\u026c\u026d\7{\2\2\u026d\u0088")
        buf.write("\3\2\2\2\u026e\u028a\5Y-\2\u026f\u028a\5[.\2\u0270\u028a")
        buf.write("\5]/\2\u0271\u028a\5_\60\2\u0272\u028a\5a\61\2\u0273\u028a")
        buf.write("\3\2\2\2\u0274\u028a\5c\62\2\u0275\u028a\5e\63\2\u0276")
        buf.write("\u028a\5g\64\2\u0277\u028a\5i\65\2\u0278\u028a\5k\66\2")
        buf.write("\u0279\u028a\3\2\2\2\u027a\u028a\5m\67\2\u027b\u028a\5")
        buf.write("o8\2\u027c\u028a\5q9\2\u027d\u028a\5s:\2\u027e\u028a\5")
        buf.write("u;\2\u027f\u028a\3\2\2\2\u0280\u028a\5y=\2\u0281\u028a")
        buf.write("\5w<\2\u0282\u028a\5{>\2\u0283\u028a\5}?\2\u0284\u028a")
        buf.write("\3\2\2\2\u0285\u028a\5\u0081A\2\u0286\u028a\5\u0083B\2")
        buf.write("\u0287\u028a\5\u0085C\2\u0288\u028a\5\u0087D\2\u0289\u026e")
        buf.write("\3\2\2\2\u0289\u026f\3\2\2\2\u0289\u0270\3\2\2\2\u0289")
        buf.write("\u0271\3\2\2\2\u0289\u0272\3\2\2\2\u0289\u0273\3\2\2\2")
        buf.write("\u0289\u0274\3\2\2\2\u0289\u0275\3\2\2\2\u0289\u0276\3")
        buf.write("\2\2\2\u0289\u0277\3\2\2\2\u0289\u0278\3\2\2\2\u0289\u0279")
        buf.write("\3\2\2\2\u0289\u027a\3\2\2\2\u0289\u027b\3\2\2\2\u0289")
        buf.write("\u027c\3\2\2\2\u0289\u027d\3\2\2\2\u0289\u027e\3\2\2\2")
        buf.write("\u0289\u027f\3\2\2\2\u0289\u0280\3\2\2\2\u0289\u0281\3")
        buf.write("\2\2\2\u0289\u0282\3\2\2\2\u0289\u0283\3\2\2\2\u0289\u0284")
        buf.write("\3\2\2\2\u0289\u0285\3\2\2\2\u0289\u0286\3\2\2\2\u0289")
        buf.write("\u0287\3\2\2\2\u0289\u0288\3\2\2\2\u028a\u008a\3\2\2\2")
        buf.write("\u028b\u028c\7-\2\2\u028c\u008c\3\2\2\2\u028d\u028e\7")
        buf.write("/\2\2\u028e\u008e\3\2\2\2\u028f\u0290\7,\2\2\u0290\u0090")
        buf.write("\3\2\2\2\u0291\u0292\7\61\2\2\u0292\u0092\3\2\2\2\u0293")
        buf.write("\u0294\7\'\2\2\u0294\u0094\3\2\2\2\u0295\u0296\7#\2\2")
        buf.write("\u0296\u0096\3\2\2\2\u0297\u0298\7(\2\2\u0298\u0299\7")
        buf.write("(\2\2\u0299\u0098\3\2\2\2\u029a\u029b\7~\2\2\u029b\u029c")
        buf.write("\7~\2\2\u029c\u009a\3\2\2\2\u029d\u029e\7?\2\2\u029e\u029f")
        buf.write("\7?\2\2\u029f\u009c\3\2\2\2\u02a0\u02a1\7#\2\2\u02a1\u02a2")
        buf.write("\7?\2\2\u02a2\u009e\3\2\2\2\u02a3\u02a4\7?\2\2\u02a4\u00a0")
        buf.write("\3\2\2\2\u02a5\u02a6\7@\2\2\u02a6\u00a2\3\2\2\2\u02a7")
        buf.write("\u02a8\7>\2\2\u02a8\u00a4\3\2\2\2\u02a9\u02aa\7@\2\2\u02aa")
        buf.write("\u02ab\7?\2\2\u02ab\u00a6\3\2\2\2\u02ac\u02ad\7>\2\2\u02ad")
        buf.write("\u02ae\7?\2\2\u02ae\u00a8\3\2\2\2\u02af\u02b0\7?\2\2\u02b0")
        buf.write("\u02b1\7?\2\2\u02b1\u02b2\7\60\2\2\u02b2\u00aa\3\2\2\2")
        buf.write("\u02b3\u02b4\7-\2\2\u02b4\u02b5\7\60\2\2\u02b5\u00ac\3")
        buf.write("\2\2\2\u02b6\u02b7\7<\2\2\u02b7\u02b8\7<\2\2\u02b8\u00ae")
        buf.write("\3\2\2\2\u02b9\u02ba\7*\2\2\u02ba\u00b0\3\2\2\2\u02bb")
        buf.write("\u02bc\7+\2\2\u02bc\u00b2\3\2\2\2\u02bd\u02be\7]\2\2\u02be")
        buf.write("\u00b4\3\2\2\2\u02bf\u02c0\7_\2\2\u02c0\u00b6\3\2\2\2")
        buf.write("\u02c1\u02c2\7}\2\2\u02c2\u00b8\3\2\2\2\u02c3\u02c4\7")
        buf.write("\177\2\2\u02c4\u00ba\3\2\2\2\u02c5\u02c6\7=\2\2\u02c6")
        buf.write("\u00bc\3\2\2\2\u02c7\u02c8\7\60\2\2\u02c8\u00be\3\2\2")
        buf.write("\2\u02c9\u02ca\7.\2\2\u02ca\u00c0\3\2\2\2\u02cb\u02cd")
        buf.write("\t\24\2\2\u02cc\u02cb\3\2\2\2\u02cd\u02ce\3\2\2\2\u02ce")
        buf.write("\u02cc\3\2\2\2\u02ce\u02cf\3\2\2\2\u02cf\u02d0\3\2\2\2")
        buf.write("\u02d0\u02d1\ba\2\2\u02d1\u00c2\3\2\2\2\u02d2\u02d3\13")
        buf.write("\2\2\2\u02d3\u02d4\bb\b\2\u02d4\u00c4\3\2\2\2%\2\u00f0")
        buf.write("\u00fa\u0100\u0107\u010d\u0117\u011f\u0124\u012a\u0132")
        buf.write("\u0136\u013b\u013f\u0142\u0149\u0152\u015b\u0160\u0167")
        buf.write("\u016e\u0170\u0177\u0182\u0187\u0189\u0190\u019a\u01a1")
        buf.write("\u01a3\u01aa\u01b8\u01c3\u0289\u02ce\t\b\2\2\3\30\2\3")
        buf.write("\31\3\3\"\4\3#\5\3$\6\3b\7")
        return buf.getvalue()


class D96Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    Class_word = 3
    Bool_word = 4
    Int_word = 5
    Float_word = 6
    Str_word = 7
    Array_word = 8
    Var_word = 9
    Val_word = 10
    If_word = 11
    Else_word = 12
    Elseif_word = 13
    Foreach_word = 14
    In_word = 15
    By_word = 16
    Return_word = 17
    New_word = 18
    BLOCKCOMMENT = 19
    ID = 20
    INTLIT = 21
    FLOATLIT = 22
    BOOLEANLIT = 23
    STRINGLIT = 24
    UNCLOSE_STRING = 25
    ILLEGAL_ESCAPE = 26
    PROGRAM = 27
    MAIN = 28
    BREAK = 29
    CONT = 30
    IF = 31
    ELSEIF = 32
    ELSE = 33
    FOREACH = 34
    BOOLTRUE = 35
    BOOLFALSE = 36
    ARRAY = 37
    IN = 38
    INT = 39
    FLOAT = 40
    BOOL = 41
    STR = 42
    RETURN = 43
    CLASS = 44
    NULL = 45
    VAL = 46
    VAR = 47
    SELF = 48
    CONS = 49
    DEST = 50
    KEYWORD_NEW = 51
    BY = 52
    ADD_OP = 53
    SUB_OP = 54
    MUL_OP = 55
    DIV_OP = 56
    MOD_OP = 57
    NOT_OP = 58
    AND_OP = 59
    OR_OP = 60
    EQUAL_OP = 61
    DIFF_OP = 62
    ASSIGN_OP = 63
    GREATER_OP = 64
    LESSER_OP = 65
    GREATER_EQUAL_OP = 66
    LESSER_EQUAL_OP = 67
    STRING_COMP_OP = 68
    STRING_CONCAT_OP = 69
    MEMBER_ACCESS_OUT = 70
    LP = 71
    RP = 72
    LSB = 73
    RSB = 74
    LB = 75
    RB = 76
    SEMI = 77
    DOT = 78
    COMA = 79
    WS = 80
    ERROR_CHAR = 81

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "':'", "'..'", "'Program'", "'main'", "'Break'", "'Continue'", 
            "'If'", "'Elseif'", "'Else'", "'Foreach'", "'True'", "'False'", 
            "'Array'", "'In'", "'Int'", "'Float'", "'Boolean'", "'String'", 
            "'Return'", "'Class'", "'Null'", "'Val'", "'Var'", "'Self'", 
            "'Constructor'", "'Destructor'", "'New'", "'By'", "'+'", "'-'", 
            "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", "'=='", "'!='", 
            "'='", "'>'", "'<'", "'>='", "'<='", "'==.'", "'+.'", "'::'", 
            "'('", "')'", "'['", "']'", "'{'", "'}'", "';'", "'.'", "','" ]

    symbolicNames = [ "<INVALID>",
            "Class_word", "Bool_word", "Int_word", "Float_word", "Str_word", 
            "Array_word", "Var_word", "Val_word", "If_word", "Else_word", 
            "Elseif_word", "Foreach_word", "In_word", "By_word", "Return_word", 
            "New_word", "BLOCKCOMMENT", "ID", "INTLIT", "FLOATLIT", "BOOLEANLIT", 
            "STRINGLIT", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "PROGRAM", 
            "MAIN", "BREAK", "CONT", "IF", "ELSEIF", "ELSE", "FOREACH", 
            "BOOLTRUE", "BOOLFALSE", "ARRAY", "IN", "INT", "FLOAT", "BOOL", 
            "STR", "RETURN", "CLASS", "NULL", "VAL", "VAR", "SELF", "CONS", 
            "DEST", "KEYWORD_NEW", "BY", "ADD_OP", "SUB_OP", "MUL_OP", "DIV_OP", 
            "MOD_OP", "NOT_OP", "AND_OP", "OR_OP", "EQUAL_OP", "DIFF_OP", 
            "ASSIGN_OP", "GREATER_OP", "LESSER_OP", "GREATER_EQUAL_OP", 
            "LESSER_EQUAL_OP", "STRING_COMP_OP", "STRING_CONCAT_OP", "MEMBER_ACCESS_OUT", 
            "LP", "RP", "LSB", "RSB", "LB", "RB", "SEMI", "DOT", "COMA", 
            "WS", "ERROR_CHAR" ]

    ruleNames = [ "T__0", "T__1", "Class_word", "Bool_word", "Int_word", 
                  "Float_word", "Str_word", "Array_word", "Var_word", "Val_word", 
                  "If_word", "Else_word", "Elseif_word", "Foreach_word", 
                  "In_word", "By_word", "Return_word", "New_word", "BLOCKCOMMENT", 
                  "ID", "NORM_ID", "SPEC_ID", "INTLIT", "FLOATLIT", "INTERGER_PART", 
                  "EXPONENT", "FRACTION", "DECIMAL", "OCTAL", "HEX", "BIN", 
                  "BOOLEANLIT", "STRINGLIT", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "ESC_SEQ", "ILL_ESC_SEQ", "OCTAL_ESC", "UNICODE_ESC", 
                  "HEX_DIGIT", "UNKNOW_ESC", "PROGRAM", "MAIN", "BREAK", 
                  "CONT", "IF", "ELSEIF", "ELSE", "FOREACH", "BOOLTRUE", 
                  "BOOLFALSE", "ARRAY", "IN", "INT", "FLOAT", "BOOL", "STR", 
                  "RETURN", "CLASS", "NULL", "VAL", "VAR", "SELF", "CONS", 
                  "DEST", "KEYWORD_NEW", "BY", "KEYWORD", "ADD_OP", "SUB_OP", 
                  "MUL_OP", "DIV_OP", "MOD_OP", "NOT_OP", "AND_OP", "OR_OP", 
                  "EQUAL_OP", "DIFF_OP", "ASSIGN_OP", "GREATER_OP", "LESSER_OP", 
                  "GREATER_EQUAL_OP", "LESSER_EQUAL_OP", "STRING_COMP_OP", 
                  "STRING_CONCAT_OP", "MEMBER_ACCESS_OUT", "LP", "RP", "LSB", 
                  "RSB", "LB", "RB", "SEMI", "DOT", "COMA", "WS", "ERROR_CHAR" ]

    grammarFileName = "D96.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[22] = self.INTLIT_action 
            actions[23] = self.FLOATLIT_action 
            actions[32] = self.STRINGLIT_action 
            actions[33] = self.UNCLOSE_STRING_action 
            actions[34] = self.ILLEGAL_ESCAPE_action 
            actions[96] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INTLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            	
            	self.text = self.text.replace('_','')

     

    def FLOATLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

            	self.text = self.text.replace('_','')
            	##print("Float: ", self.text)

     

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            	s = ""
            	check = False;
            	for i in range(len(self.text)):
            		s += self.text[i]
            		a = ''
            		if(i == len(self.text)-1): a = ''
            		else: a = self.text[i+1]
            		b = ((a != 'b') and  (a != 'f') and  (a != 'r') and  (a != 'n') and  (a != 't') and (a != '\'') and  (a != '"') and (a != '\\'))
            		if(self.text[i] == '\\' and b == True):
            			s += self.text[i+1]
            			check = True
            			break;
            	if(check == True):
            		self.text = s
            		self.text = self.text[1:]
            		raise IllegalEscape(self.text) 
            	else:
            		self.text = s
            		self.text = self.text[1:-1]

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            	self.text = self.text[1:]
            	##print("UNCLOSE_STRING: ", self.text)
            	raise UncloseString(self.text) 

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

            	self.text = self.text[1:]
            	##print("ILLEGAL_ESCAPE: ", self.text)
            	raise IllegalEscape(self.text) 

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
             raise ErrorToken(self.text) 
     


