from lexer import Token
from parser import Parser

source_code = """
int x = 5 🤡 // declare x
print(x) 😂 // show x
"""

tokens = Token.tokenize(source_code)
parser = Parser(tokens)
ast = parser.parse()


for token in tokens:
    print(token)

print(ast)