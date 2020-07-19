import ply.yacc as yacc
import os
import codecs
import re
from lexico import tokens
from sys import stdin
procedence = (
			  ('right', 'ASIG'),
			  ('left', 'NO'),
			  ('left','MENOR','MENORIGUAL','MAYOR','MAYORIGUAL'),
              ('left','PLUS','MINUS'),
              ('left','NUMBER','DIV'),
			  ('left', 'LPARENT', 'RPARENT')
              )
def p_program(p):
    '''program=block'''
    print("program")
    #p[0] = program(p[1], "program")
def p_consDecl(p):
    '''program=block'''
    print("Bloque")
    #p[0]= consDecl(p[2])
def p_constDeclEmpty(p):
    '''constDecl =empty'''
    print("constDecl")
    #p[0] = Null()
def p_constDEclEmpty(p):
    '''constDecl= CONST consAssigmentList'''
    #p[0]= NULL()
    print("Nulo")
def p_constAssignmentList1(p):
	'''constAssignmentList : ID ASSIGN NUMBER'''
	print ("constAssignmentList 1")

def p_constAssignmentList2(p):
	'''constAssignmentList : constAssignmentList COMMA ID ASSIGN NUMBER'''
	print ("constAssignmentList 2")

def p_varDecl1(p):
	'''varDecl : VAR identList SEMMICOLOM'''
	print ("varDecl 1")

def p_varDeclEmpty(p):
	'''varDecl : empty'''
	print ("nulo")

def p_identList1(p):
	'''identList : ID'''
	print ("identList 1")

def p_identList2(p):
	'''identList : identList COMMA ID'''
	print ("identList 2")

def p_procDecl1(p):
	'''procDecl : procDecl PROCEDURE ID SEMMICOLOM block SEMMICOLOM'''
	print ("procDecl 1")

def p_procDeclEmpty(p):
	'''procDecl : empty'''
	print ("nulo")

def p_statement1(p):
	'''statement : ID UPDATE expression'''
	print ("statement 1")

def p_statement2(p):
	'''statement : CALL ID'''
	print ("statement 2")

def p_statement3(p):
	'''statement : BEGIN statementList END'''
	print ("statement 3")

def p_statement4(p):
	'''statement : IF condition THEN statement'''
	print ("statement 4")

def p_statement5(p):
	'''statement : WHILE condition DO statement'''
	print ("statement 5")

def p_statementEmpty(p):
	'''statement : empty'''
	print ("nulo")

def p_statementList1(p):
	'''statementList : statement'''
	print ("statementList 1")

def p_statementList2(p):
	'''statementList : statementList SEMMICOLOM statement'''
	print ("statementList 2")

def p_condition1(p):
	'''condition : ODD expression'''
	print ("condition 1")

def p_condition2(p):
	'''condition : expression relation expression'''
	print ("condition 2")

def p_relation1(p):
	'''relation : ASSIGN'''
	print ("relation 1")

def p_relation2(p):
	'''relation : NE'''
	print ("relation 2")

def p_relation3(p):
	'''relation : MENOR'''
	print ("relation 3")

def p_relation4(p):
	'''relation : MAYOR'''
	print ("relation 4")

def p_relation5(p):
	'''relation : MENORIGUAL'''
	print ("relation 5")

def p_relation6(p):
	'''relation : MAYORIGUAL'''
	print ("relation 6")

def p_expression1(p):
	'''expression : term'''
	print ("expresion 1")

def p_expression2(p):
	'''expression : addingOperator term'''
	print ("expresion 2")

def p_expression3(p):
	'''expression : expression addingOperator term'''
	print ("expresion 3")

def p_addingOperator1(p):
	'''addingOperator : PLUS'''
	print ("addingOperator 1")

def p_addingOperator2(p):
	'''addingOperator : MINUS'''
	print ("addingOperator 1")

def p_term1(p):
	'''term : factor'''
	print ("term 1")

def p_term2(p):
	'''term : term multiplyingOperator factor'''
	print ("term 1")

def p_multiplyingOperator1(p):
	'''multiplyingOperator : MULT'''
	print ("multiplyingOperator 1")

def p_multiplyingOperator2(p):
	'''multiplyingOperator : DIV'''
	print ("multiplyingOperator 2")

def p_factor1(p):
	'''factor : ID'''
	print ("factor 1")

def p_factor2(p):
	'''factor : NUMBER'''
	print ("factor 1")

def p_factor3(p):
	'''factor : LPARENT expression RPARENT'''
	print ("factor 1")

def p_empty(p):
	'''empty :'''
	pass

def p_error(p):
	print ("Error de sintaxis ", p)
	#print "Error en la linea "+str(p.lineno)