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
class_decl: 'Class' (ID|Program) (':'(ID|Program))? LB member_lists RB;

member_lists: (member member_list_tail)?;
member_list_tail: (member member_list_tail)?;
member: attributes | methods;

attributes: (Val|Var) attribute_list ':' types ('=' expr_list)? SEMI;
attribute_list: attribute_name attribute_list_tail;
attribute_list_tail: (attribute_name attribute_list_tail)?;
attribute_name: '$'?ID;

types: primitive_Type | array_Type | class_type;
primitive_Type: Boolean | Int | Float | String;
array_Type: Array LSB (element_type COMA array_size)? RSB; 
element_type: primitive_Type | array_Type;
array_size: INTLIT;
class_type: ID;

methods: '$'?(ID|Main|Constructor|Destructor) param block_stmt;
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
| ID MEMBER_ACCESS_OUT '$'?ID (LP expr_list RP)?
| ID DOT '$'?ID (LP expr_list RP)?
| index_expr
| math_expr
| relational_expr
| string_expr
| ID;

class_expr: <assoc=right> KEYWORD_New ID LP expr_list RP;

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
| INTLIT | FLOATLIT | ID;

mod_expr: mod_expr MOD_OP mod_expr 
| INTLIT | ID;

logical_not_expr: <assoc=right> NOT_OP logical_not_expr
| BOOLEANLIT | ID;

logical_expr: logical_expr AND_OP logical_expr | logical_expr OR_OP logical_expr
| BOOLEANLIT | ID;

relational_expr: relational_expr_1 | relational_expr_2;
relational_expr_1: relational_expr_1 (EQUAL_OP | DIFF_OP ) relational_expr_1 
| INTLIT | BOOLEANLIT | ID;
relational_expr_2: relational_expr_2 (GREATER_OP | LESSER_OP | GREATER_EQUAL_OP | LESSER_EQUAL_OP) relational_expr_2
| INTLIT | FLOATLIT | ID;

string_expr: string_expr (STRING_COMP_OP | STRING_CONCAT_OP) string_expr
| STRINGLIT | ID;

block_stmt: LB block_stmt_list RB;
block_stmt_list: (stmt block_stmt_list_tail)?;
block_stmt_list_tail: (stmt block_stmt_list_tail)?;

stmt: stmt_list SEMI;
stmt_list: var_cons_decl | asm | if_stmt | loop_stmt | Break | Continue | return_stmt;

var_cons_decl: (Val|Var) var_cons_list ':' types ('=' expr_list)? SEMI;
var_cons_list: var_cons_name var_cons_list_tail;
var_cons_list_tail: (var_cons_name var_cons_list_tail)?;
var_cons_name: ID;

asm: (ID | index_expr) ASSIGN_OP expr;

if_stmt : matchStmt
| unmatchStmt;
matchStmt: If expr matchStmt
(elseif_list)
(Else matchStmt)?
| block_stmt;
unmatchStmt: If expr if_stmt
| If expr matchStmt
(elseif_list)
(Else unmatchStmt)?;

elseif_list: (elseif_stmt elseif_list_tail)?;
elseif_list_tail: (elseif_stmt elseif_list_tail)?;
elseif_stmt: Elseif if_stmt;

loop_stmt: Foreach LP ID In expr '..' expr (By expr)? RP block_stmt;

call: ID LB expr_list RB;

return_stmt: Return (expr)?;

//Block comment
BLOCKCOMMENT: '##' .*? '##' -> skip;

//Identifiers
ID: [a-zA-Z_][a-zA-Z0-9_]*;

//These fragments for Keywords and other uses
Program: 'Program';
Main: 'main';
Break: 'Break';
Continue: 'Continue';
If: 'If';
Elseif: 'Elseif';
Else: 'Else';
Foreach: 'Foreach';
BooleanTrue: 'True';
BooleanFalse: 'False';
Array: 'Array';
In: 'In';
Int: 'Int';
Float: 'Float';
Boolean: 'Boolean';
String: 'String';
Return: 'Return';
Class: 'Class';
Null: 'Null';
Val: 'Val';
Var: 'Var';
Self: 'Self';
Constructor: 'Constructor';
Destructor: 'Destructor';
KEYWORD_New: 'New';
By: 'By';
//Total Keywords available
fragment KEYWORD: Break | Continue | If | Elseif | Else |
| Foreach | BooleanTrue | BooleanFalse | Array | In |
| Int | Float | Boolean | String | Return |
| Null | Class | Val | Var |
| Constructor | Destructor | KEYWORD_New | By ;

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

//Describe Interger Literal
fragment DECIMAL: ('0') | ([1-9]([0-9]*('_'?)[0-9]+)*);
fragment OCTAL: '0'[0-7]+;
fragment HEX: '0'[xX][a-fA-F0-9]+;
fragment BIN: '0'[bB][01]+;
INTLIT: DECIMAL | OCTAL | HEX | BIN
{
	self.text = self.text.replace("_","")
};

// For Floating point number
fragment INTERGER_PART: DECIMAL;
fragment EXPONENT: [eE][+-]? INTERGER_PART; 
fragment FRACTION: (DOT INTERGER_PART)?; 
FLOATLIT: INTERGER_PART ( FRACTION | EXPONENT | FRACTION EXPONENT ) 
{
	self.text = self.text.replace("_","")
};

// For Boolean literal
BOOLEANLIT: BooleanTrue | BooleanFalse;

// For string litteral
STRINGLIT:  '"' ('\'"')* ( ESC_SEQ | ~[\\"\r\n] )* ('\'"')* '"' EOF?;
fragment ESC_SEQ:   '\\' ('b'|'f'|'r'|'n'|'t'|'\''|'\\');
fragment OCTAL_ESC:   '\\' ('0'..'3') ('0'..'7') ('0'..'7')
    |   '\\' ('0'..'7') ('0'..'7')
    |   '\\' ('0'..'7');

fragment UNICODE_ESC:   '\\' 'u' HEX_DIGIT HEX_DIGIT HEX_DIGIT HEX_DIGIT ;

fragment HEX_DIGIT : ('0'..'9'|'a'..'f'|'A'..'F') ; 

// For arrays in array
multi_ArrayLIT: Array LP array_list RP;
array_list: (index_ArrayLIT array_list_tail)?;
array_list_tail: (COMA index_ArrayLIT array_list_tail)?;
// For indexed array
index_ArrayLIT: Array elements;
elements: LP element_list RP;
element_list: (expr elements_tail)?;
elements_tail: (COMA expr elements_tail)?;

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


UNCLOSE_STRING: '"' ('\'"')* ( ESC_SEQ | ~[\\"\r\n] )* ('\'"')* EOF? {raise UncloseString(self.text) };
fragment ILL_ESC_SEQ: '\\' ('h') | UNICODE_ESC | OCTAL_ESC;
ILLEGAL_ESCAPE: '"' ('\'"')* ( ILL_ESC_SEQ | ~[\\"\r\n] )* ('\'"')* '"' EOF? {raise IllegalEscape(self.text) };
//UNTERMINATED_COMMENT: '##' .*? EOF { raise UnterminatedComment(self.text) }; //This is removed from assignment requirement
ERROR_CHAR: . { raise ErrorToken(self.text) };