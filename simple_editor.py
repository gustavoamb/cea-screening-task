import sys
import enum


class Operations(enum.Enum):
    APPEND = "1"
    DELETE = "2"
    PRINT = "3"
    UNDO = "4"


if __name__ == "__main__":
    s = ""
    states = []

    for i, e in enumerate(sys.stdin):
        if i == 0:
            continue

        line = e.rstrip()

        if line[0] is Operations.APPEND.value:
            states.append(s)
            s = s + line[2:]
        elif line[0] is Operations.DELETE.value:
            states.append(s)
            index = int(line[2:])
            s = s[:-index]
        elif line[0] is Operations.PRINT.value:
            index = int(line[2:]) - 1
            print(s[index])
        elif line[0] is Operations.UNDO.value:
            s = states.pop()
