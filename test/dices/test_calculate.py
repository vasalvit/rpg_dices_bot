from unittest import TestCase, main
from unittest.mock import patch

from dices import calculate


class TestCalculate(TestCase):
    dices_1d2 = (1, 2, 0)
    dices_2d4 = (2, 4, -2)
    dices_3d6 = (3, 6, 3)

    @patch('numpy.random.randint')
    def test_should_use_min_and_max_for_1d2(self, mock_randint):
        mock_randint.return_value = 1

        _ = calculate(self.dices_1d2)

        mock_randint.assert_called_with(1, 2)

    @patch('numpy.random.randint')
    def test_should_use_min_and_max_for_2d4(self, mock_randint):
        mock_randint.return_value = 1

        _ = calculate(self.dices_2d4)

        mock_randint.assert_called_with(2*1-2, 2*4-2)

    @patch('numpy.random.randint')
    def test_should_use_min_and_max_for_3d6(self, mock_randint):
        mock_randint.return_value = 1

        _ = calculate(self.dices_3d6)

        mock_randint.assert_called_with(3*1+3, 3*6+3)

    @patch('numpy.random.randint')
    def test_should_use_randint_once_for_1d(self, mock_randint):
        mock_randint.return_value = 1

        _ = calculate(self.dices_1d2)

        self.assertEqual(1, mock_randint.call_count)

    @patch('numpy.random.randint')
    def test_should_use_randint_once_for_2d(self, mock_randint):
        mock_randint.return_value = 1

        _ = calculate(self.dices_2d4)

        self.assertEqual(1, mock_randint.call_count)

    @patch('numpy.random.randint')
    def test_should_use_randint_once_for_3d(self, mock_randint):
        mock_randint.return_value = 1

        _ = calculate(self.dices_3d6)

        self.assertEqual(1, mock_randint.call_count)

    @patch('numpy.random.randint')
    def test_minimal_value_for_1d2(self, mock_randint):
        mock_randint.side_effect = lambda a, _: a

        value, minimal, _ = calculate(self.dices_1d2)

        self.assertEqual(self.dices_1d2[0] * 1 + self.dices_1d2[2], value)
        self.assertEqual(self.dices_1d2[0] * 1 + self.dices_1d2[2], minimal)

    @patch('numpy.random.randint')
    def test_maximal_value_for_1d2(self, mock_randint):
        mock_randint.side_effect = lambda _, b: b

        value, _, maximal = calculate(self.dices_1d2)

        self.assertEqual(self.dices_1d2[0] * 2 + self.dices_1d2[2], value)
        self.assertEqual(self.dices_1d2[0] * 2 + self.dices_1d2[2], maximal)

    @patch('numpy.random.randint')
    def test_minimal_value_for_2d4(self, mock_randint):
        mock_randint.side_effect = lambda a, _: a

        value, minimal, _ = calculate(self.dices_2d4)

        self.assertEqual(self.dices_2d4[0] * 1 + self.dices_2d4[2], value)
        self.assertEqual(self.dices_2d4[0] * 1 + self.dices_2d4[2], minimal)

    @patch('numpy.random.randint')
    def test_maximal_value_for_2d4(self, mock_randint):
        mock_randint.side_effect = lambda _, b: b

        value, _, maximal = calculate(self.dices_2d4)

        self.assertEqual(self.dices_2d4[0] * 4 + self.dices_2d4[2], value)
        self.assertEqual(self.dices_2d4[0] * 4 + self.dices_2d4[2], maximal)

    @patch('numpy.random.randint')
    def test_minimal_value_for_3d6(self, mock_randint):
        mock_randint.side_effect = lambda a, _: a

        value, minimal, _ = calculate(self.dices_3d6)

        self.assertEqual(self.dices_3d6[0] * 1 + self.dices_3d6[2], value)
        self.assertEqual(self.dices_3d6[0] * 1 + self.dices_3d6[2], minimal)

    @patch('numpy.random.randint')
    def test_maximal_value_for_3d6(self, mock_randint):
        mock_randint.side_effect = lambda _, b: b

        value, _, maximal = calculate(self.dices_3d6)

        self.assertEqual(self.dices_3d6[0] * 6 + self.dices_3d6[2], value)
        self.assertEqual(self.dices_3d6[0] * 6 + self.dices_3d6[2], maximal)


if __name__ == '__main__':
    main()
