import ply.lex as lex

    # List of token names. This is always required
tokens = [
       'NUMBER',
       'PLUS',
       'MINUS',
       'TIMES',
       'DIVIDE',
       'LPAREN',
       'RPAREN',
       'EMPTY',
       'SIZE',
       'INTER',
       'SUBC'

    ]

    # Regular expression rules for simple tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LCOR = 'r\['
t_RCOR = 'r\]'
t_AND = 'r\and'
t_OR = 'r\or'
t_TRUE = 'r\true'
t_TRUE = 'r\false'
t_COMA = 'r\,'
t_EMPTY = r'\.empty[?]'
t_SIZE = r'\.size|[==][0-9]*'
t_INTER = r'\[a-zA-Z]*[=]["][a-zA-Z]*["]'
t_SUBC1 = r'\[a-z]*\[[0-9][","][0-9]\]'


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Give the lexer some input
data=""
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok)