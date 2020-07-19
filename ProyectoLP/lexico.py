import ply.lex as lex
import re
import codecs

tokens =['ID',
         'SYMBOL',
         'SYMBOL_UPPER',
         'TEXT',
         'BEGIN',
         'LOOP',
         'TIMES',
         'COMMIT',
         'LLLAVE',
         'RLLAVE',
         'LCOR',
         'RCOR',
         'LPARENT',
         'RPARENT',
         'COMA',
         'PUNTOYCOMA',
         'DOT',
         'COMILLA_SIMPLE',
         'COMILLA_DOBLE',
         'COND',
         'NO',
         'PLUS',
         'MINUS',
         'PES',
         'MULT',
         'EXP',
         'DIV',
         'MODULO',
         'LCOMILLABAJA',
         'RCOMILLABAJA',
         'Y',
         'O',
         'ACENTO',
         'IGUAL',
         'COMP',
         'DIFER',
         'COMPNAVE',
         'MAYORIGUAL',
         'MAYOR',
         'MENOR',
         'MENORIGUAL',
         'ASIG',
         'MODULOIGUAL',
         'DIVIGUAL',
         'MINUSIGUAL',
         'PLUSIGUAL',
         'MULTIGUAL',
         'MULT2IGUAL',
         'DOT2',
         'DOT3',
         'Y2',
         'O2',
         'CONDTERN',
         'NUMBER',
         'DECIMAL'


]
t_ignore = ' \t'
t_SYMBOL = r'\${0,1}[a-z]\w*'
t_SYMBOL_UPPER = r'\${0,1}[A-Z]\w*'
t_TEXT = r"(\'[\w\s\.]*\'|\"[\w\s\.]*\")"
t_BEGIN = r'\begin'   #Revisar
t_LOOP = r'loop'   #revisar si se pone lo que continua
t_TIMES = r'times'  #times(Numero en ingles)
t_COMMIT = r'\#[\w\s\.]*'
#DELIMITADORES
t_LLLAVE = r'\{'
t_RLLAVE = r'\}'
t_LCOR = r'\['
t_RCOR = r'\]'
t_LPARENT = r'\('
t_RPARENT = r'\)'
t_COMA = r'\,'
t_PUNTOYCOMA = r'\;'
t_DOT = r'\.'
t_COMILLA_SIMPLE = r"\'"
t_COMILLA_DOBLE = r'\"'
t_COND = r'\[?]'


# Operacion Asignacion
t_NO= r'\!'
t_PLUS = r'\[+]'
t_MINUS = r'-'
t_PES = r"~"
t_MULT = 'r\[*]'
t_EXP = 'r\[*]{2}'
t_DIV = r'/'
t_MODULO = r'%'
t_LCOMILLABAJA = r'<<'
t_RCOMILLABAJA = r'>>'
t_Y = r'&'
t_O = r'\|'
t_ACENTO = r'\^'
t_IGUAL = r'={2}'
t_COMP = r'={3}'
t_DIFER = r'!='
t_COMPNAVE = r'<=>'
t_MAYORIGUAL = r'>='
t_MAYOR = r'>'
t_MENOR = r'<'
t_MENORIGUAL = r'<='
t_ASIG = r'={1}'
t_MODULOIGUAL = r'%='
t_DIVIGUAL = r'/='
t_MINUSIGUAL = '-='
t_PLUSIGUAL = '\[+]='
t_MULTIGUAL= '\[*]='
t_MULT2IGUAL= '\[*]{2}='
t_DOT2 = r'\..'
t_DOT3 = r'\.{3}'
#and or not son reservadas
t_Y2 = r'&&'
t_O2 = r'\|{2}'
t_CONDTERN = r'\[?]:'


reservadas = {
    'alias': "ALIAS",
    'and': "AND",
    'break' : "BREAK",
    'case' : "CASE",
    'class' : "CLASS",
    'def' : "DEF",
    'defined?' : "DEFINED",
    'do' : "DO",
    'else' : "ELSE",
    'elsif' : "ELSIF",
    'end' : "END",
    'ensure' : "ENSURE",
    'false' : "FALSE",
    'true' : "TRUE",
    'for' : "FOR",
    'if' : "IF",
    'in' : "IN",
    'module' : "MODULE",
    'next' : "NEXT",
    'nil' : "NIL",
    'not' : "NOT",
    'or' : "OR",
    'redo' : "REDO",
    'rescue' : "RESCUE",
    'retry' : "RETRY",
    'return' : "RETURN",
    'self' : "SELF",
    'super' : "SUPER",
    'then' : "THEN",
    'undef' : "UNDEF",
    'unless' : "UNLESS",
    'until' : 'UNTIL',
    'when' : "WHEN",
    'while' : "WHILE",
    'yield' : "YIELD",
    '_FILE_' : "_FILE_",
    '_LINE_' : "_LINE_"
}
tokens = tokens+list(reservadas.values())

def t_newline(t):
    r'\n+'

    t.lexer.lineno += len(t.value)
#def t_COMMIT(t):
    r'\#.*'
#    pass

def t_ID(t):
    r'([a-z\-0-9]+)'
    if t.value in reservadas:
        t.type = reservadas[t.value]
    else:
        t.type = 'SYMBOL'
    return t
 
def t_NUMBER(t):
    r'\d+'
    t.value= int(t.value)
    return t
def t_DECIMAL(t):
	r'\d+\.\d+'
	t.value = float(t.value)
	return t

def t_error(t):
	print("Incorrect character '%s'" % t.value[0])
	t.lexer.skip(1)


lexer = lex.lex()


def test(code):
	lexer.input(code)
	while True:
		tok = lexer.token()
		if not tok:
			break
		print(tok)

test("def geeks")
test("class GFG")
test("# comentario bonito en rubby")
test("arr = ['a', 'b', 'c']")
test("if a > b")
test("string.split(\"s\")")
test("a.join(\"blabla\")")
test("puts \"The total is #{1+1}\"")
test("""\n
def geeks\n
\n
    puts \"Hello Geeks\"\n
end
""")
