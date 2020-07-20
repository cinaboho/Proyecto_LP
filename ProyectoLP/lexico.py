import ply.lex as lex
# resultado del analisis
resultado_lexema = []
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
         'DOSPUNTOS',
         'DOT',
         'COMILLA_SIMPLE',
         'COMILLA_DOBLE',
         'COND',
         'NO',
         'PLUS',
         'MINUS',
         'PES',
         'MULT',
         'SPLAT',
         'DIV',
         'MODULO',
         'LCOMILLABAJA',
         'RCOMILLABAJA',
         'Y',
         'O',
        # 'ACENTO',
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
         'INC',
         'VARNAME',
         'GLOBAL',
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
t_DOSPUNTOS = r'\:'
t_DOT = r'\.'
t_COMILLA_SIMPLE = r"\'"
t_COMILLA_DOBLE = r'\"'
t_COND = r'\[?]'


# Operacion Asignacion
t_NO= r'\!'
t_PLUS = r'\+'
t_MINUS = r'-'
t_PES = r"~"
t_MULT = r'\*'
t_SPLAT = r'(\*{2}| \^)'
t_DIV = r'/'
t_MODULO = r'%'
t_LCOMILLABAJA = r'<<'
t_RCOMILLABAJA = r'>>'
t_Y = r'&'
t_O = r'\|'
#t_ACENTO = r'\^'
t_IGUAL = r'={2}'
#t_COMP = r'={3}'
t_DIFER = r'!='
t_COMPNAVE = r'<=>'
t_MAYORIGUAL = r'>='
t_MAYOR = r'>'
t_MENOR = r'<'
t_MENORIGUAL = r'<='
t_ASIG = r'={1}'
t_MODULOIGUAL = r'%='
t_DIVIGUAL = r'/='
t_MINUSIGUAL = r'-='
t_PLUSIGUAL = r'\+='
t_MULTIGUAL= r'\[*]='
t_MULT2IGUAL= r'\[*]{2}='
t_DOT2 = r'\..'
t_DOT3 = r'\.{3}'
#and or not son reservadas
t_Y2 = r'&&'
t_O2 = r'\|{2}'
t_CONDTERN = r'\?\:'
t_INC= r'\?'
t_VARNAME= r'\@+[a-zA-Z_][a-zA-Z0-9_]*'
t_GLOBAL= r'\$+[a-zA-Z_][a-zA-Z0-9_]*'


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
def t_COMP(t):
    r'={3}'
    return t
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
#def t_COMMIT(t):
    r'\#.*'
#    pass

def t_ID(t):
    r'\[a-zA-Z_][a-zA-Z0-9_]*'
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
    global resultado_lexema
    estado = "** Token no valido en la Linea {:4} Valor {:16} Posicion {:4}".format(str(t.lineno), str(t.value),str(t.lexpos))
    resultado_lexema.append(estado)
    t.lexer.skip(1)


# Prueba de ingreso
def prueba(data):
    global resultado_lexema

    analizador = lex.lex()
    analizador.input(data)

    resultado_lexema.clear()
    while True:
        tok = analizador.token()
        if not tok:
            break
        # print("lexema de "+tok.type+" valor "+tok.value+" linea "tok.lineno)
        estado = "Linea {:4} Tipo {:16} Valor {:16} Posicion {:4}".format(str(tok.lineno),str(tok.type) ,str(tok.value), str(tok.lexpos) )
        resultado_lexema.append(estado)
    return resultado_lexema

 # instanciamos el analizador lexico
analizador = lex.lex()

if __name__ == '__main__':
    while True:
        data = input("ingrese: ")
        prueba(data)
        print(resultado_lexema)
