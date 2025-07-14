import re
from errors import SarcasticError
from dataclasses import dataclass
from typing import List


VALID_EMOJIS = ["🤡", "💀", "😈", "😂", "😵", "🫠", "👻", "😒", "😭"]


KEYWORDS = {"int", "string", "print", "return", "try", "catch", "function", "if", "else", "while", "try", "catch", "true", "false"}
OPERATORS = {"+", "-", "*", "/", "=", "==", "!=", "<", ">", "<=", ">=", "&&", "||", "!"}
SYMBOLS = {"(", ")", "{", "}", ",", ";"}

@dataclass
class Token:
    type: str
    value: str
    line: int

    def tokenize(source_code: str) -> List["Token"]:
        open_count = source_code.count('/*')
        close_count = source_code.count('*/')
        if open_count > close_count:
            pos = source_code.rfind('/*')
            line_num = source_code[:pos].count('\n') + 1
            raise SarcasticError("unterminated_block_comment", line=line_num)
        source_code = re.sub(r'/\*.*?\*/', '', source_code, flags=re.DOTALL)
        tokens = []
        lines = source_code.splitlines()

        for line_num, raw_line in enumerate(lines, 1):
            stripped = raw_line.strip()

            if not stripped:
                continue

            is_statement_line = (
                not stripped.startswith("if") and
                not stripped.startswith("else") and
                not stripped.startswith("while") and
                not stripped.startswith("}") and
                not stripped.startswith("function") and
                (
                    "print(" in stripped or 
                    "return " in stripped or 
                    re.search(r'\w+\s*=\s*[^=]', stripped)
                )
            )
            
            if is_statement_line and not any(e in raw_line for e in VALID_EMOJIS):
                raise SarcasticError("emoji_missing", line_num)

            if is_statement_line and "//" not in raw_line:
                raise SarcasticError("missing_comment", line_num)

            
            line = raw_line
            if "//" in line:
                line = re.split(r"//", line)[0]

            line = re.sub(rf"{'|'.join(re.escape(e) for e in VALID_EMOJIS)}", "", line).strip()
            words = re.findall(r'"[^"]*"|==|!=|<=|>=|&&|\|\||[+\-*/=<>!(),{};]|[A-Za-z_]\w*|\d+', line)

            for word in words:
                if word in KEYWORDS:
                    token_type = "KEYWORD"
                elif word in OPERATORS:
                    token_type = "OPERATOR"
                elif word in SYMBOLS:
                    token_type = "SYMBOL"
                elif word.isdigit():
                    token_type = "NUMBER"
                elif word.startswith('"') and word.endswith('"'):
                    token_type = "STRING"
                elif re.match(r'[A-Za-z_]\w*', word):
                    token_type = "IDENTIFIER"
                elif word == "true":
                    token_type = "BOOLEAN"
                    word = True
                elif word == "false":
                    token_type = "BOOLEAN"
                    word = False
                else:
                    raise SarcasticError("unknown_token", word, line_num)

                tokens.append(Token(type=token_type, value=word, line=line_num))

        return tokens