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


    # Visit a parse tree produced by D96Parser#many_class_decl.
    def visitMany_class_decl(self, ctx:D96Parser.Many_class_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#class_decl_list.
    def visitClass_decl_list(self, ctx:D96Parser.Class_decl_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#class_decl.
    def visitClass_decl(self, ctx:D96Parser.Class_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#member_lists.
    def visitMember_lists(self, ctx:D96Parser.Member_listsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#member_list_tail.
    def visitMember_list_tail(self, ctx:D96Parser.Member_list_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#member.
    def visitMember(self, ctx:D96Parser.MemberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attributes.
    def visitAttributes(self, ctx:D96Parser.AttributesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attribute_list.
    def visitAttribute_list(self, ctx:D96Parser.Attribute_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attribute_list_tail.
    def visitAttribute_list_tail(self, ctx:D96Parser.Attribute_list_tailContext):
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


    # Visit a parse tree produced by D96Parser#param.
    def visitParam(self, ctx:D96Parser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#paramlist.
    def visitParamlist(self, ctx:D96Parser.ParamlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#paramlist_tail.
    def visitParamlist_tail(self, ctx:D96Parser.Paramlist_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#param_decl.
    def visitParam_decl(self, ctx:D96Parser.Param_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#idlist.
    def visitIdlist(self, ctx:D96Parser.IdlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#idlist_tail.
    def visitIdlist_tail(self, ctx:D96Parser.Idlist_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr_list.
    def visitExpr_list(self, ctx:D96Parser.Expr_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr_list_tail.
    def visitExpr_list_tail(self, ctx:D96Parser.Expr_list_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr.
    def visitExpr(self, ctx:D96Parser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#class_expr.
    def visitClass_expr(self, ctx:D96Parser.Class_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#member_access_out.
    def visitMember_access_out(self, ctx:D96Parser.Member_access_outContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#member_access_in.
    def visitMember_access_in(self, ctx:D96Parser.Member_access_inContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#self_word.
    def visitSelf_word(self, ctx:D96Parser.Self_wordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#index_expr.
    def visitIndex_expr(self, ctx:D96Parser.Index_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#index_operators.
    def visitIndex_operators(self, ctx:D96Parser.Index_operatorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#lower_expr.
    def visitLower_expr(self, ctx:D96Parser.Lower_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#math_expr.
    def visitMath_expr(self, ctx:D96Parser.Math_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#mod_expr.
    def visitMod_expr(self, ctx:D96Parser.Mod_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#logical_not_expr.
    def visitLogical_not_expr(self, ctx:D96Parser.Logical_not_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#logical_expr.
    def visitLogical_expr(self, ctx:D96Parser.Logical_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#relational_expr.
    def visitRelational_expr(self, ctx:D96Parser.Relational_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#relational_expr_1.
    def visitRelational_expr_1(self, ctx:D96Parser.Relational_expr_1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#relational_expr_2.
    def visitRelational_expr_2(self, ctx:D96Parser.Relational_expr_2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#string_expr.
    def visitString_expr(self, ctx:D96Parser.String_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#block_stmt.
    def visitBlock_stmt(self, ctx:D96Parser.Block_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#block_stmt_list.
    def visitBlock_stmt_list(self, ctx:D96Parser.Block_stmt_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#block_stmt_list_tail.
    def visitBlock_stmt_list_tail(self, ctx:D96Parser.Block_stmt_list_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stmt.
    def visitStmt(self, ctx:D96Parser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stmt_list.
    def visitStmt_list(self, ctx:D96Parser.Stmt_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#var_cons_decl.
    def visitVar_cons_decl(self, ctx:D96Parser.Var_cons_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#var_cons_list.
    def visitVar_cons_list(self, ctx:D96Parser.Var_cons_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#var_cons_list_tail.
    def visitVar_cons_list_tail(self, ctx:D96Parser.Var_cons_list_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#var_cons_name.
    def visitVar_cons_name(self, ctx:D96Parser.Var_cons_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#asm.
    def visitAsm(self, ctx:D96Parser.AsmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#if_stmt.
    def visitIf_stmt(self, ctx:D96Parser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#matchStmt.
    def visitMatchStmt(self, ctx:D96Parser.MatchStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#unmatchStmt.
    def visitUnmatchStmt(self, ctx:D96Parser.UnmatchStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#elseif_list.
    def visitElseif_list(self, ctx:D96Parser.Elseif_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#elseif_list_tail.
    def visitElseif_list_tail(self, ctx:D96Parser.Elseif_list_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#elseif_stmt.
    def visitElseif_stmt(self, ctx:D96Parser.Elseif_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#loop_stmt.
    def visitLoop_stmt(self, ctx:D96Parser.Loop_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#call.
    def visitCall(self, ctx:D96Parser.CallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#return_stmt.
    def visitReturn_stmt(self, ctx:D96Parser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#multi_ArrayLIT.
    def visitMulti_ArrayLIT(self, ctx:D96Parser.Multi_ArrayLITContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#array_list.
    def visitArray_list(self, ctx:D96Parser.Array_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#array_list_tail.
    def visitArray_list_tail(self, ctx:D96Parser.Array_list_tailContext):
        return self.visitChildren(ctx)



del D96Parser