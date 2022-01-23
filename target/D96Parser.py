# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3D")
        buf.write("\u0243\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\3\2\3\2\3")
        buf.write("\2\3\3\3\3\3\3\3\4\3\4\3\4\5\4\u008e\n\4\3\5\3\5\3\5\3")
        buf.write("\5\5\5\u0094\n\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\5\6\u009d")
        buf.write("\n\6\3\7\3\7\3\7\5\7\u00a2\n\7\3\b\3\b\5\b\u00a6\n\b\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\5\t\u00ae\n\t\3\t\3\t\3\n\3\n\3")
        buf.write("\n\3\13\3\13\3\13\5\13\u00b8\n\13\3\f\5\f\u00bb\n\f\3")
        buf.write("\f\3\f\3\r\3\r\3\r\5\r\u00c2\n\r\3\16\3\16\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\17\5\17\u00cc\n\17\3\17\3\17\3\20\3\20")
        buf.write("\5\20\u00d2\n\20\3\21\3\21\3\22\3\22\3\23\5\23\u00d9\n")
        buf.write("\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\25\3\25")
        buf.write("\3\25\5\25\u00e6\n\25\3\26\3\26\3\26\3\26\5\26\u00ec\n")
        buf.write("\26\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\31\3\31\3\31")
        buf.write("\5\31\u00f8\n\31\3\32\3\32\3\32\5\32\u00fd\n\32\3\33\3")
        buf.write("\33\3\33\3\33\5\33\u0103\n\33\3\34\3\34\3\34\3\34\5\34")
        buf.write("\u0109\n\34\3\34\3\34\3\34\3\34\3\34\5\34\u0110\n\34\3")
        buf.write("\34\3\34\3\34\5\34\u0115\n\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\5\34\u011c\n\34\3\34\3\34\3\34\3\34\3\34\5\34\u0123\n")
        buf.write("\34\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\5\37\u0137\n")
        buf.write("\37\3 \3 \3 \3 \5 \u013d\n \3!\3!\3!\3!\3!\3!\3!\3!\3")
        buf.write("!\5!\u0148\n!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\7!\u0156")
        buf.write("\n!\f!\16!\u0159\13!\3\"\3\"\3\"\5\"\u015e\n\"\3\"\3\"")
        buf.write("\3\"\7\"\u0163\n\"\f\"\16\"\u0166\13\"\3#\3#\3#\3#\5#")
        buf.write("\u016c\n#\3$\3$\3$\5$\u0171\n$\3$\3$\3$\3$\3$\3$\7$\u0179")
        buf.write("\n$\f$\16$\u017c\13$\3%\3%\5%\u0180\n%\3&\3&\3&\3&\5&")
        buf.write("\u0186\n&\3&\3&\3&\7&\u018b\n&\f&\16&\u018e\13&\3\'\3")
        buf.write("\'\3\'\3\'\5\'\u0194\n\'\3\'\3\'\3\'\7\'\u0199\n\'\f\'")
        buf.write("\16\'\u019c\13\'\3(\3(\3(\5(\u01a1\n(\3(\3(\3(\7(\u01a6")
        buf.write("\n(\f(\16(\u01a9\13(\3)\3)\3)\3)\3*\3*\3*\5*\u01b2\n*")
        buf.write("\3+\3+\3+\5+\u01b7\n+\3,\3,\3,\3-\3-\3-\3-\3-\3-\3-\5")
        buf.write("-\u01c3\n-\3.\3.\3.\3.\3.\3.\5.\u01cb\n.\3.\3.\3/\3/\3")
        buf.write("/\3\60\3\60\3\60\5\60\u01d5\n\60\3\61\3\61\3\62\3\62\5")
        buf.write("\62\u01db\n\62\3\62\3\62\3\62\3\63\3\63\5\63\u01e2\n\63")
        buf.write("\3\64\3\64\3\64\3\64\3\64\3\64\5\64\u01ea\n\64\3\64\5")
        buf.write("\64\u01ed\n\64\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65")
        buf.write("\3\65\3\65\5\65\u01f9\n\65\5\65\u01fb\n\65\3\66\3\66\3")
        buf.write("\66\5\66\u0200\n\66\3\67\3\67\3\67\5\67\u0205\n\67\38")
        buf.write("\38\38\39\39\39\39\39\39\39\39\39\59\u0213\n9\39\39\3")
        buf.write("9\3:\3:\3:\3:\3:\3;\3;\5;\u021f\n;\3<\3<\3<\3<\3<\3=\3")
        buf.write("=\3=\5=\u0229\n=\3>\3>\3>\3>\5>\u022f\n>\3?\3?\3?\3@\3")
        buf.write("@\3@\3@\3A\3A\3A\5A\u023b\nA\3B\3B\3B\3B\5B\u0241\nB\3")
        buf.write("B\2\b@BFJLNC\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"")
        buf.write("$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz")
        buf.write("|~\u0080\u0082\2\t\3\2\7\b\3\2\33\34\3\2\24\27\5\2\7\7")
        buf.write("\t\t\36\37\3\2*+\3\2-\60\3\2\61\62\2\u0254\2\u0084\3\2")
        buf.write("\2\2\4\u0087\3\2\2\2\6\u008d\3\2\2\2\b\u008f\3\2\2\2\n")
        buf.write("\u009c\3\2\2\2\f\u00a1\3\2\2\2\16\u00a5\3\2\2\2\20\u00a7")
        buf.write("\3\2\2\2\22\u00b1\3\2\2\2\24\u00b7\3\2\2\2\26\u00ba\3")
        buf.write("\2\2\2\30\u00c1\3\2\2\2\32\u00c3\3\2\2\2\34\u00c5\3\2")
        buf.write("\2\2\36\u00d1\3\2\2\2 \u00d3\3\2\2\2\"\u00d5\3\2\2\2$")
        buf.write("\u00d8\3\2\2\2&\u00de\3\2\2\2(\u00e5\3\2\2\2*\u00eb\3")
        buf.write("\2\2\2,\u00ed\3\2\2\2.\u00f1\3\2\2\2\60\u00f7\3\2\2\2")
        buf.write("\62\u00fc\3\2\2\2\64\u0102\3\2\2\2\66\u0122\3\2\2\28\u0124")
        buf.write("\3\2\2\2:\u012a\3\2\2\2<\u0136\3\2\2\2>\u013c\3\2\2\2")
        buf.write("@\u0147\3\2\2\2B\u015d\3\2\2\2D\u016b\3\2\2\2F\u0170\3")
        buf.write("\2\2\2H\u017f\3\2\2\2J\u0185\3\2\2\2L\u0193\3\2\2\2N\u01a0")
        buf.write("\3\2\2\2P\u01aa\3\2\2\2R\u01b1\3\2\2\2T\u01b6\3\2\2\2")
        buf.write("V\u01b8\3\2\2\2X\u01c2\3\2\2\2Z\u01c4\3\2\2\2\\\u01ce")
        buf.write("\3\2\2\2^\u01d4\3\2\2\2`\u01d6\3\2\2\2b\u01da\3\2\2\2")
        buf.write("d\u01e1\3\2\2\2f\u01ec\3\2\2\2h\u01fa\3\2\2\2j\u01ff\3")
        buf.write("\2\2\2l\u0204\3\2\2\2n\u0206\3\2\2\2p\u0209\3\2\2\2r\u0217")
        buf.write("\3\2\2\2t\u021c\3\2\2\2v\u0220\3\2\2\2x\u0228\3\2\2\2")
        buf.write("z\u022e\3\2\2\2|\u0230\3\2\2\2~\u0233\3\2\2\2\u0080\u023a")
        buf.write("\3\2\2\2\u0082\u0240\3\2\2\2\u0084\u0085\5\4\3\2\u0085")
        buf.write("\u0086\7\2\2\3\u0086\3\3\2\2\2\u0087\u0088\5\b\5\2\u0088")
        buf.write("\u0089\5\6\4\2\u0089\5\3\2\2\2\u008a\u008b\5\b\5\2\u008b")
        buf.write("\u008c\5\6\4\2\u008c\u008e\3\2\2\2\u008d\u008a\3\2\2\2")
        buf.write("\u008d\u008e\3\2\2\2\u008e\7\3\2\2\2\u008f\u0090\7\31")
        buf.write("\2\2\u0090\u0093\t\2\2\2\u0091\u0092\7\3\2\2\u0092\u0094")
        buf.write("\t\2\2\2\u0093\u0091\3\2\2\2\u0093\u0094\3\2\2\2\u0094")
        buf.write("\u0095\3\2\2\2\u0095\u0096\7<\2\2\u0096\u0097\5\n\6\2")
        buf.write("\u0097\u0098\7=\2\2\u0098\t\3\2\2\2\u0099\u009a\5\16\b")
        buf.write("\2\u009a\u009b\5\f\7\2\u009b\u009d\3\2\2\2\u009c\u0099")
        buf.write("\3\2\2\2\u009c\u009d\3\2\2\2\u009d\13\3\2\2\2\u009e\u009f")
        buf.write("\5\16\b\2\u009f\u00a0\5\f\7\2\u00a0\u00a2\3\2\2\2\u00a1")
        buf.write("\u009e\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2\r\3\2\2\2\u00a3")
        buf.write("\u00a6\5\20\t\2\u00a4\u00a6\5$\23\2\u00a5\u00a3\3\2\2")
        buf.write("\2\u00a5\u00a4\3\2\2\2\u00a6\17\3\2\2\2\u00a7\u00a8\t")
        buf.write("\3\2\2\u00a8\u00a9\5\22\n\2\u00a9\u00aa\7\3\2\2\u00aa")
        buf.write("\u00ad\5\30\r\2\u00ab\u00ac\7,\2\2\u00ac\u00ae\5\62\32")
        buf.write("\2\u00ad\u00ab\3\2\2\2\u00ad\u00ae\3\2\2\2\u00ae\u00af")
        buf.write("\3\2\2\2\u00af\u00b0\7>\2\2\u00b0\21\3\2\2\2\u00b1\u00b2")
        buf.write("\5\26\f\2\u00b2\u00b3\5\24\13\2\u00b3\23\3\2\2\2\u00b4")
        buf.write("\u00b5\5\26\f\2\u00b5\u00b6\5\24\13\2\u00b6\u00b8\3\2")
        buf.write("\2\2\u00b7\u00b4\3\2\2\2\u00b7\u00b8\3\2\2\2\u00b8\25")
        buf.write("\3\2\2\2\u00b9\u00bb\7\4\2\2\u00ba\u00b9\3\2\2\2\u00ba")
        buf.write("\u00bb\3\2\2\2\u00bb\u00bc\3\2\2\2\u00bc\u00bd\7\7\2\2")
        buf.write("\u00bd\27\3\2\2\2\u00be\u00c2\5\32\16\2\u00bf\u00c2\5")
        buf.write("\34\17\2\u00c0\u00c2\5\"\22\2\u00c1\u00be\3\2\2\2\u00c1")
        buf.write("\u00bf\3\2\2\2\u00c1\u00c0\3\2\2\2\u00c2\31\3\2\2\2\u00c3")
        buf.write("\u00c4\t\4\2\2\u00c4\33\3\2\2\2\u00c5\u00c6\7\22\2\2\u00c6")
        buf.write("\u00cb\7:\2\2\u00c7\u00c8\5\36\20\2\u00c8\u00c9\7@\2\2")
        buf.write("\u00c9\u00ca\5 \21\2\u00ca\u00cc\3\2\2\2\u00cb\u00c7\3")
        buf.write("\2\2\2\u00cb\u00cc\3\2\2\2\u00cc\u00cd\3\2\2\2\u00cd\u00ce")
        buf.write("\7;\2\2\u00ce\35\3\2\2\2\u00cf\u00d2\5\32\16\2\u00d0\u00d2")
        buf.write("\5\34\17\2\u00d1\u00cf\3\2\2\2\u00d1\u00d0\3\2\2\2\u00d2")
        buf.write("\37\3\2\2\2\u00d3\u00d4\7\64\2\2\u00d4!\3\2\2\2\u00d5")
        buf.write("\u00d6\7\7\2\2\u00d6#\3\2\2\2\u00d7\u00d9\7\4\2\2\u00d8")
        buf.write("\u00d7\3\2\2\2\u00d8\u00d9\3\2\2\2\u00d9\u00da\3\2\2\2")
        buf.write("\u00da\u00db\t\5\2\2\u00db\u00dc\5&\24\2\u00dc\u00dd\5")
        buf.write("P)\2\u00dd%\3\2\2\2\u00de\u00df\78\2\2\u00df\u00e0\5(")
        buf.write("\25\2\u00e0\u00e1\79\2\2\u00e1\'\3\2\2\2\u00e2\u00e3\5")
        buf.write(",\27\2\u00e3\u00e4\5*\26\2\u00e4\u00e6\3\2\2\2\u00e5\u00e2")
        buf.write("\3\2\2\2\u00e5\u00e6\3\2\2\2\u00e6)\3\2\2\2\u00e7\u00e8")
        buf.write("\7>\2\2\u00e8\u00e9\5,\27\2\u00e9\u00ea\5*\26\2\u00ea")
        buf.write("\u00ec\3\2\2\2\u00eb\u00e7\3\2\2\2\u00eb\u00ec\3\2\2\2")
        buf.write("\u00ec+\3\2\2\2\u00ed\u00ee\5.\30\2\u00ee\u00ef\7\3\2")
        buf.write("\2\u00ef\u00f0\5\30\r\2\u00f0-\3\2\2\2\u00f1\u00f2\7\7")
        buf.write("\2\2\u00f2\u00f3\5\60\31\2\u00f3/\3\2\2\2\u00f4\u00f5")
        buf.write("\7@\2\2\u00f5\u00f6\7\7\2\2\u00f6\u00f8\5\60\31\2\u00f7")
        buf.write("\u00f4\3\2\2\2\u00f7\u00f8\3\2\2\2\u00f8\61\3\2\2\2\u00f9")
        buf.write("\u00fa\5\66\34\2\u00fa\u00fb\5\64\33\2\u00fb\u00fd\3\2")
        buf.write("\2\2\u00fc\u00f9\3\2\2\2\u00fc\u00fd\3\2\2\2\u00fd\63")
        buf.write("\3\2\2\2\u00fe\u00ff\7@\2\2\u00ff\u0100\5\66\34\2\u0100")
        buf.write("\u0101\5\64\33\2\u0101\u0103\3\2\2\2\u0102\u00fe\3\2\2")
        buf.write("\2\u0102\u0103\3\2\2\2\u0103\65\3\2\2\2\u0104\u0123\5")
        buf.write("8\35\2\u0105\u0106\7\7\2\2\u0106\u0108\7\63\2\2\u0107")
        buf.write("\u0109\7\4\2\2\u0108\u0107\3\2\2\2\u0108\u0109\3\2\2\2")
        buf.write("\u0109\u010a\3\2\2\2\u010a\u010f\7\7\2\2\u010b\u010c\7")
        buf.write("8\2\2\u010c\u010d\5\62\32\2\u010d\u010e\79\2\2\u010e\u0110")
        buf.write("\3\2\2\2\u010f\u010b\3\2\2\2\u010f\u0110\3\2\2\2\u0110")
        buf.write("\u0123\3\2\2\2\u0111\u0112\7\7\2\2\u0112\u0114\7?\2\2")
        buf.write("\u0113\u0115\7\4\2\2\u0114\u0113\3\2\2\2\u0114\u0115\3")
        buf.write("\2\2\2\u0115\u0116\3\2\2\2\u0116\u011b\7\7\2\2\u0117\u0118")
        buf.write("\78\2\2\u0118\u0119\5\62\32\2\u0119\u011a\79\2\2\u011a")
        buf.write("\u011c\3\2\2\2\u011b\u0117\3\2\2\2\u011b\u011c\3\2\2\2")
        buf.write("\u011c\u0123\3\2\2\2\u011d\u0123\5:\36\2\u011e\u0123\5")
        buf.write("@!\2\u011f\u0123\5H%\2\u0120\u0123\5N(\2\u0121\u0123\7")
        buf.write("\7\2\2\u0122\u0104\3\2\2\2\u0122\u0105\3\2\2\2\u0122\u0111")
        buf.write("\3\2\2\2\u0122\u011d\3\2\2\2\u0122\u011e\3\2\2\2\u0122")
        buf.write("\u011f\3\2\2\2\u0122\u0120\3\2\2\2\u0122\u0121\3\2\2\2")
        buf.write("\u0123\67\3\2\2\2\u0124\u0125\7 \2\2\u0125\u0126\7\7\2")
        buf.write("\2\u0126\u0127\78\2\2\u0127\u0128\5\62\32\2\u0128\u0129")
        buf.write("\79\2\2\u01299\3\2\2\2\u012a\u012b\5> \2\u012b\u012c\5")
        buf.write("<\37\2\u012c;\3\2\2\2\u012d\u012e\7<\2\2\u012e\u012f\5")
        buf.write("> \2\u012f\u0130\7=\2\2\u0130\u0137\3\2\2\2\u0131\u0132")
        buf.write("\7<\2\2\u0132\u0133\5> \2\u0133\u0134\7=\2\2\u0134\u0135")
        buf.write("\5<\37\2\u0135\u0137\3\2\2\2\u0136\u012d\3\2\2\2\u0136")
        buf.write("\u0131\3\2\2\2\u0137=\3\2\2\2\u0138\u013d\5@!\2\u0139")
        buf.write("\u013d\5H%\2\u013a\u013d\5N(\2\u013b\u013d\7\7\2\2\u013c")
        buf.write("\u0138\3\2\2\2\u013c\u0139\3\2\2\2\u013c\u013a\3\2\2\2")
        buf.write("\u013c\u013b\3\2\2\2\u013d?\3\2\2\2\u013e\u013f\b!\1\2")
        buf.write("\u013f\u0140\7#\2\2\u0140\u0148\5@!\r\u0141\u0148\5D#")
        buf.write("\2\u0142\u0148\5B\"\2\u0143\u0148\5F$\2\u0144\u0148\7")
        buf.write("\64\2\2\u0145\u0148\7\65\2\2\u0146\u0148\7\7\2\2\u0147")
        buf.write("\u013e\3\2\2\2\u0147\u0141\3\2\2\2\u0147\u0142\3\2\2\2")
        buf.write("\u0147\u0143\3\2\2\2\u0147\u0144\3\2\2\2\u0147\u0145\3")
        buf.write("\2\2\2\u0147\u0146\3\2\2\2\u0148\u0157\3\2\2\2\u0149\u014a")
        buf.write("\f\13\2\2\u014a\u014b\7$\2\2\u014b\u0156\5@!\f\u014c\u014d")
        buf.write("\f\n\2\2\u014d\u014e\7%\2\2\u014e\u0156\5@!\13\u014f\u0150")
        buf.write("\f\b\2\2\u0150\u0151\7\"\2\2\u0151\u0156\5@!\t\u0152\u0153")
        buf.write("\f\7\2\2\u0153\u0154\7#\2\2\u0154\u0156\5@!\b\u0155\u0149")
        buf.write("\3\2\2\2\u0155\u014c\3\2\2\2\u0155\u014f\3\2\2\2\u0155")
        buf.write("\u0152\3\2\2\2\u0156\u0159\3\2\2\2\u0157\u0155\3\2\2\2")
        buf.write("\u0157\u0158\3\2\2\2\u0158A\3\2\2\2\u0159\u0157\3\2\2")
        buf.write("\2\u015a\u015b\b\"\1\2\u015b\u015e\7\64\2\2\u015c\u015e")
        buf.write("\7\7\2\2\u015d\u015a\3\2\2\2\u015d\u015c\3\2\2\2\u015e")
        buf.write("\u0164\3\2\2\2\u015f\u0160\f\5\2\2\u0160\u0161\7&\2\2")
        buf.write("\u0161\u0163\5B\"\6\u0162\u015f\3\2\2\2\u0163\u0166\3")
        buf.write("\2\2\2\u0164\u0162\3\2\2\2\u0164\u0165\3\2\2\2\u0165C")
        buf.write("\3\2\2\2\u0166\u0164\3\2\2\2\u0167\u0168\7\'\2\2\u0168")
        buf.write("\u016c\5D#\2\u0169\u016c\7\66\2\2\u016a\u016c\7\7\2\2")
        buf.write("\u016b\u0167\3\2\2\2\u016b\u0169\3\2\2\2\u016b\u016a\3")
        buf.write("\2\2\2\u016cE\3\2\2\2\u016d\u016e\b$\1\2\u016e\u0171\7")
        buf.write("\66\2\2\u016f\u0171\7\7\2\2\u0170\u016d\3\2\2\2\u0170")
        buf.write("\u016f\3\2\2\2\u0171\u017a\3\2\2\2\u0172\u0173\f\6\2\2")
        buf.write("\u0173\u0174\7(\2\2\u0174\u0179\5F$\7\u0175\u0176\f\5")
        buf.write("\2\2\u0176\u0177\7)\2\2\u0177\u0179\5F$\6\u0178\u0172")
        buf.write("\3\2\2\2\u0178\u0175\3\2\2\2\u0179\u017c\3\2\2\2\u017a")
        buf.write("\u0178\3\2\2\2\u017a\u017b\3\2\2\2\u017bG\3\2\2\2\u017c")
        buf.write("\u017a\3\2\2\2\u017d\u0180\5J&\2\u017e\u0180\5L\'\2\u017f")
        buf.write("\u017d\3\2\2\2\u017f\u017e\3\2\2\2\u0180I\3\2\2\2\u0181")
        buf.write("\u0182\b&\1\2\u0182\u0186\7\64\2\2\u0183\u0186\7\66\2")
        buf.write("\2\u0184\u0186\7\7\2\2\u0185\u0181\3\2\2\2\u0185\u0183")
        buf.write("\3\2\2\2\u0185\u0184\3\2\2\2\u0186\u018c\3\2\2\2\u0187")
        buf.write("\u0188\f\6\2\2\u0188\u0189\t\6\2\2\u0189\u018b\5J&\7\u018a")
        buf.write("\u0187\3\2\2\2\u018b\u018e\3\2\2\2\u018c\u018a\3\2\2\2")
        buf.write("\u018c\u018d\3\2\2\2\u018dK\3\2\2\2\u018e\u018c\3\2\2")
        buf.write("\2\u018f\u0190\b\'\1\2\u0190\u0194\7\64\2\2\u0191\u0194")
        buf.write("\7\65\2\2\u0192\u0194\7\7\2\2\u0193\u018f\3\2\2\2\u0193")
        buf.write("\u0191\3\2\2\2\u0193\u0192\3\2\2\2\u0194\u019a\3\2\2\2")
        buf.write("\u0195\u0196\f\6\2\2\u0196\u0197\t\7\2\2\u0197\u0199\5")
        buf.write("L\'\7\u0198\u0195\3\2\2\2\u0199\u019c\3\2\2\2\u019a\u0198")
        buf.write("\3\2\2\2\u019a\u019b\3\2\2\2\u019bM\3\2\2\2\u019c\u019a")
        buf.write("\3\2\2\2\u019d\u019e\b(\1\2\u019e\u01a1\7\67\2\2\u019f")
        buf.write("\u01a1\7\7\2\2\u01a0\u019d\3\2\2\2\u01a0\u019f\3\2\2\2")
        buf.write("\u01a1\u01a7\3\2\2\2\u01a2\u01a3\f\5\2\2\u01a3\u01a4\t")
        buf.write("\b\2\2\u01a4\u01a6\5N(\6\u01a5\u01a2\3\2\2\2\u01a6\u01a9")
        buf.write("\3\2\2\2\u01a7\u01a5\3\2\2\2\u01a7\u01a8\3\2\2\2\u01a8")
        buf.write("O\3\2\2\2\u01a9\u01a7\3\2\2\2\u01aa\u01ab\7<\2\2\u01ab")
        buf.write("\u01ac\5R*\2\u01ac\u01ad\7=\2\2\u01adQ\3\2\2\2\u01ae\u01af")
        buf.write("\5V,\2\u01af\u01b0\5T+\2\u01b0\u01b2\3\2\2\2\u01b1\u01ae")
        buf.write("\3\2\2\2\u01b1\u01b2\3\2\2\2\u01b2S\3\2\2\2\u01b3\u01b4")
        buf.write("\5V,\2\u01b4\u01b5\5T+\2\u01b5\u01b7\3\2\2\2\u01b6\u01b3")
        buf.write("\3\2\2\2\u01b6\u01b7\3\2\2\2\u01b7U\3\2\2\2\u01b8\u01b9")
        buf.write("\5X-\2\u01b9\u01ba\7>\2\2\u01baW\3\2\2\2\u01bb\u01c3\5")
        buf.write("Z.\2\u01bc\u01c3\5b\62\2\u01bd\u01c3\5d\63\2\u01be\u01c3")
        buf.write("\5p9\2\u01bf\u01c3\7\n\2\2\u01c0\u01c3\7\13\2\2\u01c1")
        buf.write("\u01c3\5t;\2\u01c2\u01bb\3\2\2\2\u01c2\u01bc\3\2\2\2\u01c2")
        buf.write("\u01bd\3\2\2\2\u01c2\u01be\3\2\2\2\u01c2\u01bf\3\2\2\2")
        buf.write("\u01c2\u01c0\3\2\2\2\u01c2\u01c1\3\2\2\2\u01c3Y\3\2\2")
        buf.write("\2\u01c4\u01c5\t\3\2\2\u01c5\u01c6\5\\/\2\u01c6\u01c7")
        buf.write("\7\3\2\2\u01c7\u01ca\5\30\r\2\u01c8\u01c9\7,\2\2\u01c9")
        buf.write("\u01cb\5\62\32\2\u01ca\u01c8\3\2\2\2\u01ca\u01cb\3\2\2")
        buf.write("\2\u01cb\u01cc\3\2\2\2\u01cc\u01cd\7>\2\2\u01cd[\3\2\2")
        buf.write("\2\u01ce\u01cf\5`\61\2\u01cf\u01d0\5^\60\2\u01d0]\3\2")
        buf.write("\2\2\u01d1\u01d2\5`\61\2\u01d2\u01d3\5^\60\2\u01d3\u01d5")
        buf.write("\3\2\2\2\u01d4\u01d1\3\2\2\2\u01d4\u01d5\3\2\2\2\u01d5")
        buf.write("_\3\2\2\2\u01d6\u01d7\7\7\2\2\u01d7a\3\2\2\2\u01d8\u01db")
        buf.write("\7\7\2\2\u01d9\u01db\5:\36\2\u01da\u01d8\3\2\2\2\u01da")
        buf.write("\u01d9\3\2\2\2\u01db\u01dc\3\2\2\2\u01dc\u01dd\7,\2\2")
        buf.write("\u01dd\u01de\5\66\34\2\u01dec\3\2\2\2\u01df\u01e2\5f\64")
        buf.write("\2\u01e0\u01e2\5h\65\2\u01e1\u01df\3\2\2\2\u01e1\u01e0")
        buf.write("\3\2\2\2\u01e2e\3\2\2\2\u01e3\u01e4\7\f\2\2\u01e4\u01e5")
        buf.write("\5\66\34\2\u01e5\u01e6\5f\64\2\u01e6\u01e9\5j\66\2\u01e7")
        buf.write("\u01e8\7\16\2\2\u01e8\u01ea\5f\64\2\u01e9\u01e7\3\2\2")
        buf.write("\2\u01e9\u01ea\3\2\2\2\u01ea\u01ed\3\2\2\2\u01eb\u01ed")
        buf.write("\5P)\2\u01ec\u01e3\3\2\2\2\u01ec\u01eb\3\2\2\2\u01edg")
        buf.write("\3\2\2\2\u01ee\u01ef\7\f\2\2\u01ef\u01f0\5\66\34\2\u01f0")
        buf.write("\u01f1\5d\63\2\u01f1\u01fb\3\2\2\2\u01f2\u01f3\7\f\2\2")
        buf.write("\u01f3\u01f4\5\66\34\2\u01f4\u01f5\5f\64\2\u01f5\u01f8")
        buf.write("\5j\66\2\u01f6\u01f7\7\16\2\2\u01f7\u01f9\5h\65\2\u01f8")
        buf.write("\u01f6\3\2\2\2\u01f8\u01f9\3\2\2\2\u01f9\u01fb\3\2\2\2")
        buf.write("\u01fa\u01ee\3\2\2\2\u01fa\u01f2\3\2\2\2\u01fbi\3\2\2")
        buf.write("\2\u01fc\u01fd\5n8\2\u01fd\u01fe\5l\67\2\u01fe\u0200\3")
        buf.write("\2\2\2\u01ff\u01fc\3\2\2\2\u01ff\u0200\3\2\2\2\u0200k")
        buf.write("\3\2\2\2\u0201\u0202\5n8\2\u0202\u0203\5l\67\2\u0203\u0205")
        buf.write("\3\2\2\2\u0204\u0201\3\2\2\2\u0204\u0205\3\2\2\2\u0205")
        buf.write("m\3\2\2\2\u0206\u0207\7\r\2\2\u0207\u0208\5d\63\2\u0208")
        buf.write("o\3\2\2\2\u0209\u020a\7\17\2\2\u020a\u020b\78\2\2\u020b")
        buf.write("\u020c\7\7\2\2\u020c\u020d\7\23\2\2\u020d\u020e\5\66\34")
        buf.write("\2\u020e\u020f\7\5\2\2\u020f\u0212\5\66\34\2\u0210\u0211")
        buf.write("\7!\2\2\u0211\u0213\5\66\34\2\u0212\u0210\3\2\2\2\u0212")
        buf.write("\u0213\3\2\2\2\u0213\u0214\3\2\2\2\u0214\u0215\79\2\2")
        buf.write("\u0215\u0216\5P)\2\u0216q\3\2\2\2\u0217\u0218\7\7\2\2")
        buf.write("\u0218\u0219\7<\2\2\u0219\u021a\5\62\32\2\u021a\u021b")
        buf.write("\7=\2\2\u021bs\3\2\2\2\u021c\u021e\7\30\2\2\u021d\u021f")
        buf.write("\5\66\34\2\u021e\u021d\3\2\2\2\u021e\u021f\3\2\2\2\u021f")
        buf.write("u\3\2\2\2\u0220\u0221\7\22\2\2\u0221\u0222\78\2\2\u0222")
        buf.write("\u0223\5x=\2\u0223\u0224\79\2\2\u0224w\3\2\2\2\u0225\u0226")
        buf.write("\5|?\2\u0226\u0227\5z>\2\u0227\u0229\3\2\2\2\u0228\u0225")
        buf.write("\3\2\2\2\u0228\u0229\3\2\2\2\u0229y\3\2\2\2\u022a\u022b")
        buf.write("\7@\2\2\u022b\u022c\5|?\2\u022c\u022d\5z>\2\u022d\u022f")
        buf.write("\3\2\2\2\u022e\u022a\3\2\2\2\u022e\u022f\3\2\2\2\u022f")
        buf.write("{\3\2\2\2\u0230\u0231\7\22\2\2\u0231\u0232\5~@\2\u0232")
        buf.write("}\3\2\2\2\u0233\u0234\78\2\2\u0234\u0235\5\u0080A\2\u0235")
        buf.write("\u0236\79\2\2\u0236\177\3\2\2\2\u0237\u0238\5\66\34\2")
        buf.write("\u0238\u0239\5\u0082B\2\u0239\u023b\3\2\2\2\u023a\u0237")
        buf.write("\3\2\2\2\u023a\u023b\3\2\2\2\u023b\u0081\3\2\2\2\u023c")
        buf.write("\u023d\7@\2\2\u023d\u023e\5\66\34\2\u023e\u023f\5\u0082")
        buf.write("B\2\u023f\u0241\3\2\2\2\u0240\u023c\3\2\2\2\u0240\u0241")
        buf.write("\3\2\2\2\u0241\u0083\3\2\2\2=\u008d\u0093\u009c\u00a1")
        buf.write("\u00a5\u00ad\u00b7\u00ba\u00c1\u00cb\u00d1\u00d8\u00e5")
        buf.write("\u00eb\u00f7\u00fc\u0102\u0108\u010f\u0114\u011b\u0122")
        buf.write("\u0136\u013c\u0147\u0155\u0157\u015d\u0164\u016b\u0170")
        buf.write("\u0178\u017a\u017f\u0185\u018c\u0193\u019a\u01a0\u01a7")
        buf.write("\u01b1\u01b6\u01c2\u01ca\u01d4\u01da\u01e1\u01e9\u01ec")
        buf.write("\u01f8\u01fa\u01ff\u0204\u0212\u021e\u0228\u022e\u023a")
        buf.write("\u0240")
        return buf.getvalue()


class D96Parser ( Parser ):

    grammarFileName = "D96.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':'", "'$'", "'..'", "<INVALID>", "<INVALID>", 
                     "'Program'", "'main'", "'Break'", "'Continue'", "'If'", 
                     "'Elseif'", "'Else'", "'Foreach'", "'True'", "'False'", 
                     "'Array'", "'In'", "'Int'", "'Float'", "'Boolean'", 
                     "'String'", "'Return'", "'Class'", "'Null'", "'Val'", 
                     "'Var'", "'Self'", "'Constructor'", "'Destructor'", 
                     "'New'", "'By'", "'+'", "'-'", "'*'", "'/'", "'%'", 
                     "'!'", "'&&'", "'||'", "'=='", "'!='", "'='", "'>'", 
                     "'<'", "'>='", "'<='", "'==.'", "'+.'", "'::'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'('", "')'", 
                     "'['", "']'", "'{'", "'}'", "';'", "'.'", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "BLOCKCOMMENT", "ID", "Program", "Main", "Break", 
                      "Continue", "If", "Elseif", "Else", "Foreach", "BooleanTrue", 
                      "BooleanFalse", "Array", "In", "Int", "Float", "Boolean", 
                      "String", "Return", "Class", "Null", "Val", "Var", 
                      "Self", "Constructor", "Destructor", "KEYWORD_New", 
                      "By", "ADD_OP", "SUB_OP", "MUL_OP", "DIV_OP", "MOD_OP", 
                      "NOT_OP", "AND_OP", "OR_OP", "EQUAL_OP", "DIFF_OP", 
                      "ASSIGN_OP", "GREATER_OP", "LESSER_OP", "GREATER_EQUAL_OP", 
                      "LESSER_EQUAL_OP", "STRING_COMP_OP", "STRING_CONCAT_OP", 
                      "MEMBER_ACCESS_OUT", "INTLIT", "FLOATLIT", "BOOLEANLIT", 
                      "STRINGLIT", "LP", "RP", "LSB", "RSB", "LB", "RB", 
                      "SEMI", "DOT", "COMA", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                      "ERROR_CHAR" ]

    RULE_program = 0
    RULE_many_class_decl = 1
    RULE_class_decl_list = 2
    RULE_class_decl = 3
    RULE_member_lists = 4
    RULE_member_list_tail = 5
    RULE_member = 6
    RULE_attributes = 7
    RULE_attribute_list = 8
    RULE_attribute_list_tail = 9
    RULE_attribute_name = 10
    RULE_types = 11
    RULE_primitive_Type = 12
    RULE_array_Type = 13
    RULE_element_type = 14
    RULE_array_size = 15
    RULE_class_type = 16
    RULE_methods = 17
    RULE_param = 18
    RULE_paramlist = 19
    RULE_paramlist_tail = 20
    RULE_param_decl = 21
    RULE_idlist = 22
    RULE_idlist_tail = 23
    RULE_expr_list = 24
    RULE_expr_list_tail = 25
    RULE_expr = 26
    RULE_class_expr = 27
    RULE_index_expr = 28
    RULE_index_operators = 29
    RULE_lower_expr = 30
    RULE_math_expr = 31
    RULE_mod_expr = 32
    RULE_logical_not_expr = 33
    RULE_logical_expr = 34
    RULE_relational_expr = 35
    RULE_relational_expr_1 = 36
    RULE_relational_expr_2 = 37
    RULE_string_expr = 38
    RULE_block_stmt = 39
    RULE_block_stmt_list = 40
    RULE_block_stmt_list_tail = 41
    RULE_stmt = 42
    RULE_stmt_list = 43
    RULE_var_cons_decl = 44
    RULE_var_cons_list = 45
    RULE_var_cons_list_tail = 46
    RULE_var_cons_name = 47
    RULE_asm = 48
    RULE_if_stmt = 49
    RULE_matchStmt = 50
    RULE_unmatchStmt = 51
    RULE_elseif_list = 52
    RULE_elseif_list_tail = 53
    RULE_elseif_stmt = 54
    RULE_loop_stmt = 55
    RULE_call = 56
    RULE_return_stmt = 57
    RULE_multi_ArrayLIT = 58
    RULE_array_list = 59
    RULE_array_list_tail = 60
    RULE_index_ArrayLIT = 61
    RULE_elements = 62
    RULE_element_list = 63
    RULE_elements_tail = 64

    ruleNames =  [ "program", "many_class_decl", "class_decl_list", "class_decl", 
                   "member_lists", "member_list_tail", "member", "attributes", 
                   "attribute_list", "attribute_list_tail", "attribute_name", 
                   "types", "primitive_Type", "array_Type", "element_type", 
                   "array_size", "class_type", "methods", "param", "paramlist", 
                   "paramlist_tail", "param_decl", "idlist", "idlist_tail", 
                   "expr_list", "expr_list_tail", "expr", "class_expr", 
                   "index_expr", "index_operators", "lower_expr", "math_expr", 
                   "mod_expr", "logical_not_expr", "logical_expr", "relational_expr", 
                   "relational_expr_1", "relational_expr_2", "string_expr", 
                   "block_stmt", "block_stmt_list", "block_stmt_list_tail", 
                   "stmt", "stmt_list", "var_cons_decl", "var_cons_list", 
                   "var_cons_list_tail", "var_cons_name", "asm", "if_stmt", 
                   "matchStmt", "unmatchStmt", "elseif_list", "elseif_list_tail", 
                   "elseif_stmt", "loop_stmt", "call", "return_stmt", "multi_ArrayLIT", 
                   "array_list", "array_list_tail", "index_ArrayLIT", "elements", 
                   "element_list", "elements_tail" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    BLOCKCOMMENT=4
    ID=5
    Program=6
    Main=7
    Break=8
    Continue=9
    If=10
    Elseif=11
    Else=12
    Foreach=13
    BooleanTrue=14
    BooleanFalse=15
    Array=16
    In=17
    Int=18
    Float=19
    Boolean=20
    String=21
    Return=22
    Class=23
    Null=24
    Val=25
    Var=26
    Self=27
    Constructor=28
    Destructor=29
    KEYWORD_New=30
    By=31
    ADD_OP=32
    SUB_OP=33
    MUL_OP=34
    DIV_OP=35
    MOD_OP=36
    NOT_OP=37
    AND_OP=38
    OR_OP=39
    EQUAL_OP=40
    DIFF_OP=41
    ASSIGN_OP=42
    GREATER_OP=43
    LESSER_OP=44
    GREATER_EQUAL_OP=45
    LESSER_EQUAL_OP=46
    STRING_COMP_OP=47
    STRING_CONCAT_OP=48
    MEMBER_ACCESS_OUT=49
    INTLIT=50
    FLOATLIT=51
    BOOLEANLIT=52
    STRINGLIT=53
    LP=54
    RP=55
    LSB=56
    RSB=57
    LB=58
    RB=59
    SEMI=60
    DOT=61
    COMA=62
    WS=63
    UNCLOSE_STRING=64
    ILLEGAL_ESCAPE=65
    ERROR_CHAR=66

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def many_class_decl(self):
            return self.getTypedRuleContext(D96Parser.Many_class_declContext,0)


        def EOF(self):
            return self.getToken(D96Parser.EOF, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = D96Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.many_class_decl()
            self.state = 131
            self.match(D96Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Many_class_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def class_decl(self):
            return self.getTypedRuleContext(D96Parser.Class_declContext,0)


        def class_decl_list(self):
            return self.getTypedRuleContext(D96Parser.Class_decl_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_many_class_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMany_class_decl" ):
                return visitor.visitMany_class_decl(self)
            else:
                return visitor.visitChildren(self)




    def many_class_decl(self):

        localctx = D96Parser.Many_class_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_many_class_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self.class_decl()
            self.state = 134
            self.class_decl_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_decl_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def class_decl(self):
            return self.getTypedRuleContext(D96Parser.Class_declContext,0)


        def class_decl_list(self):
            return self.getTypedRuleContext(D96Parser.Class_decl_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_class_decl_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_decl_list" ):
                return visitor.visitClass_decl_list(self)
            else:
                return visitor.visitChildren(self)




    def class_decl_list(self):

        localctx = D96Parser.Class_decl_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_class_decl_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.Class:
                self.state = 136
                self.class_decl()
                self.state = 137
                self.class_decl_list()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Class(self):
            return self.getToken(D96Parser.Class, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def member_lists(self):
            return self.getTypedRuleContext(D96Parser.Member_listsContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ID)
            else:
                return self.getToken(D96Parser.ID, i)

        def Program(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.Program)
            else:
                return self.getToken(D96Parser.Program, i)

        def getRuleIndex(self):
            return D96Parser.RULE_class_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_decl" ):
                return visitor.visitClass_decl(self)
            else:
                return visitor.visitChildren(self)




    def class_decl(self):

        localctx = D96Parser.Class_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_class_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.match(D96Parser.Class)
            self.state = 142
            _la = self._input.LA(1)
            if not(_la==D96Parser.ID or _la==D96Parser.Program):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 145
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.T__0:
                self.state = 143
                self.match(D96Parser.T__0)
                self.state = 144
                _la = self._input.LA(1)
                if not(_la==D96Parser.ID or _la==D96Parser.Program):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 147
            self.match(D96Parser.LB)
            self.state = 148
            self.member_lists()
            self.state = 149
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Member_listsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def member(self):
            return self.getTypedRuleContext(D96Parser.MemberContext,0)


        def member_list_tail(self):
            return self.getTypedRuleContext(D96Parser.Member_list_tailContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_member_lists

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMember_lists" ):
                return visitor.visitMember_lists(self)
            else:
                return visitor.visitChildren(self)




    def member_lists(self):

        localctx = D96Parser.Member_listsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_member_lists)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.T__1) | (1 << D96Parser.ID) | (1 << D96Parser.Main) | (1 << D96Parser.Val) | (1 << D96Parser.Var) | (1 << D96Parser.Constructor) | (1 << D96Parser.Destructor))) != 0):
                self.state = 151
                self.member()
                self.state = 152
                self.member_list_tail()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Member_list_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def member(self):
            return self.getTypedRuleContext(D96Parser.MemberContext,0)


        def member_list_tail(self):
            return self.getTypedRuleContext(D96Parser.Member_list_tailContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_member_list_tail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMember_list_tail" ):
                return visitor.visitMember_list_tail(self)
            else:
                return visitor.visitChildren(self)




    def member_list_tail(self):

        localctx = D96Parser.Member_list_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_member_list_tail)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.T__1) | (1 << D96Parser.ID) | (1 << D96Parser.Main) | (1 << D96Parser.Val) | (1 << D96Parser.Var) | (1 << D96Parser.Constructor) | (1 << D96Parser.Destructor))) != 0):
                self.state = 156
                self.member()
                self.state = 157
                self.member_list_tail()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attributes(self):
            return self.getTypedRuleContext(D96Parser.AttributesContext,0)


        def methods(self):
            return self.getTypedRuleContext(D96Parser.MethodsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_member

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMember" ):
                return visitor.visitMember(self)
            else:
                return visitor.visitChildren(self)




    def member(self):

        localctx = D96Parser.MemberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_member)
        try:
            self.state = 163
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.Val, D96Parser.Var]:
                self.enterOuterAlt(localctx, 1)
                self.state = 161
                self.attributes()
                pass
            elif token in [D96Parser.T__1, D96Parser.ID, D96Parser.Main, D96Parser.Constructor, D96Parser.Destructor]:
                self.enterOuterAlt(localctx, 2)
                self.state = 162
                self.methods()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttributesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attribute_list(self):
            return self.getTypedRuleContext(D96Parser.Attribute_listContext,0)


        def types(self):
            return self.getTypedRuleContext(D96Parser.TypesContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def Val(self):
            return self.getToken(D96Parser.Val, 0)

        def Var(self):
            return self.getToken(D96Parser.Var, 0)

        def ASSIGN_OP(self):
            return self.getToken(D96Parser.ASSIGN_OP, 0)

        def expr_list(self):
            return self.getTypedRuleContext(D96Parser.Expr_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_attributes

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttributes" ):
                return visitor.visitAttributes(self)
            else:
                return visitor.visitChildren(self)




    def attributes(self):

        localctx = D96Parser.AttributesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_attributes)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            _la = self._input.LA(1)
            if not(_la==D96Parser.Val or _la==D96Parser.Var):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 166
            self.attribute_list()
            self.state = 167
            self.match(D96Parser.T__0)
            self.state = 168
            self.types()
            self.state = 171
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ASSIGN_OP:
                self.state = 169
                self.match(D96Parser.ASSIGN_OP)
                self.state = 170
                self.expr_list()


            self.state = 173
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attribute_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attribute_name(self):
            return self.getTypedRuleContext(D96Parser.Attribute_nameContext,0)


        def attribute_list_tail(self):
            return self.getTypedRuleContext(D96Parser.Attribute_list_tailContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_attribute_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute_list" ):
                return visitor.visitAttribute_list(self)
            else:
                return visitor.visitChildren(self)




    def attribute_list(self):

        localctx = D96Parser.Attribute_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_attribute_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self.attribute_name()
            self.state = 176
            self.attribute_list_tail()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attribute_list_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attribute_name(self):
            return self.getTypedRuleContext(D96Parser.Attribute_nameContext,0)


        def attribute_list_tail(self):
            return self.getTypedRuleContext(D96Parser.Attribute_list_tailContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_attribute_list_tail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute_list_tail" ):
                return visitor.visitAttribute_list_tail(self)
            else:
                return visitor.visitChildren(self)




    def attribute_list_tail(self):

        localctx = D96Parser.Attribute_list_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_attribute_list_tail)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.T__1 or _la==D96Parser.ID:
                self.state = 178
                self.attribute_name()
                self.state = 179
                self.attribute_list_tail()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attribute_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_attribute_name

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute_name" ):
                return visitor.visitAttribute_name(self)
            else:
                return visitor.visitChildren(self)




    def attribute_name(self):

        localctx = D96Parser.Attribute_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_attribute_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.T__1:
                self.state = 183
                self.match(D96Parser.T__1)


            self.state = 186
            self.match(D96Parser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_Type(self):
            return self.getTypedRuleContext(D96Parser.Primitive_TypeContext,0)


        def array_Type(self):
            return self.getTypedRuleContext(D96Parser.Array_TypeContext,0)


        def class_type(self):
            return self.getTypedRuleContext(D96Parser.Class_typeContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_types

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypes" ):
                return visitor.visitTypes(self)
            else:
                return visitor.visitChildren(self)




    def types(self):

        localctx = D96Parser.TypesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_types)
        try:
            self.state = 191
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.Int, D96Parser.Float, D96Parser.Boolean, D96Parser.String]:
                self.enterOuterAlt(localctx, 1)
                self.state = 188
                self.primitive_Type()
                pass
            elif token in [D96Parser.Array]:
                self.enterOuterAlt(localctx, 2)
                self.state = 189
                self.array_Type()
                pass
            elif token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 190
                self.class_type()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primitive_TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Boolean(self):
            return self.getToken(D96Parser.Boolean, 0)

        def Int(self):
            return self.getToken(D96Parser.Int, 0)

        def Float(self):
            return self.getToken(D96Parser.Float, 0)

        def String(self):
            return self.getToken(D96Parser.String, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_primitive_Type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive_Type" ):
                return visitor.visitPrimitive_Type(self)
            else:
                return visitor.visitChildren(self)




    def primitive_Type(self):

        localctx = D96Parser.Primitive_TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_primitive_Type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.Int) | (1 << D96Parser.Float) | (1 << D96Parser.Boolean) | (1 << D96Parser.String))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Array(self):
            return self.getToken(D96Parser.Array, 0)

        def LSB(self):
            return self.getToken(D96Parser.LSB, 0)

        def RSB(self):
            return self.getToken(D96Parser.RSB, 0)

        def element_type(self):
            return self.getTypedRuleContext(D96Parser.Element_typeContext,0)


        def COMA(self):
            return self.getToken(D96Parser.COMA, 0)

        def array_size(self):
            return self.getTypedRuleContext(D96Parser.Array_sizeContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_array_Type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_Type" ):
                return visitor.visitArray_Type(self)
            else:
                return visitor.visitChildren(self)




    def array_Type(self):

        localctx = D96Parser.Array_TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_array_Type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            self.match(D96Parser.Array)
            self.state = 196
            self.match(D96Parser.LSB)
            self.state = 201
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.Array) | (1 << D96Parser.Int) | (1 << D96Parser.Float) | (1 << D96Parser.Boolean) | (1 << D96Parser.String))) != 0):
                self.state = 197
                self.element_type()
                self.state = 198
                self.match(D96Parser.COMA)
                self.state = 199
                self.array_size()


            self.state = 203
            self.match(D96Parser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Element_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_Type(self):
            return self.getTypedRuleContext(D96Parser.Primitive_TypeContext,0)


        def array_Type(self):
            return self.getTypedRuleContext(D96Parser.Array_TypeContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_element_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElement_type" ):
                return visitor.visitElement_type(self)
            else:
                return visitor.visitChildren(self)




    def element_type(self):

        localctx = D96Parser.Element_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_element_type)
        try:
            self.state = 207
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.Int, D96Parser.Float, D96Parser.Boolean, D96Parser.String]:
                self.enterOuterAlt(localctx, 1)
                self.state = 205
                self.primitive_Type()
                pass
            elif token in [D96Parser.Array]:
                self.enterOuterAlt(localctx, 2)
                self.state = 206
                self.array_Type()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_sizeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(D96Parser.INTLIT, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_array_size

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_size" ):
                return visitor.visitArray_size(self)
            else:
                return visitor.visitChildren(self)




    def array_size(self):

        localctx = D96Parser.Array_sizeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_array_size)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self.match(D96Parser.INTLIT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_class_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_type" ):
                return visitor.visitClass_type(self)
            else:
                return visitor.visitChildren(self)




    def class_type(self):

        localctx = D96Parser.Class_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_class_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            self.match(D96Parser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(D96Parser.ParamContext,0)


        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def Main(self):
            return self.getToken(D96Parser.Main, 0)

        def Constructor(self):
            return self.getToken(D96Parser.Constructor, 0)

        def Destructor(self):
            return self.getToken(D96Parser.Destructor, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_methods

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethods" ):
                return visitor.visitMethods(self)
            else:
                return visitor.visitChildren(self)




    def methods(self):

        localctx = D96Parser.MethodsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_methods)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.T__1:
                self.state = 213
                self.match(D96Parser.T__1)


            self.state = 216
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.ID) | (1 << D96Parser.Main) | (1 << D96Parser.Constructor) | (1 << D96Parser.Destructor))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 217
            self.param()
            self.state = 218
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def paramlist(self):
            return self.getTypedRuleContext(D96Parser.ParamlistContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = D96Parser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            self.match(D96Parser.LP)
            self.state = 221
            self.paramlist()
            self.state = 222
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param_decl(self):
            return self.getTypedRuleContext(D96Parser.Param_declContext,0)


        def paramlist_tail(self):
            return self.getTypedRuleContext(D96Parser.Paramlist_tailContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_paramlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamlist" ):
                return visitor.visitParamlist(self)
            else:
                return visitor.visitChildren(self)




    def paramlist(self):

        localctx = D96Parser.ParamlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_paramlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ID:
                self.state = 224
                self.param_decl()
                self.state = 225
                self.paramlist_tail()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Paramlist_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def param_decl(self):
            return self.getTypedRuleContext(D96Parser.Param_declContext,0)


        def paramlist_tail(self):
            return self.getTypedRuleContext(D96Parser.Paramlist_tailContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_paramlist_tail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamlist_tail" ):
                return visitor.visitParamlist_tail(self)
            else:
                return visitor.visitChildren(self)




    def paramlist_tail(self):

        localctx = D96Parser.Paramlist_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_paramlist_tail)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.SEMI:
                self.state = 229
                self.match(D96Parser.SEMI)
                self.state = 230
                self.param_decl()
                self.state = 231
                self.paramlist_tail()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idlist(self):
            return self.getTypedRuleContext(D96Parser.IdlistContext,0)


        def types(self):
            return self.getTypedRuleContext(D96Parser.TypesContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_param_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_decl" ):
                return visitor.visitParam_decl(self)
            else:
                return visitor.visitChildren(self)




    def param_decl(self):

        localctx = D96Parser.Param_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_param_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235
            self.idlist()
            self.state = 236
            self.match(D96Parser.T__0)
            self.state = 237
            self.types()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def idlist_tail(self):
            return self.getTypedRuleContext(D96Parser.Idlist_tailContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_idlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdlist" ):
                return visitor.visitIdlist(self)
            else:
                return visitor.visitChildren(self)




    def idlist(self):

        localctx = D96Parser.IdlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_idlist)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self.match(D96Parser.ID)
            self.state = 240
            self.idlist_tail()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Idlist_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMA(self):
            return self.getToken(D96Parser.COMA, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def idlist_tail(self):
            return self.getTypedRuleContext(D96Parser.Idlist_tailContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_idlist_tail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdlist_tail" ):
                return visitor.visitIdlist_tail(self)
            else:
                return visitor.visitChildren(self)




    def idlist_tail(self):

        localctx = D96Parser.Idlist_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_idlist_tail)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.COMA:
                self.state = 242
                self.match(D96Parser.COMA)
                self.state = 243
                self.match(D96Parser.ID)
                self.state = 244
                self.idlist_tail()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def expr_list_tail(self):
            return self.getTypedRuleContext(D96Parser.Expr_list_tailContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_list" ):
                return visitor.visitExpr_list(self)
            else:
                return visitor.visitChildren(self)




    def expr_list(self):

        localctx = D96Parser.Expr_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_expr_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 250
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.ID) | (1 << D96Parser.KEYWORD_New) | (1 << D96Parser.SUB_OP) | (1 << D96Parser.NOT_OP) | (1 << D96Parser.INTLIT) | (1 << D96Parser.FLOATLIT) | (1 << D96Parser.BOOLEANLIT) | (1 << D96Parser.STRINGLIT))) != 0):
                self.state = 247
                self.expr()
                self.state = 248
                self.expr_list_tail()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_list_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMA(self):
            return self.getToken(D96Parser.COMA, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def expr_list_tail(self):
            return self.getTypedRuleContext(D96Parser.Expr_list_tailContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr_list_tail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_list_tail" ):
                return visitor.visitExpr_list_tail(self)
            else:
                return visitor.visitChildren(self)




    def expr_list_tail(self):

        localctx = D96Parser.Expr_list_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_expr_list_tail)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 256
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.COMA:
                self.state = 252
                self.match(D96Parser.COMA)
                self.state = 253
                self.expr()
                self.state = 254
                self.expr_list_tail()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def class_expr(self):
            return self.getTypedRuleContext(D96Parser.Class_exprContext,0)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ID)
            else:
                return self.getToken(D96Parser.ID, i)

        def MEMBER_ACCESS_OUT(self):
            return self.getToken(D96Parser.MEMBER_ACCESS_OUT, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def expr_list(self):
            return self.getTypedRuleContext(D96Parser.Expr_listContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def index_expr(self):
            return self.getTypedRuleContext(D96Parser.Index_exprContext,0)


        def math_expr(self):
            return self.getTypedRuleContext(D96Parser.Math_exprContext,0)


        def relational_expr(self):
            return self.getTypedRuleContext(D96Parser.Relational_exprContext,0)


        def string_expr(self):
            return self.getTypedRuleContext(D96Parser.String_exprContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = D96Parser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.state = 288
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 258
                self.class_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 259
                self.match(D96Parser.ID)
                self.state = 260
                self.match(D96Parser.MEMBER_ACCESS_OUT)
                self.state = 262
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==D96Parser.T__1:
                    self.state = 261
                    self.match(D96Parser.T__1)


                self.state = 264
                self.match(D96Parser.ID)
                self.state = 269
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==D96Parser.LP:
                    self.state = 265
                    self.match(D96Parser.LP)
                    self.state = 266
                    self.expr_list()
                    self.state = 267
                    self.match(D96Parser.RP)


                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 271
                self.match(D96Parser.ID)
                self.state = 272
                self.match(D96Parser.DOT)
                self.state = 274
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==D96Parser.T__1:
                    self.state = 273
                    self.match(D96Parser.T__1)


                self.state = 276
                self.match(D96Parser.ID)
                self.state = 281
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==D96Parser.LP:
                    self.state = 277
                    self.match(D96Parser.LP)
                    self.state = 278
                    self.expr_list()
                    self.state = 279
                    self.match(D96Parser.RP)


                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 283
                self.index_expr()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 284
                self.math_expr(0)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 285
                self.relational_expr()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 286
                self.string_expr(0)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 287
                self.match(D96Parser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KEYWORD_New(self):
            return self.getToken(D96Parser.KEYWORD_New, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def expr_list(self):
            return self.getTypedRuleContext(D96Parser.Expr_listContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_class_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_expr" ):
                return visitor.visitClass_expr(self)
            else:
                return visitor.visitChildren(self)




    def class_expr(self):

        localctx = D96Parser.Class_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_class_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 290
            self.match(D96Parser.KEYWORD_New)
            self.state = 291
            self.match(D96Parser.ID)
            self.state = 292
            self.match(D96Parser.LP)
            self.state = 293
            self.expr_list()
            self.state = 294
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lower_expr(self):
            return self.getTypedRuleContext(D96Parser.Lower_exprContext,0)


        def index_operators(self):
            return self.getTypedRuleContext(D96Parser.Index_operatorsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_index_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_expr" ):
                return visitor.visitIndex_expr(self)
            else:
                return visitor.visitChildren(self)




    def index_expr(self):

        localctx = D96Parser.Index_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_index_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 296
            self.lower_expr()
            self.state = 297
            self.index_operators()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_operatorsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def lower_expr(self):
            return self.getTypedRuleContext(D96Parser.Lower_exprContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def index_operators(self):
            return self.getTypedRuleContext(D96Parser.Index_operatorsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_index_operators

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_operators" ):
                return visitor.visitIndex_operators(self)
            else:
                return visitor.visitChildren(self)




    def index_operators(self):

        localctx = D96Parser.Index_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_index_operators)
        try:
            self.state = 308
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 299
                self.match(D96Parser.LB)
                self.state = 300
                self.lower_expr()
                self.state = 301
                self.match(D96Parser.RB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 303
                self.match(D96Parser.LB)
                self.state = 304
                self.lower_expr()
                self.state = 305
                self.match(D96Parser.RB)
                self.state = 306
                self.index_operators()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Lower_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def math_expr(self):
            return self.getTypedRuleContext(D96Parser.Math_exprContext,0)


        def relational_expr(self):
            return self.getTypedRuleContext(D96Parser.Relational_exprContext,0)


        def string_expr(self):
            return self.getTypedRuleContext(D96Parser.String_exprContext,0)


        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_lower_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLower_expr" ):
                return visitor.visitLower_expr(self)
            else:
                return visitor.visitChildren(self)




    def lower_expr(self):

        localctx = D96Parser.Lower_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_lower_expr)
        try:
            self.state = 314
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 310
                self.math_expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 311
                self.relational_expr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 312
                self.string_expr(0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 313
                self.match(D96Parser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Math_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUB_OP(self):
            return self.getToken(D96Parser.SUB_OP, 0)

        def math_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Math_exprContext)
            else:
                return self.getTypedRuleContext(D96Parser.Math_exprContext,i)


        def logical_not_expr(self):
            return self.getTypedRuleContext(D96Parser.Logical_not_exprContext,0)


        def mod_expr(self):
            return self.getTypedRuleContext(D96Parser.Mod_exprContext,0)


        def logical_expr(self):
            return self.getTypedRuleContext(D96Parser.Logical_exprContext,0)


        def INTLIT(self):
            return self.getToken(D96Parser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(D96Parser.FLOATLIT, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def MUL_OP(self):
            return self.getToken(D96Parser.MUL_OP, 0)

        def DIV_OP(self):
            return self.getToken(D96Parser.DIV_OP, 0)

        def ADD_OP(self):
            return self.getToken(D96Parser.ADD_OP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_math_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMath_expr" ):
                return visitor.visitMath_expr(self)
            else:
                return visitor.visitChildren(self)



    def math_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Math_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 62
        self.enterRecursionRule(localctx, 62, self.RULE_math_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 325
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.state = 317
                self.match(D96Parser.SUB_OP)
                self.state = 318
                self.math_expr(11)
                pass

            elif la_ == 2:
                self.state = 319
                self.logical_not_expr()
                pass

            elif la_ == 3:
                self.state = 320
                self.mod_expr(0)
                pass

            elif la_ == 4:
                self.state = 321
                self.logical_expr(0)
                pass

            elif la_ == 5:
                self.state = 322
                self.match(D96Parser.INTLIT)
                pass

            elif la_ == 6:
                self.state = 323
                self.match(D96Parser.FLOATLIT)
                pass

            elif la_ == 7:
                self.state = 324
                self.match(D96Parser.ID)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 341
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 339
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.Math_exprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_math_expr)
                        self.state = 327
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 328
                        self.match(D96Parser.MUL_OP)
                        self.state = 329
                        self.math_expr(10)
                        pass

                    elif la_ == 2:
                        localctx = D96Parser.Math_exprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_math_expr)
                        self.state = 330
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 331
                        self.match(D96Parser.DIV_OP)
                        self.state = 332
                        self.math_expr(9)
                        pass

                    elif la_ == 3:
                        localctx = D96Parser.Math_exprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_math_expr)
                        self.state = 333
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 334
                        self.match(D96Parser.ADD_OP)
                        self.state = 335
                        self.math_expr(7)
                        pass

                    elif la_ == 4:
                        localctx = D96Parser.Math_exprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_math_expr)
                        self.state = 336
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 337
                        self.match(D96Parser.SUB_OP)
                        self.state = 338
                        self.math_expr(6)
                        pass

             
                self.state = 343
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Mod_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(D96Parser.INTLIT, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def mod_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Mod_exprContext)
            else:
                return self.getTypedRuleContext(D96Parser.Mod_exprContext,i)


        def MOD_OP(self):
            return self.getToken(D96Parser.MOD_OP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_mod_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMod_expr" ):
                return visitor.visitMod_expr(self)
            else:
                return visitor.visitChildren(self)



    def mod_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Mod_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 64
        self.enterRecursionRule(localctx, 64, self.RULE_mod_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 347
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INTLIT]:
                self.state = 345
                self.match(D96Parser.INTLIT)
                pass
            elif token in [D96Parser.ID]:
                self.state = 346
                self.match(D96Parser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 354
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Mod_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_mod_expr)
                    self.state = 349
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 350
                    self.match(D96Parser.MOD_OP)
                    self.state = 351
                    self.mod_expr(4) 
                self.state = 356
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Logical_not_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT_OP(self):
            return self.getToken(D96Parser.NOT_OP, 0)

        def logical_not_expr(self):
            return self.getTypedRuleContext(D96Parser.Logical_not_exprContext,0)


        def BOOLEANLIT(self):
            return self.getToken(D96Parser.BOOLEANLIT, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_logical_not_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogical_not_expr" ):
                return visitor.visitLogical_not_expr(self)
            else:
                return visitor.visitChildren(self)




    def logical_not_expr(self):

        localctx = D96Parser.Logical_not_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_logical_not_expr)
        try:
            self.state = 361
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NOT_OP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 357
                self.match(D96Parser.NOT_OP)
                self.state = 358
                self.logical_not_expr()
                pass
            elif token in [D96Parser.BOOLEANLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 359
                self.match(D96Parser.BOOLEANLIT)
                pass
            elif token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 360
                self.match(D96Parser.ID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Logical_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOLEANLIT(self):
            return self.getToken(D96Parser.BOOLEANLIT, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def logical_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Logical_exprContext)
            else:
                return self.getTypedRuleContext(D96Parser.Logical_exprContext,i)


        def AND_OP(self):
            return self.getToken(D96Parser.AND_OP, 0)

        def OR_OP(self):
            return self.getToken(D96Parser.OR_OP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_logical_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogical_expr" ):
                return visitor.visitLogical_expr(self)
            else:
                return visitor.visitChildren(self)



    def logical_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Logical_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 68
        self.enterRecursionRule(localctx, 68, self.RULE_logical_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 366
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.BOOLEANLIT]:
                self.state = 364
                self.match(D96Parser.BOOLEANLIT)
                pass
            elif token in [D96Parser.ID]:
                self.state = 365
                self.match(D96Parser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 376
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 374
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.Logical_exprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_logical_expr)
                        self.state = 368
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 369
                        self.match(D96Parser.AND_OP)
                        self.state = 370
                        self.logical_expr(5)
                        pass

                    elif la_ == 2:
                        localctx = D96Parser.Logical_exprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_logical_expr)
                        self.state = 371
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 372
                        self.match(D96Parser.OR_OP)
                        self.state = 373
                        self.logical_expr(4)
                        pass

             
                self.state = 378
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Relational_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relational_expr_1(self):
            return self.getTypedRuleContext(D96Parser.Relational_expr_1Context,0)


        def relational_expr_2(self):
            return self.getTypedRuleContext(D96Parser.Relational_expr_2Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_relational_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelational_expr" ):
                return visitor.visitRelational_expr(self)
            else:
                return visitor.visitChildren(self)




    def relational_expr(self):

        localctx = D96Parser.Relational_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_relational_expr)
        try:
            self.state = 381
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 379
                self.relational_expr_1(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 380
                self.relational_expr_2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Relational_expr_1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(D96Parser.INTLIT, 0)

        def BOOLEANLIT(self):
            return self.getToken(D96Parser.BOOLEANLIT, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def relational_expr_1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Relational_expr_1Context)
            else:
                return self.getTypedRuleContext(D96Parser.Relational_expr_1Context,i)


        def EQUAL_OP(self):
            return self.getToken(D96Parser.EQUAL_OP, 0)

        def DIFF_OP(self):
            return self.getToken(D96Parser.DIFF_OP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_relational_expr_1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelational_expr_1" ):
                return visitor.visitRelational_expr_1(self)
            else:
                return visitor.visitChildren(self)



    def relational_expr_1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Relational_expr_1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 72
        self.enterRecursionRule(localctx, 72, self.RULE_relational_expr_1, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 387
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INTLIT]:
                self.state = 384
                self.match(D96Parser.INTLIT)
                pass
            elif token in [D96Parser.BOOLEANLIT]:
                self.state = 385
                self.match(D96Parser.BOOLEANLIT)
                pass
            elif token in [D96Parser.ID]:
                self.state = 386
                self.match(D96Parser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 394
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Relational_expr_1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_relational_expr_1)
                    self.state = 389
                    if not self.precpred(self._ctx, 4):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                    self.state = 390
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.EQUAL_OP or _la==D96Parser.DIFF_OP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 391
                    self.relational_expr_1(5) 
                self.state = 396
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Relational_expr_2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(D96Parser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(D96Parser.FLOATLIT, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def relational_expr_2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Relational_expr_2Context)
            else:
                return self.getTypedRuleContext(D96Parser.Relational_expr_2Context,i)


        def GREATER_OP(self):
            return self.getToken(D96Parser.GREATER_OP, 0)

        def LESSER_OP(self):
            return self.getToken(D96Parser.LESSER_OP, 0)

        def GREATER_EQUAL_OP(self):
            return self.getToken(D96Parser.GREATER_EQUAL_OP, 0)

        def LESSER_EQUAL_OP(self):
            return self.getToken(D96Parser.LESSER_EQUAL_OP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_relational_expr_2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelational_expr_2" ):
                return visitor.visitRelational_expr_2(self)
            else:
                return visitor.visitChildren(self)



    def relational_expr_2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Relational_expr_2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 74
        self.enterRecursionRule(localctx, 74, self.RULE_relational_expr_2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 401
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INTLIT]:
                self.state = 398
                self.match(D96Parser.INTLIT)
                pass
            elif token in [D96Parser.FLOATLIT]:
                self.state = 399
                self.match(D96Parser.FLOATLIT)
                pass
            elif token in [D96Parser.ID]:
                self.state = 400
                self.match(D96Parser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 408
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,37,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Relational_expr_2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_relational_expr_2)
                    self.state = 403
                    if not self.precpred(self._ctx, 4):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                    self.state = 404
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.GREATER_OP) | (1 << D96Parser.LESSER_OP) | (1 << D96Parser.GREATER_EQUAL_OP) | (1 << D96Parser.LESSER_EQUAL_OP))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 405
                    self.relational_expr_2(5) 
                self.state = 410
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,37,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class String_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRINGLIT(self):
            return self.getToken(D96Parser.STRINGLIT, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def string_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.String_exprContext)
            else:
                return self.getTypedRuleContext(D96Parser.String_exprContext,i)


        def STRING_COMP_OP(self):
            return self.getToken(D96Parser.STRING_COMP_OP, 0)

        def STRING_CONCAT_OP(self):
            return self.getToken(D96Parser.STRING_CONCAT_OP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_string_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString_expr" ):
                return visitor.visitString_expr(self)
            else:
                return visitor.visitChildren(self)



    def string_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.String_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 76
        self.enterRecursionRule(localctx, 76, self.RULE_string_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 414
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.STRINGLIT]:
                self.state = 412
                self.match(D96Parser.STRINGLIT)
                pass
            elif token in [D96Parser.ID]:
                self.state = 413
                self.match(D96Parser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 421
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,39,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.String_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_string_expr)
                    self.state = 416
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 417
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.STRING_COMP_OP or _la==D96Parser.STRING_CONCAT_OP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 418
                    self.string_expr(4) 
                self.state = 423
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,39,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Block_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def block_stmt_list(self):
            return self.getTypedRuleContext(D96Parser.Block_stmt_listContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_block_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_stmt" ):
                return visitor.visitBlock_stmt(self)
            else:
                return visitor.visitChildren(self)




    def block_stmt(self):

        localctx = D96Parser.Block_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_block_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 424
            self.match(D96Parser.LB)
            self.state = 425
            self.block_stmt_list()
            self.state = 426
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_stmt_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(D96Parser.StmtContext,0)


        def block_stmt_list_tail(self):
            return self.getTypedRuleContext(D96Parser.Block_stmt_list_tailContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_block_stmt_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_stmt_list" ):
                return visitor.visitBlock_stmt_list(self)
            else:
                return visitor.visitChildren(self)




    def block_stmt_list(self):

        localctx = D96Parser.Block_stmt_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_block_stmt_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 431
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.ID) | (1 << D96Parser.Break) | (1 << D96Parser.Continue) | (1 << D96Parser.If) | (1 << D96Parser.Foreach) | (1 << D96Parser.Return) | (1 << D96Parser.Val) | (1 << D96Parser.Var) | (1 << D96Parser.SUB_OP) | (1 << D96Parser.NOT_OP) | (1 << D96Parser.INTLIT) | (1 << D96Parser.FLOATLIT) | (1 << D96Parser.BOOLEANLIT) | (1 << D96Parser.STRINGLIT) | (1 << D96Parser.LB))) != 0):
                self.state = 428
                self.stmt()
                self.state = 429
                self.block_stmt_list_tail()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_stmt_list_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(D96Parser.StmtContext,0)


        def block_stmt_list_tail(self):
            return self.getTypedRuleContext(D96Parser.Block_stmt_list_tailContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_block_stmt_list_tail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_stmt_list_tail" ):
                return visitor.visitBlock_stmt_list_tail(self)
            else:
                return visitor.visitChildren(self)




    def block_stmt_list_tail(self):

        localctx = D96Parser.Block_stmt_list_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_block_stmt_list_tail)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 436
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.ID) | (1 << D96Parser.Break) | (1 << D96Parser.Continue) | (1 << D96Parser.If) | (1 << D96Parser.Foreach) | (1 << D96Parser.Return) | (1 << D96Parser.Val) | (1 << D96Parser.Var) | (1 << D96Parser.SUB_OP) | (1 << D96Parser.NOT_OP) | (1 << D96Parser.INTLIT) | (1 << D96Parser.FLOATLIT) | (1 << D96Parser.BOOLEANLIT) | (1 << D96Parser.STRINGLIT) | (1 << D96Parser.LB))) != 0):
                self.state = 433
                self.stmt()
                self.state = 434
                self.block_stmt_list_tail()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt_list(self):
            return self.getTypedRuleContext(D96Parser.Stmt_listContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = D96Parser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 438
            self.stmt_list()
            self.state = 439
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_cons_decl(self):
            return self.getTypedRuleContext(D96Parser.Var_cons_declContext,0)


        def asm(self):
            return self.getTypedRuleContext(D96Parser.AsmContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(D96Parser.If_stmtContext,0)


        def loop_stmt(self):
            return self.getTypedRuleContext(D96Parser.Loop_stmtContext,0)


        def Break(self):
            return self.getToken(D96Parser.Break, 0)

        def Continue(self):
            return self.getToken(D96Parser.Continue, 0)

        def return_stmt(self):
            return self.getTypedRuleContext(D96Parser.Return_stmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_stmt_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_list" ):
                return visitor.visitStmt_list(self)
            else:
                return visitor.visitChildren(self)




    def stmt_list(self):

        localctx = D96Parser.Stmt_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_stmt_list)
        try:
            self.state = 448
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.Val, D96Parser.Var]:
                self.enterOuterAlt(localctx, 1)
                self.state = 441
                self.var_cons_decl()
                pass
            elif token in [D96Parser.ID, D96Parser.SUB_OP, D96Parser.NOT_OP, D96Parser.INTLIT, D96Parser.FLOATLIT, D96Parser.BOOLEANLIT, D96Parser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 442
                self.asm()
                pass
            elif token in [D96Parser.If, D96Parser.LB]:
                self.enterOuterAlt(localctx, 3)
                self.state = 443
                self.if_stmt()
                pass
            elif token in [D96Parser.Foreach]:
                self.enterOuterAlt(localctx, 4)
                self.state = 444
                self.loop_stmt()
                pass
            elif token in [D96Parser.Break]:
                self.enterOuterAlt(localctx, 5)
                self.state = 445
                self.match(D96Parser.Break)
                pass
            elif token in [D96Parser.Continue]:
                self.enterOuterAlt(localctx, 6)
                self.state = 446
                self.match(D96Parser.Continue)
                pass
            elif token in [D96Parser.Return]:
                self.enterOuterAlt(localctx, 7)
                self.state = 447
                self.return_stmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_cons_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_cons_list(self):
            return self.getTypedRuleContext(D96Parser.Var_cons_listContext,0)


        def types(self):
            return self.getTypedRuleContext(D96Parser.TypesContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def Val(self):
            return self.getToken(D96Parser.Val, 0)

        def Var(self):
            return self.getToken(D96Parser.Var, 0)

        def ASSIGN_OP(self):
            return self.getToken(D96Parser.ASSIGN_OP, 0)

        def expr_list(self):
            return self.getTypedRuleContext(D96Parser.Expr_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_var_cons_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_cons_decl" ):
                return visitor.visitVar_cons_decl(self)
            else:
                return visitor.visitChildren(self)




    def var_cons_decl(self):

        localctx = D96Parser.Var_cons_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_var_cons_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 450
            _la = self._input.LA(1)
            if not(_la==D96Parser.Val or _la==D96Parser.Var):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 451
            self.var_cons_list()
            self.state = 452
            self.match(D96Parser.T__0)
            self.state = 453
            self.types()
            self.state = 456
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ASSIGN_OP:
                self.state = 454
                self.match(D96Parser.ASSIGN_OP)
                self.state = 455
                self.expr_list()


            self.state = 458
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_cons_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_cons_name(self):
            return self.getTypedRuleContext(D96Parser.Var_cons_nameContext,0)


        def var_cons_list_tail(self):
            return self.getTypedRuleContext(D96Parser.Var_cons_list_tailContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_var_cons_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_cons_list" ):
                return visitor.visitVar_cons_list(self)
            else:
                return visitor.visitChildren(self)




    def var_cons_list(self):

        localctx = D96Parser.Var_cons_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_var_cons_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 460
            self.var_cons_name()
            self.state = 461
            self.var_cons_list_tail()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_cons_list_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_cons_name(self):
            return self.getTypedRuleContext(D96Parser.Var_cons_nameContext,0)


        def var_cons_list_tail(self):
            return self.getTypedRuleContext(D96Parser.Var_cons_list_tailContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_var_cons_list_tail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_cons_list_tail" ):
                return visitor.visitVar_cons_list_tail(self)
            else:
                return visitor.visitChildren(self)




    def var_cons_list_tail(self):

        localctx = D96Parser.Var_cons_list_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_var_cons_list_tail)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 466
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ID:
                self.state = 463
                self.var_cons_name()
                self.state = 464
                self.var_cons_list_tail()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_cons_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_var_cons_name

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_cons_name" ):
                return visitor.visitVar_cons_name(self)
            else:
                return visitor.visitChildren(self)




    def var_cons_name(self):

        localctx = D96Parser.Var_cons_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_var_cons_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 468
            self.match(D96Parser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN_OP(self):
            return self.getToken(D96Parser.ASSIGN_OP, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def index_expr(self):
            return self.getTypedRuleContext(D96Parser.Index_exprContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_asm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsm" ):
                return visitor.visitAsm(self)
            else:
                return visitor.visitChildren(self)




    def asm(self):

        localctx = D96Parser.AsmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_asm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 472
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.state = 470
                self.match(D96Parser.ID)
                pass

            elif la_ == 2:
                self.state = 471
                self.index_expr()
                pass


            self.state = 474
            self.match(D96Parser.ASSIGN_OP)
            self.state = 475
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def matchStmt(self):
            return self.getTypedRuleContext(D96Parser.MatchStmtContext,0)


        def unmatchStmt(self):
            return self.getTypedRuleContext(D96Parser.UnmatchStmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_if_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = D96Parser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_if_stmt)
        try:
            self.state = 479
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 477
                self.matchStmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 478
                self.unmatchStmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MatchStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def If(self):
            return self.getToken(D96Parser.If, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def matchStmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.MatchStmtContext)
            else:
                return self.getTypedRuleContext(D96Parser.MatchStmtContext,i)


        def elseif_list(self):
            return self.getTypedRuleContext(D96Parser.Elseif_listContext,0)


        def Else(self):
            return self.getToken(D96Parser.Else, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_matchStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatchStmt" ):
                return visitor.visitMatchStmt(self)
            else:
                return visitor.visitChildren(self)




    def matchStmt(self):

        localctx = D96Parser.MatchStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_matchStmt)
        try:
            self.state = 490
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.If]:
                self.enterOuterAlt(localctx, 1)
                self.state = 481
                self.match(D96Parser.If)
                self.state = 482
                self.expr()
                self.state = 483
                self.matchStmt()

                self.state = 484
                self.elseif_list()
                self.state = 487
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
                if la_ == 1:
                    self.state = 485
                    self.match(D96Parser.Else)
                    self.state = 486
                    self.matchStmt()


                pass
            elif token in [D96Parser.LB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 489
                self.block_stmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnmatchStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def If(self):
            return self.getToken(D96Parser.If, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(D96Parser.If_stmtContext,0)


        def matchStmt(self):
            return self.getTypedRuleContext(D96Parser.MatchStmtContext,0)


        def elseif_list(self):
            return self.getTypedRuleContext(D96Parser.Elseif_listContext,0)


        def Else(self):
            return self.getToken(D96Parser.Else, 0)

        def unmatchStmt(self):
            return self.getTypedRuleContext(D96Parser.UnmatchStmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_unmatchStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnmatchStmt" ):
                return visitor.visitUnmatchStmt(self)
            else:
                return visitor.visitChildren(self)




    def unmatchStmt(self):

        localctx = D96Parser.UnmatchStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_unmatchStmt)
        try:
            self.state = 504
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 492
                self.match(D96Parser.If)
                self.state = 493
                self.expr()
                self.state = 494
                self.if_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 496
                self.match(D96Parser.If)
                self.state = 497
                self.expr()
                self.state = 498
                self.matchStmt()

                self.state = 499
                self.elseif_list()
                self.state = 502
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
                if la_ == 1:
                    self.state = 500
                    self.match(D96Parser.Else)
                    self.state = 501
                    self.unmatchStmt()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elseif_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elseif_stmt(self):
            return self.getTypedRuleContext(D96Parser.Elseif_stmtContext,0)


        def elseif_list_tail(self):
            return self.getTypedRuleContext(D96Parser.Elseif_list_tailContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_elseif_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseif_list" ):
                return visitor.visitElseif_list(self)
            else:
                return visitor.visitChildren(self)




    def elseif_list(self):

        localctx = D96Parser.Elseif_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_elseif_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 509
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
            if la_ == 1:
                self.state = 506
                self.elseif_stmt()
                self.state = 507
                self.elseif_list_tail()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elseif_list_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elseif_stmt(self):
            return self.getTypedRuleContext(D96Parser.Elseif_stmtContext,0)


        def elseif_list_tail(self):
            return self.getTypedRuleContext(D96Parser.Elseif_list_tailContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_elseif_list_tail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseif_list_tail" ):
                return visitor.visitElseif_list_tail(self)
            else:
                return visitor.visitChildren(self)




    def elseif_list_tail(self):

        localctx = D96Parser.Elseif_list_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_elseif_list_tail)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 514
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
            if la_ == 1:
                self.state = 511
                self.elseif_stmt()
                self.state = 512
                self.elseif_list_tail()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elseif_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Elseif(self):
            return self.getToken(D96Parser.Elseif, 0)

        def if_stmt(self):
            return self.getTypedRuleContext(D96Parser.If_stmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_elseif_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseif_stmt" ):
                return visitor.visitElseif_stmt(self)
            else:
                return visitor.visitChildren(self)




    def elseif_stmt(self):

        localctx = D96Parser.Elseif_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_elseif_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 516
            self.match(D96Parser.Elseif)
            self.state = 517
            self.if_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Loop_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Foreach(self):
            return self.getToken(D96Parser.Foreach, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def In(self):
            return self.getToken(D96Parser.In, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExprContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExprContext,i)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def By(self):
            return self.getToken(D96Parser.By, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_loop_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoop_stmt" ):
                return visitor.visitLoop_stmt(self)
            else:
                return visitor.visitChildren(self)




    def loop_stmt(self):

        localctx = D96Parser.Loop_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_loop_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 519
            self.match(D96Parser.Foreach)
            self.state = 520
            self.match(D96Parser.LP)
            self.state = 521
            self.match(D96Parser.ID)
            self.state = 522
            self.match(D96Parser.In)
            self.state = 523
            self.expr()
            self.state = 524
            self.match(D96Parser.T__2)
            self.state = 525
            self.expr()
            self.state = 528
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.By:
                self.state = 526
                self.match(D96Parser.By)
                self.state = 527
                self.expr()


            self.state = 530
            self.match(D96Parser.RP)
            self.state = 531
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def expr_list(self):
            return self.getTypedRuleContext(D96Parser.Expr_listContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall" ):
                return visitor.visitCall(self)
            else:
                return visitor.visitChildren(self)




    def call(self):

        localctx = D96Parser.CallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 533
            self.match(D96Parser.ID)
            self.state = 534
            self.match(D96Parser.LB)
            self.state = 535
            self.expr_list()
            self.state = 536
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Return(self):
            return self.getToken(D96Parser.Return, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_return_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = D96Parser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 538
            self.match(D96Parser.Return)
            self.state = 540
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.ID) | (1 << D96Parser.KEYWORD_New) | (1 << D96Parser.SUB_OP) | (1 << D96Parser.NOT_OP) | (1 << D96Parser.INTLIT) | (1 << D96Parser.FLOATLIT) | (1 << D96Parser.BOOLEANLIT) | (1 << D96Parser.STRINGLIT))) != 0):
                self.state = 539
                self.expr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Multi_ArrayLITContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Array(self):
            return self.getToken(D96Parser.Array, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def array_list(self):
            return self.getTypedRuleContext(D96Parser.Array_listContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_multi_ArrayLIT

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulti_ArrayLIT" ):
                return visitor.visitMulti_ArrayLIT(self)
            else:
                return visitor.visitChildren(self)




    def multi_ArrayLIT(self):

        localctx = D96Parser.Multi_ArrayLITContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_multi_ArrayLIT)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 542
            self.match(D96Parser.Array)
            self.state = 543
            self.match(D96Parser.LP)
            self.state = 544
            self.array_list()
            self.state = 545
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def index_ArrayLIT(self):
            return self.getTypedRuleContext(D96Parser.Index_ArrayLITContext,0)


        def array_list_tail(self):
            return self.getTypedRuleContext(D96Parser.Array_list_tailContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_array_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_list" ):
                return visitor.visitArray_list(self)
            else:
                return visitor.visitChildren(self)




    def array_list(self):

        localctx = D96Parser.Array_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_array_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 550
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.Array:
                self.state = 547
                self.index_ArrayLIT()
                self.state = 548
                self.array_list_tail()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_list_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMA(self):
            return self.getToken(D96Parser.COMA, 0)

        def index_ArrayLIT(self):
            return self.getTypedRuleContext(D96Parser.Index_ArrayLITContext,0)


        def array_list_tail(self):
            return self.getTypedRuleContext(D96Parser.Array_list_tailContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_array_list_tail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_list_tail" ):
                return visitor.visitArray_list_tail(self)
            else:
                return visitor.visitChildren(self)




    def array_list_tail(self):

        localctx = D96Parser.Array_list_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_array_list_tail)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 556
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.COMA:
                self.state = 552
                self.match(D96Parser.COMA)
                self.state = 553
                self.index_ArrayLIT()
                self.state = 554
                self.array_list_tail()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_ArrayLITContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Array(self):
            return self.getToken(D96Parser.Array, 0)

        def elements(self):
            return self.getTypedRuleContext(D96Parser.ElementsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_index_ArrayLIT

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_ArrayLIT" ):
                return visitor.visitIndex_ArrayLIT(self)
            else:
                return visitor.visitChildren(self)




    def index_ArrayLIT(self):

        localctx = D96Parser.Index_ArrayLITContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_index_ArrayLIT)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 558
            self.match(D96Parser.Array)
            self.state = 559
            self.elements()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def element_list(self):
            return self.getTypedRuleContext(D96Parser.Element_listContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_elements

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElements" ):
                return visitor.visitElements(self)
            else:
                return visitor.visitChildren(self)




    def elements(self):

        localctx = D96Parser.ElementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_elements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 561
            self.match(D96Parser.LP)
            self.state = 562
            self.element_list()
            self.state = 563
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Element_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def elements_tail(self):
            return self.getTypedRuleContext(D96Parser.Elements_tailContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_element_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElement_list" ):
                return visitor.visitElement_list(self)
            else:
                return visitor.visitChildren(self)




    def element_list(self):

        localctx = D96Parser.Element_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_element_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 568
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.ID) | (1 << D96Parser.KEYWORD_New) | (1 << D96Parser.SUB_OP) | (1 << D96Parser.NOT_OP) | (1 << D96Parser.INTLIT) | (1 << D96Parser.FLOATLIT) | (1 << D96Parser.BOOLEANLIT) | (1 << D96Parser.STRINGLIT))) != 0):
                self.state = 565
                self.expr()
                self.state = 566
                self.elements_tail()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elements_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMA(self):
            return self.getToken(D96Parser.COMA, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def elements_tail(self):
            return self.getTypedRuleContext(D96Parser.Elements_tailContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_elements_tail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElements_tail" ):
                return visitor.visitElements_tail(self)
            else:
                return visitor.visitChildren(self)




    def elements_tail(self):

        localctx = D96Parser.Elements_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_elements_tail)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 574
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.COMA:
                self.state = 570
                self.match(D96Parser.COMA)
                self.state = 571
                self.expr()
                self.state = 572
                self.elements_tail()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[31] = self.math_expr_sempred
        self._predicates[32] = self.mod_expr_sempred
        self._predicates[34] = self.logical_expr_sempred
        self._predicates[36] = self.relational_expr_1_sempred
        self._predicates[37] = self.relational_expr_2_sempred
        self._predicates[38] = self.string_expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def math_expr_sempred(self, localctx:Math_exprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 5)
         

    def mod_expr_sempred(self, localctx:Mod_exprContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 3)
         

    def logical_expr_sempred(self, localctx:Logical_exprContext, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 3)
         

    def relational_expr_1_sempred(self, localctx:Relational_expr_1Context, predIndex:int):
            if predIndex == 7:
                return self.precpred(self._ctx, 4)
         

    def relational_expr_2_sempred(self, localctx:Relational_expr_2Context, predIndex:int):
            if predIndex == 8:
                return self.precpred(self._ctx, 4)
         

    def string_expr_sempred(self, localctx:String_exprContext, predIndex:int):
            if predIndex == 9:
                return self.precpred(self._ctx, 3)
         




