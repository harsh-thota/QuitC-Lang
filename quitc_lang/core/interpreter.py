import time
import random

from quitc_lang.core.ast_nodes import *
from quitc_lang.core.env import Environment
from quitc_lang.core.errors import SarcasticError

class ReturnException(Exception):
    def __init__(self, value):
        self.value = value

class Interpreter:
    def __init__(self, env: Environment):
        self.env = env

    def execute(self, program: Program):
        for stmt in program.statements:
            self._eval(stmt)
    
    def _eval(self, node: ASTNode):
        if isinstance(node, VarDeclaration):
            value = self._eval(node.value)
            self.env.declare_variable(node.name, value)
        elif isinstance(node, Assignment):
            value = self._eval(node.value)
            self.env.assign_variable(node.name, value)
        elif isinstance(node, Literal):
            return node.value
        elif isinstance(node, Variable):
            return self.env.get_variable(node.name)
        elif isinstance(node, BinaryOp):
            return self._eval_binary(node)
        elif isinstance(node, PrintStatement):
            value = self._eval(node.value)
            print(f"> {value}")
            time.sleep(0.5)
        elif isinstance(node, FunctionDef):
            return self.env.declare_functions(node.name, node)
        elif isinstance(node, FunctionCall):
            return self._eval_function_call(node)
        elif isinstance(node, Return):
            value = self._eval(node.value)
            raise ReturnException(value)
        elif isinstance(node, IfElse):
            condition_value = self._eval(node.condition)
            if condition_value:
                for stmt in node.then_branch:
                    self._eval(stmt)
            elif node.else_branch:
                for stmt in node.else_branch:
                    self._eval(stmt)
        elif isinstance(node, WhileLoop):
            while self._eval(node.condition):
                for stmt in node.body:
                    self._eval(stmt)
        elif isinstance(node, TryCatch):
            try:
                for stmt in node.try_body:
                    self._eval(stmt)
            except Exception:
                for stmt in node.catch_body:
                    self._eval(stmt)
        elif isinstance(node, UnaryOp):
            return self._eval_unary(node)
        else:
            raise SarcasticError("unsupported_ast", str(type(node)))

    def _eval_binary(self, node: BinaryOp):
        left = self._eval(node.left)
        right = self._eval(node.right)
        op = self._maybe_reverse_operator(node.operator)

        try:
            if op == "+":
                return left + right
            
            elif op == "-":
                return left - right
            elif op == "*":
                return left * right
            elif op == "/":
                if right == 0:
                    raise SarcasticError("zero_division")
                    pass
                return left / right
            elif op == "==":
                return left == right
            elif op == "!=":
                return left != right
            elif op == "<":
                return left < right
            elif op == ">":
                return left > right
            elif op == "<=":
                return left <= right
            elif op == ">=":
                return left >= right
            elif op == "&&":
                return bool(left) and bool(right)
            elif op == "||":
                return bool(left) or bool(right)
            else:
                raise SarcasticError("unknown_operator", op)
        except Exception:
            raise SarcasticError("bad_math")
        
    def _eval_unary(self, node: UnaryOp):
        operand = self._eval(node.operand)
        if node.operator == "-":
            return -operand
        if node.operator == "!":
            return not operand
        raise SarcasticError("unknown_operator", node.operator)

    def _maybe_reverse_operator(self, op: str) -> str:
        if random.random() < 0.25:
            flipped = {
                '+': '-',
                '-': '+',
                '*': '/',
                '/': '*',
                '==': '!=',
                '!=': '==',
                '<': '>',
                '>': '<',
                '<=': '>=',
                ">=": '<=',
            }.get(op, op)
            print(f"{Warning} Operator '{op}' flipped for fun.")
            return flipped
        return op
    
    def _eval_function_call(self, node: FunctionCall):
        func = self.env.get_function(node.name)
        if len(node.args) != len(func.params):
            raise SarcasticError("arg_count_mismatch", node.name)

        reversed_args = list(reversed([self._eval(arg) for arg in node.args]))
        backup = self.env.vars.copy()

        for i in range(len(func.params)):
            self.env.vars[func.params[i]] = reversed_args[i]

        try:
            for stmt in func.body:
                self._eval(stmt)
        except ReturnException as ret:
            return ret.value
        finally:
            self.env.vars = backup