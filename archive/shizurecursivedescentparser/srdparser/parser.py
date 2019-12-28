#!/bin/python
import math

__author__ = "IceArrow256"
__version__ = '2'


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
            arg.print(tab_count+1)

class Parser:
    def __init__(self, input: str):
        self.iter = 0
        self.input = input.replace(" ", "")

    def eval(self, e: Expression):
        if len(e.args) == 2:
            a = self.eval(e.args[0])
            b = self.eval(e.args[1])
            print(a, e.token, b)
            if e.token == "+":
                return a + b
            if e.token == "-":
                return a - b
            if e.token == "*":
                return a * b
            if e.token == "/":
                return a / b
            if e.token == "**":
                return a ** b
            if e.token == "mod":
                return a % b
        if len(e.args) == 1:
            a = self.eval(e.args[0])
            print(e.token, a)
            if e.token == "+":
                return +a
            if e.token == "-":
                return -a
            if e.token == "sin":
                return math.sin(a)
            if e.token == "cos":
                return math.cos(a)
            raise RuntimeError("Unknown unary operation")
        if len(e.args) == 0:
            return float(e.token)
        raise RuntimeError("Unknown expression type")


    def execute(self):
        return self.eval(self.parse())

    def parse(self):
        return self._parse_binary_expression(0)

    def _parse_token(self):
        if len(self.input) > self.iter:
            if self.input[self.iter].isdigit():
                number: str = ''
                while len(self.input) > self.iter and (self.input[self.iter].isdigit() or self.input[self.iter] == '.'):
                    number = number + self.input[self.iter]
                    self.iter += 1
                return number
            tokens = ['+', '-', '**', '*', '/', 'mod', 'abs', 'sin', 'cos', '(', ')']
            for token in tokens:
                if self.input[self.iter:self.iter + len(token)] == token:
                    self.iter += len(token)
                    return token
        return ''

    def _parse_simple_expression(self):
        token = self._parse_token()
        if not token:
            raise RuntimeError("Invalid input")
        if token[0].isdigit():
            return Expression(token)
        if token == '(':
            result = self.parse()
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
        if token == "+" or token == "-":
            return 1
        if token == "*" or token == "/" or token == "mod":
            return 2
        if token == "**":
            return 3
        return 0

