from ply import lex
import ply.yacc as yacc

tokens = (
    'PLUS',
    'MINUS',
    'TIMES',
    'DIV',
    'LPAREN',
    'RPAREN',
    'NUMBER',
    'LCOR',
    'RCOR',
    'AND',
    'OR',
    'TRUE',
    'FALSE',
    'COMA',
    'EMPTY',
    'SIZE',
    'INTER',
    'SUBC'
)

t_ignore = ' \t'

t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIV     = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'

t_LCOR = 'r\['
t_RCOR = 'r\]'
t_AND = 'r\and'
t_OR = 'r\or'
t_TRUE = 'r\true'
t_FALSE = 'r\false'
t_COMA = 'r\,'


t_EMPTY = r'\.empty[?]'
t_SIZE = r'\.size|[==][0-9]*'
t_INTER = r'\[a-zA-Z]*[=]["][a-zA-Z]*["]'
t_SUBC = r'\[a-z]*\[[0-9]..\-[0-9]\]'

def t_NUMBER( t ) :
    r'[0-9]+'
    t.value = int( t.value )
    return t

def t_newline( t ):
  r'\n+'
  t.lexer.lineno += len( t.value )

def t_error( t ):
  print("Invalid Token:",t.value[0])
  t.lexer.skip( 1 )

lexer = lex.lex()

precedence = (
    ( 'left', 'PLUS', 'MINUS' ),
    ( 'left', 'TIMES', 'DIV' ),
    ( 'nonassoc', 'UMINUS' )
)

def p_add( p ) :
    'expr : expr PLUS expr'
    p[0] = p[1] + p[3]

def p_sub( p ) :
    'expr : expr MINUS expr'
    p[0] = p[1] - p[3]

def p_expr2uminus( p ) :
    'expr : MINUS expr %prec UMINUS'
    p[0] = - p[2]

def p_mult_div( p ) :
    '''expr : expr TIMES expr
            | expr DIV expr'''

    if p[2] == '*' :
        p[0] = p[1] * p[3]
    else :
        if p[3] == 0 :
            print("Can't divide by 0")
            raise ZeroDivisionError('integer division by 0')
        p[0] = p[1] / p[3]

def p_expr2NUM( p ) :
    'expr : NUMBER'
    p[0] = p[1]

def p_parens( p ) :
    'expr : LPAREN expr RPAREN'
    p[0] = p[2]

def p_error( p ):
    print("Error de sintaxis en la entrada!")


parser = yacc.yacc()

res = parser.parse("string[0,9]") # the input
print(res)
