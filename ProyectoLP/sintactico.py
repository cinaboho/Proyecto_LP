import ply.yacc as yacc
import os
import codecs
import re
from ProyectoLP.lexico import tokens
from ProyectoLP.lexico import analizador
from sys import stdin

resultado_gramatica=[]
procedence = (
			  ('right', 'ASIG'),
			  ('left', 'NO'),
			  ('left','MENOR','MENORIGUAL','MAYOR','MAYORIGUAL'),
              ('left','PLUS','MINUS'),
              ('left','NUMBER','DIV'),
			  ('left', 'LPARENT', 'RPARENT')

)
nombres= {}
def p_declaracion_asignar(t):
    'declaracion : ID ASIG expresion'
    nombres[t[1]] = t[3]

def p_declaracion_expr(t):
    'declaracion : expresion'
    # print("Resultado: " + str(t[1]))
    t[0] = t[1]
def p_expresion_operaciones(t):
    '''
    expresion  :   expresion PLUS expresion
                |   expresion MINUS expresion
                |   expresion TIMES expresion
                |   expresion DIV expresion
                |   expresion SPLAT expresion
                |   expresion MODULO expresion
    '''
    if t[2] == '+':
        t[0] = t[1] + t[3]
    elif t[2] == '-':
        t[0] = t[1] - t[3]
    elif t[2] == '*':
        t[0] = t[1] * t[3]
    elif t[2] == '/':
        t[0] = t[1] / t[3]
    elif t[2] == '%':
        t[0] = t[1] % t[3]

    elif t[2] == '**':
        i = t[3]
        t[0] = t[1]
        while i > 1:
            t[0] *= t[1]
            i -= 1



def p_expresion_grupo(t):
    '''
    expresion  : LPARENT expresion RPARENT
                | LLLAVE expresion RLLAVE
                | LCOR expresion RCOR
    '''
    t[0] = t[2]
# sintactico de expresiones logicas
def p_expresion_logicas(t):
    '''
    expresion   :  expresion MENOR expresion
                |  expresion MAYOR expresion
                |  expresion MENORIGUAL expresion
                |   expresion MAYORIGUAL expresion
                |   expresion IGUAL expresion
                |   expresion DIFER expresion
                |  LPARENT expresion RPARENT MENOR LPARENT expresion RPARENT
                |  LPARENT expresion RPARENT MAYOR LPARENT expresion RPARENT
                |  LPARENT expresion RPARENT MENORIGUAL LPARENT expresion RPARENT
                |  LPARENT  expresion RPARENT MAYORIGUAL LPARENT expresion RPARENT
                |  LPARENT  expresion RPARENT ASIG LPARENT expresion RPARENT
                |  LPARENT  expresion RPARENT DIFER LPARENT expresion RPARENT
    '''
    if t[2] == "<": t[0] = t[1] < t[3]
    elif t[2] == ">": t[0] = t[1] > t[3]
    elif t[2] == "<=": t[0] = t[1] <= t[3]
    elif t[2] == ">=": t[0] = t[1] >= t[3]
    elif t[2] == "==": t[0] = t[1] is t[3]
    elif t[2] == "!=": t[0] = t[1] != t[3]
    elif t[3] == "<":
        t[0] = t[2] < t[4]
    elif t[2] == ">":
        t[0] = t[2] > t[4]
    elif t[3] == "<=":
        t[0] = t[2] <= t[4]
    elif t[3] == ">=":
        t[0] = t[2] >= t[4]
    elif t[3] == "==":
        t[0] = t[2] is t[4]
    elif t[3] == "!=":
        t[0] = t[2] != t[4]

    # print('logica ',[x for x in t])

# gramatica de expresiones booleanadas
def p_expresion_booleana(t):
    '''
    expresion   :   expresion AND expresion
                |   expresion OR expresion
                |   expresion NOT expresion
                |  LPARENT expresion AND expresion RPARENT
                |  LPARENT expresion OR expresion RPARENT
                |  LPARENT expresion NOT expresion RPARENT
    '''
    if t[2] == "and":
        t[0] = t[1] and t[3]
    elif t[2] == "or":
        t[0] = t[1] or t[3]
    elif t[2] == "not":
        t[0] =  t[1] is not t[3]
    elif t[3] == "and":
        t[0] = t[2] and t[4]
    elif t[3] == "or":
        t[0] = t[2] or t[4]
    elif t[3] == "not":
        t[0] =  t[2] is not t[4]

def p_expresion_booleana2(t):
    '''
    expresion   :   expresion Y2 expresion
                |   expresion O2 expresion
                |   expresion NO expresion
                |  LPARENT expresion Y2 expresion RPARENT
                |  LPARENT expresion O2 expresion RPARENT
                |  LPARENT expresion NO expresion RPARENT
    '''
    if t[2] == "&&":
        t[0] = t[1] and t[3]
    elif t[2] == "||":
        t[0] = t[1] or t[3]
    elif t[2] == "!":
        t[0] =  t[1] is not t[3]
    elif t[3] == "&&":
        t[0] = t[2] and t[4]
    elif t[3] == "||":
        t[0] = t[2] or t[4]
    elif t[3] == "!":
        t[0] =  t[2] is not t[4]



def p_expresion_numero(t):
    'expresion : NUMBER'
    t[0] = t[1]
def p_expresion_decimal(t):
    'expresion : DECIMAL'
    t[0] = t[1]

def p_expresion_cadena(t):
    '''
    expresion : COMILLA_DOBLE expresion COMILLA_DOBLE
    | COMILLA_SIMPLE expresion COMILLA_SIMPLE
    '''
    t[0] = t[2]

def p_expresion_nombre(t):
    'expresion : ID'
    try:
        t[0] = nombres[t[1]]
    except LookupError:
        print("Nombre desconocido ", t[1])
        t[0] = 0

def p_expresion_commit(t):
	'expresion : COMMIT'
	t[0]=t[1]
def p_expresion_global(t):
	'expresion : GLOBAL'
	t[0]=t[1]

def p_expresion_varname(t):
	'expresion : VARNAME'
	t[0]=t[1]



def p_error(t):
    global resultado_gramatica
    if t:
        resultado = "Error sintactico de tipo {} en el valor {}".format( str(t.type),str(t.value))
        print(resultado)
    else:
        resultado = "Error sintactico {}".format(t)
        print(resultado)
    resultado_gramatica.append(resultado)



# instanciamos el analizador sistactico
parser = yacc.yacc()

def prueba_sintactica(data):
    global resultado_gramatica
    resultado_gramatica.clear()

    for item in data.splitlines():
        if item:
            gram = parser.parse(item)
            if gram:
                resultado_gramatica.append(str(gram))
        else: print("data vacia")

    print("result: ", resultado_gramatica)
    return resultado_gramatica

if __name__ == '__main__':
    while True:
        try:
            s = input(' ingresa dato >>> ')
        except EOFError:
            continue
        if not s: continue

        # gram = parser.parse(s)
        # print("Resultado ", gram)

        prueba_sintactica(s)