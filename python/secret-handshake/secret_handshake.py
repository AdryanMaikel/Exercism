CODE_COMMANDS = {0: "wink", 1: "double blink", 2: "close your eyes", 3: "jump"}


def commands(binary_str: str) -> list[str]:
    result_command = [CODE_COMMANDS[i]
                      for i, number in enumerate(reversed(binary_str[1:]))
                      if number == "1"]
    if binary_str.startswith("1"):
        result_command.reverse()
    return result_command


print(commands("01111"))
