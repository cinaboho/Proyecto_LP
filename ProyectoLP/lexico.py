import ply.lex as lex
import re
import codecs

tokens =['TEXT','COMMIT', 'BEGIN','EXP','MULT','DIV','MODULO','PLUS','MINUS',
         'IGUALQ','DIFER','MENOR','MAYOR','MENORIGUAL','MAYORIGUAL','Y','AND',
         'O','OR','NO','IF','WHILE','LOOP','FOR','TIMES','LLLAVE',
         'RLLAVE','LCOR','RCOR','LPARENT','RPARENT','COMA','VAR','COMMA','DOT',
         'SIMBOL','SYMBOL_UPPER','COMILLA_SIMPLE','COMILLA_DOBLE','IGUAL'
        ]

reservadas = {
    'alias': 'ALIAS',
    'and': 'AND',
    'break' : 'BREAK',
    'case' : 'CASE',
    'class' : 'CLASS',
    'def' : 'DEF',
    'defined?' : 'DEFINED',
    'do' : 'DO',
    'else' : 'ELSE',
    'elsif' : 'ELSIF',
    'end' : 'END',
    'ensure' : 'ENSURE',
    'false' : 'FALSE',
    'true' : 'TRUE',
    'for' : 'FOR',
    'if' : 'IF',
    'in' : 'IN',
    'module' : 'MODULE',
    'next' : 'NEXT',
    'nil' : 'NIL',
    'not' : 'NOT',
    'or' : 'OR',
    'redo' : 'REDO',
    'rescue' : 'RESCUE',
    'retry' : 'RETRY',
    'return' : 'RETURN',
    'self' : 'SELF',
    'super' : 'SUPER',
    'then' : 'THEN',
    'undef' : 'UNDEF',
    'unless' : 'UNLESS',
    'until' : 'UNTIL',
    'when' : 'WHEN',
    'while' : 'WHILE',
    'yield' : 'YIELD',
    '_FILE_' : '_FILE_',
    '_LINE_' : '_LINE_'
}
tokens = tokens+list(reservadas.values())
t_ignore = '\t'
t_TEXT = r"(\'[\w\s\.]*\'|\"[\w\s\.]*\")"
t_COMMIT = r'\#[\w\s\.]*'
t_BEGIN = r'\begin'   #Revisar
t_EXP= 'r\**'
t_MULT= 'r\*'
t_DIV = r'/'
t_MODULO= r'%'
t_PLUS = r'\+'
t_MINUS = r'-'
t_IGUALQ = r'=='
t_DIFER = r'!='
t_MENOR = r'<'
t_MAYOR = r'>'
t_MENORIGUAL = r'<='
t_MAYORIGUAL = r'>='
t_Y = r'\&&'
t_AND = r'\and'    #revisar
t_O = r'\||'
t_OR = r'\or'      #revisar
t_NO = r'\!'
t_IF = r'if'       #revisar
t_WHILE = r'while' #revisar
t_LOOP = r'loop'   #revisar si se pone lo que continua
t_FOR = r'for'     #for
t_TIMES = r'times'  #times(Numero en ingles)
t_LLLAVE = r'\{'
t_RLLAVE = r'\}'
t_LCOR = r'\['
t_RCOR = r'\]'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r'\,'
t_DOT = r'\.'
t_SYMBOL = r'[a-z]\w*'
t_SYMBOL_UPPER = r'[A-Z]\w*'
t_COMILLA_SIMPLE = r"\'"
t_COMILLA_DOBLE = r'\"'
t_IGUAL = r'='


