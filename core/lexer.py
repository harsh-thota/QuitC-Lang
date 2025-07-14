import re
# from errors import SarcasticError
from dataclasses import dataclass
from typing import List


VALID_EMOJIS = ["🤡", "💀", "😈", "😂", "😵", "🫠", "👻", "😒"]


KEYWORDS = {"int", "string", "print", "return", "try", "catch", "return", "function"}
OPERATORS = {"+", "-", "*", "/", "=", "==", "!=", "<", ">", "<=", ">="}
SYMBOLS = {"(", ")", "{", "}", ",", ";"}

@dataclass
class Token:
    type: str
    value: str
    line: int

    def tokenize(source_code: str) -> List["Token"]:
        tokens = []
        lines = source_code.splitlines()

        for line_num, raw_line in enumerate(lines, 1):
            line = raw_line.strip()

            if not line:
                continue

            if not any(line.endswith(e) for e in VALID_EMOJIS):
                # raise SarcasticError("emoji_missing", line_num)
                pass
            
            if "//" not in line:
                # raise SarcasticError("missing_comment", line_num)
                pass
            
            line = re.split(r"//", line)[0].strip()
            line = re.sub(rf"{'|'.join(re.escape(e) for e in VALID_EMOJIS)}$", "", line).strip()


            words = re.findall(r'[A-Za-z_]\w*|\d+|==|!=|<=|>=|[+\-*/=<>(),{};"]', line)

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
                else:
                    # raise SarcasticError("unknown_token", word, line_num)
                    pass
                
                tokens.append(Token(type=token_type, value=word, line=line_num))

        return tokens