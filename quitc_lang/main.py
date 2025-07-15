from quitc_lang.core.parser import Parser
from quitc_lang.core.lexer import Token
from quitc_lang.core.interpreter import Interpreter
from quitc_lang.core.env import Environment
from quitc_lang.core.errors import SarcasticError
from rich.console import Console
from pathlib import Path

console = Console()

def run_qc_file(source_code: str, filename: str = "<stdin>"):
    console.print("[bold cyan]=== TOKENIZING ===[/]")
    tokens = Token.tokenize(source_code)
    console.print(f"[dim]Generated {len(tokens)} tokens[/]")

    console.print("[bold cyan]=== PARSING ===[/]")
    try:
        parser = Parser(tokens)
        ast = parser.parse()
        console.print(f"[green]AST successfully generated[/]")
        console.print(ast)
    except SarcasticError as e:
        console.print(f"[bold red]Parser error:[/]", e)
        return

    console.print("[bold cyan]=== INTERPRETING ===[/]")
    try:
        env = Environment()
        interpreter = Interpreter(env)
        interpreter.execute(ast)
    except SarcasticError as e:
        console.print(f"[bold red]Runtime error:[/]", e)
        return

    console.print("[bold green]=== DONE ===[/]")