import ply.yacc as yacc
from ProyectoLP.ruby_lex import tokens

# resultado del analisis
resultado_gramatica = []
nombres = {}
def p_body(p):
    """
    body : comment
         | statement_if_unless
         | expression_function
         | expression_assign
         | expression_when
         | expression_math
    """


def p_statement_if_unless(p):
    """ statement_if_unless : IF expression_comp
                     | UNLESS expression_comp
                     | ELSIF expression_comp
    """

def p_expression_comp(p):
    """
    expression_comp : statement_comp
                    | expression_comp AND statement_comp
                    | expression_comp OR statement_comp
    """

def p_expression_when(p):
    """
    expression_when : WHEN NUMBER DDOT NUMBER
    """

def p_statement_comp(p):
    """ statement_comp : factor GT factor
              | factor LT factor
              | factor GEQT factor
              | factor LEQT factor
              | factor EQUAL factor
              | factor_boolean
    """

def p_expression_function(p):
    """
    expression_function : PUTS TEXT
                        |  PUTS factor
                        |  DEF SYMBOL
    """

def p_expression_assign(p):
    """
    expression_assign : factor ASIGN factor
    """

def p_expression_math(p):
    """
    expression_math : factor operator_math factor
    """

def p_factor(p):
    """ factor : NUMBER
                | DECIMAL
                | SYMBOL
    """

def p_factor_boolean(p):
    """ factor_boolean : TRUE
           | FALSE
    """

def p_operator_math(p):
    """ operator_math : PLUS
                  | MINUS
                  | TIMES
                  | DIVIDED
    """

def p_comment(p):
    """ comment : COMMENT
    """

parser = yacc.yacc()

'''
while True:
    try:
        s = input('parser > ')  
    except EOFError:
        break
    parser.parse(s)
'''

def p_error(t):
    global resultado_gramatica
    if t:
        resultado = "Error sintactico de tipo {} en el valor {}".format(str(t.type), str(t.value))
        print(resultado)
    else:
        resultado = "Error sintactico {}".format(t)
        print(resultado)
    resultado_gramatica.append(resultado)

def validate(expr):

    global resultado_gramatica
    resultado_gramatica.clear()

    for item in expr.splitlines():
        if item:
            gram = parser.parse(item)
            if gram:
                resultado_gramatica.append(str(gram))
        else:
            print("data vacia")

    print("result: ", resultado_gramatica)
    return resultado_gramatica


print("#comentario")
validate("#comentario")  # correcto

print("x = 1")
validate("x = 1")  # correcto

print("$x = 1")
validate("$x = 1")  # correcto

print("2 + 1 - f")
validate("2 + 1 - f")  # correcto

print("unless x == c")
validate("unless x == c")  # correcto

print("when 0 .. 2")
validate("when 0 .. 2")  # correcto

print("elsif a > b and c <= d or true")
validate("elsif a > b and c <= d or true")  # correcto

print("if a > b and c <= d or true")
validate("if a > b and c <= d or true")  # correcto

print("puts \"I cant guess the number\"")
validate("puts \"I cant guess the number\"")  # correcto

print("o0111@")
validate("o0111@")