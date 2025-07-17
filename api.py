import io
import sys
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from quitc_lang.main import run_qc_file
from quitc_lang.core.errors import SarcasticError

app = FastAPI()

@app.get("/", include_in_schema=False)
def serve_index():
    return FileResponse("web/index.html")

app.mount("/static", StaticFiles(directory="web"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class CodeRequest(BaseModel):
    code: str

@app.post("/run")
async def run_code(request: CodeRequest):
    buf = io.StringIO()
    old_stdout = sys.stdout
    sys.stdout = buf

    try:
        run_qc_file(request.code)
    except SarcasticError as e:
        sys.stdout = old_stdout
        return {"success": False, "error": str(e)}
    except Exception as e:
        sys.stdout = old_stdout
        return {"success": False, "error": f"Unexpected error: {e}"}
    finally:
        # restore stdout no matter what
        sys.stdout = old_stdout

    # strip ANSI escape sequences (Rich color codes) for clean frontend display
    import re
    raw = buf.getvalue()
    clean = re.sub(r'\x1b\[[0-9;]*m', '', raw)
    return {"success": True, "output": clean}