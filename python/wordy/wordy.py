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

    if not any(operator in OPERATORS for operator in question_split):
        raise ValueError("unknown operation")

    if len(question_split) < 3:
        raise ValueError("syntax error")

    iter_question = iter(question_split)

    try:
        result = int(next(iter_question))
    except Exception:
        raise ValueError("syntax error")
    while True:
        try:
            operator = next(iter_question)
            if operator not in OPERATORS:
                raise ValueError("syntax error")

            y = next(iter_question)
            try:
                y = int(y)
            except Exception:
                raise ValueError("syntax error")

            result = OPERATORS[operator](int(result), y)
        except StopIteration:
            break
    return result


print(answer("What is 1 plus four?"))
