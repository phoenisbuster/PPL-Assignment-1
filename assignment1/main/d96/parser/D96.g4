/**
*   Student's Name: Nguyen Dinh Bao Phuc
*   Student's ID: 1852068
**/
grammar D96;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}
//Program includes one/many Class (Objects)
program: class_decl+ EOF;
class_decl: Class_word class_name (Colon (ID | Prog_word))? LB member_lists* RB;
class_name: ID | Prog_word | Class_word | Main_word;
Class_word: CLASS;
Prog_word: PROGRAM;

/* 
Keyword: Main_word | Cons_word | Dest_word
| Bool_word | Int_word | Float_word | Str_word | Array_word 
| Var_word | Val_word
| If_word | Elseif_word | Else_word
| In_word | By_word | Break_word | Cont_word | Return_word | New_word
| Self_word;
*/

//Each Class has class's attributes and class's methods
member_lists: attributes | methods;

//This is attribute declaration, which include Types
attributes: (Var_word | Val_word) attribute_list Colon types (Assign_op expr_list)? SEMI;
attribute_list: attribute_name (COMA attribute_name)*;
attribute_name: ID;

//Types in d96 include: primitive types (int, float, bool, string), array and object(class)
types: primitive_Type | array_Type | class_type;
primitive_Type: Bool_word | Int_word | Float_word | Str_word;
Bool_word: BOOL;
Int_word: INT;
Float_word: FLOAT;
Str_word: STR;
array_Type: Array_word LSB (element_type COMA array_size)? RSB; 
Array_word: ARRAY;
element_type: primitive_Type | array_Type;
array_size: INTLIT;
class_type: class_name;

//This is method declaration, which includes many statements (block stmts)
methods: (ID| Main_word | Cons_word | Dest_word) LP paramlist? RP block_stmt;
Main_word: MAIN;
Cons_word: CONS;
Dest_word: DEST;
paramlist: param_decl (SEMI param_decl)*;
param_decl: idlist Colon types;
//List of ids
idlist: ID (COMA ID)*;

//This is praser rules for block stmts
block_stmt: LB block_stmt_list* RB;
block_stmt_list: stmt | var_cons_decl; //including stmts and variables/constants declaration

//Rules for variables/constants
var_cons_decl: (Var_word | Val_word) idlist Colon types (Assign_op expr_list)? SEMI;
Var_word: VAR;
Val_word: VAL;
var_cons_list: var_cons_name (COMA var_cons_name)*;
var_cons_name: ID;

//All type of stmts
stmt: as_stmt | if_stmt | loop_stmt | break_stmt | cont_stmt | return_stmt | invocation_stmt;

as_stmt: index_expr Assign_op expr SEMI; //Assignmet stmt

//If stmt
if_stmt: (If_word LP expr RP block_stmt) (Elseif_word  LP expr RP block_stmt)* (Else_word block_stmt)?; 
If_word: IF;
Else_word: ELSE;
Elseif_word: ELSEIF;

//Loop (Foreach) stmt
loop_stmt: Foreach_word LP ID In_word expr '..' expr (By_word expr)? RP block_stmt;
Foreach_word: FOREACH;
In_word: IN;
By_word: BY;

//Instance/static (member_access_in/member_access_out) method invocation
invocation_stmt: (member_access_in | member_access_out) SEMI;

//Look at the names => rules
break_stmt: Break_word SEMI;
Break_word: BREAK;
cont_stmt: Cont_word SEMI;
Cont_word: CONT;
return_stmt: Return_word (expr)? SEMI;
Return_word: RETURN;

//Rules for expressions, very complicated
expr_list: expr (COMA expr)*;

expr: string_expr;

string_expr: relational_expr (String_comp | String_concat) relational_expr
| relational_expr;

relational_expr: logical_expr (Equal | Diff | Greater | Lesser | Greater_euqal | Lesser_equal) logical_expr 
| logical_expr;

logical_expr: adding_expr (And | Or) adding_expr
| adding_expr;

adding_expr: adding_expr (Add | Sub) multiplying_expr
| multiplying_expr;

multiplying_expr: multiplying_expr (Mul | Div | Mod) logical_not_expr
| logical_not_expr;

logical_not_expr: Not logical_not_expr
| sign_expr;

sign_expr: Sub sign_expr
| index_expr;

index_expr: index_expr (LSB expr RSB)+
| member_access_in;

member_access_in: member_access_in Member_access_in member_access_out (LP expr_list? RP)?
| member_access_out;

member_access_out: class_expr Member_access_out class_expr (LP expr_list? RP)?
| class_expr;

class_expr: New_word class_expr LP expr_list? RP
| piority_exp;
New_word: KEYWORD_NEW;

piority_exp: LP expr RP 
| operands;

operands: INTLIT | FLOATLIT | BOOLEANLIT | STRINGLIT | arrayLIT | multi_ArrayLIT | ID | Self_word | class_name;
Self_word: SELF;

Add: ADD_OP;
Sub: SUB_OP;
Mul: MUL_OP;
Div: DIV_OP;
Mod: MOD_OP;
Not: NOT_OP;
And: AND_OP;
Or: OR_OP;
Assign_op: ASSIGN_OP;
Equal: EQUAL_OP;
Diff: DIFF_OP;
Greater: GREATER_OP;
Lesser: LESSER_OP;
Greater_euqal: GREATER_EQUAL_OP;
Lesser_equal: LESSER_EQUAL_OP;
String_comp: STRING_COMP_OP;
String_concat: STRING_CONCAT_OP;
Member_access_in: DOT;
Member_access_out: MEMBER_ACCESS_OUT;
Colon: COLON;

/////////////////// Lexer Rules//////////////////////

//Block comment
BLOCKCOMMENT: '##' .*? '##' -> skip;

//Identifiers
ID: NORM_ID | SPEC_ID;
fragment NORM_ID: [a-zA-Z_][a-zA-Z0-9_]*;
fragment SPEC_ID: '$'[a-zA-Z0-9_]+;

//Describe Interger Literal
INTLIT: (DECIMAL | OCTAL | HEX | BIN)
{	
	self.text = self.text.replace('_','')
};

//For Floating point number
FLOATLIT: INTERGER_PART (FRACTION  | EXPONENT | FRACTION EXPONENT)
{
	self.text = self.text.replace('_','')
	##print("Float: ", self.text)
};
fragment INTERGER_PART: DECIMAL;
fragment EXPONENT: [eE] [+-]? [0-9]+; 
fragment FRACTION: DOT [0-9]*; 

fragment DECIMAL: ('0') | ([1-9]([0-9]*'_'?[0-9]+)*);
fragment OCTAL: '0'[0-7][0-7_]*;
fragment HEX: '0'[xX][A-F0-9][A-F0-9_]*;
fragment BIN: '0'[bB][01][01_]*;


//For Boolean literal
BOOLEANLIT: BOOLTRUE | BOOLFALSE;

//For string litteral
STRINGLIT:  '"' ('\'"')* ( ESC_SEQ | ~["] | ('\'"'))* ('\'"')* '"' //'"' ( ESC_SEQ | (~[\\"]) | ('\'"'))* '"'
{
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
};

//For Error in string
UNCLOSE_STRING: '"' ('\'"')* ( ESC_SEQ | ~[\\"] )* ('\'"')* 
{
	self.text = self.text[1:]
	##print("UNCLOSE_STRING: ", self.text)
	raise UncloseString(self.text) 
};

ILLEGAL_ESCAPE: '"' ('\'"')* (~["\\] | ESC_SEQ | '\'"')* ('\'"')* ILL_ESC_SEQ
{
	self.text = self.text[1:]
	##print("ILLEGAL_ESCAPE: ", self.text)
	raise IllegalEscape(self.text) 
};

//fragment for string literals
fragment ESC_SEQ: '\\' ('b'|'f'|'r'|'n'|'t'|'\''|'\\');
fragment ILL_ESC_SEQ: ('\\' ~([bfnrt\\] | '\'') ) | UNICODE_ESC | OCTAL_ESC | UNKNOW_ESC;
fragment OCTAL_ESC:   '\\' ('0'..'3') ('0'..'7') ('0'..'7')
    |   '\\' ('0'..'7') ('0'..'7')
    |   '\\' ('0'..'7');

fragment UNICODE_ESC:   '\\' 'u' HEX_DIGIT HEX_DIGIT HEX_DIGIT HEX_DIGIT ;

fragment HEX_DIGIT : ('0'..'9'|'a'..'f'|'A'..'F') ; 

fragment UNKNOW_ESC: '\\' 'h';

//This is not lexer rules!!!
// For arrays in array
multi_ArrayLIT: Array_word LP array_list? RP;
array_list: arrayLIT (COMA arrayLIT)*;
// For indexed array
arrayLIT: Array_word LP element_list? RP;
element_list: elements (COMA elements)*;
elements: expr;
//This is not lexer rules!!!

PROGRAM: 'Program';
MAIN: 'main';
//These are for Keywords
BREAK: 'Break';
CONT: 'Continue';
IF: 'If';
ELSEIF: 'Elseif';
ELSE: 'Else';
FOREACH: 'Foreach';
BOOLTRUE: 'True';
BOOLFALSE: 'False';
ARRAY: 'Array';
IN: 'In';
INT: 'Int';
FLOAT: 'Float';
BOOL: 'Boolean';
STR: 'String';
RETURN: 'Return';
CLASS: 'Class';
NULL: 'Null';
VAL: 'Val';
VAR: 'Var';
SELF: 'Self';
CONS: 'Constructor';
DEST: 'Destructor';
KEYWORD_NEW: 'New';
BY: 'By';
//Total Keywords available
fragment KEYWORD: BREAK | CONT | IF | ELSEIF | ELSE |
| FOREACH | BOOLTRUE | BOOLFALSE | ARRAY | IN |
| INT | FLOAT | BOOL | STR | RETURN |
| NULL | CLASS | VAL | VAR |
| CONS | DEST | KEYWORD_NEW | BY ;

//These tokens for operators
ADD_OP: '+';
SUB_OP: '-';
MUL_OP: '*';
DIV_OP: '/';
MOD_OP: '%';
NOT_OP: '!';
AND_OP: '&&';
OR_OP: '||';
EQUAL_OP: '==';
DIFF_OP: '!=';
ASSIGN_OP: '=';
GREATER_OP: '>';
LESSER_OP: '<';
GREATER_EQUAL_OP: '>=';
LESSER_EQUAL_OP: '<=';
STRING_COMP_OP: '==.';
STRING_CONCAT_OP: '+.';
//MEMBER_ACCESS_IN: '.'; //Can be presented by dot in Special Character
MEMBER_ACCESS_OUT: '::';

//These tokens for Special Character
LP: '(';
RP: ')';

LSB: '[';
RSB: ']';

LB: '{';
RB: '}';

SEMI: ';';

DOT: '.';

COMA: ',';

COLON: ':';

WS: [ \t\b\f\r\n]+ -> skip; // skip blanks, tabs, backspaces, form feed, carriage return, newline

//UNTERMINATED_COMMENT: '##' .*? EOF { raise UnterminatedComment(self.text) }; //This is removed from assignment requirement
ERROR_CHAR: . { raise ErrorToken(self.text) };