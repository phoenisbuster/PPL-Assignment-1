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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3I")
        buf.write("\u0242\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\3\2\3\2\3\2\3\3")
        buf.write("\3\3\3\3\3\4\3\4\3\4\5\4\u008c\n\4\3\5\3\5\3\5\3\5\5\5")
        buf.write("\u0092\n\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\5\6\u009b\n\6\3")
        buf.write("\7\3\7\3\7\5\7\u00a0\n\7\3\b\3\b\5\b\u00a4\n\b\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\t\5\t\u00ac\n\t\3\t\3\t\3\n\3\n\3\n\3\13")
        buf.write("\3\13\3\13\5\13\u00b6\n\13\3\f\5\f\u00b9\n\f\3\f\3\f\3")
        buf.write("\r\3\r\3\r\5\r\u00c0\n\r\3\16\3\16\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\5\17\u00ca\n\17\3\17\3\17\3\20\3\20\5\20\u00d0")
        buf.write("\n\20\3\21\3\21\3\22\3\22\3\23\5\23\u00d7\n\23\3\23\3")
        buf.write("\23\3\23\3\23\3\24\3\24\3\24\3\24\3\25\3\25\3\25\5\25")
        buf.write("\u00e4\n\25\3\26\3\26\3\26\3\26\5\26\u00ea\n\26\3\27\3")
        buf.write("\27\3\27\3\27\3\30\3\30\3\30\3\31\3\31\3\31\5\31\u00f6")
        buf.write("\n\31\3\32\3\32\3\32\5\32\u00fb\n\32\3\33\3\33\3\33\3")
        buf.write("\33\5\33\u0101\n\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\5\34\u010b\n\34\3\35\3\35\3\35\3\35\3\35\3\35\3")
        buf.write("\36\3\36\3\36\5\36\u0116\n\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\5\36\u011d\n\36\3\37\3\37\5\37\u0121\n\37\3\37\3\37\5")
        buf.write("\37\u0125\n\37\3\37\3\37\3\37\3\37\3\37\5\37\u012c\n\37")
        buf.write("\3 \3 \3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\5")
        buf.write("\"\u013c\n\"\3#\3#\3#\3#\5#\u0142\n#\3$\3$\3$\3$\3$\3")
        buf.write("$\3$\3$\3$\3$\3$\5$\u014f\n$\3$\3$\3$\3$\3$\3$\3$\3$\3")
        buf.write("$\3$\3$\3$\7$\u015d\n$\f$\16$\u0160\13$\3%\3%\3%\3%\3")
        buf.write("%\5%\u0167\n%\3%\3%\3%\7%\u016c\n%\f%\16%\u016f\13%\3")
        buf.write("&\3&\3&\3&\3&\3&\5&\u0177\n&\3\'\3\'\3\'\3\'\3\'\5\'\u017e")
        buf.write("\n\'\3\'\3\'\3\'\3\'\3\'\3\'\7\'\u0186\n\'\f\'\16\'\u0189")
        buf.write("\13\'\3(\3(\5(\u018d\n(\3)\3)\3)\3)\3)\3)\5)\u0195\n)")
        buf.write("\3)\3)\3)\7)\u019a\n)\f)\16)\u019d\13)\3*\3*\3*\3*\3*")
        buf.write("\3*\5*\u01a5\n*\3*\3*\3*\7*\u01aa\n*\f*\16*\u01ad\13*")
        buf.write("\3+\3+\3+\3+\3+\5+\u01b4\n+\3+\3+\3+\7+\u01b9\n+\f+\16")
        buf.write("+\u01bc\13+\3,\3,\3,\3,\3-\3-\3-\5-\u01c5\n-\3.\3.\3.")
        buf.write("\5.\u01ca\n.\3/\3/\3/\3\60\3\60\3\60\3\60\3\60\3\60\3")
        buf.write("\60\5\60\u01d6\n\60\3\61\3\61\3\61\3\61\3\61\3\61\5\61")
        buf.write("\u01de\n\61\3\61\3\61\3\62\3\62\3\62\3\63\3\63\3\63\5")
        buf.write("\63\u01e8\n\63\3\64\3\64\3\65\3\65\5\65\u01ee\n\65\3\65")
        buf.write("\3\65\3\65\3\66\3\66\5\66\u01f5\n\66\3\67\3\67\3\67\3")
        buf.write("\67\3\67\3\67\5\67\u01fd\n\67\3\67\5\67\u0200\n\67\38")
        buf.write("\38\38\38\38\38\38\38\38\38\58\u020c\n8\58\u020e\n8\3")
        buf.write("9\39\39\59\u0213\n9\3:\3:\3:\5:\u0218\n:\3;\3;\3;\3<\3")
        buf.write("<\3<\3<\3<\3<\3<\3<\3<\5<\u0226\n<\3<\3<\3<\3=\3=\3=\3")
        buf.write("=\3=\3>\3>\5>\u0232\n>\3?\3?\3?\3?\3?\3@\3@\5@\u023b\n")
        buf.write("@\3A\3A\3A\5A\u0240\nA\3A\2\bFHLPRTB\2\4\6\b\n\f\16\20")
        buf.write("\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJL")
        buf.write("NPRTVXZ\\^`bdfhjlnprtvxz|~\u0080\2\t\3\2\22\23\3\2&\'")
        buf.write("\3\2\37\"\5\2\22\22\24\24)*\3\2\65\66\3\28;\3\2<=\2\u0261")
        buf.write("\2\u0082\3\2\2\2\4\u0085\3\2\2\2\6\u008b\3\2\2\2\b\u008d")
        buf.write("\3\2\2\2\n\u009a\3\2\2\2\f\u009f\3\2\2\2\16\u00a3\3\2")
        buf.write("\2\2\20\u00a5\3\2\2\2\22\u00af\3\2\2\2\24\u00b5\3\2\2")
        buf.write("\2\26\u00b8\3\2\2\2\30\u00bf\3\2\2\2\32\u00c1\3\2\2\2")
        buf.write("\34\u00c3\3\2\2\2\36\u00cf\3\2\2\2 \u00d1\3\2\2\2\"\u00d3")
        buf.write("\3\2\2\2$\u00d6\3\2\2\2&\u00dc\3\2\2\2(\u00e3\3\2\2\2")
        buf.write("*\u00e9\3\2\2\2,\u00eb\3\2\2\2.\u00ef\3\2\2\2\60\u00f5")
        buf.write("\3\2\2\2\62\u00fa\3\2\2\2\64\u0100\3\2\2\2\66\u010a\3")
        buf.write("\2\2\28\u010c\3\2\2\2:\u0112\3\2\2\2<\u0120\3\2\2\2>\u012d")
        buf.write("\3\2\2\2@\u012f\3\2\2\2B\u013b\3\2\2\2D\u0141\3\2\2\2")
        buf.write("F\u014e\3\2\2\2H\u0166\3\2\2\2J\u0176\3\2\2\2L\u017d\3")
        buf.write("\2\2\2N\u018c\3\2\2\2P\u0194\3\2\2\2R\u01a4\3\2\2\2T\u01b3")
        buf.write("\3\2\2\2V\u01bd\3\2\2\2X\u01c4\3\2\2\2Z\u01c9\3\2\2\2")
        buf.write("\\\u01cb\3\2\2\2^\u01d5\3\2\2\2`\u01d7\3\2\2\2b\u01e1")
        buf.write("\3\2\2\2d\u01e7\3\2\2\2f\u01e9\3\2\2\2h\u01ed\3\2\2\2")
        buf.write("j\u01f4\3\2\2\2l\u01ff\3\2\2\2n\u020d\3\2\2\2p\u0212\3")
        buf.write("\2\2\2r\u0217\3\2\2\2t\u0219\3\2\2\2v\u021c\3\2\2\2x\u022a")
        buf.write("\3\2\2\2z\u022f\3\2\2\2|\u0233\3\2\2\2~\u023a\3\2\2\2")
        buf.write("\u0080\u023f\3\2\2\2\u0082\u0083\5\4\3\2\u0083\u0084\7")
        buf.write("\2\2\3\u0084\3\3\2\2\2\u0085\u0086\5\b\5\2\u0086\u0087")
        buf.write("\5\6\4\2\u0087\5\3\2\2\2\u0088\u0089\5\b\5\2\u0089\u008a")
        buf.write("\5\6\4\2\u008a\u008c\3\2\2\2\u008b\u0088\3\2\2\2\u008b")
        buf.write("\u008c\3\2\2\2\u008c\7\3\2\2\2\u008d\u008e\7\6\2\2\u008e")
        buf.write("\u0091\t\2\2\2\u008f\u0090\7\3\2\2\u0090\u0092\t\2\2\2")
        buf.write("\u0091\u008f\3\2\2\2\u0091\u0092\3\2\2\2\u0092\u0093\3")
        buf.write("\2\2\2\u0093\u0094\7C\2\2\u0094\u0095\5\n\6\2\u0095\u0096")
        buf.write("\7D\2\2\u0096\t\3\2\2\2\u0097\u0098\5\16\b\2\u0098\u0099")
        buf.write("\5\f\7\2\u0099\u009b\3\2\2\2\u009a\u0097\3\2\2\2\u009a")
        buf.write("\u009b\3\2\2\2\u009b\13\3\2\2\2\u009c\u009d\5\16\b\2\u009d")
        buf.write("\u009e\5\f\7\2\u009e\u00a0\3\2\2\2\u009f\u009c\3\2\2\2")
        buf.write("\u009f\u00a0\3\2\2\2\u00a0\r\3\2\2\2\u00a1\u00a4\5\20")
        buf.write("\t\2\u00a2\u00a4\5$\23\2\u00a3\u00a1\3\2\2\2\u00a3\u00a2")
        buf.write("\3\2\2\2\u00a4\17\3\2\2\2\u00a5\u00a6\t\3\2\2\u00a6\u00a7")
        buf.write("\5\22\n\2\u00a7\u00a8\7\3\2\2\u00a8\u00ab\5\30\r\2\u00a9")
        buf.write("\u00aa\7\67\2\2\u00aa\u00ac\5\62\32\2\u00ab\u00a9\3\2")
        buf.write("\2\2\u00ab\u00ac\3\2\2\2\u00ac\u00ad\3\2\2\2\u00ad\u00ae")
        buf.write("\7E\2\2\u00ae\21\3\2\2\2\u00af\u00b0\5\26\f\2\u00b0\u00b1")
        buf.write("\5\24\13\2\u00b1\23\3\2\2\2\u00b2\u00b3\5\26\f\2\u00b3")
        buf.write("\u00b4\5\24\13\2\u00b4\u00b6\3\2\2\2\u00b5\u00b2\3\2\2")
        buf.write("\2\u00b5\u00b6\3\2\2\2\u00b6\25\3\2\2\2\u00b7\u00b9\7")
        buf.write("\4\2\2\u00b8\u00b7\3\2\2\2\u00b8\u00b9\3\2\2\2\u00b9\u00ba")
        buf.write("\3\2\2\2\u00ba\u00bb\7\22\2\2\u00bb\27\3\2\2\2\u00bc\u00c0")
        buf.write("\5\32\16\2\u00bd\u00c0\5\34\17\2\u00be\u00c0\5\"\22\2")
        buf.write("\u00bf\u00bc\3\2\2\2\u00bf\u00bd\3\2\2\2\u00bf\u00be\3")
        buf.write("\2\2\2\u00c0\31\3\2\2\2\u00c1\u00c2\t\4\2\2\u00c2\33\3")
        buf.write("\2\2\2\u00c3\u00c4\7\35\2\2\u00c4\u00c9\7A\2\2\u00c5\u00c6")
        buf.write("\5\36\20\2\u00c6\u00c7\7G\2\2\u00c7\u00c8\5 \21\2\u00c8")
        buf.write("\u00ca\3\2\2\2\u00c9\u00c5\3\2\2\2\u00c9\u00ca\3\2\2\2")
        buf.write("\u00ca\u00cb\3\2\2\2\u00cb\u00cc\7B\2\2\u00cc\35\3\2\2")
        buf.write("\2\u00cd\u00d0\5\32\16\2\u00ce\u00d0\5\34\17\2\u00cf\u00cd")
        buf.write("\3\2\2\2\u00cf\u00ce\3\2\2\2\u00d0\37\3\2\2\2\u00d1\u00d2")
        buf.write("\7\t\2\2\u00d2!\3\2\2\2\u00d3\u00d4\7\22\2\2\u00d4#\3")
        buf.write("\2\2\2\u00d5\u00d7\7\4\2\2\u00d6\u00d5\3\2\2\2\u00d6\u00d7")
        buf.write("\3\2\2\2\u00d7\u00d8\3\2\2\2\u00d8\u00d9\t\5\2\2\u00d9")
        buf.write("\u00da\5&\24\2\u00da\u00db\5V,\2\u00db%\3\2\2\2\u00dc")
        buf.write("\u00dd\7?\2\2\u00dd\u00de\5(\25\2\u00de\u00df\7@\2\2\u00df")
        buf.write("\'\3\2\2\2\u00e0\u00e1\5,\27\2\u00e1\u00e2\5*\26\2\u00e2")
        buf.write("\u00e4\3\2\2\2\u00e3\u00e0\3\2\2\2\u00e3\u00e4\3\2\2\2")
        buf.write("\u00e4)\3\2\2\2\u00e5\u00e6\7E\2\2\u00e6\u00e7\5,\27\2")
        buf.write("\u00e7\u00e8\5*\26\2\u00e8\u00ea\3\2\2\2\u00e9\u00e5\3")
        buf.write("\2\2\2\u00e9\u00ea\3\2\2\2\u00ea+\3\2\2\2\u00eb\u00ec")
        buf.write("\5.\30\2\u00ec\u00ed\7\3\2\2\u00ed\u00ee\5\30\r\2\u00ee")
        buf.write("-\3\2\2\2\u00ef\u00f0\7\22\2\2\u00f0\u00f1\5\60\31\2\u00f1")
        buf.write("/\3\2\2\2\u00f2\u00f3\7G\2\2\u00f3\u00f4\7\22\2\2\u00f4")
        buf.write("\u00f6\5\60\31\2\u00f5\u00f2\3\2\2\2\u00f5\u00f6\3\2\2")
        buf.write("\2\u00f6\61\3\2\2\2\u00f7\u00f8\5\66\34\2\u00f8\u00f9")
        buf.write("\5\64\33\2\u00f9\u00fb\3\2\2\2\u00fa\u00f7\3\2\2\2\u00fa")
        buf.write("\u00fb\3\2\2\2\u00fb\63\3\2\2\2\u00fc\u00fd\7G\2\2\u00fd")
        buf.write("\u00fe\5\66\34\2\u00fe\u00ff\5\64\33\2\u00ff\u0101\3\2")
        buf.write("\2\2\u0100\u00fc\3\2\2\2\u0100\u0101\3\2\2\2\u0101\65")
        buf.write("\3\2\2\2\u0102\u010b\58\35\2\u0103\u010b\5:\36\2\u0104")
        buf.write("\u010b\5<\37\2\u0105\u010b\5@!\2\u0106\u010b\5F$\2\u0107")
        buf.write("\u010b\5N(\2\u0108\u010b\5T+\2\u0109\u010b\7\22\2\2\u010a")
        buf.write("\u0102\3\2\2\2\u010a\u0103\3\2\2\2\u010a\u0104\3\2\2\2")
        buf.write("\u010a\u0105\3\2\2\2\u010a\u0106\3\2\2\2\u010a\u0107\3")
        buf.write("\2\2\2\u010a\u0108\3\2\2\2\u010a\u0109\3\2\2\2\u010b\67")
        buf.write("\3\2\2\2\u010c\u010d\7+\2\2\u010d\u010e\7\22\2\2\u010e")
        buf.write("\u010f\7?\2\2\u010f\u0110\5\62\32\2\u0110\u0111\7@\2\2")
        buf.write("\u01119\3\2\2\2\u0112\u0113\7\22\2\2\u0113\u0115\7>\2")
        buf.write("\2\u0114\u0116\7\4\2\2\u0115\u0114\3\2\2\2\u0115\u0116")
        buf.write("\3\2\2\2\u0116\u0117\3\2\2\2\u0117\u011c\7\22\2\2\u0118")
        buf.write("\u0119\7?\2\2\u0119\u011a\5\62\32\2\u011a\u011b\7@\2\2")
        buf.write("\u011b\u011d\3\2\2\2\u011c\u0118\3\2\2\2\u011c\u011d\3")
        buf.write("\2\2\2\u011d;\3\2\2\2\u011e\u0121\7\22\2\2\u011f\u0121")
        buf.write("\5> \2\u0120\u011e\3\2\2\2\u0120\u011f\3\2\2\2\u0121\u0122")
        buf.write("\3\2\2\2\u0122\u0124\7F\2\2\u0123\u0125\7\4\2\2\u0124")
        buf.write("\u0123\3\2\2\2\u0124\u0125\3\2\2\2\u0125\u0126\3\2\2\2")
        buf.write("\u0126\u012b\7\22\2\2\u0127\u0128\7?\2\2\u0128\u0129\5")
        buf.write("\62\32\2\u0129\u012a\7@\2\2\u012a\u012c\3\2\2\2\u012b")
        buf.write("\u0127\3\2\2\2\u012b\u012c\3\2\2\2\u012c=\3\2\2\2\u012d")
        buf.write("\u012e\7(\2\2\u012e?\3\2\2\2\u012f\u0130\5D#\2\u0130\u0131")
        buf.write("\5B\"\2\u0131A\3\2\2\2\u0132\u0133\7C\2\2\u0133\u0134")
        buf.write("\5D#\2\u0134\u0135\7D\2\2\u0135\u013c\3\2\2\2\u0136\u0137")
        buf.write("\7C\2\2\u0137\u0138\5D#\2\u0138\u0139\7D\2\2\u0139\u013a")
        buf.write("\5B\"\2\u013a\u013c\3\2\2\2\u013b\u0132\3\2\2\2\u013b")
        buf.write("\u0136\3\2\2\2\u013cC\3\2\2\2\u013d\u0142\5F$\2\u013e")
        buf.write("\u0142\5N(\2\u013f\u0142\5T+\2\u0140\u0142\7\22\2\2\u0141")
        buf.write("\u013d\3\2\2\2\u0141\u013e\3\2\2\2\u0141\u013f\3\2\2\2")
        buf.write("\u0141\u0140\3\2\2\2\u0142E\3\2\2\2\u0143\u0144\b$\1\2")
        buf.write("\u0144\u0145\7.\2\2\u0145\u014f\5F$\17\u0146\u014f\5J")
        buf.write("&\2\u0147\u014f\5H%\2\u0148\u014f\5L\'\2\u0149\u014f\5")
        buf.write(":\36\2\u014a\u014f\5<\37\2\u014b\u014f\7\t\2\2\u014c\u014f")
        buf.write("\7\n\2\2\u014d\u014f\7\22\2\2\u014e\u0143\3\2\2\2\u014e")
        buf.write("\u0146\3\2\2\2\u014e\u0147\3\2\2\2\u014e\u0148\3\2\2\2")
        buf.write("\u014e\u0149\3\2\2\2\u014e\u014a\3\2\2\2\u014e\u014b\3")
        buf.write("\2\2\2\u014e\u014c\3\2\2\2\u014e\u014d\3\2\2\2\u014f\u015e")
        buf.write("\3\2\2\2\u0150\u0151\f\r\2\2\u0151\u0152\7/\2\2\u0152")
        buf.write("\u015d\5F$\16\u0153\u0154\f\f\2\2\u0154\u0155\7\60\2\2")
        buf.write("\u0155\u015d\5F$\r\u0156\u0157\f\n\2\2\u0157\u0158\7-")
        buf.write("\2\2\u0158\u015d\5F$\13\u0159\u015a\f\t\2\2\u015a\u015b")
        buf.write("\7.\2\2\u015b\u015d\5F$\n\u015c\u0150\3\2\2\2\u015c\u0153")
        buf.write("\3\2\2\2\u015c\u0156\3\2\2\2\u015c\u0159\3\2\2\2\u015d")
        buf.write("\u0160\3\2\2\2\u015e\u015c\3\2\2\2\u015e\u015f\3\2\2\2")
        buf.write("\u015fG\3\2\2\2\u0160\u015e\3\2\2\2\u0161\u0162\b%\1\2")
        buf.write("\u0162\u0167\5:\36\2\u0163\u0167\5<\37\2\u0164\u0167\7")
        buf.write("\t\2\2\u0165\u0167\7\22\2\2\u0166\u0161\3\2\2\2\u0166")
        buf.write("\u0163\3\2\2\2\u0166\u0164\3\2\2\2\u0166\u0165\3\2\2\2")
        buf.write("\u0167\u016d\3\2\2\2\u0168\u0169\f\7\2\2\u0169\u016a\7")
        buf.write("\61\2\2\u016a\u016c\5H%\b\u016b\u0168\3\2\2\2\u016c\u016f")
        buf.write("\3\2\2\2\u016d\u016b\3\2\2\2\u016d\u016e\3\2\2\2\u016e")
        buf.write("I\3\2\2\2\u016f\u016d\3\2\2\2\u0170\u0171\7\62\2\2\u0171")
        buf.write("\u0177\5J&\2\u0172\u0177\5:\36\2\u0173\u0177\5<\37\2\u0174")
        buf.write("\u0177\7\13\2\2\u0175\u0177\7\22\2\2\u0176\u0170\3\2\2")
        buf.write("\2\u0176\u0172\3\2\2\2\u0176\u0173\3\2\2\2\u0176\u0174")
        buf.write("\3\2\2\2\u0176\u0175\3\2\2\2\u0177K\3\2\2\2\u0178\u0179")
        buf.write("\b\'\1\2\u0179\u017e\5:\36\2\u017a\u017e\5<\37\2\u017b")
        buf.write("\u017e\7\13\2\2\u017c\u017e\7\22\2\2\u017d\u0178\3\2\2")
        buf.write("\2\u017d\u017a\3\2\2\2\u017d\u017b\3\2\2\2\u017d\u017c")
        buf.write("\3\2\2\2\u017e\u0187\3\2\2\2\u017f\u0180\f\b\2\2\u0180")
        buf.write("\u0181\7\63\2\2\u0181\u0186\5L\'\t\u0182\u0183\f\7\2\2")
        buf.write("\u0183\u0184\7\64\2\2\u0184\u0186\5L\'\b\u0185\u017f\3")
        buf.write("\2\2\2\u0185\u0182\3\2\2\2\u0186\u0189\3\2\2\2\u0187\u0185")
        buf.write("\3\2\2\2\u0187\u0188\3\2\2\2\u0188M\3\2\2\2\u0189\u0187")
        buf.write("\3\2\2\2\u018a\u018d\5P)\2\u018b\u018d\5R*\2\u018c\u018a")
        buf.write("\3\2\2\2\u018c\u018b\3\2\2\2\u018dO\3\2\2\2\u018e\u018f")
        buf.write("\b)\1\2\u018f\u0195\5:\36\2\u0190\u0195\5<\37\2\u0191")
        buf.write("\u0195\7\t\2\2\u0192\u0195\7\13\2\2\u0193\u0195\7\22\2")
        buf.write("\2\u0194\u018e\3\2\2\2\u0194\u0190\3\2\2\2\u0194\u0191")
        buf.write("\3\2\2\2\u0194\u0192\3\2\2\2\u0194\u0193\3\2\2\2\u0195")
        buf.write("\u019b\3\2\2\2\u0196\u0197\f\b\2\2\u0197\u0198\t\6\2\2")
        buf.write("\u0198\u019a\5P)\t\u0199\u0196\3\2\2\2\u019a\u019d\3\2")
        buf.write("\2\2\u019b\u0199\3\2\2\2\u019b\u019c\3\2\2\2\u019cQ\3")
        buf.write("\2\2\2\u019d\u019b\3\2\2\2\u019e\u019f\b*\1\2\u019f\u01a5")
        buf.write("\5:\36\2\u01a0\u01a5\5<\37\2\u01a1\u01a5\7\t\2\2\u01a2")
        buf.write("\u01a5\7\n\2\2\u01a3\u01a5\7\22\2\2\u01a4\u019e\3\2\2")
        buf.write("\2\u01a4\u01a0\3\2\2\2\u01a4\u01a1\3\2\2\2\u01a4\u01a2")
        buf.write("\3\2\2\2\u01a4\u01a3\3\2\2\2\u01a5\u01ab\3\2\2\2\u01a6")
        buf.write("\u01a7\f\b\2\2\u01a7\u01a8\t\7\2\2\u01a8\u01aa\5R*\t\u01a9")
        buf.write("\u01a6\3\2\2\2\u01aa\u01ad\3\2\2\2\u01ab\u01a9\3\2\2\2")
        buf.write("\u01ab\u01ac\3\2\2\2\u01acS\3\2\2\2\u01ad\u01ab\3\2\2")
        buf.write("\2\u01ae\u01af\b+\1\2\u01af\u01b4\5:\36\2\u01b0\u01b4")
        buf.write("\5<\37\2\u01b1\u01b4\7\f\2\2\u01b2\u01b4\7\22\2\2\u01b3")
        buf.write("\u01ae\3\2\2\2\u01b3\u01b0\3\2\2\2\u01b3\u01b1\3\2\2\2")
        buf.write("\u01b3\u01b2\3\2\2\2\u01b4\u01ba\3\2\2\2\u01b5\u01b6\f")
        buf.write("\7\2\2\u01b6\u01b7\t\b\2\2\u01b7\u01b9\5T+\b\u01b8\u01b5")
        buf.write("\3\2\2\2\u01b9\u01bc\3\2\2\2\u01ba\u01b8\3\2\2\2\u01ba")
        buf.write("\u01bb\3\2\2\2\u01bbU\3\2\2\2\u01bc\u01ba\3\2\2\2\u01bd")
        buf.write("\u01be\7C\2\2\u01be\u01bf\5X-\2\u01bf\u01c0\7D\2\2\u01c0")
        buf.write("W\3\2\2\2\u01c1\u01c2\5\\/\2\u01c2\u01c3\5Z.\2\u01c3\u01c5")
        buf.write("\3\2\2\2\u01c4\u01c1\3\2\2\2\u01c4\u01c5\3\2\2\2\u01c5")
        buf.write("Y\3\2\2\2\u01c6\u01c7\5\\/\2\u01c7\u01c8\5Z.\2\u01c8\u01ca")
        buf.write("\3\2\2\2\u01c9\u01c6\3\2\2\2\u01c9\u01ca\3\2\2\2\u01ca")
        buf.write("[\3\2\2\2\u01cb\u01cc\5^\60\2\u01cc\u01cd\7E\2\2\u01cd")
        buf.write("]\3\2\2\2\u01ce\u01d6\5`\61\2\u01cf\u01d6\5h\65\2\u01d0")
        buf.write("\u01d6\5j\66\2\u01d1\u01d6\5v<\2\u01d2\u01d6\7\25\2\2")
        buf.write("\u01d3\u01d6\7\26\2\2\u01d4\u01d6\5z>\2\u01d5\u01ce\3")
        buf.write("\2\2\2\u01d5\u01cf\3\2\2\2\u01d5\u01d0\3\2\2\2\u01d5\u01d1")
        buf.write("\3\2\2\2\u01d5\u01d2\3\2\2\2\u01d5\u01d3\3\2\2\2\u01d5")
        buf.write("\u01d4\3\2\2\2\u01d6_\3\2\2\2\u01d7\u01d8\t\3\2\2\u01d8")
        buf.write("\u01d9\5b\62\2\u01d9\u01da\7\3\2\2\u01da\u01dd\5\30\r")
        buf.write("\2\u01db\u01dc\7\67\2\2\u01dc\u01de\5\62\32\2\u01dd\u01db")
        buf.write("\3\2\2\2\u01dd\u01de\3\2\2\2\u01de\u01df\3\2\2\2\u01df")
        buf.write("\u01e0\7E\2\2\u01e0a\3\2\2\2\u01e1\u01e2\5f\64\2\u01e2")
        buf.write("\u01e3\5d\63\2\u01e3c\3\2\2\2\u01e4\u01e5\5f\64\2\u01e5")
        buf.write("\u01e6\5d\63\2\u01e6\u01e8\3\2\2\2\u01e7\u01e4\3\2\2\2")
        buf.write("\u01e7\u01e8\3\2\2\2\u01e8e\3\2\2\2\u01e9\u01ea\7\22\2")
        buf.write("\2\u01eag\3\2\2\2\u01eb\u01ee\7\22\2\2\u01ec\u01ee\5@")
        buf.write("!\2\u01ed\u01eb\3\2\2\2\u01ed\u01ec\3\2\2\2\u01ee\u01ef")
        buf.write("\3\2\2\2\u01ef\u01f0\7\67\2\2\u01f0\u01f1\5\66\34\2\u01f1")
        buf.write("i\3\2\2\2\u01f2\u01f5\5l\67\2\u01f3\u01f5\5n8\2\u01f4")
        buf.write("\u01f2\3\2\2\2\u01f4\u01f3\3\2\2\2\u01f5k\3\2\2\2\u01f6")
        buf.write("\u01f7\7\27\2\2\u01f7\u01f8\5\66\34\2\u01f8\u01f9\5l\67")
        buf.write("\2\u01f9\u01fc\5p9\2\u01fa\u01fb\7\31\2\2\u01fb\u01fd")
        buf.write("\5l\67\2\u01fc\u01fa\3\2\2\2\u01fc\u01fd\3\2\2\2\u01fd")
        buf.write("\u0200\3\2\2\2\u01fe\u0200\5V,\2\u01ff\u01f6\3\2\2\2\u01ff")
        buf.write("\u01fe\3\2\2\2\u0200m\3\2\2\2\u0201\u0202\7\27\2\2\u0202")
        buf.write("\u0203\5\66\34\2\u0203\u0204\5j\66\2\u0204\u020e\3\2\2")
        buf.write("\2\u0205\u0206\7\27\2\2\u0206\u0207\5\66\34\2\u0207\u0208")
        buf.write("\5l\67\2\u0208\u020b\5p9\2\u0209\u020a\7\31\2\2\u020a")
        buf.write("\u020c\5n8\2\u020b\u0209\3\2\2\2\u020b\u020c\3\2\2\2\u020c")
        buf.write("\u020e\3\2\2\2\u020d\u0201\3\2\2\2\u020d\u0205\3\2\2\2")
        buf.write("\u020eo\3\2\2\2\u020f\u0210\5t;\2\u0210\u0211\5r:\2\u0211")
        buf.write("\u0213\3\2\2\2\u0212\u020f\3\2\2\2\u0212\u0213\3\2\2\2")
        buf.write("\u0213q\3\2\2\2\u0214\u0215\5t;\2\u0215\u0216\5r:\2\u0216")
        buf.write("\u0218\3\2\2\2\u0217\u0214\3\2\2\2\u0217\u0218\3\2\2\2")
        buf.write("\u0218s\3\2\2\2\u0219\u021a\7\30\2\2\u021a\u021b\5j\66")
        buf.write("\2\u021bu\3\2\2\2\u021c\u021d\7\32\2\2\u021d\u021e\7?")
        buf.write("\2\2\u021e\u021f\7\22\2\2\u021f\u0220\7\36\2\2\u0220\u0221")
        buf.write("\5\66\34\2\u0221\u0222\7\5\2\2\u0222\u0225\5\66\34\2\u0223")
        buf.write("\u0224\7,\2\2\u0224\u0226\5\66\34\2\u0225\u0223\3\2\2")
        buf.write("\2\u0225\u0226\3\2\2\2\u0226\u0227\3\2\2\2\u0227\u0228")
        buf.write("\7@\2\2\u0228\u0229\5V,\2\u0229w\3\2\2\2\u022a\u022b\7")
        buf.write("\22\2\2\u022b\u022c\7C\2\2\u022c\u022d\5\62\32\2\u022d")
        buf.write("\u022e\7D\2\2\u022ey\3\2\2\2\u022f\u0231\7\7\2\2\u0230")
        buf.write("\u0232\5\66\34\2\u0231\u0230\3\2\2\2\u0231\u0232\3\2\2")
        buf.write("\2\u0232{\3\2\2\2\u0233\u0234\7\17\2\2\u0234\u0235\7?")
        buf.write("\2\2\u0235\u0236\5~@\2\u0236\u0237\7@\2\2\u0237}\3\2\2")
        buf.write("\2\u0238\u0239\7\20\2\2\u0239\u023b\5\u0080A\2\u023a\u0238")
        buf.write("\3\2\2\2\u023a\u023b\3\2\2\2\u023b\177\3\2\2\2\u023c\u023d")
        buf.write("\7G\2\2\u023d\u023e\7\20\2\2\u023e\u0240\5\u0080A\2\u023f")
        buf.write("\u023c\3\2\2\2\u023f\u0240\3\2\2\2\u0240\u0081\3\2\2\2")
        buf.write("<\u008b\u0091\u009a\u009f\u00a3\u00ab\u00b5\u00b8\u00bf")
        buf.write("\u00c9\u00cf\u00d6\u00e3\u00e9\u00f5\u00fa\u0100\u010a")
        buf.write("\u0115\u011c\u0120\u0124\u012b\u013b\u0141\u014e\u015c")
        buf.write("\u015e\u0166\u016d\u0176\u017d\u0185\u0187\u018c\u0194")
        buf.write("\u019b\u01a4\u01ab\u01b3\u01ba\u01c4\u01c9\u01d5\u01dd")
        buf.write("\u01e7\u01ed\u01f4\u01fc\u01ff\u020b\u020d\u0212\u0217")
        buf.write("\u0225\u0231\u023a\u023f")
        return buf.getvalue()


class D96Parser ( Parser ):

    grammarFileName = "D96.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':'", "'$'", "'..'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'Program'", 
                     "'main'", "'Break'", "'Continue'", "'If'", "'Elseif'", 
                     "'Else'", "'Foreach'", "'True'", "'False'", "'Array'", 
                     "'In'", "'Int'", "'Float'", "'Boolean'", "'String'", 
                     "'Return'", "'Class'", "'Null'", "'Val'", "'Var'", 
                     "'Self'", "'Constructor'", "'Destructor'", "'New'", 
                     "'By'", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", 
                     "'||'", "'=='", "'!='", "'='", "'>'", "'<'", "'>='", 
                     "'<='", "'==.'", "'+.'", "'::'", "'('", "')'", "'['", 
                     "']'", "'{'", "'}'", "';'", "'.'", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "Class_word", "Return_word", "BLOCKCOMMENT", "INTLIT", 
                      "FLOATLIT", "BOOLEANLIT", "STRINGLIT", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE", "Array_word", "ARRAY_LIT", "Literal_list", 
                      "ID", "Program", "Main", "Break", "Continue", "If", 
                      "Elseif", "Else", "Foreach", "BooleanTrue", "BooleanFalse", 
                      "Array", "In", "Int", "Float", "Boolean", "String", 
                      "Return", "Class", "Null", "Val", "Var", "Self", "Constructor", 
                      "Destructor", "KEYWORD_New", "By", "ADD_OP", "SUB_OP", 
                      "MUL_OP", "DIV_OP", "MOD_OP", "NOT_OP", "AND_OP", 
                      "OR_OP", "EQUAL_OP", "DIFF_OP", "ASSIGN_OP", "GREATER_OP", 
                      "LESSER_OP", "GREATER_EQUAL_OP", "LESSER_EQUAL_OP", 
                      "STRING_COMP_OP", "STRING_CONCAT_OP", "MEMBER_ACCESS_OUT", 
                      "LP", "RP", "LSB", "RSB", "LB", "RB", "SEMI", "DOT", 
                      "COMA", "WS", "ERROR_CHAR" ]

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
    RULE_member_access_out = 28
    RULE_member_access_in = 29
    RULE_self_word = 30
    RULE_index_expr = 31
    RULE_index_operators = 32
    RULE_lower_expr = 33
    RULE_math_expr = 34
    RULE_mod_expr = 35
    RULE_logical_not_expr = 36
    RULE_logical_expr = 37
    RULE_relational_expr = 38
    RULE_relational_expr_1 = 39
    RULE_relational_expr_2 = 40
    RULE_string_expr = 41
    RULE_block_stmt = 42
    RULE_block_stmt_list = 43
    RULE_block_stmt_list_tail = 44
    RULE_stmt = 45
    RULE_stmt_list = 46
    RULE_var_cons_decl = 47
    RULE_var_cons_list = 48
    RULE_var_cons_list_tail = 49
    RULE_var_cons_name = 50
    RULE_asm = 51
    RULE_if_stmt = 52
    RULE_matchStmt = 53
    RULE_unmatchStmt = 54
    RULE_elseif_list = 55
    RULE_elseif_list_tail = 56
    RULE_elseif_stmt = 57
    RULE_loop_stmt = 58
    RULE_call = 59
    RULE_return_stmt = 60
    RULE_multi_ArrayLIT = 61
    RULE_array_list = 62
    RULE_array_list_tail = 63

    ruleNames =  [ "program", "many_class_decl", "class_decl_list", "class_decl", 
                   "member_lists", "member_list_tail", "member", "attributes", 
                   "attribute_list", "attribute_list_tail", "attribute_name", 
                   "types", "primitive_Type", "array_Type", "element_type", 
                   "array_size", "class_type", "methods", "param", "paramlist", 
                   "paramlist_tail", "param_decl", "idlist", "idlist_tail", 
                   "expr_list", "expr_list_tail", "expr", "class_expr", 
                   "member_access_out", "member_access_in", "self_word", 
                   "index_expr", "index_operators", "lower_expr", "math_expr", 
                   "mod_expr", "logical_not_expr", "logical_expr", "relational_expr", 
                   "relational_expr_1", "relational_expr_2", "string_expr", 
                   "block_stmt", "block_stmt_list", "block_stmt_list_tail", 
                   "stmt", "stmt_list", "var_cons_decl", "var_cons_list", 
                   "var_cons_list_tail", "var_cons_name", "asm", "if_stmt", 
                   "matchStmt", "unmatchStmt", "elseif_list", "elseif_list_tail", 
                   "elseif_stmt", "loop_stmt", "call", "return_stmt", "multi_ArrayLIT", 
                   "array_list", "array_list_tail" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    Class_word=4
    Return_word=5
    BLOCKCOMMENT=6
    INTLIT=7
    FLOATLIT=8
    BOOLEANLIT=9
    STRINGLIT=10
    UNCLOSE_STRING=11
    ILLEGAL_ESCAPE=12
    Array_word=13
    ARRAY_LIT=14
    Literal_list=15
    ID=16
    Program=17
    Main=18
    Break=19
    Continue=20
    If=21
    Elseif=22
    Else=23
    Foreach=24
    BooleanTrue=25
    BooleanFalse=26
    Array=27
    In=28
    Int=29
    Float=30
    Boolean=31
    String=32
    Return=33
    Class=34
    Null=35
    Val=36
    Var=37
    Self=38
    Constructor=39
    Destructor=40
    KEYWORD_New=41
    By=42
    ADD_OP=43
    SUB_OP=44
    MUL_OP=45
    DIV_OP=46
    MOD_OP=47
    NOT_OP=48
    AND_OP=49
    OR_OP=50
    EQUAL_OP=51
    DIFF_OP=52
    ASSIGN_OP=53
    GREATER_OP=54
    LESSER_OP=55
    GREATER_EQUAL_OP=56
    LESSER_EQUAL_OP=57
    STRING_COMP_OP=58
    STRING_CONCAT_OP=59
    MEMBER_ACCESS_OUT=60
    LP=61
    RP=62
    LSB=63
    RSB=64
    LB=65
    RB=66
    SEMI=67
    DOT=68
    COMA=69
    WS=70
    ERROR_CHAR=71

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
            self.state = 128
            self.many_class_decl()
            self.state = 129
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
            self.state = 131
            self.class_decl()
            self.state = 132
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
            self.state = 137
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.Class_word:
                self.state = 134
                self.class_decl()
                self.state = 135
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

        def Class_word(self):
            return self.getToken(D96Parser.Class_word, 0)

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
            self.state = 139
            self.match(D96Parser.Class_word)
            self.state = 140
            _la = self._input.LA(1)
            if not(_la==D96Parser.ID or _la==D96Parser.Program):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 143
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.T__0:
                self.state = 141
                self.match(D96Parser.T__0)
                self.state = 142
                _la = self._input.LA(1)
                if not(_la==D96Parser.ID or _la==D96Parser.Program):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 145
            self.match(D96Parser.LB)
            self.state = 146
            self.member_lists()
            self.state = 147
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
            self.state = 152
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.T__1) | (1 << D96Parser.ID) | (1 << D96Parser.Main) | (1 << D96Parser.Val) | (1 << D96Parser.Var) | (1 << D96Parser.Constructor) | (1 << D96Parser.Destructor))) != 0):
                self.state = 149
                self.member()
                self.state = 150
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
            self.state = 157
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.T__1) | (1 << D96Parser.ID) | (1 << D96Parser.Main) | (1 << D96Parser.Val) | (1 << D96Parser.Var) | (1 << D96Parser.Constructor) | (1 << D96Parser.Destructor))) != 0):
                self.state = 154
                self.member()
                self.state = 155
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
            self.state = 161
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.Val, D96Parser.Var]:
                self.enterOuterAlt(localctx, 1)
                self.state = 159
                self.attributes()
                pass
            elif token in [D96Parser.T__1, D96Parser.ID, D96Parser.Main, D96Parser.Constructor, D96Parser.Destructor]:
                self.enterOuterAlt(localctx, 2)
                self.state = 160
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
            self.state = 163
            _la = self._input.LA(1)
            if not(_la==D96Parser.Val or _la==D96Parser.Var):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 164
            self.attribute_list()
            self.state = 165
            self.match(D96Parser.T__0)
            self.state = 166
            self.types()
            self.state = 169
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ASSIGN_OP:
                self.state = 167
                self.match(D96Parser.ASSIGN_OP)
                self.state = 168
                self.expr_list()


            self.state = 171
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
            self.state = 173
            self.attribute_name()
            self.state = 174
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
            self.state = 179
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.T__1 or _la==D96Parser.ID:
                self.state = 176
                self.attribute_name()
                self.state = 177
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
            self.state = 182
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.T__1:
                self.state = 181
                self.match(D96Parser.T__1)


            self.state = 184
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
            self.state = 189
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.Int, D96Parser.Float, D96Parser.Boolean, D96Parser.String]:
                self.enterOuterAlt(localctx, 1)
                self.state = 186
                self.primitive_Type()
                pass
            elif token in [D96Parser.Array]:
                self.enterOuterAlt(localctx, 2)
                self.state = 187
                self.array_Type()
                pass
            elif token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 188
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
            self.state = 191
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
            self.state = 193
            self.match(D96Parser.Array)
            self.state = 194
            self.match(D96Parser.LSB)
            self.state = 199
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.Array) | (1 << D96Parser.Int) | (1 << D96Parser.Float) | (1 << D96Parser.Boolean) | (1 << D96Parser.String))) != 0):
                self.state = 195
                self.element_type()
                self.state = 196
                self.match(D96Parser.COMA)
                self.state = 197
                self.array_size()


            self.state = 201
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
            self.state = 205
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.Int, D96Parser.Float, D96Parser.Boolean, D96Parser.String]:
                self.enterOuterAlt(localctx, 1)
                self.state = 203
                self.primitive_Type()
                pass
            elif token in [D96Parser.Array]:
                self.enterOuterAlt(localctx, 2)
                self.state = 204
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
            self.state = 207
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
            self.state = 209
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
            self.state = 212
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.T__1:
                self.state = 211
                self.match(D96Parser.T__1)


            self.state = 214
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.ID) | (1 << D96Parser.Main) | (1 << D96Parser.Constructor) | (1 << D96Parser.Destructor))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 215
            self.param()
            self.state = 216
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
            self.state = 218
            self.match(D96Parser.LP)
            self.state = 219
            self.paramlist()
            self.state = 220
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
            self.state = 225
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ID:
                self.state = 222
                self.param_decl()
                self.state = 223
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
            self.state = 231
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.SEMI:
                self.state = 227
                self.match(D96Parser.SEMI)
                self.state = 228
                self.param_decl()
                self.state = 229
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
            self.state = 233
            self.idlist()
            self.state = 234
            self.match(D96Parser.T__0)
            self.state = 235
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
            self.state = 237
            self.match(D96Parser.ID)
            self.state = 238
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
            self.state = 243
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.COMA:
                self.state = 240
                self.match(D96Parser.COMA)
                self.state = 241
                self.match(D96Parser.ID)
                self.state = 242
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
            self.state = 248
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.INTLIT) | (1 << D96Parser.FLOATLIT) | (1 << D96Parser.BOOLEANLIT) | (1 << D96Parser.STRINGLIT) | (1 << D96Parser.ID) | (1 << D96Parser.Self) | (1 << D96Parser.KEYWORD_New) | (1 << D96Parser.SUB_OP) | (1 << D96Parser.NOT_OP))) != 0):
                self.state = 245
                self.expr()
                self.state = 246
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
            self.state = 254
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.COMA:
                self.state = 250
                self.match(D96Parser.COMA)
                self.state = 251
                self.expr()
                self.state = 252
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


        def member_access_out(self):
            return self.getTypedRuleContext(D96Parser.Member_access_outContext,0)


        def member_access_in(self):
            return self.getTypedRuleContext(D96Parser.Member_access_inContext,0)


        def index_expr(self):
            return self.getTypedRuleContext(D96Parser.Index_exprContext,0)


        def math_expr(self):
            return self.getTypedRuleContext(D96Parser.Math_exprContext,0)


        def relational_expr(self):
            return self.getTypedRuleContext(D96Parser.Relational_exprContext,0)


        def string_expr(self):
            return self.getTypedRuleContext(D96Parser.String_exprContext,0)


        def ID(self):
            return self.getToken(D96Parser.ID, 0)

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
        try:
            self.state = 264
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 256
                self.class_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 257
                self.member_access_out()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 258
                self.member_access_in()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 259
                self.index_expr()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 260
                self.math_expr(0)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 261
                self.relational_expr()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 262
                self.string_expr(0)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 263
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
            self.state = 266
            self.match(D96Parser.KEYWORD_New)
            self.state = 267
            self.match(D96Parser.ID)
            self.state = 268
            self.match(D96Parser.LP)
            self.state = 269
            self.expr_list()
            self.state = 270
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Member_access_outContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

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

        def getRuleIndex(self):
            return D96Parser.RULE_member_access_out

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMember_access_out" ):
                return visitor.visitMember_access_out(self)
            else:
                return visitor.visitChildren(self)




    def member_access_out(self):

        localctx = D96Parser.Member_access_outContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_member_access_out)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self.match(D96Parser.ID)
            self.state = 273
            self.match(D96Parser.MEMBER_ACCESS_OUT)
            self.state = 275
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.T__1:
                self.state = 274
                self.match(D96Parser.T__1)


            self.state = 277
            self.match(D96Parser.ID)
            self.state = 282
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 278
                self.match(D96Parser.LP)
                self.state = 279
                self.expr_list()
                self.state = 280
                self.match(D96Parser.RP)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Member_access_inContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ID)
            else:
                return self.getToken(D96Parser.ID, i)

        def self_word(self):
            return self.getTypedRuleContext(D96Parser.Self_wordContext,0)


        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def expr_list(self):
            return self.getTypedRuleContext(D96Parser.Expr_listContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_member_access_in

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMember_access_in" ):
                return visitor.visitMember_access_in(self)
            else:
                return visitor.visitChildren(self)




    def member_access_in(self):

        localctx = D96Parser.Member_access_inContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_member_access_in)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ID]:
                self.state = 284
                self.match(D96Parser.ID)
                pass
            elif token in [D96Parser.Self]:
                self.state = 285
                self.self_word()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 288
            self.match(D96Parser.DOT)
            self.state = 290
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.T__1:
                self.state = 289
                self.match(D96Parser.T__1)


            self.state = 292
            self.match(D96Parser.ID)
            self.state = 297
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.state = 293
                self.match(D96Parser.LP)
                self.state = 294
                self.expr_list()
                self.state = 295
                self.match(D96Parser.RP)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Self_wordContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Self(self):
            return self.getToken(D96Parser.Self, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_self_word

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelf_word" ):
                return visitor.visitSelf_word(self)
            else:
                return visitor.visitChildren(self)




    def self_word(self):

        localctx = D96Parser.Self_wordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_self_word)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 299
            self.match(D96Parser.Self)
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
        self.enterRule(localctx, 62, self.RULE_index_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 301
            self.lower_expr()
            self.state = 302
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
        self.enterRule(localctx, 64, self.RULE_index_operators)
        try:
            self.state = 313
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 304
                self.match(D96Parser.LB)
                self.state = 305
                self.lower_expr()
                self.state = 306
                self.match(D96Parser.RB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 308
                self.match(D96Parser.LB)
                self.state = 309
                self.lower_expr()
                self.state = 310
                self.match(D96Parser.RB)
                self.state = 311
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
        self.enterRule(localctx, 66, self.RULE_lower_expr)
        try:
            self.state = 319
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 315
                self.math_expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 316
                self.relational_expr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 317
                self.string_expr(0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 318
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


        def member_access_out(self):
            return self.getTypedRuleContext(D96Parser.Member_access_outContext,0)


        def member_access_in(self):
            return self.getTypedRuleContext(D96Parser.Member_access_inContext,0)


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
        _startState = 68
        self.enterRecursionRule(localctx, 68, self.RULE_math_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 332
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.state = 322
                self.match(D96Parser.SUB_OP)
                self.state = 323
                self.math_expr(13)
                pass

            elif la_ == 2:
                self.state = 324
                self.logical_not_expr()
                pass

            elif la_ == 3:
                self.state = 325
                self.mod_expr(0)
                pass

            elif la_ == 4:
                self.state = 326
                self.logical_expr(0)
                pass

            elif la_ == 5:
                self.state = 327
                self.member_access_out()
                pass

            elif la_ == 6:
                self.state = 328
                self.member_access_in()
                pass

            elif la_ == 7:
                self.state = 329
                self.match(D96Parser.INTLIT)
                pass

            elif la_ == 8:
                self.state = 330
                self.match(D96Parser.FLOATLIT)
                pass

            elif la_ == 9:
                self.state = 331
                self.match(D96Parser.ID)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 348
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 346
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.Math_exprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_math_expr)
                        self.state = 334
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 335
                        self.match(D96Parser.MUL_OP)
                        self.state = 336
                        self.math_expr(12)
                        pass

                    elif la_ == 2:
                        localctx = D96Parser.Math_exprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_math_expr)
                        self.state = 337
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 338
                        self.match(D96Parser.DIV_OP)
                        self.state = 339
                        self.math_expr(11)
                        pass

                    elif la_ == 3:
                        localctx = D96Parser.Math_exprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_math_expr)
                        self.state = 340
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 341
                        self.match(D96Parser.ADD_OP)
                        self.state = 342
                        self.math_expr(9)
                        pass

                    elif la_ == 4:
                        localctx = D96Parser.Math_exprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_math_expr)
                        self.state = 343
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 344
                        self.match(D96Parser.SUB_OP)
                        self.state = 345
                        self.math_expr(8)
                        pass

             
                self.state = 350
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

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

        def member_access_out(self):
            return self.getTypedRuleContext(D96Parser.Member_access_outContext,0)


        def member_access_in(self):
            return self.getTypedRuleContext(D96Parser.Member_access_inContext,0)


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
        _startState = 70
        self.enterRecursionRule(localctx, 70, self.RULE_mod_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 356
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.state = 352
                self.member_access_out()
                pass

            elif la_ == 2:
                self.state = 353
                self.member_access_in()
                pass

            elif la_ == 3:
                self.state = 354
                self.match(D96Parser.INTLIT)
                pass

            elif la_ == 4:
                self.state = 355
                self.match(D96Parser.ID)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 363
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Mod_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_mod_expr)
                    self.state = 358
                    if not self.precpred(self._ctx, 5):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                    self.state = 359
                    self.match(D96Parser.MOD_OP)
                    self.state = 360
                    self.mod_expr(6) 
                self.state = 365
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

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


        def member_access_out(self):
            return self.getTypedRuleContext(D96Parser.Member_access_outContext,0)


        def member_access_in(self):
            return self.getTypedRuleContext(D96Parser.Member_access_inContext,0)


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
        self.enterRule(localctx, 72, self.RULE_logical_not_expr)
        try:
            self.state = 372
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 366
                self.match(D96Parser.NOT_OP)
                self.state = 367
                self.logical_not_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 368
                self.member_access_out()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 369
                self.member_access_in()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 370
                self.match(D96Parser.BOOLEANLIT)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 371
                self.match(D96Parser.ID)
                pass


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

        def member_access_out(self):
            return self.getTypedRuleContext(D96Parser.Member_access_outContext,0)


        def member_access_in(self):
            return self.getTypedRuleContext(D96Parser.Member_access_inContext,0)


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
        _startState = 74
        self.enterRecursionRule(localctx, 74, self.RULE_logical_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 379
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.state = 375
                self.member_access_out()
                pass

            elif la_ == 2:
                self.state = 376
                self.member_access_in()
                pass

            elif la_ == 3:
                self.state = 377
                self.match(D96Parser.BOOLEANLIT)
                pass

            elif la_ == 4:
                self.state = 378
                self.match(D96Parser.ID)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 389
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 387
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.Logical_exprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_logical_expr)
                        self.state = 381
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 382
                        self.match(D96Parser.AND_OP)
                        self.state = 383
                        self.logical_expr(7)
                        pass

                    elif la_ == 2:
                        localctx = D96Parser.Logical_exprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_logical_expr)
                        self.state = 384
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 385
                        self.match(D96Parser.OR_OP)
                        self.state = 386
                        self.logical_expr(6)
                        pass

             
                self.state = 391
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

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
        self.enterRule(localctx, 76, self.RULE_relational_expr)
        try:
            self.state = 394
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 392
                self.relational_expr_1(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 393
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

        def member_access_out(self):
            return self.getTypedRuleContext(D96Parser.Member_access_outContext,0)


        def member_access_in(self):
            return self.getTypedRuleContext(D96Parser.Member_access_inContext,0)


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
        _startState = 78
        self.enterRecursionRule(localctx, 78, self.RULE_relational_expr_1, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 402
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.state = 397
                self.member_access_out()
                pass

            elif la_ == 2:
                self.state = 398
                self.member_access_in()
                pass

            elif la_ == 3:
                self.state = 399
                self.match(D96Parser.INTLIT)
                pass

            elif la_ == 4:
                self.state = 400
                self.match(D96Parser.BOOLEANLIT)
                pass

            elif la_ == 5:
                self.state = 401
                self.match(D96Parser.ID)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 409
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,36,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Relational_expr_1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_relational_expr_1)
                    self.state = 404
                    if not self.precpred(self._ctx, 6):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                    self.state = 405
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.EQUAL_OP or _la==D96Parser.DIFF_OP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 406
                    self.relational_expr_1(7) 
                self.state = 411
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,36,self._ctx)

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

        def member_access_out(self):
            return self.getTypedRuleContext(D96Parser.Member_access_outContext,0)


        def member_access_in(self):
            return self.getTypedRuleContext(D96Parser.Member_access_inContext,0)


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
        _startState = 80
        self.enterRecursionRule(localctx, 80, self.RULE_relational_expr_2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 418
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.state = 413
                self.member_access_out()
                pass

            elif la_ == 2:
                self.state = 414
                self.member_access_in()
                pass

            elif la_ == 3:
                self.state = 415
                self.match(D96Parser.INTLIT)
                pass

            elif la_ == 4:
                self.state = 416
                self.match(D96Parser.FLOATLIT)
                pass

            elif la_ == 5:
                self.state = 417
                self.match(D96Parser.ID)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 425
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,38,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Relational_expr_2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_relational_expr_2)
                    self.state = 420
                    if not self.precpred(self._ctx, 6):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                    self.state = 421
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.GREATER_OP) | (1 << D96Parser.LESSER_OP) | (1 << D96Parser.GREATER_EQUAL_OP) | (1 << D96Parser.LESSER_EQUAL_OP))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 422
                    self.relational_expr_2(7) 
                self.state = 427
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,38,self._ctx)

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

        def member_access_out(self):
            return self.getTypedRuleContext(D96Parser.Member_access_outContext,0)


        def member_access_in(self):
            return self.getTypedRuleContext(D96Parser.Member_access_inContext,0)


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
        _startState = 82
        self.enterRecursionRule(localctx, 82, self.RULE_string_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 433
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.state = 429
                self.member_access_out()
                pass

            elif la_ == 2:
                self.state = 430
                self.member_access_in()
                pass

            elif la_ == 3:
                self.state = 431
                self.match(D96Parser.STRINGLIT)
                pass

            elif la_ == 4:
                self.state = 432
                self.match(D96Parser.ID)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 440
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,40,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.String_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_string_expr)
                    self.state = 435
                    if not self.precpred(self._ctx, 5):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                    self.state = 436
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.STRING_COMP_OP or _la==D96Parser.STRING_CONCAT_OP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 437
                    self.string_expr(6) 
                self.state = 442
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,40,self._ctx)

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
        self.enterRule(localctx, 84, self.RULE_block_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 443
            self.match(D96Parser.LB)
            self.state = 444
            self.block_stmt_list()
            self.state = 445
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
        self.enterRule(localctx, 86, self.RULE_block_stmt_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 450
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 5)) & ~0x3f) == 0 and ((1 << (_la - 5)) & ((1 << (D96Parser.Return_word - 5)) | (1 << (D96Parser.INTLIT - 5)) | (1 << (D96Parser.FLOATLIT - 5)) | (1 << (D96Parser.BOOLEANLIT - 5)) | (1 << (D96Parser.STRINGLIT - 5)) | (1 << (D96Parser.ID - 5)) | (1 << (D96Parser.Break - 5)) | (1 << (D96Parser.Continue - 5)) | (1 << (D96Parser.If - 5)) | (1 << (D96Parser.Foreach - 5)) | (1 << (D96Parser.Val - 5)) | (1 << (D96Parser.Var - 5)) | (1 << (D96Parser.Self - 5)) | (1 << (D96Parser.SUB_OP - 5)) | (1 << (D96Parser.NOT_OP - 5)) | (1 << (D96Parser.LB - 5)))) != 0):
                self.state = 447
                self.stmt()
                self.state = 448
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
        self.enterRule(localctx, 88, self.RULE_block_stmt_list_tail)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 455
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 5)) & ~0x3f) == 0 and ((1 << (_la - 5)) & ((1 << (D96Parser.Return_word - 5)) | (1 << (D96Parser.INTLIT - 5)) | (1 << (D96Parser.FLOATLIT - 5)) | (1 << (D96Parser.BOOLEANLIT - 5)) | (1 << (D96Parser.STRINGLIT - 5)) | (1 << (D96Parser.ID - 5)) | (1 << (D96Parser.Break - 5)) | (1 << (D96Parser.Continue - 5)) | (1 << (D96Parser.If - 5)) | (1 << (D96Parser.Foreach - 5)) | (1 << (D96Parser.Val - 5)) | (1 << (D96Parser.Var - 5)) | (1 << (D96Parser.Self - 5)) | (1 << (D96Parser.SUB_OP - 5)) | (1 << (D96Parser.NOT_OP - 5)) | (1 << (D96Parser.LB - 5)))) != 0):
                self.state = 452
                self.stmt()
                self.state = 453
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
        self.enterRule(localctx, 90, self.RULE_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 457
            self.stmt_list()
            self.state = 458
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
        self.enterRule(localctx, 92, self.RULE_stmt_list)
        try:
            self.state = 467
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.Val, D96Parser.Var]:
                self.enterOuterAlt(localctx, 1)
                self.state = 460
                self.var_cons_decl()
                pass
            elif token in [D96Parser.INTLIT, D96Parser.FLOATLIT, D96Parser.BOOLEANLIT, D96Parser.STRINGLIT, D96Parser.ID, D96Parser.Self, D96Parser.SUB_OP, D96Parser.NOT_OP]:
                self.enterOuterAlt(localctx, 2)
                self.state = 461
                self.asm()
                pass
            elif token in [D96Parser.If, D96Parser.LB]:
                self.enterOuterAlt(localctx, 3)
                self.state = 462
                self.if_stmt()
                pass
            elif token in [D96Parser.Foreach]:
                self.enterOuterAlt(localctx, 4)
                self.state = 463
                self.loop_stmt()
                pass
            elif token in [D96Parser.Break]:
                self.enterOuterAlt(localctx, 5)
                self.state = 464
                self.match(D96Parser.Break)
                pass
            elif token in [D96Parser.Continue]:
                self.enterOuterAlt(localctx, 6)
                self.state = 465
                self.match(D96Parser.Continue)
                pass
            elif token in [D96Parser.Return_word]:
                self.enterOuterAlt(localctx, 7)
                self.state = 466
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
        self.enterRule(localctx, 94, self.RULE_var_cons_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 469
            _la = self._input.LA(1)
            if not(_la==D96Parser.Val or _la==D96Parser.Var):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 470
            self.var_cons_list()
            self.state = 471
            self.match(D96Parser.T__0)
            self.state = 472
            self.types()
            self.state = 475
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ASSIGN_OP:
                self.state = 473
                self.match(D96Parser.ASSIGN_OP)
                self.state = 474
                self.expr_list()


            self.state = 477
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
        self.enterRule(localctx, 96, self.RULE_var_cons_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 479
            self.var_cons_name()
            self.state = 480
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
        self.enterRule(localctx, 98, self.RULE_var_cons_list_tail)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 485
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ID:
                self.state = 482
                self.var_cons_name()
                self.state = 483
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
        self.enterRule(localctx, 100, self.RULE_var_cons_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 487
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
        self.enterRule(localctx, 102, self.RULE_asm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 491
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                self.state = 489
                self.match(D96Parser.ID)
                pass

            elif la_ == 2:
                self.state = 490
                self.index_expr()
                pass


            self.state = 493
            self.match(D96Parser.ASSIGN_OP)
            self.state = 494
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
        self.enterRule(localctx, 104, self.RULE_if_stmt)
        try:
            self.state = 498
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 496
                self.matchStmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 497
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
        self.enterRule(localctx, 106, self.RULE_matchStmt)
        try:
            self.state = 509
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.If]:
                self.enterOuterAlt(localctx, 1)
                self.state = 500
                self.match(D96Parser.If)
                self.state = 501
                self.expr()
                self.state = 502
                self.matchStmt()

                self.state = 503
                self.elseif_list()
                self.state = 506
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
                if la_ == 1:
                    self.state = 504
                    self.match(D96Parser.Else)
                    self.state = 505
                    self.matchStmt()


                pass
            elif token in [D96Parser.LB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 508
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
        self.enterRule(localctx, 108, self.RULE_unmatchStmt)
        try:
            self.state = 523
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 511
                self.match(D96Parser.If)
                self.state = 512
                self.expr()
                self.state = 513
                self.if_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 515
                self.match(D96Parser.If)
                self.state = 516
                self.expr()
                self.state = 517
                self.matchStmt()

                self.state = 518
                self.elseif_list()
                self.state = 521
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
                if la_ == 1:
                    self.state = 519
                    self.match(D96Parser.Else)
                    self.state = 520
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
        self.enterRule(localctx, 110, self.RULE_elseif_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 528
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
            if la_ == 1:
                self.state = 525
                self.elseif_stmt()
                self.state = 526
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
        self.enterRule(localctx, 112, self.RULE_elseif_list_tail)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 533
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
            if la_ == 1:
                self.state = 530
                self.elseif_stmt()
                self.state = 531
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
        self.enterRule(localctx, 114, self.RULE_elseif_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 535
            self.match(D96Parser.Elseif)
            self.state = 536
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
        self.enterRule(localctx, 116, self.RULE_loop_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 538
            self.match(D96Parser.Foreach)
            self.state = 539
            self.match(D96Parser.LP)
            self.state = 540
            self.match(D96Parser.ID)
            self.state = 541
            self.match(D96Parser.In)
            self.state = 542
            self.expr()
            self.state = 543
            self.match(D96Parser.T__2)
            self.state = 544
            self.expr()
            self.state = 547
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.By:
                self.state = 545
                self.match(D96Parser.By)
                self.state = 546
                self.expr()


            self.state = 549
            self.match(D96Parser.RP)
            self.state = 550
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
        self.enterRule(localctx, 118, self.RULE_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 552
            self.match(D96Parser.ID)
            self.state = 553
            self.match(D96Parser.LB)
            self.state = 554
            self.expr_list()
            self.state = 555
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

        def Return_word(self):
            return self.getToken(D96Parser.Return_word, 0)

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
        self.enterRule(localctx, 120, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 557
            self.match(D96Parser.Return_word)
            self.state = 559
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.INTLIT) | (1 << D96Parser.FLOATLIT) | (1 << D96Parser.BOOLEANLIT) | (1 << D96Parser.STRINGLIT) | (1 << D96Parser.ID) | (1 << D96Parser.Self) | (1 << D96Parser.KEYWORD_New) | (1 << D96Parser.SUB_OP) | (1 << D96Parser.NOT_OP))) != 0):
                self.state = 558
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

        def Array_word(self):
            return self.getToken(D96Parser.Array_word, 0)

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
        self.enterRule(localctx, 122, self.RULE_multi_ArrayLIT)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 561
            self.match(D96Parser.Array_word)
            self.state = 562
            self.match(D96Parser.LP)
            self.state = 563
            self.array_list()
            self.state = 564
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

        def ARRAY_LIT(self):
            return self.getToken(D96Parser.ARRAY_LIT, 0)

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
        self.enterRule(localctx, 124, self.RULE_array_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 568
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ARRAY_LIT:
                self.state = 566
                self.match(D96Parser.ARRAY_LIT)
                self.state = 567
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

        def ARRAY_LIT(self):
            return self.getToken(D96Parser.ARRAY_LIT, 0)

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
        self.enterRule(localctx, 126, self.RULE_array_list_tail)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 573
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.COMA:
                self.state = 570
                self.match(D96Parser.COMA)
                self.state = 571
                self.match(D96Parser.ARRAY_LIT)
                self.state = 572
                self.array_list_tail()


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
        self._predicates[34] = self.math_expr_sempred
        self._predicates[35] = self.mod_expr_sempred
        self._predicates[37] = self.logical_expr_sempred
        self._predicates[39] = self.relational_expr_1_sempred
        self._predicates[40] = self.relational_expr_2_sempred
        self._predicates[41] = self.string_expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def math_expr_sempred(self, localctx:Math_exprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 7)
         

    def mod_expr_sempred(self, localctx:Mod_exprContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 5)
         

    def logical_expr_sempred(self, localctx:Logical_exprContext, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 5)
         

    def relational_expr_1_sempred(self, localctx:Relational_expr_1Context, predIndex:int):
            if predIndex == 7:
                return self.precpred(self._ctx, 6)
         

    def relational_expr_2_sempred(self, localctx:Relational_expr_2Context, predIndex:int):
            if predIndex == 8:
                return self.precpred(self._ctx, 6)
         

    def string_expr_sempred(self, localctx:String_exprContext, predIndex:int):
            if predIndex == 9:
                return self.precpred(self._ctx, 5)
         




