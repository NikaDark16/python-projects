import rikaset.set as S

__author__ = "IceArrow256"
__version__ = '4'


class Expression:
    def __init__(self, token: str, args=None):
        if args is None:
            args = []
        self.args = args
        self.token = token

    def print(self, tab_count=0):
        tab = ""
        for i in range(tab_count):
            tab += "\t"
        print(tab + self.token)
        for arg in self.args:
            arg.print(tab_count + 1)


class SetsCalculator:
    def __init__(self, input_expression: str = ''):
        self.input = input_expression.replace(' ', '')
        self.iter = 0
        self.step = 1
        self.tokens = ['u', 'n', '\\', '+', '_', '(', ')']
        self._sets = None
        self.solution = []

    @property
    def sets(self):
        i = 0
        sets = {}
        while len(self.input) > i:
            if self.input[i].isupper():
                name: str = ''
                while len(self.input) > i and self.input[i].isupper():
                    name += self.input[i]
                    i += 1
                sets[name] = S.Set(name, set())
            else:
                i += 1
        return sets

    @sets.setter
    def sets(self, sets=None):
        if sets is None:
            sets = {}
        sets["U"] = S.Set("U", set())
        for s in sets:
            if s != "U":
                sets['U'] = sets["U"].union(sets[s])
        self._sets = sets

    def execute(self):
        self.solution.clear()
        if not self._sets:
            self.set_sets(self.get_sets())
        return self._eval(self._parse())

    def _get_current_operation(self):
        return str(self.step) + ')'

    def _parse(self):
        return self._parse_binary_expression(0)

    def _eval(self, e: Expression):
        if len(e.args) == 2:
            a: S.Set = self._eval(e.args[0])
            b: S.Set = self._eval(e.args[1])
            solution_step = {"n": a.name + " " + e.token + " " + b.name,
                             "s": str(a) + " " + e.token + " " + str(b)}
            self.step += 1
            if e.token == "u":
                result = a.union(b)
            if e.token == "n":
                result = a.intersection(b)
            if e.token == "\\":
                result = a.difference(b)
            if e.token == "+":
                result = a.symmetric_difference(b)
            solution_step["r"] = "Result : " + str(result)
            solution_step["v"] = result.venn_set
            self.solution.append(solution_step)
            return result
        if len(e.args) == 1:
            a = self._eval(e.args[0])
            solution_step = {"n": e.token + "(" + a.name + ")",
                             "s": e.token + "(" + str(a) + ")"}
            self.step += 1
            if e.token == "_":
                result = a.addition(self._sets['U'])
                solution_step["r"] = "Result : " + str(result)
                solution_step["v"] = result.venn_set
                self.solution.append(solution_step)
                return result
            raise RuntimeError("Unknown unary operation")
        if len(e.args) == 0:
            return self._sets[e.token]
        raise RuntimeError("Unknown expression type")

    def _parse_token(self):
        if len(self.input) > self.iter:
            if self.input[self.iter].isupper():
                name: str = ''
                while len(self.input) > self.iter and self.input[self.iter].isupper():
                    name += self.input[self.iter]
                    self.iter += 1
                return name

            for token in self.tokens:
                if self.input[self.iter:self.iter + len(token)] == token:
                    self.iter += len(token)
                    return token
        return ''

    def _parse_simple_expression(self):
        token = self._parse_token()
        if not token:
            raise RuntimeError("Invalid input")
        if token[0].isupper():
            return Expression(token)
        if token == '(':
            result = self._parse()
            if self._parse_token() != ')':
                raise RuntimeError("Expected ')'")
            return result

        return Expression(token, [self._parse_simple_expression()])

    def _parse_binary_expression(self, min_priority: int):
        left_expr = self._parse_simple_expression()

        while True:
            op = self._parse_token()
            priority = self._get_priority(op)
            if priority <= min_priority:
                self.iter -= len(op)
                return left_expr
            right_expr = self._parse_binary_expression(priority)
            left_expr = Expression(op, [left_expr, right_expr])

    def _get_priority(self, token):
        if token in ['_', 'u', '\\', 'n', '+']:
            return 1
        return 0
