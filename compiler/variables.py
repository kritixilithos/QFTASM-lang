from tree_builder.tree_builder import GrammarTree

class VariableStore:
    def __init__(self):
        self._vars = {}

    def __contains__(self, item):
        return VariableStore.get_name(item) in self._vars

    def __getitem__(self, item):
        return self._vars[VariableStore.get_name(item)]

    @staticmethod
    def get_name(var: GrammarTree):
        return var[var["_block_name"]]["name"]

    def add_var(self, var: GrammarTree):
        rtn = Variable(var)
        self._vars[var["name"]] = rtn
        return rtn


class Variable:
    def __init__(self, var: GrammarTree):
        self.type = var["type"]
        self.name = var["name"]
        self.is_pointer = var["_block_name"] == "pointer_type"
        self.is_global = var["_global"]

    def __str__(self):
        return self.name

    def __repr__(self):
        rtn = []
        if self.is_global:
            rtn.append("global ")
        if self.is_pointer:
            rtn.append("*")
        rtn.append(self.type+" ")
        rtn.append(self.name)
        return "".join(rtn)