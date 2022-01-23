# Generated from d:\E-Learning HK 212\PPL\ASSIGNMENT\Assignment 1\assignment1\main\d96\parser\D96.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2D")
        buf.write("\u027d\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\3\2\3\2\3\3\3\3\3\4\3\4\3\4")
        buf.write("\3\5\3\5\3\5\3\5\7\5\u00ad\n\5\f\5\16\5\u00b0\13\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\6\3\6\7\6\u00b9\n\6\f\6\16\6\u00bc")
        buf.write("\13\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\23")
        buf.write("\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\32\3\32")
        buf.write("\3\32\3\32\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\37\3\37\3\37\3\37\3 \3 \3 \3!\3!\3!\3!\3!\3!\3")
        buf.write("!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3")
        buf.write("!\3!\3!\5!\u0176\n!\3\"\3\"\3#\3#\3$\3$\3%\3%\3&\3&\3")
        buf.write("\'\3\'\3(\3(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3+\3,\3,\3-\3")
        buf.write("-\3.\3.\3/\3/\3/\3\60\3\60\3\60\3\61\3\61\3\61\3\61\3")
        buf.write("\62\3\62\3\62\3\63\3\63\3\63\3\64\3\64\3\64\7\64\u01a9")
        buf.write("\n\64\f\64\16\64\u01ac\13\64\3\64\5\64\u01af\n\64\3\64")
        buf.write("\6\64\u01b2\n\64\r\64\16\64\u01b3\7\64\u01b6\n\64\f\64")
        buf.write("\16\64\u01b9\13\64\5\64\u01bb\n\64\3\65\3\65\6\65\u01bf")
        buf.write("\n\65\r\65\16\65\u01c0\3\66\3\66\3\66\6\66\u01c6\n\66")
        buf.write("\r\66\16\66\u01c7\3\67\3\67\3\67\6\67\u01cd\n\67\r\67")
        buf.write("\16\67\u01ce\38\38\38\38\38\38\58\u01d7\n8\39\39\3:\3")
        buf.write(":\5:\u01dd\n:\3:\3:\3;\3;\3;\5;\u01e4\n;\3<\3<\3<\3<\3")
        buf.write("<\3<\5<\u01ec\n<\3<\3<\3=\3=\5=\u01f2\n=\3>\3>\3>\7>\u01f7")
        buf.write("\n>\f>\16>\u01fa\13>\3>\3>\7>\u01fe\n>\f>\16>\u0201\13")
        buf.write(">\3>\3>\7>\u0205\n>\f>\16>\u0208\13>\3>\3>\5>\u020c\n")
        buf.write(">\3?\3?\3?\3@\3@\3@\3@\3@\3@\3@\3@\3@\5@\u021a\n@\3A\3")
        buf.write("A\3A\3A\3A\3A\3A\3B\3B\3C\3C\3D\3D\3E\3E\3F\3F\3G\3G\3")
        buf.write("H\3H\3I\3I\3J\3J\3K\3K\3L\6L\u0238\nL\rL\16L\u0239\3L")
        buf.write("\3L\3M\3M\3M\7M\u0241\nM\fM\16M\u0244\13M\3M\3M\7M\u0248")
        buf.write("\nM\fM\16M\u024b\13M\3M\3M\7M\u024f\nM\fM\16M\u0252\13")
        buf.write("M\3M\5M\u0255\nM\3M\3M\3N\3N\3N\3N\5N\u025d\nN\3O\3O\3")
        buf.write("O\7O\u0262\nO\fO\16O\u0265\13O\3O\3O\7O\u0269\nO\fO\16")
        buf.write("O\u026c\13O\3O\3O\7O\u0270\nO\fO\16O\u0273\13O\3O\3O\5")
        buf.write("O\u0277\nO\3O\3O\3P\3P\3P\3\u00ae\2Q\3\3\5\4\7\5\t\6\13")
        buf.write("\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37")
        buf.write("\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34")
        buf.write("\67\359\36;\37= ?!A\2C\"E#G$I%K&M\'O(Q)S*U+W,Y-[.]/_\60")
        buf.write("a\61c\62e\63g\2i\2k\2m\2o\64q\2s\2u\2w\65y\66{\67}\2\177")
        buf.write("\2\u0081\2\u0083\2\u00858\u00879\u0089:\u008b;\u008d<")
        buf.write("\u008f=\u0091>\u0093?\u0095@\u0097A\u0099B\u009b\2\u009d")
        buf.write("C\u009fD\3\2\20\5\2C\\aac|\6\2\62;C\\aac|\3\2\63;\3\2")
        buf.write("\62;\3\2\629\4\2ZZzz\5\2\62;CHch\4\2DDdd\3\2\62\63\4\2")
        buf.write("GGgg\4\2--//\6\2\f\f\17\17$$^^\t\2))^^ddhhppttvv\5\2\n")
        buf.write("\f\16\17\"\"\2\u02af\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2")
        buf.write("\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2")
        buf.write("\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31")
        buf.write("\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2")
        buf.write("\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3")
        buf.write("\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2")
        buf.write("\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3")
        buf.write("\2\2\2\2?\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I")
        buf.write("\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2")
        buf.write("S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2")
        buf.write("\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2")
        buf.write("\2\2o\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2\u0085")
        buf.write("\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2")
        buf.write("\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093")
        buf.write("\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2\2\2\u0099\3\2\2")
        buf.write("\2\2\u009d\3\2\2\2\2\u009f\3\2\2\2\3\u00a1\3\2\2\2\5\u00a3")
        buf.write("\3\2\2\2\7\u00a5\3\2\2\2\t\u00a8\3\2\2\2\13\u00b6\3\2")
        buf.write("\2\2\r\u00bd\3\2\2\2\17\u00c5\3\2\2\2\21\u00ca\3\2\2\2")
        buf.write("\23\u00d0\3\2\2\2\25\u00d9\3\2\2\2\27\u00dc\3\2\2\2\31")
        buf.write("\u00e3\3\2\2\2\33\u00e8\3\2\2\2\35\u00f0\3\2\2\2\37\u00f5")
        buf.write("\3\2\2\2!\u00fb\3\2\2\2#\u0101\3\2\2\2%\u0104\3\2\2\2")
        buf.write("\'\u0108\3\2\2\2)\u010e\3\2\2\2+\u0116\3\2\2\2-\u011d")
        buf.write("\3\2\2\2/\u0124\3\2\2\2\61\u012a\3\2\2\2\63\u012f\3\2")
        buf.write("\2\2\65\u0133\3\2\2\2\67\u0137\3\2\2\29\u013c\3\2\2\2")
        buf.write(";\u0148\3\2\2\2=\u0153\3\2\2\2?\u0157\3\2\2\2A\u0175\3")
        buf.write("\2\2\2C\u0177\3\2\2\2E\u0179\3\2\2\2G\u017b\3\2\2\2I\u017d")
        buf.write("\3\2\2\2K\u017f\3\2\2\2M\u0181\3\2\2\2O\u0183\3\2\2\2")
        buf.write("Q\u0186\3\2\2\2S\u0189\3\2\2\2U\u018c\3\2\2\2W\u018f\3")
        buf.write("\2\2\2Y\u0191\3\2\2\2[\u0193\3\2\2\2]\u0195\3\2\2\2_\u0198")
        buf.write("\3\2\2\2a\u019b\3\2\2\2c\u019f\3\2\2\2e\u01a2\3\2\2\2")
        buf.write("g\u01ba\3\2\2\2i\u01bc\3\2\2\2k\u01c2\3\2\2\2m\u01c9\3")
        buf.write("\2\2\2o\u01d6\3\2\2\2q\u01d8\3\2\2\2s\u01da\3\2\2\2u\u01e3")
        buf.write("\3\2\2\2w\u01e5\3\2\2\2y\u01f1\3\2\2\2{\u01f3\3\2\2\2")
        buf.write("}\u020d\3\2\2\2\177\u0219\3\2\2\2\u0081\u021b\3\2\2\2")
        buf.write("\u0083\u0222\3\2\2\2\u0085\u0224\3\2\2\2\u0087\u0226\3")
        buf.write("\2\2\2\u0089\u0228\3\2\2\2\u008b\u022a\3\2\2\2\u008d\u022c")
        buf.write("\3\2\2\2\u008f\u022e\3\2\2\2\u0091\u0230\3\2\2\2\u0093")
        buf.write("\u0232\3\2\2\2\u0095\u0234\3\2\2\2\u0097\u0237\3\2\2\2")
        buf.write("\u0099\u023d\3\2\2\2\u009b\u025c\3\2\2\2\u009d\u025e\3")
        buf.write("\2\2\2\u009f\u027a\3\2\2\2\u00a1\u00a2\7<\2\2\u00a2\4")
        buf.write("\3\2\2\2\u00a3\u00a4\7&\2\2\u00a4\6\3\2\2\2\u00a5\u00a6")
        buf.write("\7\60\2\2\u00a6\u00a7\7\60\2\2\u00a7\b\3\2\2\2\u00a8\u00a9")
        buf.write("\7%\2\2\u00a9\u00aa\7%\2\2\u00aa\u00ae\3\2\2\2\u00ab\u00ad")
        buf.write("\13\2\2\2\u00ac\u00ab\3\2\2\2\u00ad\u00b0\3\2\2\2\u00ae")
        buf.write("\u00af\3\2\2\2\u00ae\u00ac\3\2\2\2\u00af\u00b1\3\2\2\2")
        buf.write("\u00b0\u00ae\3\2\2\2\u00b1\u00b2\7%\2\2\u00b2\u00b3\7")
        buf.write("%\2\2\u00b3\u00b4\3\2\2\2\u00b4\u00b5\b\5\2\2\u00b5\n")
        buf.write("\3\2\2\2\u00b6\u00ba\t\2\2\2\u00b7\u00b9\t\3\2\2\u00b8")
        buf.write("\u00b7\3\2\2\2\u00b9\u00bc\3\2\2\2\u00ba\u00b8\3\2\2\2")
        buf.write("\u00ba\u00bb\3\2\2\2\u00bb\f\3\2\2\2\u00bc\u00ba\3\2\2")
        buf.write("\2\u00bd\u00be\7R\2\2\u00be\u00bf\7t\2\2\u00bf\u00c0\7")
        buf.write("q\2\2\u00c0\u00c1\7i\2\2\u00c1\u00c2\7t\2\2\u00c2\u00c3")
        buf.write("\7c\2\2\u00c3\u00c4\7o\2\2\u00c4\16\3\2\2\2\u00c5\u00c6")
        buf.write("\7o\2\2\u00c6\u00c7\7c\2\2\u00c7\u00c8\7k\2\2\u00c8\u00c9")
        buf.write("\7p\2\2\u00c9\20\3\2\2\2\u00ca\u00cb\7D\2\2\u00cb\u00cc")
        buf.write("\7t\2\2\u00cc\u00cd\7g\2\2\u00cd\u00ce\7c\2\2\u00ce\u00cf")
        buf.write("\7m\2\2\u00cf\22\3\2\2\2\u00d0\u00d1\7E\2\2\u00d1\u00d2")
        buf.write("\7q\2\2\u00d2\u00d3\7p\2\2\u00d3\u00d4\7v\2\2\u00d4\u00d5")
        buf.write("\7k\2\2\u00d5\u00d6\7p\2\2\u00d6\u00d7\7w\2\2\u00d7\u00d8")
        buf.write("\7g\2\2\u00d8\24\3\2\2\2\u00d9\u00da\7K\2\2\u00da\u00db")
        buf.write("\7h\2\2\u00db\26\3\2\2\2\u00dc\u00dd\7G\2\2\u00dd\u00de")
        buf.write("\7n\2\2\u00de\u00df\7u\2\2\u00df\u00e0\7g\2\2\u00e0\u00e1")
        buf.write("\7k\2\2\u00e1\u00e2\7h\2\2\u00e2\30\3\2\2\2\u00e3\u00e4")
        buf.write("\7G\2\2\u00e4\u00e5\7n\2\2\u00e5\u00e6\7u\2\2\u00e6\u00e7")
        buf.write("\7g\2\2\u00e7\32\3\2\2\2\u00e8\u00e9\7H\2\2\u00e9\u00ea")
        buf.write("\7q\2\2\u00ea\u00eb\7t\2\2\u00eb\u00ec\7g\2\2\u00ec\u00ed")
        buf.write("\7c\2\2\u00ed\u00ee\7e\2\2\u00ee\u00ef\7j\2\2\u00ef\34")
        buf.write("\3\2\2\2\u00f0\u00f1\7V\2\2\u00f1\u00f2\7t\2\2\u00f2\u00f3")
        buf.write("\7w\2\2\u00f3\u00f4\7g\2\2\u00f4\36\3\2\2\2\u00f5\u00f6")
        buf.write("\7H\2\2\u00f6\u00f7\7c\2\2\u00f7\u00f8\7n\2\2\u00f8\u00f9")
        buf.write("\7u\2\2\u00f9\u00fa\7g\2\2\u00fa \3\2\2\2\u00fb\u00fc")
        buf.write("\7C\2\2\u00fc\u00fd\7t\2\2\u00fd\u00fe\7t\2\2\u00fe\u00ff")
        buf.write("\7c\2\2\u00ff\u0100\7{\2\2\u0100\"\3\2\2\2\u0101\u0102")
        buf.write("\7K\2\2\u0102\u0103\7p\2\2\u0103$\3\2\2\2\u0104\u0105")
        buf.write("\7K\2\2\u0105\u0106\7p\2\2\u0106\u0107\7v\2\2\u0107&\3")
        buf.write("\2\2\2\u0108\u0109\7H\2\2\u0109\u010a\7n\2\2\u010a\u010b")
        buf.write("\7q\2\2\u010b\u010c\7c\2\2\u010c\u010d\7v\2\2\u010d(\3")
        buf.write("\2\2\2\u010e\u010f\7D\2\2\u010f\u0110\7q\2\2\u0110\u0111")
        buf.write("\7q\2\2\u0111\u0112\7n\2\2\u0112\u0113\7g\2\2\u0113\u0114")
        buf.write("\7c\2\2\u0114\u0115\7p\2\2\u0115*\3\2\2\2\u0116\u0117")
        buf.write("\7U\2\2\u0117\u0118\7v\2\2\u0118\u0119\7t\2\2\u0119\u011a")
        buf.write("\7k\2\2\u011a\u011b\7p\2\2\u011b\u011c\7i\2\2\u011c,\3")
        buf.write("\2\2\2\u011d\u011e\7T\2\2\u011e\u011f\7g\2\2\u011f\u0120")
        buf.write("\7v\2\2\u0120\u0121\7w\2\2\u0121\u0122\7t\2\2\u0122\u0123")
        buf.write("\7p\2\2\u0123.\3\2\2\2\u0124\u0125\7E\2\2\u0125\u0126")
        buf.write("\7n\2\2\u0126\u0127\7c\2\2\u0127\u0128\7u\2\2\u0128\u0129")
        buf.write("\7u\2\2\u0129\60\3\2\2\2\u012a\u012b\7P\2\2\u012b\u012c")
        buf.write("\7w\2\2\u012c\u012d\7n\2\2\u012d\u012e\7n\2\2\u012e\62")
        buf.write("\3\2\2\2\u012f\u0130\7X\2\2\u0130\u0131\7c\2\2\u0131\u0132")
        buf.write("\7n\2\2\u0132\64\3\2\2\2\u0133\u0134\7X\2\2\u0134\u0135")
        buf.write("\7c\2\2\u0135\u0136\7t\2\2\u0136\66\3\2\2\2\u0137\u0138")
        buf.write("\7U\2\2\u0138\u0139\7g\2\2\u0139\u013a\7n\2\2\u013a\u013b")
        buf.write("\7h\2\2\u013b8\3\2\2\2\u013c\u013d\7E\2\2\u013d\u013e")
        buf.write("\7q\2\2\u013e\u013f\7p\2\2\u013f\u0140\7u\2\2\u0140\u0141")
        buf.write("\7v\2\2\u0141\u0142\7t\2\2\u0142\u0143\7w\2\2\u0143\u0144")
        buf.write("\7e\2\2\u0144\u0145\7v\2\2\u0145\u0146\7q\2\2\u0146\u0147")
        buf.write("\7t\2\2\u0147:\3\2\2\2\u0148\u0149\7F\2\2\u0149\u014a")
        buf.write("\7g\2\2\u014a\u014b\7u\2\2\u014b\u014c\7v\2\2\u014c\u014d")
        buf.write("\7t\2\2\u014d\u014e\7w\2\2\u014e\u014f\7e\2\2\u014f\u0150")
        buf.write("\7v\2\2\u0150\u0151\7q\2\2\u0151\u0152\7t\2\2\u0152<\3")
        buf.write("\2\2\2\u0153\u0154\7P\2\2\u0154\u0155\7g\2\2\u0155\u0156")
        buf.write("\7y\2\2\u0156>\3\2\2\2\u0157\u0158\7D\2\2\u0158\u0159")
        buf.write("\7{\2\2\u0159@\3\2\2\2\u015a\u0176\5\21\t\2\u015b\u0176")
        buf.write("\5\23\n\2\u015c\u0176\5\25\13\2\u015d\u0176\5\27\f\2\u015e")
        buf.write("\u0176\5\31\r\2\u015f\u0176\3\2\2\2\u0160\u0176\5\33\16")
        buf.write("\2\u0161\u0176\5\35\17\2\u0162\u0176\5\37\20\2\u0163\u0176")
        buf.write("\5!\21\2\u0164\u0176\5#\22\2\u0165\u0176\3\2\2\2\u0166")
        buf.write("\u0176\5%\23\2\u0167\u0176\5\'\24\2\u0168\u0176\5)\25")
        buf.write("\2\u0169\u0176\5+\26\2\u016a\u0176\5-\27\2\u016b\u0176")
        buf.write("\3\2\2\2\u016c\u0176\5\61\31\2\u016d\u0176\5/\30\2\u016e")
        buf.write("\u0176\5\63\32\2\u016f\u0176\5\65\33\2\u0170\u0176\3\2")
        buf.write("\2\2\u0171\u0176\59\35\2\u0172\u0176\5;\36\2\u0173\u0176")
        buf.write("\5=\37\2\u0174\u0176\5? \2\u0175\u015a\3\2\2\2\u0175\u015b")
        buf.write("\3\2\2\2\u0175\u015c\3\2\2\2\u0175\u015d\3\2\2\2\u0175")
        buf.write("\u015e\3\2\2\2\u0175\u015f\3\2\2\2\u0175\u0160\3\2\2\2")
        buf.write("\u0175\u0161\3\2\2\2\u0175\u0162\3\2\2\2\u0175\u0163\3")
        buf.write("\2\2\2\u0175\u0164\3\2\2\2\u0175\u0165\3\2\2\2\u0175\u0166")
        buf.write("\3\2\2\2\u0175\u0167\3\2\2\2\u0175\u0168\3\2\2\2\u0175")
        buf.write("\u0169\3\2\2\2\u0175\u016a\3\2\2\2\u0175\u016b\3\2\2\2")
        buf.write("\u0175\u016c\3\2\2\2\u0175\u016d\3\2\2\2\u0175\u016e\3")
        buf.write("\2\2\2\u0175\u016f\3\2\2\2\u0175\u0170\3\2\2\2\u0175\u0171")
        buf.write("\3\2\2\2\u0175\u0172\3\2\2\2\u0175\u0173\3\2\2\2\u0175")
        buf.write("\u0174\3\2\2\2\u0176B\3\2\2\2\u0177\u0178\7-\2\2\u0178")
        buf.write("D\3\2\2\2\u0179\u017a\7/\2\2\u017aF\3\2\2\2\u017b\u017c")
        buf.write("\7,\2\2\u017cH\3\2\2\2\u017d\u017e\7\61\2\2\u017eJ\3\2")
        buf.write("\2\2\u017f\u0180\7\'\2\2\u0180L\3\2\2\2\u0181\u0182\7")
        buf.write("#\2\2\u0182N\3\2\2\2\u0183\u0184\7(\2\2\u0184\u0185\7")
        buf.write("(\2\2\u0185P\3\2\2\2\u0186\u0187\7~\2\2\u0187\u0188\7")
        buf.write("~\2\2\u0188R\3\2\2\2\u0189\u018a\7?\2\2\u018a\u018b\7")
        buf.write("?\2\2\u018bT\3\2\2\2\u018c\u018d\7#\2\2\u018d\u018e\7")
        buf.write("?\2\2\u018eV\3\2\2\2\u018f\u0190\7?\2\2\u0190X\3\2\2\2")
        buf.write("\u0191\u0192\7@\2\2\u0192Z\3\2\2\2\u0193\u0194\7>\2\2")
        buf.write("\u0194\\\3\2\2\2\u0195\u0196\7@\2\2\u0196\u0197\7?\2\2")
        buf.write("\u0197^\3\2\2\2\u0198\u0199\7>\2\2\u0199\u019a\7?\2\2")
        buf.write("\u019a`\3\2\2\2\u019b\u019c\7?\2\2\u019c\u019d\7?\2\2")
        buf.write("\u019d\u019e\7\60\2\2\u019eb\3\2\2\2\u019f\u01a0\7-\2")
        buf.write("\2\u01a0\u01a1\7\60\2\2\u01a1d\3\2\2\2\u01a2\u01a3\7<")
        buf.write("\2\2\u01a3\u01a4\7<\2\2\u01a4f\3\2\2\2\u01a5\u01bb\7\62")
        buf.write("\2\2\u01a6\u01b7\t\4\2\2\u01a7\u01a9\t\5\2\2\u01a8\u01a7")
        buf.write("\3\2\2\2\u01a9\u01ac\3\2\2\2\u01aa\u01a8\3\2\2\2\u01aa")
        buf.write("\u01ab\3\2\2\2\u01ab\u01ae\3\2\2\2\u01ac\u01aa\3\2\2\2")
        buf.write("\u01ad\u01af\7a\2\2\u01ae\u01ad\3\2\2\2\u01ae\u01af\3")
        buf.write("\2\2\2\u01af\u01b1\3\2\2\2\u01b0\u01b2\t\5\2\2\u01b1\u01b0")
        buf.write("\3\2\2\2\u01b2\u01b3\3\2\2\2\u01b3\u01b1\3\2\2\2\u01b3")
        buf.write("\u01b4\3\2\2\2\u01b4\u01b6\3\2\2\2\u01b5\u01aa\3\2\2\2")
        buf.write("\u01b6\u01b9\3\2\2\2\u01b7\u01b5\3\2\2\2\u01b7\u01b8\3")
        buf.write("\2\2\2\u01b8\u01bb\3\2\2\2\u01b9\u01b7\3\2\2\2\u01ba\u01a5")
        buf.write("\3\2\2\2\u01ba\u01a6\3\2\2\2\u01bbh\3\2\2\2\u01bc\u01be")
        buf.write("\7\62\2\2\u01bd\u01bf\t\6\2\2\u01be\u01bd\3\2\2\2\u01bf")
        buf.write("\u01c0\3\2\2\2\u01c0\u01be\3\2\2\2\u01c0\u01c1\3\2\2\2")
        buf.write("\u01c1j\3\2\2\2\u01c2\u01c3\7\62\2\2\u01c3\u01c5\t\7\2")
        buf.write("\2\u01c4\u01c6\t\b\2\2\u01c5\u01c4\3\2\2\2\u01c6\u01c7")
        buf.write("\3\2\2\2\u01c7\u01c5\3\2\2\2\u01c7\u01c8\3\2\2\2\u01c8")
        buf.write("l\3\2\2\2\u01c9\u01ca\7\62\2\2\u01ca\u01cc\t\t\2\2\u01cb")
        buf.write("\u01cd\t\n\2\2\u01cc\u01cb\3\2\2\2\u01cd\u01ce\3\2\2\2")
        buf.write("\u01ce\u01cc\3\2\2\2\u01ce\u01cf\3\2\2\2\u01cfn\3\2\2")
        buf.write("\2\u01d0\u01d7\5g\64\2\u01d1\u01d7\5i\65\2\u01d2\u01d7")
        buf.write("\5k\66\2\u01d3\u01d4\5m\67\2\u01d4\u01d5\b8\3\2\u01d5")
        buf.write("\u01d7\3\2\2\2\u01d6\u01d0\3\2\2\2\u01d6\u01d1\3\2\2\2")
        buf.write("\u01d6\u01d2\3\2\2\2\u01d6\u01d3\3\2\2\2\u01d7p\3\2\2")
        buf.write("\2\u01d8\u01d9\5g\64\2\u01d9r\3\2\2\2\u01da\u01dc\t\13")
        buf.write("\2\2\u01db\u01dd\t\f\2\2\u01dc\u01db\3\2\2\2\u01dc\u01dd")
        buf.write("\3\2\2\2\u01dd\u01de\3\2\2\2\u01de\u01df\5q9\2\u01dft")
        buf.write("\3\2\2\2\u01e0\u01e1\5\u0093J\2\u01e1\u01e2\5q9\2\u01e2")
        buf.write("\u01e4\3\2\2\2\u01e3\u01e0\3\2\2\2\u01e3\u01e4\3\2\2\2")
        buf.write("\u01e4v\3\2\2\2\u01e5\u01eb\5q9\2\u01e6\u01ec\5u;\2\u01e7")
        buf.write("\u01ec\5s:\2\u01e8\u01e9\5u;\2\u01e9\u01ea\5s:\2\u01ea")
        buf.write("\u01ec\3\2\2\2\u01eb\u01e6\3\2\2\2\u01eb\u01e7\3\2\2\2")
        buf.write("\u01eb\u01e8\3\2\2\2\u01ec\u01ed\3\2\2\2\u01ed\u01ee\b")
        buf.write("<\4\2\u01eex\3\2\2\2\u01ef\u01f2\5\35\17\2\u01f0\u01f2")
        buf.write("\5\37\20\2\u01f1\u01ef\3\2\2\2\u01f1\u01f0\3\2\2\2\u01f2")
        buf.write("z\3\2\2\2\u01f3\u01f8\7$\2\2\u01f4\u01f5\7)\2\2\u01f5")
        buf.write("\u01f7\7$\2\2\u01f6\u01f4\3\2\2\2\u01f7\u01fa\3\2\2\2")
        buf.write("\u01f8\u01f6\3\2\2\2\u01f8\u01f9\3\2\2\2\u01f9\u01ff\3")
        buf.write("\2\2\2\u01fa\u01f8\3\2\2\2\u01fb\u01fe\5}?\2\u01fc\u01fe")
        buf.write("\n\r\2\2\u01fd\u01fb\3\2\2\2\u01fd\u01fc\3\2\2\2\u01fe")
        buf.write("\u0201\3\2\2\2\u01ff\u01fd\3\2\2\2\u01ff\u0200\3\2\2\2")
        buf.write("\u0200\u0206\3\2\2\2\u0201\u01ff\3\2\2\2\u0202\u0203\7")
        buf.write(")\2\2\u0203\u0205\7$\2\2\u0204\u0202\3\2\2\2\u0205\u0208")
        buf.write("\3\2\2\2\u0206\u0204\3\2\2\2\u0206\u0207\3\2\2\2\u0207")
        buf.write("\u0209\3\2\2\2\u0208\u0206\3\2\2\2\u0209\u020b\7$\2\2")
        buf.write("\u020a\u020c\7\2\2\3\u020b\u020a\3\2\2\2\u020b\u020c\3")
        buf.write("\2\2\2\u020c|\3\2\2\2\u020d\u020e\7^\2\2\u020e\u020f\t")
        buf.write("\16\2\2\u020f~\3\2\2\2\u0210\u0211\7^\2\2\u0211\u0212")
        buf.write("\4\62\65\2\u0212\u0213\4\629\2\u0213\u021a\4\629\2\u0214")
        buf.write("\u0215\7^\2\2\u0215\u0216\4\629\2\u0216\u021a\4\629\2")
        buf.write("\u0217\u0218\7^\2\2\u0218\u021a\4\629\2\u0219\u0210\3")
        buf.write("\2\2\2\u0219\u0214\3\2\2\2\u0219\u0217\3\2\2\2\u021a\u0080")
        buf.write("\3\2\2\2\u021b\u021c\7^\2\2\u021c\u021d\7w\2\2\u021d\u021e")
        buf.write("\5\u0083B\2\u021e\u021f\5\u0083B\2\u021f\u0220\5\u0083")
        buf.write("B\2\u0220\u0221\5\u0083B\2\u0221\u0082\3\2\2\2\u0222\u0223")
        buf.write("\t\b\2\2\u0223\u0084\3\2\2\2\u0224\u0225\7*\2\2\u0225")
        buf.write("\u0086\3\2\2\2\u0226\u0227\7+\2\2\u0227\u0088\3\2\2\2")
        buf.write("\u0228\u0229\7]\2\2\u0229\u008a\3\2\2\2\u022a\u022b\7")
        buf.write("_\2\2\u022b\u008c\3\2\2\2\u022c\u022d\7}\2\2\u022d\u008e")
        buf.write("\3\2\2\2\u022e\u022f\7\177\2\2\u022f\u0090\3\2\2\2\u0230")
        buf.write("\u0231\7=\2\2\u0231\u0092\3\2\2\2\u0232\u0233\7\60\2\2")
        buf.write("\u0233\u0094\3\2\2\2\u0234\u0235\7.\2\2\u0235\u0096\3")
        buf.write("\2\2\2\u0236\u0238\t\17\2\2\u0237\u0236\3\2\2\2\u0238")
        buf.write("\u0239\3\2\2\2\u0239\u0237\3\2\2\2\u0239\u023a\3\2\2\2")
        buf.write("\u023a\u023b\3\2\2\2\u023b\u023c\bL\2\2\u023c\u0098\3")
        buf.write("\2\2\2\u023d\u0242\7$\2\2\u023e\u023f\7)\2\2\u023f\u0241")
        buf.write("\7$\2\2\u0240\u023e\3\2\2\2\u0241\u0244\3\2\2\2\u0242")
        buf.write("\u0240\3\2\2\2\u0242\u0243\3\2\2\2\u0243\u0249\3\2\2\2")
        buf.write("\u0244\u0242\3\2\2\2\u0245\u0248\5}?\2\u0246\u0248\n\r")
        buf.write("\2\2\u0247\u0245\3\2\2\2\u0247\u0246\3\2\2\2\u0248\u024b")
        buf.write("\3\2\2\2\u0249\u0247\3\2\2\2\u0249\u024a\3\2\2\2\u024a")
        buf.write("\u0250\3\2\2\2\u024b\u0249\3\2\2\2\u024c\u024d\7)\2\2")
        buf.write("\u024d\u024f\7$\2\2\u024e\u024c\3\2\2\2\u024f\u0252\3")
        buf.write("\2\2\2\u0250\u024e\3\2\2\2\u0250\u0251\3\2\2\2\u0251\u0254")
        buf.write("\3\2\2\2\u0252\u0250\3\2\2\2\u0253\u0255\7\2\2\3\u0254")
        buf.write("\u0253\3\2\2\2\u0254\u0255\3\2\2\2\u0255\u0256\3\2\2\2")
        buf.write("\u0256\u0257\bM\5\2\u0257\u009a\3\2\2\2\u0258\u0259\7")
        buf.write("^\2\2\u0259\u025d\7j\2\2\u025a\u025d\5\u0081A\2\u025b")
        buf.write("\u025d\5\177@\2\u025c\u0258\3\2\2\2\u025c\u025a\3\2\2")
        buf.write("\2\u025c\u025b\3\2\2\2\u025d\u009c\3\2\2\2\u025e\u0263")
        buf.write("\7$\2\2\u025f\u0260\7)\2\2\u0260\u0262\7$\2\2\u0261\u025f")
        buf.write("\3\2\2\2\u0262\u0265\3\2\2\2\u0263\u0261\3\2\2\2\u0263")
        buf.write("\u0264\3\2\2\2\u0264\u026a\3\2\2\2\u0265\u0263\3\2\2\2")
        buf.write("\u0266\u0269\5\u009bN\2\u0267\u0269\n\r\2\2\u0268\u0266")
        buf.write("\3\2\2\2\u0268\u0267\3\2\2\2\u0269\u026c\3\2\2\2\u026a")
        buf.write("\u0268\3\2\2\2\u026a\u026b\3\2\2\2\u026b\u0271\3\2\2\2")
        buf.write("\u026c\u026a\3\2\2\2\u026d\u026e\7)\2\2\u026e\u0270\7")
        buf.write("$\2\2\u026f\u026d\3\2\2\2\u0270\u0273\3\2\2\2\u0271\u026f")
        buf.write("\3\2\2\2\u0271\u0272\3\2\2\2\u0272\u0274\3\2\2\2\u0273")
        buf.write("\u0271\3\2\2\2\u0274\u0276\7$\2\2\u0275\u0277\7\2\2\3")
        buf.write("\u0276\u0275\3\2\2\2\u0276\u0277\3\2\2\2\u0277\u0278\3")
        buf.write("\2\2\2\u0278\u0279\bO\6\2\u0279\u009e\3\2\2\2\u027a\u027b")
        buf.write("\13\2\2\2\u027b\u027c\bP\7\2\u027c\u00a0\3\2\2\2%\2\u00ae")
        buf.write("\u00ba\u0175\u01aa\u01ae\u01b3\u01b7\u01ba\u01c0\u01c7")
        buf.write("\u01ce\u01d6\u01dc\u01e3\u01eb\u01f1\u01f8\u01fd\u01ff")
        buf.write("\u0206\u020b\u0219\u0239\u0242\u0247\u0249\u0250\u0254")
        buf.write("\u025c\u0263\u0268\u026a\u0271\u0276\b\b\2\2\38\2\3<\3")
        buf.write("\3M\4\3O\5\3P\6")
        return buf.getvalue()


class D96Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    BLOCKCOMMENT = 4
    ID = 5
    Program = 6
    Main = 7
    Break = 8
    Continue = 9
    If = 10
    Elseif = 11
    Else = 12
    Foreach = 13
    BooleanTrue = 14
    BooleanFalse = 15
    Array = 16
    In = 17
    Int = 18
    Float = 19
    Boolean = 20
    String = 21
    Return = 22
    Class = 23
    Null = 24
    Val = 25
    Var = 26
    Self = 27
    Constructor = 28
    Destructor = 29
    KEYWORD_New = 30
    By = 31
    ADD_OP = 32
    SUB_OP = 33
    MUL_OP = 34
    DIV_OP = 35
    MOD_OP = 36
    NOT_OP = 37
    AND_OP = 38
    OR_OP = 39
    EQUAL_OP = 40
    DIFF_OP = 41
    ASSIGN_OP = 42
    GREATER_OP = 43
    LESSER_OP = 44
    GREATER_EQUAL_OP = 45
    LESSER_EQUAL_OP = 46
    STRING_COMP_OP = 47
    STRING_CONCAT_OP = 48
    MEMBER_ACCESS_OUT = 49
    INTLIT = 50
    FLOATLIT = 51
    BOOLEANLIT = 52
    STRINGLIT = 53
    LP = 54
    RP = 55
    LSB = 56
    RSB = 57
    LB = 58
    RB = 59
    SEMI = 60
    DOT = 61
    COMA = 62
    WS = 63
    UNCLOSE_STRING = 64
    ILLEGAL_ESCAPE = 65
    ERROR_CHAR = 66

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
            "BLOCKCOMMENT", "ID", "Program", "Main", "Break", "Continue", 
            "If", "Elseif", "Else", "Foreach", "BooleanTrue", "BooleanFalse", 
            "Array", "In", "Int", "Float", "Boolean", "String", "Return", 
            "Class", "Null", "Val", "Var", "Self", "Constructor", "Destructor", 
            "KEYWORD_New", "By", "ADD_OP", "SUB_OP", "MUL_OP", "DIV_OP", 
            "MOD_OP", "NOT_OP", "AND_OP", "OR_OP", "EQUAL_OP", "DIFF_OP", 
            "ASSIGN_OP", "GREATER_OP", "LESSER_OP", "GREATER_EQUAL_OP", 
            "LESSER_EQUAL_OP", "STRING_COMP_OP", "STRING_CONCAT_OP", "MEMBER_ACCESS_OUT", 
            "INTLIT", "FLOATLIT", "BOOLEANLIT", "STRINGLIT", "LP", "RP", 
            "LSB", "RSB", "LB", "RB", "SEMI", "DOT", "COMA", "WS", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "T__0", "T__1", "T__2", "BLOCKCOMMENT", "ID", "Program", 
                  "Main", "Break", "Continue", "If", "Elseif", "Else", "Foreach", 
                  "BooleanTrue", "BooleanFalse", "Array", "In", "Int", "Float", 
                  "Boolean", "String", "Return", "Class", "Null", "Val", 
                  "Var", "Self", "Constructor", "Destructor", "KEYWORD_New", 
                  "By", "KEYWORD", "ADD_OP", "SUB_OP", "MUL_OP", "DIV_OP", 
                  "MOD_OP", "NOT_OP", "AND_OP", "OR_OP", "EQUAL_OP", "DIFF_OP", 
                  "ASSIGN_OP", "GREATER_OP", "LESSER_OP", "GREATER_EQUAL_OP", 
                  "LESSER_EQUAL_OP", "STRING_COMP_OP", "STRING_CONCAT_OP", 
                  "MEMBER_ACCESS_OUT", "DECIMAL", "OCTAL", "HEX", "BIN", 
                  "INTLIT", "INTERGER_PART", "EXPONENT", "FRACTION", "FLOATLIT", 
                  "BOOLEANLIT", "STRINGLIT", "ESC_SEQ", "OCTAL_ESC", "UNICODE_ESC", 
                  "HEX_DIGIT", "LP", "RP", "LSB", "RSB", "LB", "RB", "SEMI", 
                  "DOT", "COMA", "WS", "UNCLOSE_STRING", "ILL_ESC_SEQ", 
                  "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    grammarFileName = "D96.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[54] = self.INTLIT_action 
            actions[58] = self.FLOATLIT_action 
            actions[75] = self.UNCLOSE_STRING_action 
            actions[77] = self.ILLEGAL_ESCAPE_action 
            actions[78] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INTLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            	self.text = self.text.replace("_","")

     

    def FLOATLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

            	self.text = self.text.replace("_","")

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            raise UncloseString(self.text) 
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise IllegalEscape(self.text) 
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
             raise ErrorToken(self.text) 
     


