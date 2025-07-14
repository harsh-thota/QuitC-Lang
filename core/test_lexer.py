from lexer import Token
from env import Environment
from parser import Parser
from interpreter import Interpreter

source_code = """
int x = 5 🤡 // declare x
print(x) 😂 // show x

function int double(n) {
  return n * 2 🤡 // double it
}

int result = double(4) 🤡 // should be 8
print(result) 😂 // print 8

int z = 5 🤡 // test value
if (z > 3) {
  print("yes") 😂 //yep, it's true
} else {
  print("no") 😭 //no, its not!
}
"""

print("=== TOKENIZING ===")
tokens = []
try:
    tokens = Token.tokenize(source_code)
    print(f"Generated {len(tokens)} tokens:")
    for token in tokens:
        print(f"  {token}")
except Exception as e:
    print(f"Tokenizer error: {e}")

print("\n=== PARSING ===")
ast = None
try:
    parser = Parser(tokens)
    ast = parser.parse()
    print(f"AST: {ast}")
except Exception as e:
    print(f"Parser error: {e}")

print("\n=== INTERPRETING ===")
try:
    if ast is not None:
        env = Environment()
        interpreter = Interpreter(env)
        interpreter.execute(ast)
    else:
        print("Skipping interpretation - no valid AST")
except Exception as e:
    print(f"Interpreter error: {e}")

print("\n=== DONE ===")