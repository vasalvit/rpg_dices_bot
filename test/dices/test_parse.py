from unittest import TestCase, main

from dices import parse, InvalidFormat, InvalidDicesCount, InvalidFacesCount, minimal_dices_count, \
    maximal_dices_count, minimal_faces_count, maximal_faces_count


class TestParse(TestCase):
    def test_fail_for_empty_string(self):
        with self.assertRaises(InvalidFormat):
            _ = parse('')

    def test_fail_if_count_is_not_number(self):
        with self.assertRaises(InvalidFormat):
            _ = parse('x')
        with self.assertRaises(InvalidFormat):
            _ = parse('2x')

    def test_fail_without_D(self):
        with self.assertRaises(InvalidFormat):
            _ = parse('2')

    def test_fail_without_faces(self):
        with self.assertRaises(InvalidFormat):
            _ = parse('2d')

    def test_fail_if_faces_is_not_number(self):
        with self.assertRaises(InvalidFormat):
            _ = parse('2dx')

    def test_fail_without_modifier_sign(self):
        with self.assertRaises(InvalidFormat):
            _ = parse('2d4x')

    def test_fail_if_modifier_is_not_number(self):
        with self.assertRaises(InvalidFormat):
            _ = parse('2d4+x')

    def test_fail_if_there_is_tail(self):
        with self.assertRaises(InvalidFormat):
            _ = parse('2d4+6x')

    def test_fail_for_count_with_sign(self):
        with self.assertRaises(InvalidFormat):
            _ = parse('+2d4+6')

    def test_fail_for_negative_count(self):
        with self.assertRaises(InvalidFormat):
            _ = parse('-2d4+6')

    def test_fail_for_faces_with_sign(self):
        with self.assertRaises(InvalidFormat):
            _ = parse('2d+4+6')

    def test_fail_for_negative_faces(self):
        with self.assertRaises(InvalidFormat):
            _ = parse('2d+4+6')

    def test_fail_for_minimal_count(self):
        with self.assertRaises(InvalidDicesCount):
            _ = parse(str(minimal_dices_count - 1) + 'd4+6')

    def test_fail_for_maximal_count(self):
        with self.assertRaises(InvalidDicesCount):
            _ = parse(str(maximal_dices_count + 1) + 'd4+6')

    def test_fail_for_minimal_faces(self):
        with self.assertRaises(InvalidFacesCount):
            parse('2d' + str(minimal_faces_count - 1) + '+6')

    def test_fail_for_maximal_faces(self):
        with self.assertRaises(InvalidFacesCount):
            parse('2d' + str(maximal_faces_count + 1) + '+6')

    def test_ignore_spaces(self):
        (count, faces, modifier) = parse(' 2 d 4 + 6 ')
        self.assertEqual(2, count)
        self.assertEqual(4, faces)
        self.assertEqual(6, modifier)

    def test_use_1_without_count(self):
        (count, _, _) = parse('d4')
        self.assertEqual(1, count)

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

    def test_success_with_zero_modifier(self):
        (count, faces, modifier) = parse('2d4+0')
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


if __name__ == '__main__':
    main()
