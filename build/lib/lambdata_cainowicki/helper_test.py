from helper import null_check
from helper import parse_dates
import unittest


class HelperTest(unittest.TestCase):

    def test_parse_dates(self):
        data = [['1982-06-13']]
        test_df = pd.DataFrame(data, columns=['Date'])
        new_df = parse_dates(test_df, 'Date')
        self.assertTrue(new_df.columns.to_list() == ['Date', 'year', 'month', 'day'])

    def test_null_check(self):
        test_df = pd.DataFrame(np.random.randint(0, 100, size=(15, 4)), columns=list('ABCD'))
        self.assertTrue(null_check == 'Your dataframe contains no null values')


if __name__ == "__main__": # only run if this script is invoked from the command-line:
    unittest.main()
