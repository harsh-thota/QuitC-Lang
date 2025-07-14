from lexer import Token
from ast_nodes import *
from errors import SarcasticError

from typing import List

class Parser:
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.pos = 0
    
    def parse(self) -> Program:
        statements = []
        while not self._is_at_end():
            stmt = self._parse_statement()
            statements.append(stmt)
        return Program(statements=statements)
    
    def _parse_statement(self):
        if self._match("KEYWORD", "function"):
                return self._parse_function_def()
        elif self._match("KEYWORD", "int") or self._match("KEYWORD", "string"):
            return self._parse_var_declaration()
        elif self._match("KEYWORD", "print"):
            return self._parse_print()
        elif self._peek().type == "IDENTIFIER" and self._peek(1).value == "=":
            return self._parse_assignment()
        elif self._match("KEYWORD", "return"):
            return self._parse_return()
        elif self._match("KEYWORD", "if"):
            return self._parse_if_else()
        elif self._match("KEYWORD", "try"):
            return self._parse_try_catch()
        elif self._match("KEYWORD", "while"):
            return self._parse_while()
        elif self._match("KEYWORD", "try"):
            return self._parse_try_catch()
        else:
            return self._parse_expression()
        
    def _parse_var_declaration(self):
        var_type = self._previous().value
        name = self._consume("IDENTIFIER").value
        self._consume("OPERATOR", "=")
        value = self._parse_expression()
        return VarDeclaration(var_type, name, value)
    
    def _parse_assignment(self):
        name = self._consume("IDENTIFIER").value
        self._consume("OPERATOR", "=")
        value = self._parse_expression()
        return Assignment(name, value)
    
    def _parse_print(self):
        self._consume("SYMBOL", "(")
        value = self._parse_expression()
        self._consume("SYMBOL", ")")
        return PrintStatement(value)
    
    def _parse_function_def(self):
        return_type = self._consume("KEYWORD").value
        name = self._consume("IDENTIFIER").value
        self._consume("SYMBOL", "(")

        params = []
        if not self._check("SYMBOL", ")"):
            params.append(self._consume("IDENTIFIER").value)
            while self._match("SYMBOL", ","):
                params.append(self._consume("IDENTIFIER").value)
        self._consume("SYMBOL", ")")

        body = self._parse_block()
        return FunctionDef(return_type, name, params, body)
    
    def _parse_return(self):
        value = self._parse_expression()
        return Return(value)
    
    def _parse_if_else(self):
        self._consume("SYMBOL", "(")
        condition = self._parse_expression()
        self._consume("SYMBOL", ")")

        then_branch = self._parse_block()
        else_branch = None

        if self._match("KEYWORD", "else"):
            else_branch = self._parse_block()
        
        return IfElse(condition, then_branch, else_branch)
    
    def _parse_while(self):
        self._consume("SYMBOL", "(")
        condition = self._parse_expression()
        self._consume("SYMBOL", ")")
        body = self._parse_block()
        return WhileLoop(condition, body)
    
    def _parse_block(self) -> List[ASTNode]:
        self._consume("SYMBOL", "{")
        statements = []
        while not self._check("SYMBOL", "}"):
            stmt = self._parse_statement()
            statements.append(stmt)
        self._consume("SYMBOL", "}")
        return statements
    
    def _parse_try_catch(self) -> TryCatch:
        try_body = self._parse_block()
        if not self._match("KEYWORD", "catch"):
            current = self._peek()
            raise SarcasticError("expected_token", "catch", current.line)
        catch_body = self._parse_block()
        return TryCatch(try_body=try_body, catch_body=catch_body)
    
    def _parse_unary(self):
        token = self._peek()
        if token.type == "OPERATOR" and token.value in ("-", "!"):
            operator = self._advance().value
            operand = self._parse_unary()
            return UnaryOp(operator, operand)
        return self._parse_primary()

    def _parse_expression(self):
        return self._parse_binary_op()
    
    def _parse_binary_op(self):
        expr = self._parse_unary()
        while self._match("OPERATOR"):
            operator = self._previous().value
            right = self._parse_primary()
            expr = BinaryOp(expr, operator, right)
        return expr
    
    def _parse_primary(self):
        token = self._peek()

        if token.type == "NUMBER":
            self._advance()
            return Literal(int(token.value))
        
        if token.type == "STRING":
            self._advance()
            return Literal(str(token.value))
        
        if token.type == "IDENTIFIER":
            if self._peek(1).value == "(":
                return self._parse_function_call()
            else:
                self._advance()
                return Variable(token.value)
        
        raise SarcasticError("unexpected_token", token.value, token.line)
    
    def _parse_function_call(self):
        name = self._consume("IDENTIFIER").value
        self._consume("SYMBOL", "(")
        args = []

        if not self._check("SYMBOL", ")"):
            args.append(self._parse_expression())
            while self._match("SYMBOL", ","):
                args.append(self._parse_expression())

        self._consume("SYMBOL", ")")
        return FunctionCall(name, args)
    
    def _match(self, expected_type, expected_value = None):
        if self._is_at_end():
            return False
        token = self._peek()
        if token.type != expected_type:
            return False
        if expected_value is not None and token.value != expected_value:
            return False
        
        self._advance()
        return True
    
    def _check(self, expected_type, expected_value = None, offset=0):
        if self.pos + offset >= len(self.tokens):
            return False
        token = self.tokens[self.pos + offset]
        if token.type != expected_type:
            return False
        if expected_value is not None and token.value != expected_value:
            return False
        
        return True
    
    def _consume(self, expected_type = None, expected_value = None):
        if self._is_at_end():
            raise SarcasticError("unexpected_eof", None, self._peek().line)
            pass
        
        token = self._peek()
        if expected_type and token.type != expected_type:
            raise SarcasticError("expected_token", expected_type, token.line)
            pass
        if expected_value and token.value != expected_value:
            raise SarcasticError("expected_value", expected_value, token.line)
            pass
        
        return self._advance()
    
    def _advance(self):
        if not self._is_at_end():
            self.pos += 1
        return self.tokens[self.pos - 1]
    
    def _peek(self, offset=0):
        if self.pos + offset >= len(self.tokens):
            return self.tokens[-1]
        return self.tokens[self.pos + offset]
    
    def _previous(self):
        return self.tokens[self.pos - 1]
    
    def _is_at_end(self):
        return self.pos >= len(self.tokens)