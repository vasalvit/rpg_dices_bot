import re

from typing import Optional, Tuple


def parse(string: str) -> Optional[Tuple[int, int, int]]:
    regex = r'^(\d+)[dD](\d+)([+-]\d+)?$'
    params = re.match(regex, string.replace(' ', ''))

    if not params:
        return None

    args = params.groups()

    (count, faces, modifier) = args

    # count = int(args[0])
    # faces = int(args[1])
    # modifier = int(args[2]) if len(args)

    return int(count), int(faces), int(modifier) if modifier else 0


if __name__ == '__main__':
    import unittest


    class TestParse(unittest.TestCase):
        def test_fail_for_empty_string(self):
            self.assertIsNone(parse(''))

        def test_fail_without_count(self):
            self.assertIsNone(parse('d2'))

        def test_fail_if_count_is_not_number(self):
            self.assertIsNone(parse('x'))
            self.assertIsNone(parse('2x'))

        def test_fail_without_D(self):
            self.assertIsNone(parse('2'))

        def test_fail_without_faces(self):
            self.assertIsNone(parse('2d'))

        def test_fail_if_faces_is_not_number(self):
            self.assertIsNone(parse('2dx'))

        def test_fail_without_modifier_sign(self):
            self.assertIsNone(parse('2d4x'))

        def test_fail_if_modifier_is_not_number(self):
            self.assertIsNone(parse('2d4+x'))

        def test_fail_if_there_is_tail(self):
            self.assertIsNone(parse('2d4+6x'))

        def test_fail_for_count_with_sign(self):
            self.assertIsNone(parse('+2d4+6'))

        def test_fail_for_negative_count(self):
            self.assertIsNone(parse('-2d4+6'))

        def test_fail_for_faces_with_sign(self):
            self.assertIsNone(parse('2d+4+6'))

        def test_fail_for_negative_faces(self):
            self.assertIsNone(parse('2d+4+6'))

        def test_ignore_spaces(self):
            (count, faces, modifier) = parse(' 2 d 4 + 6 ')
            self.assertEqual(2, count)
            self.assertEqual(4, faces)
            self.assertEqual(6, modifier)

        def test_success_with_d(self):
            (count, faces, modifier) = parse('2d4+6')
            self.assertEqual(2, count)
            self.assertEqual(4, faces)
            self.assertEqual(6, modifier)

        def test_success_with_D(self):
            (count, faces, modifier) = parse('2d4+6')
            self.assertEqual(2, count)
            self.assertEqual(4, faces)
            self.assertEqual(6, modifier)

        def test_success_without_modifier(self):
            (count, faces, modifier) = parse('2d4')
            self.assertEqual(2, count)
            self.assertEqual(4, faces)
            self.assertEqual(0, modifier)

        def test_success_with_positive_modifier(self):
            (count, faces, modifier) = parse('2d4+6')
            self.assertEqual(2, count)
            self.assertEqual(4, faces)
            self.assertEqual(6, modifier)

        def test_success_with_negative_modifier(self):
            (count, faces, modifier) = parse('2d4-6')
            self.assertEqual(2, count)
            self.assertEqual(4, faces)
            self.assertEqual(-6, modifier)


    unittest.main()
