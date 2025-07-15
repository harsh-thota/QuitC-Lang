from dataclasses import dataclass
from typing import List, Any, Optional

class ASTNode:
    pass

@dataclass
class Literal(ASTNode):
    value: Any

@dataclass
class Variable(ASTNode):
    name: str

@dataclass
class BinaryOp(ASTNode):
    left: ASTNode
    operator: str
    right: ASTNode

@dataclass
class VarDeclaration(ASTNode):
    var_type: str
    name: str
    value: ASTNode

@dataclass
class Assignment(ASTNode):
    name: str
    value: ASTNode

@dataclass
class PrintStatement(ASTNode):
    value: ASTNode

@dataclass
class FunctionDef(ASTNode):
    return_type: str
    name: str
    params: List[str]
    body: List[ASTNode]

@dataclass
class FunctionCall(ASTNode):
    name: str
    args: List[ASTNode]

@dataclass
class TryCatch(ASTNode):
    try_body: List[ASTNode]
    catch_body: List[ASTNode]

@dataclass
class Program(ASTNode):
    statements: List[ASTNode]

@dataclass
class Return(ASTNode):
    value: ASTNode

@dataclass
class IfElse(ASTNode):
    condition: ASTNode
    then_branch: List[ASTNode]
    else_branch: Optional[List[ASTNode]] = None

@dataclass
class WhileLoop(ASTNode):
    condition: ASTNode
    body: List[ASTNode]

@dataclass
class TryCatch(ASTNode):
    try_body: List[ASTNode]
    catch_body: List[ASTNode]

@dataclass
class UnaryOp(ASTNode):
    operator: str
    operand: ASTNode