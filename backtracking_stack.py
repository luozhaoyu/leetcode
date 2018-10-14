n = 10
m = 4
stack = []


def main():
    while True:
        if is_full_solution():
            is_acceptable()
            if has_next_solution():
                try_next_solution()
            else:
                backtrack()
            continue
        if can_expand_solution():
            expand_solution()
            continue
        break


def is_full_solution():
    return len(stack) == m


def is_acceptable():
    if len(stack) == m and stack[len(stack) - 1] < stack[len(stack) - 2]:
        print(stack)


def can_expand_solution():
    if len(stack) < m:
        return True


def expand_solution():
    stack.append(m - len(stack))


def has_next_solution():
    return stack[len(stack) - 1] + 1 < stack[len(stack) - 2]


def try_next_solution():
    stack[len(stack) - 1] += 1


def backtrack():
    global stack
    cursor = len(stack) - 1
    while stack[cursor] - stack[cursor - 1] == -1 and cursor - 1 >= 0:
        cursor -= 1
    stack = stack[:cursor+1]
    # increase one
    stack[-1] += 1
    if stack[0] > n:
        raise


main()
