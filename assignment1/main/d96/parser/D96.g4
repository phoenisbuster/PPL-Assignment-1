grammar D96;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: many_class_decl EOF;
many_class_decl: class_decl class_decl_list;
class_decl_list: (class_decl class_decl_list)?;
class_decl: Class_word (ID|PROGRAM) (':'(ID|PROGRAM))? LB member_lists RB;
Class_word: CLASS;

member_lists: (member member_list_tail)?;
member_list_tail: (member member_list_tail)?;
member: attributes | methods;

attributes: (VAL|VAR) attribute_list ':' types ('=' expr_list)? SEMI;
attribute_list: attribute_name attribute_list_tail;
attribute_list_tail: (attribute_name attribute_list_tail)?;
attribute_name: '$'?ID;

types: primitive_Type | array_Type | class_type;
primitive_Type: BOOL | INT | FLOAT | STR;
array_Type: ARRAY LSB (element_type COMA array_size)? RSB; 
element_type: primitive_Type | array_Type;
array_size: INTLIT;
class_type: ID;

methods: '$'?(ID|MAIN|CONS|DEST) param block_stmt;
param: LP paramlist RP;
paramlist: (param_decl paramlist_tail)?;
paramlist_tail: (SEMI param_decl paramlist_tail)?;
param_decl: idlist ':' types;

idlist: ID idlist_tail;
idlist_tail: (COMA ID idlist_tail)?;

expr_list: (expr expr_list_tail)?;
expr_list_tail: (COMA expr expr_list_tail)?;

expr: 
class_expr 
| member_access_out
| member_access_in
| index_expr
| math_expr
| relational_expr
| string_expr
| ID;

class_expr: <assoc=right> KEYWORD_NEW ID LP expr_list RP;

member_access_out: ID MEMBER_ACCESS_OUT '$'?ID (LP expr_list RP)?;
member_access_in: (ID | self_word) DOT '$'?ID (LP expr_list RP)?;
self_word: SELF;

index_expr: lower_expr index_operators;
index_operators: LB lower_expr RB
| LB lower_expr RB index_operators;

lower_expr: math_expr | relational_expr | string_expr | ID;

math_expr: 
<assoc=right> SUB_OP math_expr
| logical_not_expr
| math_expr MUL_OP math_expr | math_expr DIV_OP math_expr | mod_expr
| math_expr ADD_OP math_expr | math_expr SUB_OP math_expr
| logical_expr
| member_access_out | member_access_in | INTLIT | FLOATLIT | ID;

mod_expr: mod_expr MOD_OP mod_expr 
| member_access_out | member_access_in | INTLIT | ID;

logical_not_expr: <assoc=right> NOT_OP logical_not_expr
| member_access_out | member_access_in | BOOLEANLIT | ID;

logical_expr: logical_expr AND_OP logical_expr | logical_expr OR_OP logical_expr
| member_access_out | member_access_in | BOOLEANLIT | ID;

relational_expr: relational_expr_1 | relational_expr_2;
relational_expr_1: relational_expr_1 (EQUAL_OP | DIFF_OP ) relational_expr_1 
| member_access_out | member_access_in | INTLIT | BOOLEANLIT | ID;
relational_expr_2: relational_expr_2 (GREATER_OP | LESSER_OP | GREATER_EQUAL_OP | LESSER_EQUAL_OP) relational_expr_2
| member_access_out | member_access_in | INTLIT | FLOATLIT | ID;

string_expr: string_expr (STRING_COMP_OP | STRING_CONCAT_OP) string_expr
| member_access_out | member_access_in | STRINGLIT | ID;

block_stmt: LB block_stmt_list RB;
block_stmt_list: (stmt block_stmt_list_tail)?;
block_stmt_list_tail: (stmt block_stmt_list_tail)?;

stmt: stmt_list SEMI;
stmt_list: var_cons_decl | asm | if_stmt | loop_stmt | BREAK | CONT | return_stmt;

var_cons_decl: (VAL|VAR) var_cons_list ':' types ('=' expr_list)? SEMI;
var_cons_list: var_cons_name var_cons_list_tail;
var_cons_list_tail: (var_cons_name var_cons_list_tail)?;
var_cons_name: ID;

asm: (ID | index_expr) ASSIGN_OP expr;

if_stmt : matchStmt
| unmatchStmt;
matchStmt: IF expr matchStmt
(elseif_list)
(ELSE matchStmt)?
| block_stmt;
unmatchStmt: IF expr if_stmt
| IF expr matchStmt
(elseif_list)
(ELSE unmatchStmt)?;

elseif_list: (elseif_stmt elseif_list_tail)?;
elseif_list_tail: (elseif_stmt elseif_list_tail)?;
elseif_stmt: ELSEIF if_stmt;

loop_stmt: FOREACH LP ID IN expr '..' expr (BY expr)? RP block_stmt;

call: ID LB expr_list RB;

return_stmt: Return_word (expr)?;
Return_word: RETURN;

/////////////////// Lexer Rules//////////////////////

//Block comment
BLOCKCOMMENT: '##' .*? '##' -> skip;

//Describe Interger Literal
INTLIT: (DECIMAL | OCTAL | HEX | BIN)
{	
	self.text = self.text.replace('_','')
};

// For Floating point number
FLOATLIT: INTERGER_PART (FRACTION  | EXPONENT | FRACTION EXPONENT)
{
	self.text = self.text.replace('_','')
	print("Float: ", self.text)
};
fragment INTERGER_PART: DECIMAL;
fragment EXPONENT: [eE][+-]? INTERGER_PART; 
fragment FRACTION: (DOT INTERGER_PART)?; 

fragment DECIMAL: ('0') | ([1-9]([0-9]*'_'?[0-9]+)*);
fragment OCTAL: '0'[0-7_]+;
fragment HEX: '0'[xX][a-fA-F0-9_]+;
fragment BIN: '0'[bB][01_]+;


// For Boolean literal
BOOLEANLIT: BOOLTRUE | BOOLFALSE;

// For string litteral
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
		print("ILLEGAL_ESCAPE: ", self.text)
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

// For arrays in array
multi_ArrayLIT: Array_word LP array_list RP;
Array_word: ARRAY;
array_list: (arrayLIT array_list_tail)?;
array_list_tail: (COMA arrayLIT array_list_tail)?;
// For indexed array
 
arrayLIT: Array_word LP elements RP;
elements: (ele_int_list) | (ele_float_list) | (ele_bool_list) | (ele_str_list);
ele_int_list: (INTLIT ele_int_list_tail)?;
ele_int_list_tail: (COMA INTLIT ele_int_list_tail)?;
ele_float_list: (FLOATLIT ele_float_list_tail)?;
ele_float_list_tail: (COMA FLOATLIT ele_float_list_tail)?;
ele_bool_list: (BOOLEANLIT ele_bool_list_tail)?;
ele_bool_list_tail: (COMA BOOLEANLIT ele_bool_list_tail)?;
ele_str_list: (STRINGLIT ele_str_list_tail)?;
ele_str_list_tail: (COMA STRINGLIT ele_str_list_tail)?;
//element_list: (elements elements_tail)?;
//elements_tail: (COMA elements elements_tail)?;

//Identifiers
ID: '$'?[a-zA-Z_][a-zA-Z0-9_]*;

//These fragments for Keywords and other uses
PROGRAM: 'Program';
MAIN: 'main';
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

WS: [ \t\b\f\r\n]+ -> skip; // skip blanks, tabs, backspaces, form feed, carriage return, newline

//UNTERMINATED_COMMENT: '##' .*? EOF { raise UnterminatedComment(self.text) }; //This is removed from assignment requirement
ERROR_CHAR: . { raise ErrorToken(self.text) };