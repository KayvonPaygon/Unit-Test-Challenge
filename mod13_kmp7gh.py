import verifyInputs
import unittest

class TestClass(unittest.TestCase):
    def test_valid_symbol(self):
        test_cases = ['f', 'GOOGLE', '123456', '', 'ABCDEFGH']
        expected_results = [False, True, False, False, False]

        for symbol, expected_result in zip(test_cases, expected_results):
            with self.subTest(symbol=symbol, expected_result=expected_result):
                result = verifyInputs.is_valid_symbol(symbol)
                self.assertEqual(result, expected_result)

    def test_valid_chart_type(self):
        test_cases = ['1', '2', '3', 'f', 'iuwehi']
        expected_results = [True, True, False, False, False]

        for case, expected_result in zip(test_cases, expected_results):
            with self.subTest(symbol=case, expected_result=expected_result):
                result = verifyInputs.is_valid_chart_type(case)
                self.assertEqual(result, expected_result)

    def test_valid_time_series(self):
        test_cases = ['1', '2', '3', '4', 'f', '5', 'uhiwjef']
        expected_results = [True, True, True, True, False, False, False]

        for case, expected_result in zip(test_cases, expected_results):
            with self.subTest(symbol=case, expected_result=expected_result):
                result = verifyInputs.is_valid_time_series(case)
                self.assertEqual(result, expected_result)

    def test_valid_date_format(self):
        test_cases = ['2023-01-01', '2023-11-11', '2023/10/26', '23-1-1', 'abc']
        expected_results = [True, True, False, False, False]

        for date_str, expected_result in zip(test_cases, expected_results):
            with self.subTest(date_str=date_str, expected_result=expected_result):
                result = verifyInputs.is_valid_date_format(date_str)
                self.assertEqual(result, expected_result)

        

if __name__ == '__main__':
    unittest.main()
