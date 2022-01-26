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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2I")
        buf.write("\u02ac\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("U\4V\tV\4W\tW\4X\tX\4Y\tY\3\2\3\2\3\3\3\3\3\4\3\4\3\4")
        buf.write("\3\5\3\5\3\6\3\6\3\7\3\7\3\7\3\7\7\7\u00c3\n\7\f\7\16")
        buf.write("\7\u00c6\13\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\5\b")
        buf.write("\u00d1\n\b\3\b\3\b\3\t\3\t\3\t\7\t\u00d8\n\t\f\t\16\t")
        buf.write("\u00db\13\t\3\t\6\t\u00de\n\t\r\t\16\t\u00df\7\t\u00e2")
        buf.write("\n\t\f\t\16\t\u00e5\13\t\5\t\u00e7\n\t\3\n\3\n\6\n\u00eb")
        buf.write("\n\n\r\n\16\n\u00ec\3\13\3\13\3\13\6\13\u00f2\n\13\r\13")
        buf.write("\16\13\u00f3\3\f\3\f\3\f\6\f\u00f9\n\f\r\f\16\f\u00fa")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u0103\n\r\3\r\3\r\3\16\3")
        buf.write("\16\3\17\3\17\5\17\u010b\n\17\3\17\3\17\3\20\3\20\3\20")
        buf.write("\5\20\u0112\n\20\3\21\3\21\3\21\3\21\5\21\u0118\n\21\3")
        buf.write("\22\3\22\3\22\3\22\3\22\7\22\u011f\n\22\f\22\16\22\u0122")
        buf.write("\13\22\3\22\3\22\3\22\3\23\3\23\3\23\7\23\u012a\n\23\f")
        buf.write("\23\16\23\u012d\13\23\3\23\3\23\7\23\u0131\n\23\f\23\16")
        buf.write("\23\u0134\13\23\3\23\3\23\7\23\u0138\n\23\f\23\16\23\u013b")
        buf.write("\13\23\3\23\3\23\3\24\3\24\3\24\7\24\u0142\n\24\f\24\16")
        buf.write("\24\u0145\13\24\3\24\3\24\3\24\3\24\7\24\u014b\n\24\f")
        buf.write("\24\16\24\u014e\13\24\3\24\3\24\3\24\3\25\3\25\3\25\3")
        buf.write("\26\3\26\3\26\3\26\5\26\u015a\n\26\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\5\27\u0165\n\27\3\30\3\30\3")
        buf.write("\30\3\30\3\30\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33")
        buf.write("\3\33\5\33\u0175\n\33\3\33\3\33\3\33\3\34\3\34\3\34\3")
        buf.write("\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\5\34\u0186")
        buf.write("\n\34\3\35\3\35\3\35\3\35\5\35\u018c\n\35\3\36\3\36\3")
        buf.write("\36\3\36\5\36\u0192\n\36\3\37\3\37\3\37\3\37\5\37\u0198")
        buf.write("\n\37\3 \3 \3 \3 \5 \u019e\n \3!\3!\7!\u01a2\n!\f!\16")
        buf.write("!\u01a5\13!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3#\3")
        buf.write("#\3#\3#\3#\3$\3$\3$\3$\3$\3$\3%\3%\3%\3%\3%\3%\3%\3%\3")
        buf.write("%\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3(")
        buf.write("\3)\3)\3)\3)\3)\3)\3)\3)\3*\3*\3*\3*\3*\3+\3+\3+\3+\3")
        buf.write("+\3+\3,\3,\3,\3,\3,\3,\3-\3-\3-\3.\3.\3.\3.\3/\3/\3/\3")
        buf.write("/\3/\3/\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\61\3")
        buf.write("\61\3\61\3\61\3\61\3\61\3\61\3\62\3\62\3\62\3\62\3\62")
        buf.write("\3\62\3\62\3\63\3\63\3\63\3\63\3\63\3\63\3\64\3\64\3\64")
        buf.write("\3\64\3\64\3\65\3\65\3\65\3\65\3\66\3\66\3\66\3\66\3\67")
        buf.write("\3\67\3\67\3\67\3\67\38\38\38\38\38\38\38\38\38\38\38")
        buf.write("\38\39\39\39\39\39\39\39\39\39\39\39\3:\3:\3:\3:\3;\3")
        buf.write(";\3;\3<\3<\3<\3<\3<\3<\3<\3<\3<\3<\3<\3<\3<\3<\3<\3<\3")
        buf.write("<\3<\3<\3<\3<\3<\3<\3<\3<\3<\3<\5<\u0261\n<\3=\3=\3>\3")
        buf.write(">\3?\3?\3@\3@\3A\3A\3B\3B\3C\3C\3C\3D\3D\3D\3E\3E\3E\3")
        buf.write("F\3F\3F\3G\3G\3H\3H\3I\3I\3J\3J\3J\3K\3K\3K\3L\3L\3L\3")
        buf.write("L\3M\3M\3M\3N\3N\3N\3O\3O\3P\3P\3Q\3Q\3R\3R\3S\3S\3T\3")
        buf.write("T\3U\3U\3V\3V\3W\3W\3X\6X\u02a4\nX\rX\16X\u02a5\3X\3X")
        buf.write("\3Y\3Y\3Y\3\u00c4\2Z\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21")
        buf.write("\2\23\2\25\2\27\2\31\n\33\2\35\2\37\2!\13#\f%\r\'\16)")
        buf.write("\2+\2-\2/\2\61\2\63\17\65\20\67\219\2;\2=\2?\2A\22C\23")
        buf.write("E\24G\25I\26K\27M\30O\31Q\32S\33U\34W\35Y\36[\37] _!a")
        buf.write("\"c#e$g%i&k\'m(o)q*s+u,w\2y-{.}/\177\60\u0081\61\u0083")
        buf.write("\62\u0085\63\u0087\64\u0089\65\u008b\66\u008d\67\u008f")
        buf.write("8\u00919\u0093:\u0095;\u0097<\u0099=\u009b>\u009d?\u009f")
        buf.write("@\u00a1A\u00a3B\u00a5C\u00a7D\u00a9E\u00abF\u00adG\u00af")
        buf.write("H\u00b1I\3\2\20\3\2\63;\4\2\62;aa\3\2\629\4\2ZZzz\5\2")
        buf.write("\62;CHch\4\2DDdd\3\2\62\63\4\2GGgg\4\2--//\6\2\f\f\17")
        buf.write("\17$$^^\t\2))^^ddhhppttvv\5\2C\\aac|\6\2\62;C\\aac|\5")
        buf.write("\2\n\f\16\17\"\"\2\u02dd\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3")
        buf.write("\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2")
        buf.write("\2\2\31\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3")
        buf.write("\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\2A\3\2\2")
        buf.write("\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2")
        buf.write("\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3")
        buf.write("\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_")
        buf.write("\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2")
        buf.write("i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2")
        buf.write("\2s\3\2\2\2\2u\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2")
        buf.write("\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085")
        buf.write("\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2")
        buf.write("\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093")
        buf.write("\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2\2\2\u0099\3\2\2")
        buf.write("\2\2\u009b\3\2\2\2\2\u009d\3\2\2\2\2\u009f\3\2\2\2\2\u00a1")
        buf.write("\3\2\2\2\2\u00a3\3\2\2\2\2\u00a5\3\2\2\2\2\u00a7\3\2\2")
        buf.write("\2\2\u00a9\3\2\2\2\2\u00ab\3\2\2\2\2\u00ad\3\2\2\2\2\u00af")
        buf.write("\3\2\2\2\2\u00b1\3\2\2\2\3\u00b3\3\2\2\2\5\u00b5\3\2\2")
        buf.write("\2\7\u00b7\3\2\2\2\t\u00ba\3\2\2\2\13\u00bc\3\2\2\2\r")
        buf.write("\u00be\3\2\2\2\17\u00d0\3\2\2\2\21\u00e6\3\2\2\2\23\u00e8")
        buf.write("\3\2\2\2\25\u00ee\3\2\2\2\27\u00f5\3\2\2\2\31\u00fc\3")
        buf.write("\2\2\2\33\u0106\3\2\2\2\35\u0108\3\2\2\2\37\u0111\3\2")
        buf.write("\2\2!\u0117\3\2\2\2#\u0119\3\2\2\2%\u0126\3\2\2\2\'\u013e")
        buf.write("\3\2\2\2)\u0152\3\2\2\2+\u0159\3\2\2\2-\u0164\3\2\2\2")
        buf.write("/\u0166\3\2\2\2\61\u016d\3\2\2\2\63\u016f\3\2\2\2\65\u0171")
        buf.write("\3\2\2\2\67\u0185\3\2\2\29\u018b\3\2\2\2;\u0191\3\2\2")
        buf.write("\2=\u0197\3\2\2\2?\u019d\3\2\2\2A\u019f\3\2\2\2C\u01a8")
        buf.write("\3\2\2\2E\u01b0\3\2\2\2G\u01b5\3\2\2\2I\u01bb\3\2\2\2")
        buf.write("K\u01c4\3\2\2\2M\u01c7\3\2\2\2O\u01ce\3\2\2\2Q\u01d3\3")
        buf.write("\2\2\2S\u01db\3\2\2\2U\u01e0\3\2\2\2W\u01e6\3\2\2\2Y\u01ec")
        buf.write("\3\2\2\2[\u01ef\3\2\2\2]\u01f3\3\2\2\2_\u01f9\3\2\2\2")
        buf.write("a\u0201\3\2\2\2c\u0208\3\2\2\2e\u020f\3\2\2\2g\u0215\3")
        buf.write("\2\2\2i\u021a\3\2\2\2k\u021e\3\2\2\2m\u0222\3\2\2\2o\u0227")
        buf.write("\3\2\2\2q\u0233\3\2\2\2s\u023e\3\2\2\2u\u0242\3\2\2\2")
        buf.write("w\u0260\3\2\2\2y\u0262\3\2\2\2{\u0264\3\2\2\2}\u0266\3")
        buf.write("\2\2\2\177\u0268\3\2\2\2\u0081\u026a\3\2\2\2\u0083\u026c")
        buf.write("\3\2\2\2\u0085\u026e\3\2\2\2\u0087\u0271\3\2\2\2\u0089")
        buf.write("\u0274\3\2\2\2\u008b\u0277\3\2\2\2\u008d\u027a\3\2\2\2")
        buf.write("\u008f\u027c\3\2\2\2\u0091\u027e\3\2\2\2\u0093\u0280\3")
        buf.write("\2\2\2\u0095\u0283\3\2\2\2\u0097\u0286\3\2\2\2\u0099\u028a")
        buf.write("\3\2\2\2\u009b\u028d\3\2\2\2\u009d\u0290\3\2\2\2\u009f")
        buf.write("\u0292\3\2\2\2\u00a1\u0294\3\2\2\2\u00a3\u0296\3\2\2\2")
        buf.write("\u00a5\u0298\3\2\2\2\u00a7\u029a\3\2\2\2\u00a9\u029c\3")
        buf.write("\2\2\2\u00ab\u029e\3\2\2\2\u00ad\u02a0\3\2\2\2\u00af\u02a3")
        buf.write("\3\2\2\2\u00b1\u02a9\3\2\2\2\u00b3\u00b4\7<\2\2\u00b4")
        buf.write("\4\3\2\2\2\u00b5\u00b6\7&\2\2\u00b6\6\3\2\2\2\u00b7\u00b8")
        buf.write("\7\60\2\2\u00b8\u00b9\7\60\2\2\u00b9\b\3\2\2\2\u00ba\u00bb")
        buf.write("\5e\63\2\u00bb\n\3\2\2\2\u00bc\u00bd\5c\62\2\u00bd\f\3")
        buf.write("\2\2\2\u00be\u00bf\7%\2\2\u00bf\u00c0\7%\2\2\u00c0\u00c4")
        buf.write("\3\2\2\2\u00c1\u00c3\13\2\2\2\u00c2\u00c1\3\2\2\2\u00c3")
        buf.write("\u00c6\3\2\2\2\u00c4\u00c5\3\2\2\2\u00c4\u00c2\3\2\2\2")
        buf.write("\u00c5\u00c7\3\2\2\2\u00c6\u00c4\3\2\2\2\u00c7\u00c8\7")
        buf.write("%\2\2\u00c8\u00c9\7%\2\2\u00c9\u00ca\3\2\2\2\u00ca\u00cb")
        buf.write("\b\7\2\2\u00cb\16\3\2\2\2\u00cc\u00d1\5\21\t\2\u00cd\u00d1")
        buf.write("\5\23\n\2\u00ce\u00d1\5\25\13\2\u00cf\u00d1\5\27\f\2\u00d0")
        buf.write("\u00cc\3\2\2\2\u00d0\u00cd\3\2\2\2\u00d0\u00ce\3\2\2\2")
        buf.write("\u00d0\u00cf\3\2\2\2\u00d1\u00d2\3\2\2\2\u00d2\u00d3\b")
        buf.write("\b\3\2\u00d3\20\3\2\2\2\u00d4\u00e7\7\62\2\2\u00d5\u00e3")
        buf.write("\t\2\2\2\u00d6\u00d8\t\3\2\2\u00d7\u00d6\3\2\2\2\u00d8")
        buf.write("\u00db\3\2\2\2\u00d9\u00d7\3\2\2\2\u00d9\u00da\3\2\2\2")
        buf.write("\u00da\u00dd\3\2\2\2\u00db\u00d9\3\2\2\2\u00dc\u00de\t")
        buf.write("\3\2\2\u00dd\u00dc\3\2\2\2\u00de\u00df\3\2\2\2\u00df\u00dd")
        buf.write("\3\2\2\2\u00df\u00e0\3\2\2\2\u00e0\u00e2\3\2\2\2\u00e1")
        buf.write("\u00d9\3\2\2\2\u00e2\u00e5\3\2\2\2\u00e3\u00e1\3\2\2\2")
        buf.write("\u00e3\u00e4\3\2\2\2\u00e4\u00e7\3\2\2\2\u00e5\u00e3\3")
        buf.write("\2\2\2\u00e6\u00d4\3\2\2\2\u00e6\u00d5\3\2\2\2\u00e7\22")
        buf.write("\3\2\2\2\u00e8\u00ea\7\62\2\2\u00e9\u00eb\t\4\2\2\u00ea")
        buf.write("\u00e9\3\2\2\2\u00eb\u00ec\3\2\2\2\u00ec\u00ea\3\2\2\2")
        buf.write("\u00ec\u00ed\3\2\2\2\u00ed\24\3\2\2\2\u00ee\u00ef\7\62")
        buf.write("\2\2\u00ef\u00f1\t\5\2\2\u00f0\u00f2\t\6\2\2\u00f1\u00f0")
        buf.write("\3\2\2\2\u00f2\u00f3\3\2\2\2\u00f3\u00f1\3\2\2\2\u00f3")
        buf.write("\u00f4\3\2\2\2\u00f4\26\3\2\2\2\u00f5\u00f6\7\62\2\2\u00f6")
        buf.write("\u00f8\t\7\2\2\u00f7\u00f9\t\b\2\2\u00f8\u00f7\3\2\2\2")
        buf.write("\u00f9\u00fa\3\2\2\2\u00fa\u00f8\3\2\2\2\u00fa\u00fb\3")
        buf.write("\2\2\2\u00fb\30\3\2\2\2\u00fc\u0102\5\33\16\2\u00fd\u0103")
        buf.write("\5\37\20\2\u00fe\u0103\5\35\17\2\u00ff\u0100\5\37\20\2")
        buf.write("\u0100\u0101\5\35\17\2\u0101\u0103\3\2\2\2\u0102\u00fd")
        buf.write("\3\2\2\2\u0102\u00fe\3\2\2\2\u0102\u00ff\3\2\2\2\u0103")
        buf.write("\u0104\3\2\2\2\u0104\u0105\b\r\4\2\u0105\32\3\2\2\2\u0106")
        buf.write("\u0107\5\21\t\2\u0107\34\3\2\2\2\u0108\u010a\t\t\2\2\u0109")
        buf.write("\u010b\t\n\2\2\u010a\u0109\3\2\2\2\u010a\u010b\3\2\2\2")
        buf.write("\u010b\u010c\3\2\2\2\u010c\u010d\5\33\16\2\u010d\36\3")
        buf.write("\2\2\2\u010e\u010f\5\u00abV\2\u010f\u0110\5\33\16\2\u0110")
        buf.write("\u0112\3\2\2\2\u0111\u010e\3\2\2\2\u0111\u0112\3\2\2\2")
        buf.write("\u0112 \3\2\2\2\u0113\u0118\5S*\2\u0114\u0115\5U+\2\u0115")
        buf.write("\u0116\b\21\5\2\u0116\u0118\3\2\2\2\u0117\u0113\3\2\2")
        buf.write("\2\u0117\u0114\3\2\2\2\u0118\"\3\2\2\2\u0119\u0120\7$")
        buf.write("\2\2\u011a\u011f\5)\25\2\u011b\u011f\n\13\2\2\u011c\u011d")
        buf.write("\7)\2\2\u011d\u011f\7$\2\2\u011e\u011a\3\2\2\2\u011e\u011b")
        buf.write("\3\2\2\2\u011e\u011c\3\2\2\2\u011f\u0122\3\2\2\2\u0120")
        buf.write("\u011e\3\2\2\2\u0120\u0121\3\2\2\2\u0121\u0123\3\2\2\2")
        buf.write("\u0122\u0120\3\2\2\2\u0123\u0124\7$\2\2\u0124\u0125\b")
        buf.write("\22\6\2\u0125$\3\2\2\2\u0126\u012b\7$\2\2\u0127\u0128")
        buf.write("\7)\2\2\u0128\u012a\7$\2\2\u0129\u0127\3\2\2\2\u012a\u012d")
        buf.write("\3\2\2\2\u012b\u0129\3\2\2\2\u012b\u012c\3\2\2\2\u012c")
        buf.write("\u0132\3\2\2\2\u012d\u012b\3\2\2\2\u012e\u0131\5)\25\2")
        buf.write("\u012f\u0131\n\13\2\2\u0130\u012e\3\2\2\2\u0130\u012f")
        buf.write("\3\2\2\2\u0131\u0134\3\2\2\2\u0132\u0130\3\2\2\2\u0132")
        buf.write("\u0133\3\2\2\2\u0133\u0139\3\2\2\2\u0134\u0132\3\2\2\2")
        buf.write("\u0135\u0136\7)\2\2\u0136\u0138\7$\2\2\u0137\u0135\3\2")
        buf.write("\2\2\u0138\u013b\3\2\2\2\u0139\u0137\3\2\2\2\u0139\u013a")
        buf.write("\3\2\2\2\u013a\u013c\3\2\2\2\u013b\u0139\3\2\2\2\u013c")
        buf.write("\u013d\b\23\7\2\u013d&\3\2\2\2\u013e\u0143\7$\2\2\u013f")
        buf.write("\u0140\7)\2\2\u0140\u0142\7$\2\2\u0141\u013f\3\2\2\2\u0142")
        buf.write("\u0145\3\2\2\2\u0143\u0141\3\2\2\2\u0143\u0144\3\2\2\2")
        buf.write("\u0144\u014c\3\2\2\2\u0145\u0143\3\2\2\2\u0146\u014b\n")
        buf.write("\13\2\2\u0147\u014b\5)\25\2\u0148\u0149\7)\2\2\u0149\u014b")
        buf.write("\7$\2\2\u014a\u0146\3\2\2\2\u014a\u0147\3\2\2\2\u014a")
        buf.write("\u0148\3\2\2\2\u014b\u014e\3\2\2\2\u014c\u014a\3\2\2\2")
        buf.write("\u014c\u014d\3\2\2\2\u014d\u014f\3\2\2\2\u014e\u014c\3")
        buf.write("\2\2\2\u014f\u0150\5+\26\2\u0150\u0151\b\24\b\2\u0151")
        buf.write("(\3\2\2\2\u0152\u0153\7^\2\2\u0153\u0154\t\f\2\2\u0154")
        buf.write("*\3\2\2\2\u0155\u0156\7^\2\2\u0156\u015a\n\f\2\2\u0157")
        buf.write("\u015a\5/\30\2\u0158\u015a\5-\27\2\u0159\u0155\3\2\2\2")
        buf.write("\u0159\u0157\3\2\2\2\u0159\u0158\3\2\2\2\u015a,\3\2\2")
        buf.write("\2\u015b\u015c\7^\2\2\u015c\u015d\4\62\65\2\u015d\u015e")
        buf.write("\4\629\2\u015e\u0165\4\629\2\u015f\u0160\7^\2\2\u0160")
        buf.write("\u0161\4\629\2\u0161\u0165\4\629\2\u0162\u0163\7^\2\2")
        buf.write("\u0163\u0165\4\629\2\u0164\u015b\3\2\2\2\u0164\u015f\3")
        buf.write("\2\2\2\u0164\u0162\3\2\2\2\u0165.\3\2\2\2\u0166\u0167")
        buf.write("\7^\2\2\u0167\u0168\7w\2\2\u0168\u0169\5\61\31\2\u0169")
        buf.write("\u016a\5\61\31\2\u016a\u016b\5\61\31\2\u016b\u016c\5\61")
        buf.write("\31\2\u016c\60\3\2\2\2\u016d\u016e\t\6\2\2\u016e\62\3")
        buf.write("\2\2\2\u016f\u0170\5W,\2\u0170\64\3\2\2\2\u0171\u0172")
        buf.write("\5W,\2\u0172\u0174\5\u00a5S\2\u0173\u0175\5\67\34\2\u0174")
        buf.write("\u0173\3\2\2\2\u0174\u0175\3\2\2\2\u0175\u0176\3\2\2\2")
        buf.write("\u0176\u0177\5\u00a7T\2\u0177\u0178\b\33\t\2\u0178\66")
        buf.write("\3\2\2\2\u0179\u017a\5\17\b\2\u017a\u017b\59\35\2\u017b")
        buf.write("\u0186\3\2\2\2\u017c\u017d\5\31\r\2\u017d\u017e\5;\36")
        buf.write("\2\u017e\u0186\3\2\2\2\u017f\u0180\5!\21\2\u0180\u0181")
        buf.write("\5=\37\2\u0181\u0186\3\2\2\2\u0182\u0183\5#\22\2\u0183")
        buf.write("\u0184\5? \2\u0184\u0186\3\2\2\2\u0185\u0179\3\2\2\2\u0185")
        buf.write("\u017c\3\2\2\2\u0185\u017f\3\2\2\2\u0185\u0182\3\2\2\2")
        buf.write("\u01868\3\2\2\2\u0187\u0188\5\u00adW\2\u0188\u0189\5\17")
        buf.write("\b\2\u0189\u018a\59\35\2\u018a\u018c\3\2\2\2\u018b\u0187")
        buf.write("\3\2\2\2\u018b\u018c\3\2\2\2\u018c:\3\2\2\2\u018d\u018e")
        buf.write("\5\u00adW\2\u018e\u018f\5\31\r\2\u018f\u0190\5;\36\2\u0190")
        buf.write("\u0192\3\2\2\2\u0191\u018d\3\2\2\2\u0191\u0192\3\2\2\2")
        buf.write("\u0192<\3\2\2\2\u0193\u0194\5\u00adW\2\u0194\u0195\5!")
        buf.write("\21\2\u0195\u0196\5=\37\2\u0196\u0198\3\2\2\2\u0197\u0193")
        buf.write("\3\2\2\2\u0197\u0198\3\2\2\2\u0198>\3\2\2\2\u0199\u019a")
        buf.write("\5\u00adW\2\u019a\u019b\5#\22\2\u019b\u019c\5? \2\u019c")
        buf.write("\u019e\3\2\2\2\u019d\u0199\3\2\2\2\u019d\u019e\3\2\2\2")
        buf.write("\u019e@\3\2\2\2\u019f\u01a3\t\r\2\2\u01a0\u01a2\t\16\2")
        buf.write("\2\u01a1\u01a0\3\2\2\2\u01a2\u01a5\3\2\2\2\u01a3\u01a1")
        buf.write("\3\2\2\2\u01a3\u01a4\3\2\2\2\u01a4\u01a6\3\2\2\2\u01a5")
        buf.write("\u01a3\3\2\2\2\u01a6\u01a7\b!\n\2\u01a7B\3\2\2\2\u01a8")
        buf.write("\u01a9\7R\2\2\u01a9\u01aa\7t\2\2\u01aa\u01ab\7q\2\2\u01ab")
        buf.write("\u01ac\7i\2\2\u01ac\u01ad\7t\2\2\u01ad\u01ae\7c\2\2\u01ae")
        buf.write("\u01af\7o\2\2\u01afD\3\2\2\2\u01b0\u01b1\7o\2\2\u01b1")
        buf.write("\u01b2\7c\2\2\u01b2\u01b3\7k\2\2\u01b3\u01b4\7p\2\2\u01b4")
        buf.write("F\3\2\2\2\u01b5\u01b6\7D\2\2\u01b6\u01b7\7t\2\2\u01b7")
        buf.write("\u01b8\7g\2\2\u01b8\u01b9\7c\2\2\u01b9\u01ba\7m\2\2\u01ba")
        buf.write("H\3\2\2\2\u01bb\u01bc\7E\2\2\u01bc\u01bd\7q\2\2\u01bd")
        buf.write("\u01be\7p\2\2\u01be\u01bf\7v\2\2\u01bf\u01c0\7k\2\2\u01c0")
        buf.write("\u01c1\7p\2\2\u01c1\u01c2\7w\2\2\u01c2\u01c3\7g\2\2\u01c3")
        buf.write("J\3\2\2\2\u01c4\u01c5\7K\2\2\u01c5\u01c6\7h\2\2\u01c6")
        buf.write("L\3\2\2\2\u01c7\u01c8\7G\2\2\u01c8\u01c9\7n\2\2\u01c9")
        buf.write("\u01ca\7u\2\2\u01ca\u01cb\7g\2\2\u01cb\u01cc\7k\2\2\u01cc")
        buf.write("\u01cd\7h\2\2\u01cdN\3\2\2\2\u01ce\u01cf\7G\2\2\u01cf")
        buf.write("\u01d0\7n\2\2\u01d0\u01d1\7u\2\2\u01d1\u01d2\7g\2\2\u01d2")
        buf.write("P\3\2\2\2\u01d3\u01d4\7H\2\2\u01d4\u01d5\7q\2\2\u01d5")
        buf.write("\u01d6\7t\2\2\u01d6\u01d7\7g\2\2\u01d7\u01d8\7c\2\2\u01d8")
        buf.write("\u01d9\7e\2\2\u01d9\u01da\7j\2\2\u01daR\3\2\2\2\u01db")
        buf.write("\u01dc\7V\2\2\u01dc\u01dd\7t\2\2\u01dd\u01de\7w\2\2\u01de")
        buf.write("\u01df\7g\2\2\u01dfT\3\2\2\2\u01e0\u01e1\7H\2\2\u01e1")
        buf.write("\u01e2\7c\2\2\u01e2\u01e3\7n\2\2\u01e3\u01e4\7u\2\2\u01e4")
        buf.write("\u01e5\7g\2\2\u01e5V\3\2\2\2\u01e6\u01e7\7C\2\2\u01e7")
        buf.write("\u01e8\7t\2\2\u01e8\u01e9\7t\2\2\u01e9\u01ea\7c\2\2\u01ea")
        buf.write("\u01eb\7{\2\2\u01ebX\3\2\2\2\u01ec\u01ed\7K\2\2\u01ed")
        buf.write("\u01ee\7p\2\2\u01eeZ\3\2\2\2\u01ef\u01f0\7K\2\2\u01f0")
        buf.write("\u01f1\7p\2\2\u01f1\u01f2\7v\2\2\u01f2\\\3\2\2\2\u01f3")
        buf.write("\u01f4\7H\2\2\u01f4\u01f5\7n\2\2\u01f5\u01f6\7q\2\2\u01f6")
        buf.write("\u01f7\7c\2\2\u01f7\u01f8\7v\2\2\u01f8^\3\2\2\2\u01f9")
        buf.write("\u01fa\7D\2\2\u01fa\u01fb\7q\2\2\u01fb\u01fc\7q\2\2\u01fc")
        buf.write("\u01fd\7n\2\2\u01fd\u01fe\7g\2\2\u01fe\u01ff\7c\2\2\u01ff")
        buf.write("\u0200\7p\2\2\u0200`\3\2\2\2\u0201\u0202\7U\2\2\u0202")
        buf.write("\u0203\7v\2\2\u0203\u0204\7t\2\2\u0204\u0205\7k\2\2\u0205")
        buf.write("\u0206\7p\2\2\u0206\u0207\7i\2\2\u0207b\3\2\2\2\u0208")
        buf.write("\u0209\7T\2\2\u0209\u020a\7g\2\2\u020a\u020b\7v\2\2\u020b")
        buf.write("\u020c\7w\2\2\u020c\u020d\7t\2\2\u020d\u020e\7p\2\2\u020e")
        buf.write("d\3\2\2\2\u020f\u0210\7E\2\2\u0210\u0211\7n\2\2\u0211")
        buf.write("\u0212\7c\2\2\u0212\u0213\7u\2\2\u0213\u0214\7u\2\2\u0214")
        buf.write("f\3\2\2\2\u0215\u0216\7P\2\2\u0216\u0217\7w\2\2\u0217")
        buf.write("\u0218\7n\2\2\u0218\u0219\7n\2\2\u0219h\3\2\2\2\u021a")
        buf.write("\u021b\7X\2\2\u021b\u021c\7c\2\2\u021c\u021d\7n\2\2\u021d")
        buf.write("j\3\2\2\2\u021e\u021f\7X\2\2\u021f\u0220\7c\2\2\u0220")
        buf.write("\u0221\7t\2\2\u0221l\3\2\2\2\u0222\u0223\7U\2\2\u0223")
        buf.write("\u0224\7g\2\2\u0224\u0225\7n\2\2\u0225\u0226\7h\2\2\u0226")
        buf.write("n\3\2\2\2\u0227\u0228\7E\2\2\u0228\u0229\7q\2\2\u0229")
        buf.write("\u022a\7p\2\2\u022a\u022b\7u\2\2\u022b\u022c\7v\2\2\u022c")
        buf.write("\u022d\7t\2\2\u022d\u022e\7w\2\2\u022e\u022f\7e\2\2\u022f")
        buf.write("\u0230\7v\2\2\u0230\u0231\7q\2\2\u0231\u0232\7t\2\2\u0232")
        buf.write("p\3\2\2\2\u0233\u0234\7F\2\2\u0234\u0235\7g\2\2\u0235")
        buf.write("\u0236\7u\2\2\u0236\u0237\7v\2\2\u0237\u0238\7t\2\2\u0238")
        buf.write("\u0239\7w\2\2\u0239\u023a\7e\2\2\u023a\u023b\7v\2\2\u023b")
        buf.write("\u023c\7q\2\2\u023c\u023d\7t\2\2\u023dr\3\2\2\2\u023e")
        buf.write("\u023f\7P\2\2\u023f\u0240\7g\2\2\u0240\u0241\7y\2\2\u0241")
        buf.write("t\3\2\2\2\u0242\u0243\7D\2\2\u0243\u0244\7{\2\2\u0244")
        buf.write("v\3\2\2\2\u0245\u0261\5G$\2\u0246\u0261\5I%\2\u0247\u0261")
        buf.write("\5K&\2\u0248\u0261\5M\'\2\u0249\u0261\5O(\2\u024a\u0261")
        buf.write("\3\2\2\2\u024b\u0261\5Q)\2\u024c\u0261\5S*\2\u024d\u0261")
        buf.write("\5U+\2\u024e\u0261\5W,\2\u024f\u0261\5Y-\2\u0250\u0261")
        buf.write("\3\2\2\2\u0251\u0261\5[.\2\u0252\u0261\5]/\2\u0253\u0261")
        buf.write("\5_\60\2\u0254\u0261\5a\61\2\u0255\u0261\5c\62\2\u0256")
        buf.write("\u0261\3\2\2\2\u0257\u0261\5g\64\2\u0258\u0261\5e\63\2")
        buf.write("\u0259\u0261\5i\65\2\u025a\u0261\5k\66\2\u025b\u0261\3")
        buf.write("\2\2\2\u025c\u0261\5o8\2\u025d\u0261\5q9\2\u025e\u0261")
        buf.write("\5s:\2\u025f\u0261\5u;\2\u0260\u0245\3\2\2\2\u0260\u0246")
        buf.write("\3\2\2\2\u0260\u0247\3\2\2\2\u0260\u0248\3\2\2\2\u0260")
        buf.write("\u0249\3\2\2\2\u0260\u024a\3\2\2\2\u0260\u024b\3\2\2\2")
        buf.write("\u0260\u024c\3\2\2\2\u0260\u024d\3\2\2\2\u0260\u024e\3")
        buf.write("\2\2\2\u0260\u024f\3\2\2\2\u0260\u0250\3\2\2\2\u0260\u0251")
        buf.write("\3\2\2\2\u0260\u0252\3\2\2\2\u0260\u0253\3\2\2\2\u0260")
        buf.write("\u0254\3\2\2\2\u0260\u0255\3\2\2\2\u0260\u0256\3\2\2\2")
        buf.write("\u0260\u0257\3\2\2\2\u0260\u0258\3\2\2\2\u0260\u0259\3")
        buf.write("\2\2\2\u0260\u025a\3\2\2\2\u0260\u025b\3\2\2\2\u0260\u025c")
        buf.write("\3\2\2\2\u0260\u025d\3\2\2\2\u0260\u025e\3\2\2\2\u0260")
        buf.write("\u025f\3\2\2\2\u0261x\3\2\2\2\u0262\u0263\7-\2\2\u0263")
        buf.write("z\3\2\2\2\u0264\u0265\7/\2\2\u0265|\3\2\2\2\u0266\u0267")
        buf.write("\7,\2\2\u0267~\3\2\2\2\u0268\u0269\7\61\2\2\u0269\u0080")
        buf.write("\3\2\2\2\u026a\u026b\7\'\2\2\u026b\u0082\3\2\2\2\u026c")
        buf.write("\u026d\7#\2\2\u026d\u0084\3\2\2\2\u026e\u026f\7(\2\2\u026f")
        buf.write("\u0270\7(\2\2\u0270\u0086\3\2\2\2\u0271\u0272\7~\2\2\u0272")
        buf.write("\u0273\7~\2\2\u0273\u0088\3\2\2\2\u0274\u0275\7?\2\2\u0275")
        buf.write("\u0276\7?\2\2\u0276\u008a\3\2\2\2\u0277\u0278\7#\2\2\u0278")
        buf.write("\u0279\7?\2\2\u0279\u008c\3\2\2\2\u027a\u027b\7?\2\2\u027b")
        buf.write("\u008e\3\2\2\2\u027c\u027d\7@\2\2\u027d\u0090\3\2\2\2")
        buf.write("\u027e\u027f\7>\2\2\u027f\u0092\3\2\2\2\u0280\u0281\7")
        buf.write("@\2\2\u0281\u0282\7?\2\2\u0282\u0094\3\2\2\2\u0283\u0284")
        buf.write("\7>\2\2\u0284\u0285\7?\2\2\u0285\u0096\3\2\2\2\u0286\u0287")
        buf.write("\7?\2\2\u0287\u0288\7?\2\2\u0288\u0289\7\60\2\2\u0289")
        buf.write("\u0098\3\2\2\2\u028a\u028b\7-\2\2\u028b\u028c\7\60\2\2")
        buf.write("\u028c\u009a\3\2\2\2\u028d\u028e\7<\2\2\u028e\u028f\7")
        buf.write("<\2\2\u028f\u009c\3\2\2\2\u0290\u0291\7*\2\2\u0291\u009e")
        buf.write("\3\2\2\2\u0292\u0293\7+\2\2\u0293\u00a0\3\2\2\2\u0294")
        buf.write("\u0295\7]\2\2\u0295\u00a2\3\2\2\2\u0296\u0297\7_\2\2\u0297")
        buf.write("\u00a4\3\2\2\2\u0298\u0299\7}\2\2\u0299\u00a6\3\2\2\2")
        buf.write("\u029a\u029b\7\177\2\2\u029b\u00a8\3\2\2\2\u029c\u029d")
        buf.write("\7=\2\2\u029d\u00aa\3\2\2\2\u029e\u029f\7\60\2\2\u029f")
        buf.write("\u00ac\3\2\2\2\u02a0\u02a1\7.\2\2\u02a1\u00ae\3\2\2\2")
        buf.write("\u02a2\u02a4\t\17\2\2\u02a3\u02a2\3\2\2\2\u02a4\u02a5")
        buf.write("\3\2\2\2\u02a5\u02a3\3\2\2\2\u02a5\u02a6\3\2\2\2\u02a6")
        buf.write("\u02a7\3\2\2\2\u02a7\u02a8\bX\2\2\u02a8\u00b0\3\2\2\2")
        buf.write("\u02a9\u02aa\13\2\2\2\u02aa\u02ab\bY\13\2\u02ab\u00b2")
        buf.write("\3\2\2\2$\2\u00c4\u00d0\u00d9\u00df\u00e3\u00e6\u00ec")
        buf.write("\u00f3\u00fa\u0102\u010a\u0111\u0117\u011e\u0120\u012b")
        buf.write("\u0130\u0132\u0139\u0143\u014a\u014c\u0159\u0164\u0174")
        buf.write("\u0185\u018b\u0191\u0197\u019d\u01a3\u0260\u02a5\f\b\2")
        buf.write("\2\3\b\2\3\r\3\3\21\4\3\22\5\3\23\6\3\24\7\3\33\b\3!\t")
        buf.write("\3Y\n")
        return buf.getvalue()


class D96Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    Class_word = 4
    Return_word = 5
    BLOCKCOMMENT = 6
    INTLIT = 7
    FLOATLIT = 8
    BOOLEANLIT = 9
    STRINGLIT = 10
    UNCLOSE_STRING = 11
    ILLEGAL_ESCAPE = 12
    Array_word = 13
    ARRAY_LIT = 14
    Literal_list = 15
    ID = 16
    Program = 17
    Main = 18
    Break = 19
    Continue = 20
    If = 21
    Elseif = 22
    Else = 23
    Foreach = 24
    BooleanTrue = 25
    BooleanFalse = 26
    Array = 27
    In = 28
    Int = 29
    Float = 30
    Boolean = 31
    String = 32
    Return = 33
    Class = 34
    Null = 35
    Val = 36
    Var = 37
    Self = 38
    Constructor = 39
    Destructor = 40
    KEYWORD_New = 41
    By = 42
    ADD_OP = 43
    SUB_OP = 44
    MUL_OP = 45
    DIV_OP = 46
    MOD_OP = 47
    NOT_OP = 48
    AND_OP = 49
    OR_OP = 50
    EQUAL_OP = 51
    DIFF_OP = 52
    ASSIGN_OP = 53
    GREATER_OP = 54
    LESSER_OP = 55
    GREATER_EQUAL_OP = 56
    LESSER_EQUAL_OP = 57
    STRING_COMP_OP = 58
    STRING_CONCAT_OP = 59
    MEMBER_ACCESS_OUT = 60
    LP = 61
    RP = 62
    LSB = 63
    RSB = 64
    LB = 65
    RB = 66
    SEMI = 67
    DOT = 68
    COMA = 69
    WS = 70
    ERROR_CHAR = 71

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "':'", "'$'", "'..'", "'Program'", "'main'", "'Break'", "'Continue'", 
            "'If'", "'Elseif'", "'Else'", "'Foreach'", "'True'", "'False'", 
            "'Array'", "'In'", "'Int'", "'Float'", "'Boolean'", "'String'", 
            "'Return'", "'Class'", "'Null'", "'Val'", "'Var'", "'Self'", 
            "'Constructor'", "'Destructor'", "'New'", "'By'", "'+'", "'-'", 
            "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", "'=='", "'!='", 
            "'='", "'>'", "'<'", "'>='", "'<='", "'==.'", "'+.'", "'::'", 
            "'('", "')'", "'['", "']'", "'{'", "'}'", "';'", "'.'", "','" ]

    symbolicNames = [ "<INVALID>",
            "Class_word", "Return_word", "BLOCKCOMMENT", "INTLIT", "FLOATLIT", 
            "BOOLEANLIT", "STRINGLIT", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
            "Array_word", "ARRAY_LIT", "Literal_list", "ID", "Program", 
            "Main", "Break", "Continue", "If", "Elseif", "Else", "Foreach", 
            "BooleanTrue", "BooleanFalse", "Array", "In", "Int", "Float", 
            "Boolean", "String", "Return", "Class", "Null", "Val", "Var", 
            "Self", "Constructor", "Destructor", "KEYWORD_New", "By", "ADD_OP", 
            "SUB_OP", "MUL_OP", "DIV_OP", "MOD_OP", "NOT_OP", "AND_OP", 
            "OR_OP", "EQUAL_OP", "DIFF_OP", "ASSIGN_OP", "GREATER_OP", "LESSER_OP", 
            "GREATER_EQUAL_OP", "LESSER_EQUAL_OP", "STRING_COMP_OP", "STRING_CONCAT_OP", 
            "MEMBER_ACCESS_OUT", "LP", "RP", "LSB", "RSB", "LB", "RB", "SEMI", 
            "DOT", "COMA", "WS", "ERROR_CHAR" ]

    ruleNames = [ "T__0", "T__1", "T__2", "Class_word", "Return_word", "BLOCKCOMMENT", 
                  "INTLIT", "DECIMAL", "OCTAL", "HEX", "BIN", "FLOATLIT", 
                  "INTERGER_PART", "EXPONENT", "FRACTION", "BOOLEANLIT", 
                  "STRINGLIT", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ESC_SEQ", 
                  "ILL_ESC_SEQ", "OCTAL_ESC", "UNICODE_ESC", "HEX_DIGIT", 
                  "Array_word", "ARRAY_LIT", "Literal_list", "INT_list", 
                  "FLOAT_list", "BOOLEAN_list", "STRING_list", "ID", "Program", 
                  "Main", "Break", "Continue", "If", "Elseif", "Else", "Foreach", 
                  "BooleanTrue", "BooleanFalse", "Array", "In", "Int", "Float", 
                  "Boolean", "String", "Return", "Class", "Null", "Val", 
                  "Var", "Self", "Constructor", "Destructor", "KEYWORD_New", 
                  "By", "KEYWORD", "ADD_OP", "SUB_OP", "MUL_OP", "DIV_OP", 
                  "MOD_OP", "NOT_OP", "AND_OP", "OR_OP", "EQUAL_OP", "DIFF_OP", 
                  "ASSIGN_OP", "GREATER_OP", "LESSER_OP", "GREATER_EQUAL_OP", 
                  "LESSER_EQUAL_OP", "STRING_COMP_OP", "STRING_CONCAT_OP", 
                  "MEMBER_ACCESS_OUT", "LP", "RP", "LSB", "RSB", "LB", "RB", 
                  "SEMI", "DOT", "COMA", "WS", "ERROR_CHAR" ]

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
            actions[6] = self.INTLIT_action 
            actions[11] = self.FLOATLIT_action 
            actions[15] = self.BOOLEANLIT_action 
            actions[16] = self.STRINGLIT_action 
            actions[17] = self.UNCLOSE_STRING_action 
            actions[18] = self.ILLEGAL_ESCAPE_action 
            actions[25] = self.ARRAY_LIT_action 
            actions[31] = self.ID_action 
            actions[87] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INTLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            	
            	self.text = self.text.replace('_','')
            	print("Int: ", self.text)

     

    def FLOATLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

            	self.text = self.text.replace('_','')
            	print("Float: ", self.text)

     

    def BOOLEANLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            	print("Bool: ", self.text)

     

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            	print("String: ", self.text)

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

            	self.text = self.text.replace('"','',1)
            	raise UncloseString(self.text) 


     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:

            	self.text = self.text.replace('"','',1)
            	raise IllegalEscape(self.text) 

     

    def ARRAY_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 6:

            	print("ARRAY: ", self.text)

     

    def ID_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 7:

            	print("ID: ", self.text)

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 8:
             raise ErrorToken(self.text) 
     


