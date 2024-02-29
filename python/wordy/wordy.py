from operator import add, sub, mul, truediv

OPERATORS = {"plus": add, "minus": sub, "multiplied": mul, "divided": truediv}


def answer(question: str) -> int:
    question = question.removeprefix("What is").removesuffix("?").strip()
    if len(question) == 1 and question.isdigit():
        return int(question)
    if not question:
        raise ValueError("syntax error")

    question = question.replace("by ", "")
    question_split = question.split()

    if not any(map(lambda operator: operator in OPERATORS, question_split)):
        raise ValueError("unknown operation")

    if len(question_split) < 3:
        raise ValueError("syntax error")

    x, operator, y = question_split[:3]
    if operator in OPERATORS and y[-1].isnumeric():
        result = OPERATORS[operator](int(x), int(y))
    else:
        raise ValueError("syntax error")
    match len(question_split):
        case 3:
            return result
        case 5:
            operator, y = question_split[3:]
            result = OPERATORS[operator](result, int(y))
            return result
        case _:
            raise ValueError("syntax error")
