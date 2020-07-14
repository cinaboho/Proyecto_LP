import ply.lex as lex
tokens = [
	'PLUS', # +
	'MINUS', # -
	'TIMES', # *
	'DIVIDED', # /
	'LPAREN', # (
	'LBRA', # [
	'LLLAVE', # {}
	'RPAREN', # )
	'RBRA', # ]
	'RLLAVE', # }
	'SYMBOL', # variable names
	'SYMBOL_UPPER', # variable names
	'NUMBER',
	'TEXT',
	'DECIMAL',
 	'EQUAL',
 	'ASIGN',
	'GT',
	'LT',
	'GEQT',
	'LEQT',
	'FUNCTION',
	'COMMENT',
	'COMMA',
	'DDOT',
	'DOT',
]

t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDED = r'/'
t_LPAREN = r'\('
t_LBRA = r'\['
t_LLLAVE = r'\{'
t_RPAREN = r'\)'
t_RBRA = r'\]'
t_RLLAVE = r'\}'
t_SYMBOL = r'\${0,1}[a-z]\w*'
t_SYMBOL_UPPER = r'\${0,1}[A-Z]\w*'
t_TEXT = r"(\'[\w\s\.]*\'|\"[\w\s\.]*\")"
t_EQUAL = r'={2}'
t_ASIGN = r'={1}'
t_GT = r'>'
t_LT = r'<'
t_GEQT = r'>='
t_LEQT = r'<='
t_COMMENT = r'\#[\w\s\.]*'
t_COMMA = r'\,'
t_DDOT = r'\.\.'
t_DOT = r'\.'

reserved_words = {
	'alias': "ALIAS",
	'and':"AND",
	'or':"OR",
	'begin':"BEGIN",
	'end':"END",
	'break': "BREAK",
	'class': "CLASS",
	'case':"CASE",
	'self': "SELF",
	'true': "TRUE",
	'false': "FALSE",
	'for': "FOR",
	'when': "WHEN",
	'while': "WHILE",
	'if': 'IF',
	'elsif': 'ELSIF',
	'else': 'ELSE',
	'puts': "PUTS",
	'def': "DEF",
	'unless': "UNLESS"
}

tokens = tokens +  list(reserved_words.values())

def t_DECIMAL(t):
	r'\d+\.\d+'
	t.value = float(t.value)
	return t

def t_NUMBER(t):
	r'\d+'
	t.value = int(t.value)
	return t

def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)

def t_ID(t):
	r'([a-z\-0-9]+)'
	if t.value in reserved_words:
		t.type = reserved_words[t.value]
	else:
		t.type = 'SYMBOL'
	return t

t_ignore = ' \t'

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
