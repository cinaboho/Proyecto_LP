import ply.yacc as yacc
from ruby_lex import tokens

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
         | expression_slicing_indexing
         | expression_create_object
         | expression_asign_value_object
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
                        | PUTS factor
                        | DEF SYMBOL
                        | PUTS SYMBOL
    """

def p_expression_assign(p):
    """
    expression_assign : SYMBOL ASIGN factor
                      | SYMBOL ASIGN LBRA factor_list RBRA
                      | SYMBOL ASIGN LPAREN factor_list RPAREN
    """

def p_expression_math(p):
    """
    expression_math : factor operator_math factor
                    | expression_math operator_math factor
    """

def p_expression_slicing_indexing(p):
    """
    expression_slicing_indexing : SYMBOL LBRA NUMBER RBRA
                       | SYMBOL LBRA NUMBER COMMA NUMBER RBRA
                       | SYMBOL DOT FIRST
                       | SYMBOL DOT LAST
    """

def p_expression_create_object(p):
    """
    expression_create_object : SYMBOL ASIGN SYMBOL DOT NEW
                             | SYMBOL ASIGN STRUCT DOT NEW LPAREN factor_list RPAREN
    """

def p_expression_asign_value_object(p):
    """
    expression_asign_value_object : SYMBOL DOT SYMBOL ASIGN factor
    """

def p_factor_list(p):
    """
    factor_list : factor COMMA factor
                | factor_list COMMA factor
    """

def p_factor(p):
    """ factor : NUMBER
               | DECIMAL
               | SYMBOL
               | TEXT
               | ATTRIBUTE
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

def p_error(p):
    if p:
        print(p)
        print("Error sintactico")
    else:
        print("Error lexico")

parser = yacc.yacc()

def validate(expr):
    print(expr)
    return parser.parse(expr)


validate("#comentario")  # correcto

validate("x = 1")  # correcto

validate("$x = 1")  # correcto

validate("2 + 1 * f")  # correcto

validate("unless x == c")  # correcto

validate("when 0 .. 2")  # correcto

validate("elsif a > b and c <= d or true")  # correcto

validate("if a > b and c <= d or true")  # correcto

validate("puts \"I cant guess the number\"")  # correcto

validate("o0111@")

validate("a = [uno, dos, tres]")

validate("arr = ['a', 'b', 'c']")

validate("tupla = ('a', 'b', 'c')")

validate("array[1]")

validate("array[0,5]")

validate("array.first")

validate("array.last")

validate("person = struct.new(:name, :age)")

validate("person1 = person.new")

validate("person1.name = \"Nombre\"")

validate("person1.age = 70")

validate("person1.pension = 300")