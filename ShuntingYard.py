# https://en.wikipedia.org/wiki/Shunting_yard_algorithm
# comes with a simple parser and evaluator to demonstrate shunting yard's use.

import operator
from collections import deque
from dataclasses import dataclass
from decimal import Decimal
from enum import Enum, auto
from string import digits, whitespace
from typing import Callable, Generator, Protocol

operators = "+-*/"

precedence = ["-", "+", "/", "*"]


class TokenKind(Enum):
    NUMBER = auto()
    OPERATOR = auto()
    LEFT_PAREN = auto()
    RIGHT_PAREN = auto()


class OperatorFn(Protocol):
    """An operator that can be called on an arbitrary set of numbers."""

    def __call__(self, *args: float) -> float:
        ...


@dataclass(frozen=True)
class Token:
    kind: TokenKind
    number: float | None = None
    operator: OperatorFn | None = None
    precedence: int = 0


class ParseError(Exception):
    """Raised if parsing fails."""


class EvalError(Exception):
    """Raised if evaluation fails."""


class Parser:
    def __init__(self, expression: str) -> None:
        self.input = expression
        self.pos = 0

    def next_char(self) -> str:
        return self.input[self.pos]

    def consume_char(self) -> str:
        c = self.next_char()
        self.pos += 1
        return c

    def consume_while(self, test: Callable[[str], bool]) -> str:
        chars = []
        while self.pos < len(self.input):
            c = self.next_char()
            if not test(c):
                break
            chars.append(self.consume_char())
        return "".join(chars)

    def parse_number(self) -> float:
        return float(self.consume_while(lambda c: c in digits or c == "."))

    def parse_operator(self) -> OperatorFn:
        match self.consume_char():
            case "+":
                return operator.add
            case "-":
                return operator.sub
            case "*":
                return operator.mul
            case "/":
                return operator.truediv
            case op:
                raise ParseError(f"unknown operator: {op}")

    def parse(self) -> Generator[Token, None, None]:
        while self.pos < len(self.input):
            match self.next_char():
                case c if c in digits:
                    yield Token(kind=TokenKind.NUMBER, number=self.parse_number())
                case c if c in operators:
                    yield Token(
                        kind=TokenKind.OPERATOR,
                        operator=self.parse_operator(),
                        precedence=precedence.index(c),
                    )
                case c if c in whitespace:
                    self.consume_char()
                case "(":
                    self.consume_char()
                    yield Token(kind=TokenKind.LEFT_PAREN)
                case ")":
                    self.consume_char()
                    yield Token(kind=TokenKind.RIGHT_PAREN)
                case c:
                    raise ParseError(
                        f"unexpected character at position {self.pos}: {c}"
                    )


def shunting_yard(tokens: list[Token]) -> list[Token]:
    """
    Order the given tokens into a stack ready for evaluation.
    """
    output = deque()
    op_stack = []
    for token in tokens:
        match token.kind:
            case TokenKind.NUMBER:
                output.appendleft(token)
            case TokenKind.OPERATOR:
                while op_stack:
                    top = op_stack[-1]
                    if top.kind != TokenKind.LEFT_PAREN and (
                        top.precedence >= token.precedence
                    ):
                        output.appendleft(op_stack.pop())
                    else:
                        break
                op_stack.append(token)
            case TokenKind.LEFT_PAREN:
                op_stack.append(token)
            case TokenKind.RIGHT_PAREN:
                while True:
                    if not op_stack:
                        raise EvalError("mismatched parentheses")

                    if op_stack[-1].kind == TokenKind.LEFT_PAREN:
                        break

                    output.appendleft(op_stack.pop())

                if op_stack[-1].kind != TokenKind.LEFT_PAREN:
                    raise EvalError("mismatched parentheses")

                # discard the left paren
                op_stack.pop()

    while op_stack:
        top = op_stack.pop()
        if top.kind == TokenKind.LEFT_PAREN:
            raise EvalError("mismatched parentheses")
        output.appendleft(top)

    return list(output)


def evaluate(tokens: list[Token]) -> float:
    """
    Evaluate the given token stack as provided by shunting yard.
    """
    stack = []

    while tokens:
        token = tokens.pop()
        match token.kind:
            case TokenKind.NUMBER:
                stack.append(token.number)
            case TokenKind.OPERATOR:
                try:
                    b = stack.pop()
                    a = stack.pop()
                except IndexError as ex:
                    raise EvalError("wrong number of arguments") from ex

                stack.append(token.operator(a, b))

    if len(stack) != 1:
        raise EvalError("wrong number of arguments")

    return stack[0]


if __name__ == "__main__":
    print("enter an expression to evaluate")
    print("ctrl-d to exit")
    while True:
        # get input
        try:
            expression = input("> ")
        except EOFError:
            print("\nbye")
            break
        except KeyboardInterrupt:
            print()
            continue

        # parse
        try:
            tokens = list(Parser(expression).parse())
        except ParseError as ex:
            print(f"\nparse error: {ex}")
            continue

        # order with shunting yard
        try:
            tokens = shunting_yard(tokens)
        except EvalError as ex:
            print(f"evaluation error: {ex}")
            continue

        # evaluate
        try:
            result = evaluate(tokens)
        except EvalError as ex:
            print(f"evaluation error: {ex}")
            continue

        print(Decimal(result).normalize())
