from unittest import TestCase, main
from unittest.mock import patch

from dices import parse_all, InvalidFormat


class TestParseAll(TestCase):
    str_d4 = 'd4'
    str_2d6 = '2d6'
    str_3d8_4 = '3d8+4'
    str_4d10_5 = '4d10-4'

    val_d4 = (1, 4, 0)
    val_2d6 = (2, 6, 0)
    val_3d8_4 = (3, 8, 4)
    val_4d10_5 = (4, 10, -5)

    parse_impl = None

    def setUp(self):
        def parse_impl(str):
            if self.str_d4 == str:
                return self.val_d4
            elif self.str_2d6 == str:
                return self.val_2d6
            elif self.str_3d8_4 == str:
                return self.val_3d8_4
            elif self.str_4d10_5 == str:
                return self.val_4d10_5
            else:
                raise InvalidFormat(str)

        self.parse_impl = parse_impl

    @patch('dices.parse')
    def test_fail_if_empty(self, _):
        with self.assertRaises(InvalidFormat):
            _ = parse_all('')

    @patch('dices.parse')
    def test_fail_if_only_spaces(self, _):
        with self.assertRaises(InvalidFormat):
            _ = parse_all('   ')

    @patch('dices.parse')
    def test_fail_if_parse_fail(self, mock_parse):
        mock_parse.side_effect = self.parse_impl

        with self.assertRaises(InvalidFormat):
            _ = parse_all('xyz')

    @patch('dices.parse')
    def test_ok_for_comma_separators(self, mock_parse):
        mock_parse.side_effect = self.parse_impl

        values = parse_all('%s,%s,%s,%s' % (self.str_d4, self.str_2d6, self.str_3d8_4, self.str_4d10_5))

        self.assertEqual(values, [self.val_d4, self.val_2d6, self.val_3d8_4, self.val_4d10_5])
    @patch('dices.parse')
    def test_ok_for_space_separators(self, mock_parse):
        mock_parse.side_effect = self.parse_impl

        values = parse_all('%s %s %s %s' % (self.str_d4, self.str_2d6, self.str_3d8_4, self.str_4d10_5))

        self.assertEqual(values, [self.val_d4, self.val_2d6, self.val_3d8_4, self.val_4d10_5])

    @patch('dices.parse')
    def test_ok_for_semicolon_separators(self, mock_parse):
        mock_parse.side_effect = self.parse_impl

        values = parse_all('%s;%s;%s;%s' % (self.str_d4, self.str_2d6, self.str_3d8_4, self.str_4d10_5))

        self.assertEqual(values, [self.val_d4, self.val_2d6, self.val_3d8_4, self.val_4d10_5])

    @patch('dices.parse')
    def test_ignore_leading_separators(self, mock_parse):
        mock_parse.side_effect = self.parse_impl

        values = parse_all(';;;%s;%s;%s;%s' % (self.str_d4, self.str_2d6, self.str_3d8_4, self.str_4d10_5))

        self.assertEqual(values, [self.val_d4, self.val_2d6, self.val_3d8_4, self.val_4d10_5])

    @patch('dices.parse')
    def test_ignore_duplicated_separators(self, mock_parse):
        mock_parse.side_effect = self.parse_impl

        values = parse_all('%s;%s;;%s;;;%s' % (self.str_d4, self.str_2d6, self.str_3d8_4, self.str_4d10_5))

        self.assertEqual(values, [self.val_d4, self.val_2d6, self.val_3d8_4, self.val_4d10_5])

    @patch('dices.parse')
    def test_ignore_trailing_separators(self, mock_parse):
        mock_parse.side_effect = self.parse_impl

        values = parse_all('%s;%s;%s;%s;;;' % (self.str_d4, self.str_2d6, self.str_3d8_4, self.str_4d10_5))

        self.assertEqual(values, [self.val_d4, self.val_2d6, self.val_3d8_4, self.val_4d10_5])

    @patch('dices.parse')
    def test_return_single(self, mock_parse):
        mock_parse.side_effect = self.parse_impl

        values = parse_all('%s' % (self.str_d4))

        self.assertEqual(values, [self.val_d4])

    @patch('dices.parse')
    def test_return_two(self, mock_parse):
        mock_parse.side_effect = self.parse_impl

        values = parse_all('%s;%s' % (self.str_d4, self.str_2d6))

        self.assertEqual(values, [self.val_d4, self.val_2d6])

    @patch('dices.parse')
    def test_return_three(self, mock_parse):
        mock_parse.side_effect = self.parse_impl

        values = parse_all('%s;%s;%s' % (self.str_d4, self.str_2d6, self.str_3d8_4))

        self.assertEqual(values, [self.val_d4, self.val_2d6, self.val_3d8_4])


if __name__ == '__main__':
    main()
