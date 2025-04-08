from enum import Enum

class Operator(Enum):
    EQ = 0           # ==
    NE = 1           # !=
    GT = 2           # >
    GE = 3           # >=
    LT = 4           # <
    LE = 5           # <=

    def symbol(self):
        return {
            Operator.EQ: "==",
            Operator.NE: "!=",
            Operator.GT: ">",
            Operator.GE: ">=",
            Operator.LT: "<",
            Operator.LE: "<="
        }[self]

