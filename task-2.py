from collections import deque
from re import sub


def is_polyndrom(line: str) -> bool:
    queue = deque([char for char in sub(r"[^\w]", "", line)])
    while len(queue) > 1:
        left_edge = queue.popleft().lower()
        right_edge = queue.pop().lower()
        if left_edge != right_edge:
            return False
    return True

print(is_polyndrom("Aaaa"))
print(is_polyndrom("Шалаш"))
print(is_polyndrom("А роза упала на лапу Азора"))