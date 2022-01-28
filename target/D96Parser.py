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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3S")
        buf.write("\u01de\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\3\2\6\2h")
        buf.write("\n\2\r\2\16\2i\3\2\3\2\3\3\3\3\3\3\3\3\5\3r\n\3\3\3\3")
        buf.write("\3\7\3v\n\3\f\3\16\3y\13\3\3\3\3\3\3\4\3\4\5\4\177\n\4")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\5\5\u0087\n\5\3\5\3\5\3\6\3\6")
        buf.write("\3\6\7\6\u008e\n\6\f\6\16\6\u0091\13\6\3\7\3\7\3\b\3\b")
        buf.write("\3\b\5\b\u0098\n\b\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\5\n")
        buf.write("\u00a2\n\n\3\n\3\n\3\13\3\13\5\13\u00a8\n\13\3\f\3\f\3")
        buf.write("\r\3\r\3\16\3\16\3\16\5\16\u00b1\n\16\3\16\3\16\3\16\3")
        buf.write("\17\3\17\3\17\7\17\u00b9\n\17\f\17\16\17\u00bc\13\17\3")
        buf.write("\20\3\20\3\20\3\20\3\21\3\21\3\21\7\21\u00c5\n\21\f\21")
        buf.write("\16\21\u00c8\13\21\3\22\3\22\7\22\u00cc\n\22\f\22\16\22")
        buf.write("\u00cf\13\22\3\22\3\22\3\23\3\23\5\23\u00d5\n\23\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\5\24\u00dd\n\24\3\24\3\24\3")
        buf.write("\25\3\25\3\25\7\25\u00e4\n\25\f\25\16\25\u00e7\13\25\3")
        buf.write("\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\5\27\u00f2")
        buf.write("\n\27\3\30\3\30\5\30\u00f6\n\30\3\30\3\30\3\30\3\30\3")
        buf.write("\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\7\31\u0108\n\31\f\31\16\31\u010b\13\31\3\31\3\31")
        buf.write("\5\31\u010f\n\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3")
        buf.write("\32\3\32\5\32\u011a\n\32\3\32\3\32\3\32\3\33\3\33\5\33")
        buf.write("\u0121\n\33\3\33\3\33\3\34\3\34\3\34\3\35\3\35\3\35\3")
        buf.write("\36\3\36\5\36\u012d\n\36\3\36\3\36\3\37\3\37\3\37\7\37")
        buf.write("\u0134\n\37\f\37\16\37\u0137\13\37\3 \3 \3!\3!\3!\3!\3")
        buf.write("!\5!\u0140\n!\3\"\3\"\3\"\3\"\3\"\5\"\u0147\n\"\3#\3#")
        buf.write("\3#\3#\3#\5#\u014e\n#\3$\3$\3$\3$\3$\3$\7$\u0156\n$\f")
        buf.write("$\16$\u0159\13$\3%\3%\3%\3%\3%\3%\7%\u0161\n%\f%\16%\u0164")
        buf.write("\13%\3&\3&\3&\5&\u0169\n&\3\'\3\'\3\'\5\'\u016e\n\'\3")
        buf.write("(\3(\3(\3(\3(\3(\3(\3(\6(\u0178\n(\r(\16(\u0179\7(\u017c")
        buf.write("\n(\f(\16(\u017f\13(\3)\3)\3)\3)\3)\3)\3)\3)\5)\u0189")
        buf.write("\n)\3)\5)\u018c\n)\7)\u018e\n)\f)\16)\u0191\13)\3*\3*")
        buf.write("\3*\3*\3*\5*\u0198\n*\3*\5*\u019b\n*\3*\5*\u019e\n*\3")
        buf.write("+\3+\3+\3+\5+\u01a4\n+\3+\3+\3+\5+\u01a9\n+\3,\3,\3,\3")
        buf.write(",\3,\5,\u01b0\n,\3-\3-\3-\3-\3-\3-\3-\3-\5-\u01ba\n-\3")
        buf.write(".\3.\3/\3/\3/\5/\u01c1\n/\3/\3/\3\60\3\60\3\60\7\60\u01c8")
        buf.write("\n\60\f\60\16\60\u01cb\13\60\3\61\3\61\3\61\5\61\u01d0")
        buf.write("\n\61\3\61\3\61\3\62\3\62\3\62\7\62\u01d7\n\62\f\62\16")
        buf.write("\62\u01da\13\62\3\63\3\63\3\63\2\6FHNP\64\2\4\6\b\n\f")
        buf.write("\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@")
        buf.write("BDFHJLNPRTVXZ\\^`bd\2\13\4\2\26\26\35\35\3\2\13\f\3\2")
        buf.write("\6\t\5\2\26\26\36\36\63\64\3\2FG\4\2?@BE\3\2=>\3\2\67")
        buf.write("8\3\29;\2\u01e6\2g\3\2\2\2\4m\3\2\2\2\6~\3\2\2\2\b\u0080")
        buf.write("\3\2\2\2\n\u008a\3\2\2\2\f\u0092\3\2\2\2\16\u0097\3\2")
        buf.write("\2\2\20\u0099\3\2\2\2\22\u009b\3\2\2\2\24\u00a7\3\2\2")
        buf.write("\2\26\u00a9\3\2\2\2\30\u00ab\3\2\2\2\32\u00ad\3\2\2\2")
        buf.write("\34\u00b5\3\2\2\2\36\u00bd\3\2\2\2 \u00c1\3\2\2\2\"\u00c9")
        buf.write("\3\2\2\2$\u00d4\3\2\2\2&\u00d6\3\2\2\2(\u00e0\3\2\2\2")
        buf.write("*\u00e8\3\2\2\2,\u00f1\3\2\2\2.\u00f5\3\2\2\2\60\u00fb")
        buf.write("\3\2\2\2\62\u0110\3\2\2\2\64\u0120\3\2\2\2\66\u0124\3")
        buf.write("\2\2\28\u0127\3\2\2\2:\u012a\3\2\2\2<\u0130\3\2\2\2>\u0138")
        buf.write("\3\2\2\2@\u013f\3\2\2\2B\u0146\3\2\2\2D\u014d\3\2\2\2")
        buf.write("F\u014f\3\2\2\2H\u015a\3\2\2\2J\u0168\3\2\2\2L\u016d\3")
        buf.write("\2\2\2N\u016f\3\2\2\2P\u0180\3\2\2\2R\u019d\3\2\2\2T\u01a8")
        buf.write("\3\2\2\2V\u01af\3\2\2\2X\u01b9\3\2\2\2Z\u01bb\3\2\2\2")
        buf.write("\\\u01bd\3\2\2\2^\u01c4\3\2\2\2`\u01cc\3\2\2\2b\u01d3")
        buf.write("\3\2\2\2d\u01db\3\2\2\2fh\5\4\3\2gf\3\2\2\2hi\3\2\2\2")
        buf.write("ig\3\2\2\2ij\3\2\2\2jk\3\2\2\2kl\7\2\2\3l\3\3\2\2\2mn")
        buf.write("\7\5\2\2nq\t\2\2\2op\7\3\2\2pr\t\2\2\2qo\3\2\2\2qr\3\2")
        buf.write("\2\2rs\3\2\2\2sw\7M\2\2tv\5\6\4\2ut\3\2\2\2vy\3\2\2\2")
        buf.write("wu\3\2\2\2wx\3\2\2\2xz\3\2\2\2yw\3\2\2\2z{\7N\2\2{\5\3")
        buf.write("\2\2\2|\177\5\b\5\2}\177\5\32\16\2~|\3\2\2\2~}\3\2\2\2")
        buf.write("\177\7\3\2\2\2\u0080\u0081\t\3\2\2\u0081\u0082\5\n\6\2")
        buf.write("\u0082\u0083\7\3\2\2\u0083\u0086\5\16\b\2\u0084\u0085")
        buf.write("\7A\2\2\u0085\u0087\5<\37\2\u0086\u0084\3\2\2\2\u0086")
        buf.write("\u0087\3\2\2\2\u0087\u0088\3\2\2\2\u0088\u0089\7O\2\2")
        buf.write("\u0089\t\3\2\2\2\u008a\u008f\5\f\7\2\u008b\u008c\7Q\2")
        buf.write("\2\u008c\u008e\5\f\7\2\u008d\u008b\3\2\2\2\u008e\u0091")
        buf.write("\3\2\2\2\u008f\u008d\3\2\2\2\u008f\u0090\3\2\2\2\u0090")
        buf.write("\13\3\2\2\2\u0091\u008f\3\2\2\2\u0092\u0093\7\26\2\2\u0093")
        buf.write("\r\3\2\2\2\u0094\u0098\5\20\t\2\u0095\u0098\5\22\n\2\u0096")
        buf.write("\u0098\5\30\r\2\u0097\u0094\3\2\2\2\u0097\u0095\3\2\2")
        buf.write("\2\u0097\u0096\3\2\2\2\u0098\17\3\2\2\2\u0099\u009a\t")
        buf.write("\4\2\2\u009a\21\3\2\2\2\u009b\u009c\7\n\2\2\u009c\u00a1")
        buf.write("\7K\2\2\u009d\u009e\5\24\13\2\u009e\u009f\7Q\2\2\u009f")
        buf.write("\u00a0\5\26\f\2\u00a0\u00a2\3\2\2\2\u00a1\u009d\3\2\2")
        buf.write("\2\u00a1\u00a2\3\2\2\2\u00a2\u00a3\3\2\2\2\u00a3\u00a4")
        buf.write("\7L\2\2\u00a4\23\3\2\2\2\u00a5\u00a8\5\20\t\2\u00a6\u00a8")
        buf.write("\5\22\n\2\u00a7\u00a5\3\2\2\2\u00a7\u00a6\3\2\2\2\u00a8")
        buf.write("\25\3\2\2\2\u00a9\u00aa\7\27\2\2\u00aa\27\3\2\2\2\u00ab")
        buf.write("\u00ac\7\26\2\2\u00ac\31\3\2\2\2\u00ad\u00ae\t\5\2\2\u00ae")
        buf.write("\u00b0\7I\2\2\u00af\u00b1\5\34\17\2\u00b0\u00af\3\2\2")
        buf.write("\2\u00b0\u00b1\3\2\2\2\u00b1\u00b2\3\2\2\2\u00b2\u00b3")
        buf.write("\7J\2\2\u00b3\u00b4\5\"\22\2\u00b4\33\3\2\2\2\u00b5\u00ba")
        buf.write("\5\36\20\2\u00b6\u00b7\7O\2\2\u00b7\u00b9\5\36\20\2\u00b8")
        buf.write("\u00b6\3\2\2\2\u00b9\u00bc\3\2\2\2\u00ba\u00b8\3\2\2\2")
        buf.write("\u00ba\u00bb\3\2\2\2\u00bb\35\3\2\2\2\u00bc\u00ba\3\2")
        buf.write("\2\2\u00bd\u00be\5 \21\2\u00be\u00bf\7\3\2\2\u00bf\u00c0")
        buf.write("\5\16\b\2\u00c0\37\3\2\2\2\u00c1\u00c6\7\26\2\2\u00c2")
        buf.write("\u00c3\7Q\2\2\u00c3\u00c5\7\26\2\2\u00c4\u00c2\3\2\2\2")
        buf.write("\u00c5\u00c8\3\2\2\2\u00c6\u00c4\3\2\2\2\u00c6\u00c7\3")
        buf.write("\2\2\2\u00c7!\3\2\2\2\u00c8\u00c6\3\2\2\2\u00c9\u00cd")
        buf.write("\7M\2\2\u00ca\u00cc\5$\23\2\u00cb\u00ca\3\2\2\2\u00cc")
        buf.write("\u00cf\3\2\2\2\u00cd\u00cb\3\2\2\2\u00cd\u00ce\3\2\2\2")
        buf.write("\u00ce\u00d0\3\2\2\2\u00cf\u00cd\3\2\2\2\u00d0\u00d1\7")
        buf.write("N\2\2\u00d1#\3\2\2\2\u00d2\u00d5\5,\27\2\u00d3\u00d5\5")
        buf.write("&\24\2\u00d4\u00d2\3\2\2\2\u00d4\u00d3\3\2\2\2\u00d5%")
        buf.write("\3\2\2\2\u00d6\u00d7\t\3\2\2\u00d7\u00d8\5(\25\2\u00d8")
        buf.write("\u00d9\7\3\2\2\u00d9\u00dc\5\16\b\2\u00da\u00db\7A\2\2")
        buf.write("\u00db\u00dd\5<\37\2\u00dc\u00da\3\2\2\2\u00dc\u00dd\3")
        buf.write("\2\2\2\u00dd\u00de\3\2\2\2\u00de\u00df\7O\2\2\u00df\'")
        buf.write("\3\2\2\2\u00e0\u00e5\5*\26\2\u00e1\u00e2\7Q\2\2\u00e2")
        buf.write("\u00e4\5*\26\2\u00e3\u00e1\3\2\2\2\u00e4\u00e7\3\2\2\2")
        buf.write("\u00e5\u00e3\3\2\2\2\u00e5\u00e6\3\2\2\2\u00e6)\3\2\2")
        buf.write("\2\u00e7\u00e5\3\2\2\2\u00e8\u00e9\7\26\2\2\u00e9+\3\2")
        buf.write("\2\2\u00ea\u00f2\5.\30\2\u00eb\u00f2\5\60\31\2\u00ec\u00f2")
        buf.write("\5\62\32\2\u00ed\u00f2\5\66\34\2\u00ee\u00f2\58\35\2\u00ef")
        buf.write("\u00f2\5:\36\2\u00f0\u00f2\5\64\33\2\u00f1\u00ea\3\2\2")
        buf.write("\2\u00f1\u00eb\3\2\2\2\u00f1\u00ec\3\2\2\2\u00f1\u00ed")
        buf.write("\3\2\2\2\u00f1\u00ee\3\2\2\2\u00f1\u00ef\3\2\2\2\u00f1")
        buf.write("\u00f0\3\2\2\2\u00f2-\3\2\2\2\u00f3\u00f6\7\26\2\2\u00f4")
        buf.write("\u00f6\5N(\2\u00f5\u00f3\3\2\2\2\u00f5\u00f4\3\2\2\2\u00f6")
        buf.write("\u00f7\3\2\2\2\u00f7\u00f8\7A\2\2\u00f8\u00f9\5> \2\u00f9")
        buf.write("\u00fa\7O\2\2\u00fa/\3\2\2\2\u00fb\u00fc\7\r\2\2\u00fc")
        buf.write("\u00fd\7I\2\2\u00fd\u00fe\5> \2\u00fe\u00ff\7J\2\2\u00ff")
        buf.write("\u0100\5\"\22\2\u0100\u0109\3\2\2\2\u0101\u0102\7\17\2")
        buf.write("\2\u0102\u0103\7I\2\2\u0103\u0104\5> \2\u0104\u0105\7")
        buf.write("J\2\2\u0105\u0106\5\"\22\2\u0106\u0108\3\2\2\2\u0107\u0101")
        buf.write("\3\2\2\2\u0108\u010b\3\2\2\2\u0109\u0107\3\2\2\2\u0109")
        buf.write("\u010a\3\2\2\2\u010a\u010e\3\2\2\2\u010b\u0109\3\2\2\2")
        buf.write("\u010c\u010d\7\16\2\2\u010d\u010f\5\"\22\2\u010e\u010c")
        buf.write("\3\2\2\2\u010e\u010f\3\2\2\2\u010f\61\3\2\2\2\u0110\u0111")
        buf.write("\7\20\2\2\u0111\u0112\7I\2\2\u0112\u0113\7\26\2\2\u0113")
        buf.write("\u0114\7\21\2\2\u0114\u0115\5> \2\u0115\u0116\7\4\2\2")
        buf.write("\u0116\u0119\5> \2\u0117\u0118\7\22\2\2\u0118\u011a\5")
        buf.write("> \2\u0119\u0117\3\2\2\2\u0119\u011a\3\2\2\2\u011a\u011b")
        buf.write("\3\2\2\2\u011b\u011c\7J\2\2\u011c\u011d\5\"\22\2\u011d")
        buf.write("\63\3\2\2\2\u011e\u0121\5P)\2\u011f\u0121\5R*\2\u0120")
        buf.write("\u011e\3\2\2\2\u0120\u011f\3\2\2\2\u0121\u0122\3\2\2\2")
        buf.write("\u0122\u0123\7O\2\2\u0123\65\3\2\2\2\u0124\u0125\7\37")
        buf.write("\2\2\u0125\u0126\7O\2\2\u0126\67\3\2\2\2\u0127\u0128\7")
        buf.write(" \2\2\u0128\u0129\7O\2\2\u01299\3\2\2\2\u012a\u012c\7")
        buf.write("\23\2\2\u012b\u012d\5> \2\u012c\u012b\3\2\2\2\u012c\u012d")
        buf.write("\3\2\2\2\u012d\u012e\3\2\2\2\u012e\u012f\7O\2\2\u012f")
        buf.write(";\3\2\2\2\u0130\u0135\5> \2\u0131\u0132\7Q\2\2\u0132\u0134")
        buf.write("\5> \2\u0133\u0131\3\2\2\2\u0134\u0137\3\2\2\2\u0135\u0133")
        buf.write("\3\2\2\2\u0135\u0136\3\2\2\2\u0136=\3\2\2\2\u0137\u0135")
        buf.write("\3\2\2\2\u0138\u0139\5@!\2\u0139?\3\2\2\2\u013a\u013b")
        buf.write("\5B\"\2\u013b\u013c\t\6\2\2\u013c\u013d\5B\"\2\u013d\u0140")
        buf.write("\3\2\2\2\u013e\u0140\5B\"\2\u013f\u013a\3\2\2\2\u013f")
        buf.write("\u013e\3\2\2\2\u0140A\3\2\2\2\u0141\u0142\5D#\2\u0142")
        buf.write("\u0143\t\7\2\2\u0143\u0144\5D#\2\u0144\u0147\3\2\2\2\u0145")
        buf.write("\u0147\5D#\2\u0146\u0141\3\2\2\2\u0146\u0145\3\2\2\2\u0147")
        buf.write("C\3\2\2\2\u0148\u0149\5F$\2\u0149\u014a\t\b\2\2\u014a")
        buf.write("\u014b\5F$\2\u014b\u014e\3\2\2\2\u014c\u014e\5F$\2\u014d")
        buf.write("\u0148\3\2\2\2\u014d\u014c\3\2\2\2\u014eE\3\2\2\2\u014f")
        buf.write("\u0150\b$\1\2\u0150\u0151\5H%\2\u0151\u0157\3\2\2\2\u0152")
        buf.write("\u0153\f\4\2\2\u0153\u0154\t\t\2\2\u0154\u0156\5H%\2\u0155")
        buf.write("\u0152\3\2\2\2\u0156\u0159\3\2\2\2\u0157\u0155\3\2\2\2")
        buf.write("\u0157\u0158\3\2\2\2\u0158G\3\2\2\2\u0159\u0157\3\2\2")
        buf.write("\2\u015a\u015b\b%\1\2\u015b\u015c\5J&\2\u015c\u0162\3")
        buf.write("\2\2\2\u015d\u015e\f\4\2\2\u015e\u015f\t\n\2\2\u015f\u0161")
        buf.write("\5J&\2\u0160\u015d\3\2\2\2\u0161\u0164\3\2\2\2\u0162\u0160")
        buf.write("\3\2\2\2\u0162\u0163\3\2\2\2\u0163I\3\2\2\2\u0164\u0162")
        buf.write("\3\2\2\2\u0165\u0166\7<\2\2\u0166\u0169\5J&\2\u0167\u0169")
        buf.write("\5L\'\2\u0168\u0165\3\2\2\2\u0168\u0167\3\2\2\2\u0169")
        buf.write("K\3\2\2\2\u016a\u016b\78\2\2\u016b\u016e\5L\'\2\u016c")
        buf.write("\u016e\5N(\2\u016d\u016a\3\2\2\2\u016d\u016c\3\2\2\2\u016e")
        buf.write("M\3\2\2\2\u016f\u0170\b(\1\2\u0170\u0171\5P)\2\u0171\u017d")
        buf.write("\3\2\2\2\u0172\u0177\f\4\2\2\u0173\u0174\7K\2\2\u0174")
        buf.write("\u0175\5> \2\u0175\u0176\7L\2\2\u0176\u0178\3\2\2\2\u0177")
        buf.write("\u0173\3\2\2\2\u0178\u0179\3\2\2\2\u0179\u0177\3\2\2\2")
        buf.write("\u0179\u017a\3\2\2\2\u017a\u017c\3\2\2\2\u017b\u0172\3")
        buf.write("\2\2\2\u017c\u017f\3\2\2\2\u017d\u017b\3\2\2\2\u017d\u017e")
        buf.write("\3\2\2\2\u017eO\3\2\2\2\u017f\u017d\3\2\2\2\u0180\u0181")
        buf.write("\b)\1\2\u0181\u0182\5R*\2\u0182\u018f\3\2\2\2\u0183\u0184")
        buf.write("\f\4\2\2\u0184\u0185\7P\2\2\u0185\u018b\5R*\2\u0186\u0188")
        buf.write("\7I\2\2\u0187\u0189\5<\37\2\u0188\u0187\3\2\2\2\u0188")
        buf.write("\u0189\3\2\2\2\u0189\u018a\3\2\2\2\u018a\u018c\7J\2\2")
        buf.write("\u018b\u0186\3\2\2\2\u018b\u018c\3\2\2\2\u018c\u018e\3")
        buf.write("\2\2\2\u018d\u0183\3\2\2\2\u018e\u0191\3\2\2\2\u018f\u018d")
        buf.write("\3\2\2\2\u018f\u0190\3\2\2\2\u0190Q\3\2\2\2\u0191\u018f")
        buf.write("\3\2\2\2\u0192\u0193\5T+\2\u0193\u0194\7H\2\2\u0194\u019a")
        buf.write("\5T+\2\u0195\u0197\7I\2\2\u0196\u0198\5<\37\2\u0197\u0196")
        buf.write("\3\2\2\2\u0197\u0198\3\2\2\2\u0198\u0199\3\2\2\2\u0199")
        buf.write("\u019b\7J\2\2\u019a\u0195\3\2\2\2\u019a\u019b\3\2\2\2")
        buf.write("\u019b\u019e\3\2\2\2\u019c\u019e\5T+\2\u019d\u0192\3\2")
        buf.write("\2\2\u019d\u019c\3\2\2\2\u019eS\3\2\2\2\u019f\u01a0\7")
        buf.write("\24\2\2\u01a0\u01a1\5T+\2\u01a1\u01a3\7I\2\2\u01a2\u01a4")
        buf.write("\5<\37\2\u01a3\u01a2\3\2\2\2\u01a3\u01a4\3\2\2\2\u01a4")
        buf.write("\u01a5\3\2\2\2\u01a5\u01a6\7J\2\2\u01a6\u01a9\3\2\2\2")
        buf.write("\u01a7\u01a9\5V,\2\u01a8\u019f\3\2\2\2\u01a8\u01a7\3\2")
        buf.write("\2\2\u01a9U\3\2\2\2\u01aa\u01ab\7I\2\2\u01ab\u01ac\5>")
        buf.write(" \2\u01ac\u01ad\7J\2\2\u01ad\u01b0\3\2\2\2\u01ae\u01b0")
        buf.write("\5X-\2\u01af\u01aa\3\2\2\2\u01af\u01ae\3\2\2\2\u01b0W")
        buf.write("\3\2\2\2\u01b1\u01ba\7\27\2\2\u01b2\u01ba\7\30\2\2\u01b3")
        buf.write("\u01ba\7\31\2\2\u01b4\u01ba\7\32\2\2\u01b5\u01ba\5`\61")
        buf.write("\2\u01b6\u01ba\5\\/\2\u01b7\u01ba\7\26\2\2\u01b8\u01ba")
        buf.write("\5Z.\2\u01b9\u01b1\3\2\2\2\u01b9\u01b2\3\2\2\2\u01b9\u01b3")
        buf.write("\3\2\2\2\u01b9\u01b4\3\2\2\2\u01b9\u01b5\3\2\2\2\u01b9")
        buf.write("\u01b6\3\2\2\2\u01b9\u01b7\3\2\2\2\u01b9\u01b8\3\2\2\2")
        buf.write("\u01baY\3\2\2\2\u01bb\u01bc\7\62\2\2\u01bc[\3\2\2\2\u01bd")
        buf.write("\u01be\7\n\2\2\u01be\u01c0\7I\2\2\u01bf\u01c1\5^\60\2")
        buf.write("\u01c0\u01bf\3\2\2\2\u01c0\u01c1\3\2\2\2\u01c1\u01c2\3")
        buf.write("\2\2\2\u01c2\u01c3\7J\2\2\u01c3]\3\2\2\2\u01c4\u01c9\5")
        buf.write("`\61\2\u01c5\u01c6\7Q\2\2\u01c6\u01c8\5`\61\2\u01c7\u01c5")
        buf.write("\3\2\2\2\u01c8\u01cb\3\2\2\2\u01c9\u01c7\3\2\2\2\u01c9")
        buf.write("\u01ca\3\2\2\2\u01ca_\3\2\2\2\u01cb\u01c9\3\2\2\2\u01cc")
        buf.write("\u01cd\7\n\2\2\u01cd\u01cf\7I\2\2\u01ce\u01d0\5b\62\2")
        buf.write("\u01cf\u01ce\3\2\2\2\u01cf\u01d0\3\2\2\2\u01d0\u01d1\3")
        buf.write("\2\2\2\u01d1\u01d2\7J\2\2\u01d2a\3\2\2\2\u01d3\u01d8\5")
        buf.write("d\63\2\u01d4\u01d5\7Q\2\2\u01d5\u01d7\5d\63\2\u01d6\u01d4")
        buf.write("\3\2\2\2\u01d7\u01da\3\2\2\2\u01d8\u01d6\3\2\2\2\u01d8")
        buf.write("\u01d9\3\2\2\2\u01d9c\3\2\2\2\u01da\u01d8\3\2\2\2\u01db")
        buf.write("\u01dc\5> \2\u01dce\3\2\2\2\61iqw~\u0086\u008f\u0097\u00a1")
        buf.write("\u00a7\u00b0\u00ba\u00c6\u00cd\u00d4\u00dc\u00e5\u00f1")
        buf.write("\u00f5\u0109\u010e\u0119\u0120\u012c\u0135\u013f\u0146")
        buf.write("\u014d\u0157\u0162\u0168\u016d\u0179\u017d\u0188\u018b")
        buf.write("\u018f\u0197\u019a\u019d\u01a3\u01a8\u01af\u01b9\u01c0")
        buf.write("\u01c9\u01cf\u01d8")
        return buf.getvalue()


class D96Parser ( Parser ):

    grammarFileName = "D96.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':'", "'..'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'Program'", "'main'", "'Break'", 
                     "'Continue'", "'If'", "'Elseif'", "'Else'", "'Foreach'", 
                     "'True'", "'False'", "'Array'", "'In'", "'Int'", "'Float'", 
                     "'Boolean'", "'String'", "'Return'", "'Class'", "'Null'", 
                     "'Val'", "'Var'", "'Self'", "'Constructor'", "'Destructor'", 
                     "'New'", "'By'", "'+'", "'-'", "'*'", "'/'", "'%'", 
                     "'!'", "'&&'", "'||'", "'=='", "'!='", "'='", "'>'", 
                     "'<'", "'>='", "'<='", "'==.'", "'+.'", "'::'", "'('", 
                     "')'", "'['", "']'", "'{'", "'}'", "';'", "'.'", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "Class_word", 
                      "Bool_word", "Int_word", "Float_word", "Str_word", 
                      "Array_word", "Var_word", "Val_word", "If_word", "Else_word", 
                      "Elseif_word", "Foreach_word", "In_word", "By_word", 
                      "Return_word", "New_word", "BLOCKCOMMENT", "ID", "INTLIT", 
                      "FLOATLIT", "BOOLEANLIT", "STRINGLIT", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE", "PROGRAM", "MAIN", "BREAK", "CONT", 
                      "IF", "ELSEIF", "ELSE", "FOREACH", "BOOLTRUE", "BOOLFALSE", 
                      "ARRAY", "IN", "INT", "FLOAT", "BOOL", "STR", "RETURN", 
                      "CLASS", "NULL", "VAL", "VAR", "SELF", "CONS", "DEST", 
                      "KEYWORD_NEW", "BY", "ADD_OP", "SUB_OP", "MUL_OP", 
                      "DIV_OP", "MOD_OP", "NOT_OP", "AND_OP", "OR_OP", "EQUAL_OP", 
                      "DIFF_OP", "ASSIGN_OP", "GREATER_OP", "LESSER_OP", 
                      "GREATER_EQUAL_OP", "LESSER_EQUAL_OP", "STRING_COMP_OP", 
                      "STRING_CONCAT_OP", "MEMBER_ACCESS_OUT", "LP", "RP", 
                      "LSB", "RSB", "LB", "RB", "SEMI", "DOT", "COMA", "WS", 
                      "ERROR_CHAR" ]

    RULE_program = 0
    RULE_class_decl = 1
    RULE_member_lists = 2
    RULE_attributes = 3
    RULE_attribute_list = 4
    RULE_attribute_name = 5
    RULE_types = 6
    RULE_primitive_Type = 7
    RULE_array_Type = 8
    RULE_element_type = 9
    RULE_array_size = 10
    RULE_class_type = 11
    RULE_methods = 12
    RULE_paramlist = 13
    RULE_param_decl = 14
    RULE_idlist = 15
    RULE_block_stmt = 16
    RULE_block_stmt_list = 17
    RULE_var_cons_decl = 18
    RULE_var_cons_list = 19
    RULE_var_cons_name = 20
    RULE_stmt = 21
    RULE_as_stmt = 22
    RULE_if_stmt = 23
    RULE_loop_stmt = 24
    RULE_invocation_stmt = 25
    RULE_break_stmt = 26
    RULE_cont_stmt = 27
    RULE_return_stmt = 28
    RULE_expr_list = 29
    RULE_expr = 30
    RULE_string_expr = 31
    RULE_relational_expr = 32
    RULE_logical_expr = 33
    RULE_adding_expr = 34
    RULE_multiplying_expr = 35
    RULE_logical_not_expr = 36
    RULE_sign_expr = 37
    RULE_index_expr = 38
    RULE_member_access_in = 39
    RULE_member_access_out = 40
    RULE_class_expr = 41
    RULE_piority_exp = 42
    RULE_operands = 43
    RULE_self_word = 44
    RULE_multi_ArrayLIT = 45
    RULE_array_list = 46
    RULE_arrayLIT = 47
    RULE_element_list = 48
    RULE_elements = 49

    ruleNames =  [ "program", "class_decl", "member_lists", "attributes", 
                   "attribute_list", "attribute_name", "types", "primitive_Type", 
                   "array_Type", "element_type", "array_size", "class_type", 
                   "methods", "paramlist", "param_decl", "idlist", "block_stmt", 
                   "block_stmt_list", "var_cons_decl", "var_cons_list", 
                   "var_cons_name", "stmt", "as_stmt", "if_stmt", "loop_stmt", 
                   "invocation_stmt", "break_stmt", "cont_stmt", "return_stmt", 
                   "expr_list", "expr", "string_expr", "relational_expr", 
                   "logical_expr", "adding_expr", "multiplying_expr", "logical_not_expr", 
                   "sign_expr", "index_expr", "member_access_in", "member_access_out", 
                   "class_expr", "piority_exp", "operands", "self_word", 
                   "multi_ArrayLIT", "array_list", "arrayLIT", "element_list", 
                   "elements" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    Class_word=3
    Bool_word=4
    Int_word=5
    Float_word=6
    Str_word=7
    Array_word=8
    Var_word=9
    Val_word=10
    If_word=11
    Else_word=12
    Elseif_word=13
    Foreach_word=14
    In_word=15
    By_word=16
    Return_word=17
    New_word=18
    BLOCKCOMMENT=19
    ID=20
    INTLIT=21
    FLOATLIT=22
    BOOLEANLIT=23
    STRINGLIT=24
    UNCLOSE_STRING=25
    ILLEGAL_ESCAPE=26
    PROGRAM=27
    MAIN=28
    BREAK=29
    CONT=30
    IF=31
    ELSEIF=32
    ELSE=33
    FOREACH=34
    BOOLTRUE=35
    BOOLFALSE=36
    ARRAY=37
    IN=38
    INT=39
    FLOAT=40
    BOOL=41
    STR=42
    RETURN=43
    CLASS=44
    NULL=45
    VAL=46
    VAR=47
    SELF=48
    CONS=49
    DEST=50
    KEYWORD_NEW=51
    BY=52
    ADD_OP=53
    SUB_OP=54
    MUL_OP=55
    DIV_OP=56
    MOD_OP=57
    NOT_OP=58
    AND_OP=59
    OR_OP=60
    EQUAL_OP=61
    DIFF_OP=62
    ASSIGN_OP=63
    GREATER_OP=64
    LESSER_OP=65
    GREATER_EQUAL_OP=66
    LESSER_EQUAL_OP=67
    STRING_COMP_OP=68
    STRING_CONCAT_OP=69
    MEMBER_ACCESS_OUT=70
    LP=71
    RP=72
    LSB=73
    RSB=74
    LB=75
    RB=76
    SEMI=77
    DOT=78
    COMA=79
    WS=80
    ERROR_CHAR=81

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

        def EOF(self):
            return self.getToken(D96Parser.EOF, 0)

        def class_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Class_declContext)
            else:
                return self.getTypedRuleContext(D96Parser.Class_declContext,i)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 100
                self.class_decl()
                self.state = 103 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==D96Parser.Class_word):
                    break

            self.state = 105
            self.match(D96Parser.EOF)
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

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ID)
            else:
                return self.getToken(D96Parser.ID, i)

        def PROGRAM(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.PROGRAM)
            else:
                return self.getToken(D96Parser.PROGRAM, i)

        def member_lists(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Member_listsContext)
            else:
                return self.getTypedRuleContext(D96Parser.Member_listsContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_class_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_decl" ):
                return visitor.visitClass_decl(self)
            else:
                return visitor.visitChildren(self)




    def class_decl(self):

        localctx = D96Parser.Class_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_class_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.match(D96Parser.Class_word)
            self.state = 108
            _la = self._input.LA(1)
            if not(_la==D96Parser.ID or _la==D96Parser.PROGRAM):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 111
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.T__0:
                self.state = 109
                self.match(D96Parser.T__0)
                self.state = 110
                _la = self._input.LA(1)
                if not(_la==D96Parser.ID or _la==D96Parser.PROGRAM):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 113
            self.match(D96Parser.LB)
            self.state = 117
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.Var_word) | (1 << D96Parser.Val_word) | (1 << D96Parser.ID) | (1 << D96Parser.MAIN) | (1 << D96Parser.CONS) | (1 << D96Parser.DEST))) != 0):
                self.state = 114
                self.member_lists()
                self.state = 119
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 120
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

        def attributes(self):
            return self.getTypedRuleContext(D96Parser.AttributesContext,0)


        def methods(self):
            return self.getTypedRuleContext(D96Parser.MethodsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_member_lists

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMember_lists" ):
                return visitor.visitMember_lists(self)
            else:
                return visitor.visitChildren(self)




    def member_lists(self):

        localctx = D96Parser.Member_listsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_member_lists)
        try:
            self.state = 124
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.Var_word, D96Parser.Val_word]:
                self.enterOuterAlt(localctx, 1)
                self.state = 122
                self.attributes()
                pass
            elif token in [D96Parser.ID, D96Parser.MAIN, D96Parser.CONS, D96Parser.DEST]:
                self.enterOuterAlt(localctx, 2)
                self.state = 123
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

        def Var_word(self):
            return self.getToken(D96Parser.Var_word, 0)

        def Val_word(self):
            return self.getToken(D96Parser.Val_word, 0)

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
        self.enterRule(localctx, 6, self.RULE_attributes)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            _la = self._input.LA(1)
            if not(_la==D96Parser.Var_word or _la==D96Parser.Val_word):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 127
            self.attribute_list()
            self.state = 128
            self.match(D96Parser.T__0)
            self.state = 129
            self.types()
            self.state = 132
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ASSIGN_OP:
                self.state = 130
                self.match(D96Parser.ASSIGN_OP)
                self.state = 131
                self.expr_list()


            self.state = 134
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

        def attribute_name(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Attribute_nameContext)
            else:
                return self.getTypedRuleContext(D96Parser.Attribute_nameContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMA)
            else:
                return self.getToken(D96Parser.COMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_attribute_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute_list" ):
                return visitor.visitAttribute_list(self)
            else:
                return visitor.visitChildren(self)




    def attribute_list(self):

        localctx = D96Parser.Attribute_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_attribute_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.attribute_name()
            self.state = 141
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMA:
                self.state = 137
                self.match(D96Parser.COMA)
                self.state = 138
                self.attribute_name()
                self.state = 143
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self.enterRule(localctx, 10, self.RULE_attribute_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
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
        self.enterRule(localctx, 12, self.RULE_types)
        try:
            self.state = 149
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.Bool_word, D96Parser.Int_word, D96Parser.Float_word, D96Parser.Str_word]:
                self.enterOuterAlt(localctx, 1)
                self.state = 146
                self.primitive_Type()
                pass
            elif token in [D96Parser.Array_word]:
                self.enterOuterAlt(localctx, 2)
                self.state = 147
                self.array_Type()
                pass
            elif token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 148
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

        def Bool_word(self):
            return self.getToken(D96Parser.Bool_word, 0)

        def Int_word(self):
            return self.getToken(D96Parser.Int_word, 0)

        def Float_word(self):
            return self.getToken(D96Parser.Float_word, 0)

        def Str_word(self):
            return self.getToken(D96Parser.Str_word, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_primitive_Type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive_Type" ):
                return visitor.visitPrimitive_Type(self)
            else:
                return visitor.visitChildren(self)




    def primitive_Type(self):

        localctx = D96Parser.Primitive_TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_primitive_Type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.Bool_word) | (1 << D96Parser.Int_word) | (1 << D96Parser.Float_word) | (1 << D96Parser.Str_word))) != 0)):
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

        def Array_word(self):
            return self.getToken(D96Parser.Array_word, 0)

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
        self.enterRule(localctx, 16, self.RULE_array_Type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.match(D96Parser.Array_word)
            self.state = 154
            self.match(D96Parser.LSB)
            self.state = 159
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.Bool_word) | (1 << D96Parser.Int_word) | (1 << D96Parser.Float_word) | (1 << D96Parser.Str_word) | (1 << D96Parser.Array_word))) != 0):
                self.state = 155
                self.element_type()
                self.state = 156
                self.match(D96Parser.COMA)
                self.state = 157
                self.array_size()


            self.state = 161
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
        self.enterRule(localctx, 18, self.RULE_element_type)
        try:
            self.state = 165
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.Bool_word, D96Parser.Int_word, D96Parser.Float_word, D96Parser.Str_word]:
                self.enterOuterAlt(localctx, 1)
                self.state = 163
                self.primitive_Type()
                pass
            elif token in [D96Parser.Array_word]:
                self.enterOuterAlt(localctx, 2)
                self.state = 164
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
        self.enterRule(localctx, 20, self.RULE_array_size)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
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
        self.enterRule(localctx, 22, self.RULE_class_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
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

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def MAIN(self):
            return self.getToken(D96Parser.MAIN, 0)

        def CONS(self):
            return self.getToken(D96Parser.CONS, 0)

        def DEST(self):
            return self.getToken(D96Parser.DEST, 0)

        def paramlist(self):
            return self.getTypedRuleContext(D96Parser.ParamlistContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_methods

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethods" ):
                return visitor.visitMethods(self)
            else:
                return visitor.visitChildren(self)




    def methods(self):

        localctx = D96Parser.MethodsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_methods)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.ID) | (1 << D96Parser.MAIN) | (1 << D96Parser.CONS) | (1 << D96Parser.DEST))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 172
            self.match(D96Parser.LP)
            self.state = 174
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ID:
                self.state = 173
                self.paramlist()


            self.state = 176
            self.match(D96Parser.RP)
            self.state = 177
            self.block_stmt()
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

        def param_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Param_declContext)
            else:
                return self.getTypedRuleContext(D96Parser.Param_declContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.SEMI)
            else:
                return self.getToken(D96Parser.SEMI, i)

        def getRuleIndex(self):
            return D96Parser.RULE_paramlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamlist" ):
                return visitor.visitParamlist(self)
            else:
                return visitor.visitChildren(self)




    def paramlist(self):

        localctx = D96Parser.ParamlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_paramlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self.param_decl()
            self.state = 184
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.SEMI:
                self.state = 180
                self.match(D96Parser.SEMI)
                self.state = 181
                self.param_decl()
                self.state = 186
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self.enterRule(localctx, 28, self.RULE_param_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self.idlist()
            self.state = 188
            self.match(D96Parser.T__0)
            self.state = 189
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

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ID)
            else:
                return self.getToken(D96Parser.ID, i)

        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMA)
            else:
                return self.getToken(D96Parser.COMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_idlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdlist" ):
                return visitor.visitIdlist(self)
            else:
                return visitor.visitChildren(self)




    def idlist(self):

        localctx = D96Parser.IdlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_idlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self.match(D96Parser.ID)
            self.state = 196
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMA:
                self.state = 192
                self.match(D96Parser.COMA)
                self.state = 193
                self.match(D96Parser.ID)
                self.state = 198
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def block_stmt_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Block_stmt_listContext)
            else:
                return self.getTypedRuleContext(D96Parser.Block_stmt_listContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_block_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_stmt" ):
                return visitor.visitBlock_stmt(self)
            else:
                return visitor.visitChildren(self)




    def block_stmt(self):

        localctx = D96Parser.Block_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_block_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.match(D96Parser.LB)
            self.state = 203
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 8)) & ~0x3f) == 0 and ((1 << (_la - 8)) & ((1 << (D96Parser.Array_word - 8)) | (1 << (D96Parser.Var_word - 8)) | (1 << (D96Parser.Val_word - 8)) | (1 << (D96Parser.If_word - 8)) | (1 << (D96Parser.Foreach_word - 8)) | (1 << (D96Parser.Return_word - 8)) | (1 << (D96Parser.New_word - 8)) | (1 << (D96Parser.ID - 8)) | (1 << (D96Parser.INTLIT - 8)) | (1 << (D96Parser.FLOATLIT - 8)) | (1 << (D96Parser.BOOLEANLIT - 8)) | (1 << (D96Parser.STRINGLIT - 8)) | (1 << (D96Parser.BREAK - 8)) | (1 << (D96Parser.CONT - 8)) | (1 << (D96Parser.SELF - 8)) | (1 << (D96Parser.LP - 8)))) != 0):
                self.state = 200
                self.block_stmt_list()
                self.state = 205
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 206
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


        def var_cons_decl(self):
            return self.getTypedRuleContext(D96Parser.Var_cons_declContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_block_stmt_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_stmt_list" ):
                return visitor.visitBlock_stmt_list(self)
            else:
                return visitor.visitChildren(self)




    def block_stmt_list(self):

        localctx = D96Parser.Block_stmt_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_block_stmt_list)
        try:
            self.state = 210
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.Array_word, D96Parser.If_word, D96Parser.Foreach_word, D96Parser.Return_word, D96Parser.New_word, D96Parser.ID, D96Parser.INTLIT, D96Parser.FLOATLIT, D96Parser.BOOLEANLIT, D96Parser.STRINGLIT, D96Parser.BREAK, D96Parser.CONT, D96Parser.SELF, D96Parser.LP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 208
                self.stmt()
                pass
            elif token in [D96Parser.Var_word, D96Parser.Val_word]:
                self.enterOuterAlt(localctx, 2)
                self.state = 209
                self.var_cons_decl()
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

        def Var_word(self):
            return self.getToken(D96Parser.Var_word, 0)

        def Val_word(self):
            return self.getToken(D96Parser.Val_word, 0)

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
        self.enterRule(localctx, 36, self.RULE_var_cons_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            _la = self._input.LA(1)
            if not(_la==D96Parser.Var_word or _la==D96Parser.Val_word):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 213
            self.var_cons_list()
            self.state = 214
            self.match(D96Parser.T__0)
            self.state = 215
            self.types()
            self.state = 218
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ASSIGN_OP:
                self.state = 216
                self.match(D96Parser.ASSIGN_OP)
                self.state = 217
                self.expr_list()


            self.state = 220
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

        def var_cons_name(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Var_cons_nameContext)
            else:
                return self.getTypedRuleContext(D96Parser.Var_cons_nameContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMA)
            else:
                return self.getToken(D96Parser.COMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_var_cons_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_cons_list" ):
                return visitor.visitVar_cons_list(self)
            else:
                return visitor.visitChildren(self)




    def var_cons_list(self):

        localctx = D96Parser.Var_cons_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_var_cons_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self.var_cons_name()
            self.state = 227
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMA:
                self.state = 223
                self.match(D96Parser.COMA)
                self.state = 224
                self.var_cons_name()
                self.state = 229
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self.enterRule(localctx, 40, self.RULE_var_cons_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.match(D96Parser.ID)
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

        def as_stmt(self):
            return self.getTypedRuleContext(D96Parser.As_stmtContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(D96Parser.If_stmtContext,0)


        def loop_stmt(self):
            return self.getTypedRuleContext(D96Parser.Loop_stmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(D96Parser.Break_stmtContext,0)


        def cont_stmt(self):
            return self.getTypedRuleContext(D96Parser.Cont_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(D96Parser.Return_stmtContext,0)


        def invocation_stmt(self):
            return self.getTypedRuleContext(D96Parser.Invocation_stmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = D96Parser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_stmt)
        try:
            self.state = 239
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 232
                self.as_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 233
                self.if_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 234
                self.loop_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 235
                self.break_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 236
                self.cont_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 237
                self.return_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 238
                self.invocation_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class As_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN_OP(self):
            return self.getToken(D96Parser.ASSIGN_OP, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def index_expr(self):
            return self.getTypedRuleContext(D96Parser.Index_exprContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_as_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAs_stmt" ):
                return visitor.visitAs_stmt(self)
            else:
                return visitor.visitChildren(self)




    def as_stmt(self):

        localctx = D96Parser.As_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_as_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 241
                self.match(D96Parser.ID)
                pass

            elif la_ == 2:
                self.state = 242
                self.index_expr(0)
                pass


            self.state = 245
            self.match(D96Parser.ASSIGN_OP)
            self.state = 246
            self.expr()
            self.state = 247
            self.match(D96Parser.SEMI)
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

        def If_word(self):
            return self.getToken(D96Parser.If_word, 0)

        def LP(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.LP)
            else:
                return self.getToken(D96Parser.LP, i)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExprContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExprContext,i)


        def RP(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.RP)
            else:
                return self.getToken(D96Parser.RP, i)

        def block_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Block_stmtContext)
            else:
                return self.getTypedRuleContext(D96Parser.Block_stmtContext,i)


        def Elseif_word(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.Elseif_word)
            else:
                return self.getToken(D96Parser.Elseif_word, i)

        def Else_word(self):
            return self.getToken(D96Parser.Else_word, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_if_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = D96Parser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 249
            self.match(D96Parser.If_word)
            self.state = 250
            self.match(D96Parser.LP)
            self.state = 251
            self.expr()
            self.state = 252
            self.match(D96Parser.RP)
            self.state = 253
            self.block_stmt()
            self.state = 263
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.Elseif_word:
                self.state = 255
                self.match(D96Parser.Elseif_word)
                self.state = 256
                self.match(D96Parser.LP)
                self.state = 257
                self.expr()
                self.state = 258
                self.match(D96Parser.RP)
                self.state = 259
                self.block_stmt()
                self.state = 265
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 268
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.Else_word:
                self.state = 266
                self.match(D96Parser.Else_word)
                self.state = 267
                self.block_stmt()


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

        def Foreach_word(self):
            return self.getToken(D96Parser.Foreach_word, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def In_word(self):
            return self.getToken(D96Parser.In_word, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExprContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExprContext,i)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def By_word(self):
            return self.getToken(D96Parser.By_word, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_loop_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoop_stmt" ):
                return visitor.visitLoop_stmt(self)
            else:
                return visitor.visitChildren(self)




    def loop_stmt(self):

        localctx = D96Parser.Loop_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_loop_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
            self.match(D96Parser.Foreach_word)
            self.state = 271
            self.match(D96Parser.LP)
            self.state = 272
            self.match(D96Parser.ID)
            self.state = 273
            self.match(D96Parser.In_word)
            self.state = 274
            self.expr()
            self.state = 275
            self.match(D96Parser.T__1)
            self.state = 276
            self.expr()
            self.state = 279
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.By_word:
                self.state = 277
                self.match(D96Parser.By_word)
                self.state = 278
                self.expr()


            self.state = 281
            self.match(D96Parser.RP)
            self.state = 282
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Invocation_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def member_access_in(self):
            return self.getTypedRuleContext(D96Parser.Member_access_inContext,0)


        def member_access_out(self):
            return self.getTypedRuleContext(D96Parser.Member_access_outContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_invocation_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInvocation_stmt" ):
                return visitor.visitInvocation_stmt(self)
            else:
                return visitor.visitChildren(self)




    def invocation_stmt(self):

        localctx = D96Parser.Invocation_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_invocation_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 284
                self.member_access_in(0)
                pass

            elif la_ == 2:
                self.state = 285
                self.member_access_out()
                pass


            self.state = 288
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(D96Parser.BREAK, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_break_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stmt" ):
                return visitor.visitBreak_stmt(self)
            else:
                return visitor.visitChildren(self)




    def break_stmt(self):

        localctx = D96Parser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 290
            self.match(D96Parser.BREAK)
            self.state = 291
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Cont_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONT(self):
            return self.getToken(D96Parser.CONT, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_cont_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCont_stmt" ):
                return visitor.visitCont_stmt(self)
            else:
                return visitor.visitChildren(self)




    def cont_stmt(self):

        localctx = D96Parser.Cont_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_cont_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 293
            self.match(D96Parser.CONT)
            self.state = 294
            self.match(D96Parser.SEMI)
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

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

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
        self.enterRule(localctx, 56, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 296
            self.match(D96Parser.Return_word)
            self.state = 298
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 8)) & ~0x3f) == 0 and ((1 << (_la - 8)) & ((1 << (D96Parser.Array_word - 8)) | (1 << (D96Parser.New_word - 8)) | (1 << (D96Parser.ID - 8)) | (1 << (D96Parser.INTLIT - 8)) | (1 << (D96Parser.FLOATLIT - 8)) | (1 << (D96Parser.BOOLEANLIT - 8)) | (1 << (D96Parser.STRINGLIT - 8)) | (1 << (D96Parser.SELF - 8)) | (1 << (D96Parser.SUB_OP - 8)) | (1 << (D96Parser.NOT_OP - 8)) | (1 << (D96Parser.LP - 8)))) != 0):
                self.state = 297
                self.expr()


            self.state = 300
            self.match(D96Parser.SEMI)
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

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExprContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExprContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMA)
            else:
                return self.getToken(D96Parser.COMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_expr_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_list" ):
                return visitor.visitExpr_list(self)
            else:
                return visitor.visitChildren(self)




    def expr_list(self):

        localctx = D96Parser.Expr_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_expr_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 302
            self.expr()
            self.state = 307
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMA:
                self.state = 303
                self.match(D96Parser.COMA)
                self.state = 304
                self.expr()
                self.state = 309
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self.enterRule(localctx, 60, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 310
            self.string_expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class String_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relational_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Relational_exprContext)
            else:
                return self.getTypedRuleContext(D96Parser.Relational_exprContext,i)


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




    def string_expr(self):

        localctx = D96Parser.String_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_string_expr)
        self._la = 0 # Token type
        try:
            self.state = 317
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 312
                self.relational_expr()
                self.state = 313
                _la = self._input.LA(1)
                if not(_la==D96Parser.STRING_COMP_OP or _la==D96Parser.STRING_CONCAT_OP):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 314
                self.relational_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 316
                self.relational_expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Relational_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logical_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Logical_exprContext)
            else:
                return self.getTypedRuleContext(D96Parser.Logical_exprContext,i)


        def EQUAL_OP(self):
            return self.getToken(D96Parser.EQUAL_OP, 0)

        def DIFF_OP(self):
            return self.getToken(D96Parser.DIFF_OP, 0)

        def GREATER_OP(self):
            return self.getToken(D96Parser.GREATER_OP, 0)

        def LESSER_OP(self):
            return self.getToken(D96Parser.LESSER_OP, 0)

        def GREATER_EQUAL_OP(self):
            return self.getToken(D96Parser.GREATER_EQUAL_OP, 0)

        def LESSER_EQUAL_OP(self):
            return self.getToken(D96Parser.LESSER_EQUAL_OP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_relational_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelational_expr" ):
                return visitor.visitRelational_expr(self)
            else:
                return visitor.visitChildren(self)




    def relational_expr(self):

        localctx = D96Parser.Relational_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_relational_expr)
        self._la = 0 # Token type
        try:
            self.state = 324
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 319
                self.logical_expr()
                self.state = 320
                _la = self._input.LA(1)
                if not(((((_la - 61)) & ~0x3f) == 0 and ((1 << (_la - 61)) & ((1 << (D96Parser.EQUAL_OP - 61)) | (1 << (D96Parser.DIFF_OP - 61)) | (1 << (D96Parser.GREATER_OP - 61)) | (1 << (D96Parser.LESSER_OP - 61)) | (1 << (D96Parser.GREATER_EQUAL_OP - 61)) | (1 << (D96Parser.LESSER_EQUAL_OP - 61)))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 321
                self.logical_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 323
                self.logical_expr()
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

        def adding_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Adding_exprContext)
            else:
                return self.getTypedRuleContext(D96Parser.Adding_exprContext,i)


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




    def logical_expr(self):

        localctx = D96Parser.Logical_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_logical_expr)
        self._la = 0 # Token type
        try:
            self.state = 331
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 326
                self.adding_expr(0)
                self.state = 327
                _la = self._input.LA(1)
                if not(_la==D96Parser.AND_OP or _la==D96Parser.OR_OP):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 328
                self.adding_expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 330
                self.adding_expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Adding_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplying_expr(self):
            return self.getTypedRuleContext(D96Parser.Multiplying_exprContext,0)


        def adding_expr(self):
            return self.getTypedRuleContext(D96Parser.Adding_exprContext,0)


        def ADD_OP(self):
            return self.getToken(D96Parser.ADD_OP, 0)

        def SUB_OP(self):
            return self.getToken(D96Parser.SUB_OP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_adding_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdding_expr" ):
                return visitor.visitAdding_expr(self)
            else:
                return visitor.visitChildren(self)



    def adding_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Adding_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 68
        self.enterRecursionRule(localctx, 68, self.RULE_adding_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 334
            self.multiplying_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 341
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Adding_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_adding_expr)
                    self.state = 336
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 337
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.ADD_OP or _la==D96Parser.SUB_OP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 338
                    self.multiplying_expr(0) 
                self.state = 343
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Multiplying_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logical_not_expr(self):
            return self.getTypedRuleContext(D96Parser.Logical_not_exprContext,0)


        def multiplying_expr(self):
            return self.getTypedRuleContext(D96Parser.Multiplying_exprContext,0)


        def MUL_OP(self):
            return self.getToken(D96Parser.MUL_OP, 0)

        def DIV_OP(self):
            return self.getToken(D96Parser.DIV_OP, 0)

        def MOD_OP(self):
            return self.getToken(D96Parser.MOD_OP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_multiplying_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplying_expr" ):
                return visitor.visitMultiplying_expr(self)
            else:
                return visitor.visitChildren(self)



    def multiplying_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Multiplying_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 70
        self.enterRecursionRule(localctx, 70, self.RULE_multiplying_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 345
            self.logical_not_expr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 352
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Multiplying_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplying_expr)
                    self.state = 347
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 348
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.MUL_OP) | (1 << D96Parser.DIV_OP) | (1 << D96Parser.MOD_OP))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 349
                    self.logical_not_expr() 
                self.state = 354
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


        def sign_expr(self):
            return self.getTypedRuleContext(D96Parser.Sign_exprContext,0)


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
            self.state = 358
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NOT_OP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 355
                self.match(D96Parser.NOT_OP)
                self.state = 356
                self.logical_not_expr()
                pass
            elif token in [D96Parser.Array_word, D96Parser.New_word, D96Parser.ID, D96Parser.INTLIT, D96Parser.FLOATLIT, D96Parser.BOOLEANLIT, D96Parser.STRINGLIT, D96Parser.SELF, D96Parser.SUB_OP, D96Parser.LP]:
                self.enterOuterAlt(localctx, 2)
                self.state = 357
                self.sign_expr()
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


    class Sign_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUB_OP(self):
            return self.getToken(D96Parser.SUB_OP, 0)

        def sign_expr(self):
            return self.getTypedRuleContext(D96Parser.Sign_exprContext,0)


        def index_expr(self):
            return self.getTypedRuleContext(D96Parser.Index_exprContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_sign_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSign_expr" ):
                return visitor.visitSign_expr(self)
            else:
                return visitor.visitChildren(self)




    def sign_expr(self):

        localctx = D96Parser.Sign_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_sign_expr)
        try:
            self.state = 363
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.SUB_OP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 360
                self.match(D96Parser.SUB_OP)
                self.state = 361
                self.sign_expr()
                pass
            elif token in [D96Parser.Array_word, D96Parser.New_word, D96Parser.ID, D96Parser.INTLIT, D96Parser.FLOATLIT, D96Parser.BOOLEANLIT, D96Parser.STRINGLIT, D96Parser.SELF, D96Parser.LP]:
                self.enterOuterAlt(localctx, 2)
                self.state = 362
                self.index_expr(0)
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


    class Index_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def member_access_in(self):
            return self.getTypedRuleContext(D96Parser.Member_access_inContext,0)


        def index_expr(self):
            return self.getTypedRuleContext(D96Parser.Index_exprContext,0)


        def LSB(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.LSB)
            else:
                return self.getToken(D96Parser.LSB, i)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExprContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExprContext,i)


        def RSB(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.RSB)
            else:
                return self.getToken(D96Parser.RSB, i)

        def getRuleIndex(self):
            return D96Parser.RULE_index_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_expr" ):
                return visitor.visitIndex_expr(self)
            else:
                return visitor.visitChildren(self)



    def index_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Index_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 76
        self.enterRecursionRule(localctx, 76, self.RULE_index_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 366
            self.member_access_in(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 379
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Index_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_index_expr)
                    self.state = 368
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 373 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 369
                            self.match(D96Parser.LSB)
                            self.state = 370
                            self.expr()
                            self.state = 371
                            self.match(D96Parser.RSB)

                        else:
                            raise NoViableAltException(self)
                        self.state = 375 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
             
                self.state = 381
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Member_access_inContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def member_access_out(self):
            return self.getTypedRuleContext(D96Parser.Member_access_outContext,0)


        def member_access_in(self):
            return self.getTypedRuleContext(D96Parser.Member_access_inContext,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def expr_list(self):
            return self.getTypedRuleContext(D96Parser.Expr_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_member_access_in

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMember_access_in" ):
                return visitor.visitMember_access_in(self)
            else:
                return visitor.visitChildren(self)



    def member_access_in(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Member_access_inContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 78
        self.enterRecursionRule(localctx, 78, self.RULE_member_access_in, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 383
            self.member_access_out()
            self._ctx.stop = self._input.LT(-1)
            self.state = 397
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Member_access_inContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_member_access_in)
                    self.state = 385
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 386
                    self.match(D96Parser.DOT)
                    self.state = 387
                    self.member_access_out()
                    self.state = 393
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
                    if la_ == 1:
                        self.state = 388
                        self.match(D96Parser.LP)
                        self.state = 390
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if ((((_la - 8)) & ~0x3f) == 0 and ((1 << (_la - 8)) & ((1 << (D96Parser.Array_word - 8)) | (1 << (D96Parser.New_word - 8)) | (1 << (D96Parser.ID - 8)) | (1 << (D96Parser.INTLIT - 8)) | (1 << (D96Parser.FLOATLIT - 8)) | (1 << (D96Parser.BOOLEANLIT - 8)) | (1 << (D96Parser.STRINGLIT - 8)) | (1 << (D96Parser.SELF - 8)) | (1 << (D96Parser.SUB_OP - 8)) | (1 << (D96Parser.NOT_OP - 8)) | (1 << (D96Parser.LP - 8)))) != 0):
                            self.state = 389
                            self.expr_list()


                        self.state = 392
                        self.match(D96Parser.RP)

             
                self.state = 399
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Member_access_outContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def class_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Class_exprContext)
            else:
                return self.getTypedRuleContext(D96Parser.Class_exprContext,i)


        def MEMBER_ACCESS_OUT(self):
            return self.getToken(D96Parser.MEMBER_ACCESS_OUT, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def expr_list(self):
            return self.getTypedRuleContext(D96Parser.Expr_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_member_access_out

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMember_access_out" ):
                return visitor.visitMember_access_out(self)
            else:
                return visitor.visitChildren(self)




    def member_access_out(self):

        localctx = D96Parser.Member_access_outContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_member_access_out)
        self._la = 0 # Token type
        try:
            self.state = 411
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 400
                self.class_expr()
                self.state = 401
                self.match(D96Parser.MEMBER_ACCESS_OUT)
                self.state = 402
                self.class_expr()
                self.state = 408
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
                if la_ == 1:
                    self.state = 403
                    self.match(D96Parser.LP)
                    self.state = 405
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if ((((_la - 8)) & ~0x3f) == 0 and ((1 << (_la - 8)) & ((1 << (D96Parser.Array_word - 8)) | (1 << (D96Parser.New_word - 8)) | (1 << (D96Parser.ID - 8)) | (1 << (D96Parser.INTLIT - 8)) | (1 << (D96Parser.FLOATLIT - 8)) | (1 << (D96Parser.BOOLEANLIT - 8)) | (1 << (D96Parser.STRINGLIT - 8)) | (1 << (D96Parser.SELF - 8)) | (1 << (D96Parser.SUB_OP - 8)) | (1 << (D96Parser.NOT_OP - 8)) | (1 << (D96Parser.LP - 8)))) != 0):
                        self.state = 404
                        self.expr_list()


                    self.state = 407
                    self.match(D96Parser.RP)


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 410
                self.class_expr()
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

        def New_word(self):
            return self.getToken(D96Parser.New_word, 0)

        def class_expr(self):
            return self.getTypedRuleContext(D96Parser.Class_exprContext,0)


        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def expr_list(self):
            return self.getTypedRuleContext(D96Parser.Expr_listContext,0)


        def piority_exp(self):
            return self.getTypedRuleContext(D96Parser.Piority_expContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_class_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_expr" ):
                return visitor.visitClass_expr(self)
            else:
                return visitor.visitChildren(self)




    def class_expr(self):

        localctx = D96Parser.Class_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_class_expr)
        self._la = 0 # Token type
        try:
            self.state = 422
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.New_word]:
                self.enterOuterAlt(localctx, 1)
                self.state = 413
                self.match(D96Parser.New_word)
                self.state = 414
                self.class_expr()
                self.state = 415
                self.match(D96Parser.LP)
                self.state = 417
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((((_la - 8)) & ~0x3f) == 0 and ((1 << (_la - 8)) & ((1 << (D96Parser.Array_word - 8)) | (1 << (D96Parser.New_word - 8)) | (1 << (D96Parser.ID - 8)) | (1 << (D96Parser.INTLIT - 8)) | (1 << (D96Parser.FLOATLIT - 8)) | (1 << (D96Parser.BOOLEANLIT - 8)) | (1 << (D96Parser.STRINGLIT - 8)) | (1 << (D96Parser.SELF - 8)) | (1 << (D96Parser.SUB_OP - 8)) | (1 << (D96Parser.NOT_OP - 8)) | (1 << (D96Parser.LP - 8)))) != 0):
                    self.state = 416
                    self.expr_list()


                self.state = 419
                self.match(D96Parser.RP)
                pass
            elif token in [D96Parser.Array_word, D96Parser.ID, D96Parser.INTLIT, D96Parser.FLOATLIT, D96Parser.BOOLEANLIT, D96Parser.STRINGLIT, D96Parser.SELF, D96Parser.LP]:
                self.enterOuterAlt(localctx, 2)
                self.state = 421
                self.piority_exp()
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


    class Piority_expContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def operands(self):
            return self.getTypedRuleContext(D96Parser.OperandsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_piority_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPiority_exp" ):
                return visitor.visitPiority_exp(self)
            else:
                return visitor.visitChildren(self)




    def piority_exp(self):

        localctx = D96Parser.Piority_expContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_piority_exp)
        try:
            self.state = 429
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.LP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 424
                self.match(D96Parser.LP)
                self.state = 425
                self.expr()
                self.state = 426
                self.match(D96Parser.RP)
                pass
            elif token in [D96Parser.Array_word, D96Parser.ID, D96Parser.INTLIT, D96Parser.FLOATLIT, D96Parser.BOOLEANLIT, D96Parser.STRINGLIT, D96Parser.SELF]:
                self.enterOuterAlt(localctx, 2)
                self.state = 428
                self.operands()
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


    class OperandsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(D96Parser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(D96Parser.FLOATLIT, 0)

        def BOOLEANLIT(self):
            return self.getToken(D96Parser.BOOLEANLIT, 0)

        def STRINGLIT(self):
            return self.getToken(D96Parser.STRINGLIT, 0)

        def arrayLIT(self):
            return self.getTypedRuleContext(D96Parser.ArrayLITContext,0)


        def multi_ArrayLIT(self):
            return self.getTypedRuleContext(D96Parser.Multi_ArrayLITContext,0)


        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def self_word(self):
            return self.getTypedRuleContext(D96Parser.Self_wordContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_operands

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperands" ):
                return visitor.visitOperands(self)
            else:
                return visitor.visitChildren(self)




    def operands(self):

        localctx = D96Parser.OperandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_operands)
        try:
            self.state = 439
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 431
                self.match(D96Parser.INTLIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 432
                self.match(D96Parser.FLOATLIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 433
                self.match(D96Parser.BOOLEANLIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 434
                self.match(D96Parser.STRINGLIT)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 435
                self.arrayLIT()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 436
                self.multi_ArrayLIT()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 437
                self.match(D96Parser.ID)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 438
                self.self_word()
                pass


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

        def SELF(self):
            return self.getToken(D96Parser.SELF, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_self_word

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelf_word" ):
                return visitor.visitSelf_word(self)
            else:
                return visitor.visitChildren(self)




    def self_word(self):

        localctx = D96Parser.Self_wordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_self_word)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 441
            self.match(D96Parser.SELF)
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

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def array_list(self):
            return self.getTypedRuleContext(D96Parser.Array_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_multi_ArrayLIT

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulti_ArrayLIT" ):
                return visitor.visitMulti_ArrayLIT(self)
            else:
                return visitor.visitChildren(self)




    def multi_ArrayLIT(self):

        localctx = D96Parser.Multi_ArrayLITContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_multi_ArrayLIT)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 443
            self.match(D96Parser.Array_word)
            self.state = 444
            self.match(D96Parser.LP)
            self.state = 446
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.Array_word:
                self.state = 445
                self.array_list()


            self.state = 448
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

        def arrayLIT(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ArrayLITContext)
            else:
                return self.getTypedRuleContext(D96Parser.ArrayLITContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMA)
            else:
                return self.getToken(D96Parser.COMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_array_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_list" ):
                return visitor.visitArray_list(self)
            else:
                return visitor.visitChildren(self)




    def array_list(self):

        localctx = D96Parser.Array_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_array_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 450
            self.arrayLIT()
            self.state = 455
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMA:
                self.state = 451
                self.match(D96Parser.COMA)
                self.state = 452
                self.arrayLIT()
                self.state = 457
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayLITContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Array_word(self):
            return self.getToken(D96Parser.Array_word, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def element_list(self):
            return self.getTypedRuleContext(D96Parser.Element_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_arrayLIT

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayLIT" ):
                return visitor.visitArrayLIT(self)
            else:
                return visitor.visitChildren(self)




    def arrayLIT(self):

        localctx = D96Parser.ArrayLITContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_arrayLIT)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 458
            self.match(D96Parser.Array_word)
            self.state = 459
            self.match(D96Parser.LP)
            self.state = 461
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 8)) & ~0x3f) == 0 and ((1 << (_la - 8)) & ((1 << (D96Parser.Array_word - 8)) | (1 << (D96Parser.New_word - 8)) | (1 << (D96Parser.ID - 8)) | (1 << (D96Parser.INTLIT - 8)) | (1 << (D96Parser.FLOATLIT - 8)) | (1 << (D96Parser.BOOLEANLIT - 8)) | (1 << (D96Parser.STRINGLIT - 8)) | (1 << (D96Parser.SELF - 8)) | (1 << (D96Parser.SUB_OP - 8)) | (1 << (D96Parser.NOT_OP - 8)) | (1 << (D96Parser.LP - 8)))) != 0):
                self.state = 460
                self.element_list()


            self.state = 463
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

        def elements(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ElementsContext)
            else:
                return self.getTypedRuleContext(D96Parser.ElementsContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMA)
            else:
                return self.getToken(D96Parser.COMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_element_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElement_list" ):
                return visitor.visitElement_list(self)
            else:
                return visitor.visitChildren(self)




    def element_list(self):

        localctx = D96Parser.Element_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_element_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 465
            self.elements()
            self.state = 470
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMA:
                self.state = 466
                self.match(D96Parser.COMA)
                self.state = 467
                self.elements()
                self.state = 472
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_elements

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElements" ):
                return visitor.visitElements(self)
            else:
                return visitor.visitChildren(self)




    def elements(self):

        localctx = D96Parser.ElementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_elements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 473
            self.expr()
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
        self._predicates[34] = self.adding_expr_sempred
        self._predicates[35] = self.multiplying_expr_sempred
        self._predicates[38] = self.index_expr_sempred
        self._predicates[39] = self.member_access_in_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def adding_expr_sempred(self, localctx:Adding_exprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def multiplying_expr_sempred(self, localctx:Multiplying_exprContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def index_expr_sempred(self, localctx:Index_exprContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def member_access_in_sempred(self, localctx:Member_access_inContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         




