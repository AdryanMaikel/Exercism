OPERATORS = "plus", "minus", "multiplied", "divided"


def calculate(x: int, operator: str, y: int) -> int:
    match operator:
        case "plus":
            return int(x) + int(y)
        case "minus":
            return int(x) - int(y)
        case "multiplied":
            return int(x) * int(y)
        case "divided":
            return int(x) / int(y)


def answer(question: str):
    question = question.removeprefix("What is").removesuffix("?").strip()
    if len(question) == 1 and question.isdigit():
        return int(question)
    if not question:
        raise ValueError("syntax error")

    question = question.replace("by ", "")
    question_split = question.split(" ")

    if not [operator for operator in question_split if operator in OPERATORS]:
        raise ValueError("unknown operation")

    if len(question_split) < 3:
        raise ValueError("syntax error")

    x, operator, y = question_split[:3]
    if operator in OPERATORS and y[-1].isnumeric():
        result = calculate(x, operator, y)
    else:
        raise ValueError("syntax error")
    match len(question_split):
        case 3:
            return result
        case 5:
            operator, y = question_split[3:]
            result = calculate(x=result, operator=operator, y=y)
            return result
        case _:
            raise ValueError("syntax error")
