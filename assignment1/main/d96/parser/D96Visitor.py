# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .D96Parser import D96Parser
else:
    from D96Parser import D96Parser

# This class defines a complete generic visitor for a parse tree produced by D96Parser.

class D96Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by D96Parser#program.
    def visitProgram(self, ctx:D96Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#class_decl.
    def visitClass_decl(self, ctx:D96Parser.Class_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#member_lists.
    def visitMember_lists(self, ctx:D96Parser.Member_listsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attributes.
    def visitAttributes(self, ctx:D96Parser.AttributesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attribute_list.
    def visitAttribute_list(self, ctx:D96Parser.Attribute_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attribute_name.
    def visitAttribute_name(self, ctx:D96Parser.Attribute_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#types.
    def visitTypes(self, ctx:D96Parser.TypesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#primitive_Type.
    def visitPrimitive_Type(self, ctx:D96Parser.Primitive_TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#array_Type.
    def visitArray_Type(self, ctx:D96Parser.Array_TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#element_type.
    def visitElement_type(self, ctx:D96Parser.Element_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#array_size.
    def visitArray_size(self, ctx:D96Parser.Array_sizeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#class_type.
    def visitClass_type(self, ctx:D96Parser.Class_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#methods.
    def visitMethods(self, ctx:D96Parser.MethodsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#paramlist.
    def visitParamlist(self, ctx:D96Parser.ParamlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#param_decl.
    def visitParam_decl(self, ctx:D96Parser.Param_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#idlist.
    def visitIdlist(self, ctx:D96Parser.IdlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#block_stmt.
    def visitBlock_stmt(self, ctx:D96Parser.Block_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#block_stmt_list.
    def visitBlock_stmt_list(self, ctx:D96Parser.Block_stmt_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#var_cons_decl.
    def visitVar_cons_decl(self, ctx:D96Parser.Var_cons_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#var_cons_list.
    def visitVar_cons_list(self, ctx:D96Parser.Var_cons_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#var_cons_name.
    def visitVar_cons_name(self, ctx:D96Parser.Var_cons_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stmt.
    def visitStmt(self, ctx:D96Parser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#as_stmt.
    def visitAs_stmt(self, ctx:D96Parser.As_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#if_stmt.
    def visitIf_stmt(self, ctx:D96Parser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#loop_stmt.
    def visitLoop_stmt(self, ctx:D96Parser.Loop_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#invocation_stmt.
    def visitInvocation_stmt(self, ctx:D96Parser.Invocation_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#break_stmt.
    def visitBreak_stmt(self, ctx:D96Parser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#cont_stmt.
    def visitCont_stmt(self, ctx:D96Parser.Cont_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#return_stmt.
    def visitReturn_stmt(self, ctx:D96Parser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr_list.
    def visitExpr_list(self, ctx:D96Parser.Expr_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr.
    def visitExpr(self, ctx:D96Parser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#string_expr.
    def visitString_expr(self, ctx:D96Parser.String_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#relational_expr.
    def visitRelational_expr(self, ctx:D96Parser.Relational_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#logical_expr.
    def visitLogical_expr(self, ctx:D96Parser.Logical_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#adding_expr.
    def visitAdding_expr(self, ctx:D96Parser.Adding_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#multiplying_expr.
    def visitMultiplying_expr(self, ctx:D96Parser.Multiplying_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#logical_not_expr.
    def visitLogical_not_expr(self, ctx:D96Parser.Logical_not_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#sign_expr.
    def visitSign_expr(self, ctx:D96Parser.Sign_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#index_expr.
    def visitIndex_expr(self, ctx:D96Parser.Index_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#member_access_in.
    def visitMember_access_in(self, ctx:D96Parser.Member_access_inContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#member_access_out.
    def visitMember_access_out(self, ctx:D96Parser.Member_access_outContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#class_expr.
    def visitClass_expr(self, ctx:D96Parser.Class_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#piority_exp.
    def visitPiority_exp(self, ctx:D96Parser.Piority_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#operands.
    def visitOperands(self, ctx:D96Parser.OperandsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#self_word.
    def visitSelf_word(self, ctx:D96Parser.Self_wordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#multi_ArrayLIT.
    def visitMulti_ArrayLIT(self, ctx:D96Parser.Multi_ArrayLITContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#array_list.
    def visitArray_list(self, ctx:D96Parser.Array_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#arrayLIT.
    def visitArrayLIT(self, ctx:D96Parser.ArrayLITContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#element_list.
    def visitElement_list(self, ctx:D96Parser.Element_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#elements.
    def visitElements(self, ctx:D96Parser.ElementsContext):
        return self.visitChildren(ctx)



del D96Parser