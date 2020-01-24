from helper import null_check
import unittest


class HelperTest(unittest.TestCase):
    def test_split(self):
        test_df = pd.DataFrame(np.random.randint(0, 100, size=(15, 4)), columns=list('ABCD'))
        train, val, test = helper.train_test_val_split(test_df)
        self.assertEqual(val['A'].count(), 3)
    def test_parse_dates(self):
        data = [['1982-06-13']]
        test_df = pd.DataFrame(data, columns=['Date'])
        new_df = parse_dates(test_df, 'Date')
        self.assertTrue(new_df.columns.to_list(), test_df = pd.DataFrame(np.random.randint(0, 100, size=(15, 4)), columns=list('ABCD')))
    def test_null_check(self):
        test_df = pd.DataFrame(np.random.randint(0, 100, size=(15, 4)), columns=list('ABCD'))



