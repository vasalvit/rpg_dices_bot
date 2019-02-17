import re
import numpy

from typing import Tuple

minimal_dices_count = 1
maximal_dices_count = 100

minimal_faces_count = 2
maximal_faces_count = 1000000


class InvalidFormat(Exception):
    format = ''

    def __init__(self, format):
        self.format = format


class InvalidDicesCount(Exception):
    dices = 0

    def __init__(self, dices):
        self.dices = dices


class InvalidFacesCount(Exception):
    faces = 0

    def __init__(self, faces):
        self.faces = faces


def parse(string: str) -> Tuple[int, int, int]:
    regex = r'^(\d+)[dD](\d+)([+-]\d+)?$'
    params = re.match(regex, string.replace(' ', ''))

    if not params:
        raise InvalidFormat(string)

    args = params.groups()

    (dices_, faces_, modifier_) = args

    dices = int(dices_)
    faces = int(faces_)
    modifier = int(modifier_) if modifier_ else 0

    if dices < minimal_dices_count or maximal_dices_count < dices:
        raise InvalidDicesCount(dices)

    if faces < minimal_faces_count or maximal_faces_count < faces:
        raise InvalidFacesCount(faces)

    return dices, faces, modifier


def calculate(dices: Tuple[int, int, int]) -> int:
    (count, faces, modifier) = dices

    result = 0
    for _ in range(0, count):
        result += numpy.random.randint(1, faces)

    result += modifier

    return result
