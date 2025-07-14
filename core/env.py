from errors import SarcasticError

class Environment:
    MAX_VARIABLES = 5

    def __init__(self):
        self.vars = {}
        self.funcs = {}
    
    def declare_variable(self, name: str, value):
        if name in self.vars:
            raise SarcasticError("redeclare_var", name)
        if len(self.vars) >= self.MAX_VARIABLES:
            raise SarcasticError("too_many_vars", name)
        self.vars[name] = value
    
    def assign_variable(self, name: str, value):
        if name not in self.vars:
            raise SarcasticError("undefined_var", name)
        self.vars[name] = value

    def get_variable(self, name: str):
        if name not in self.vars:
            raise SarcasticError("undefined_var", name)
        return self.vars[name]
    
    def declare_functions(self, name: str, func_def_node):
        if name in self.funcs:
            raise SarcasticError("redeclare_func", name)
        self.funcs[name] = func_def_node

    def get_function(self, name: str):
        if name not in self.funcs:
            raise SarcasticError("undefined_func", name)
        return self.funcs[name]