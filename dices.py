import re
import numpy

from typing import Optional, Tuple


def parse(string: str) -> Optional[Tuple[int, int, int]]:
    regex = r'^(\d+)[dD](\d+)([+-]\d+)?$'
    params = re.match(regex, string.replace(' ', ''))

    if not params:
        return None

    args = params.groups()

    (count_, faces_, modifier_) = args

    count = int(count_)
    faces = int(faces_)
    modifier = int(modifier_) if modifier_ else 0

    if count <= 0 or faces <= 0:
        return None

    return count, faces, modifier


def calculate(dices: Tuple[int, int, int]) -> int:
    (count, faces, modifier) = dices

    result = 0
    for _ in range(0, count):
        result += numpy.random.randint(1, faces)

    result += modifier

    return result
