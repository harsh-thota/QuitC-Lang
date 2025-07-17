import typer
import uvicorn
from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from rich.syntax import Syntax
from rich.text import Text
from rich.traceback import install
from quitc_lang.core.errors import SarcasticError
from quitc_lang.main import run_qc_file

app = typer.Typer(help="CLI for the QuitC Language")
console = Console()
install()

@app.command()
def run(file: str):
    """Run a .qc file"""
    path = Path(file)
    if not path.exists() or not path.suffix == ".qc":
        console.print("[bold red]❌ File not found or not a .qc file[/]")
        raise typer.Exit(1)
    
    try:
        code = path.read_text(encoding="utf-8")
        syntax = Syntax(code, "c", theme="monokai", line_numbers=True)
        console.print(Panel(syntax, title=f"[bold cyan]{path.name}"))

        run_qc_file(code, str(path))
    except SarcasticError as e:
        console.print(Panel(str(e), title="💀 [bold red]Sarcastic QuitC Error[/]", style="bold red"))
        raise typer.Exit(code=1)
    except Exception as e:
        console.print(f"[bold red]💥 Execution failed:[/] {e}")
        raise typer.Exit(code=1)

@app.command()
def version():
    """Show CLI Version"""
    console.print("[bold cyan]QuitC CLI v0.1[/]")
    
if __name__ == "__main__":
    app()
    uvicorn.run("api:app", host="127.0.0.1", port=8000, reload=True)