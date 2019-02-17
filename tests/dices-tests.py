from unittest import TestCase, main
from unittest.mock import patch

from dices import parse, calculate


class TestParse(TestCase):
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

    def test_fail_for_zero_count(self):
        self.assertIsNone(parse('0d4+6'))

    def test_fail_for_zero_faces(self):
        self.assertIsNone(parse('2d0+6'))

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


class TestCalculate(TestCase):
    dices_1d2 = (1, 2, 0)
    dices_2d4 = (2, 4, -2)
    dices_3d6 = (3, 6, 3)

    @patch('numpy.random.randint')
    def test_should_use_1_and_2_values_for_1d2(self, mock_randint):
        mock_randint.return_value = 1

        _ = calculate(self.dices_1d2)

        mock_randint.assert_called_with(1, 2)

    @patch('numpy.random.randint')
    def test_should_use_1_and_4_values_for_2d4(self, mock_randint):
        mock_randint.return_value = 1

        _ = calculate(self.dices_2d4)

        mock_randint.assert_called_with(1, 4)

    @patch('numpy.random.randint')
    def test_should_use_1_and_6_values_for_3d6(self, mock_randint):
        mock_randint.return_value = 1

        _ = calculate(self.dices_3d6)

        mock_randint.assert_called_with(1, 6)

    @patch('numpy.random.randint')
    def test_should_use_randint_once_for_1d(self, mock_randint):
        mock_randint.return_value = 1

        _ = calculate(self.dices_1d2)

        self.assertEqual(1, mock_randint.call_count)

    @patch('numpy.random.randint')
    def test_should_use_randint_twice_for_2d(self, mock_randint):
        mock_randint.return_value = 1

        _ = calculate(self.dices_2d4)

        self.assertEqual(2, mock_randint.call_count)

    @patch('numpy.random.randint')
    def test_should_use_randint_three_times_for_3d(self, mock_randint):
        mock_randint.return_value = 1

        _ = calculate(self.dices_3d6)

        self.assertEqual(3, mock_randint.call_count)

    @patch('numpy.random.randint')
    def test_minimal_value_for_1d2(self, mock_randint):
        mock_randint.side_effect = lambda a, _: a

        self.assertEqual(self.dices_1d2[0] * 1 + self.dices_1d2[2], calculate(self.dices_1d2))

    @patch('numpy.random.randint')
    def test_maximal_value_for_1d2(self, mock_randint):
        mock_randint.side_effect = lambda _, b: b

        self.assertEqual(self.dices_1d2[0] * 2 + self.dices_1d2[2], calculate(self.dices_1d2))

    @patch('numpy.random.randint')
    def test_minimal_value_for_2d4(self, mock_randint):
        mock_randint.side_effect = lambda a, _: a

        self.assertEqual(self.dices_2d4[0] * 1 + self.dices_2d4[2], calculate(self.dices_2d4))

    @patch('numpy.random.randint')
    def test_maximal_value_for_2d4(self, mock_randint):
        mock_randint.side_effect = lambda _, b: b

        self.assertEqual(self.dices_2d4[0] * 4 + self.dices_2d4[2], calculate(self.dices_2d4))

    @patch('numpy.random.randint')
    def test_minimal_value_for_3d6(self, mock_randint):
        mock_randint.side_effect = lambda a, _: a

        self.assertEqual(self.dices_3d6[0] * 1 + self.dices_3d6[2], calculate(self.dices_3d6))

    @patch('numpy.random.randint')
    def test_maximal_value_for_3d6(self, mock_randint):
        mock_randint.side_effect = lambda _, b: b

        self.assertEqual(self.dices_3d6[0] * 6 + self.dices_3d6[2], calculate(self.dices_3d6))


main()
