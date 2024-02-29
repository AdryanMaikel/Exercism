from operator import add, sub, mul, truediv

OPERATORS = {"plus": add, "minus": sub, "multiplied": mul, "divided": truediv}


def answer(question: str) -> int | None:
    question = question.removeprefix("What is").removesuffix("?").strip()
    if len(question) == 1 and question.isdigit():
        return int(question)
    if not question:
        raise ValueError("syntax error")

    question = question.replace("by ", "")
    question_split = question.split()

    content_operators = [operator for operator in question_split
                         if operator in OPERATORS]
    if not any(content_operators):
        raise ValueError("unknown operation")

    if len(question_split) < 3:
        raise ValueError("syntax error")

    x = question_split.pop(0)
    operator = question_split.pop(0)
    y = question_split.pop(0)

    if operator in OPERATORS and y[-1].isnumeric():
        result = OPERATORS[operator](int(x), int(y))
    else:
        raise ValueError("syntax error")

    while question_split:
        try:
            operator = question_split.pop(0)
            y = question_split.pop(0)
            result = OPERATORS[operator](result, int(y))
        except Exception:
            raise ValueError("syntax error")

    return result
