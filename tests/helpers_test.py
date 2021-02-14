import unittest
from src.utils.helpers import MNISTdataset as Dataset



class TestDataset(unittest.TestCase): 

    def setUp(self):
        self.my_dataset = Dataset()

    # Tests for train_ds
    def test_len_train_ds(self): 
        self.assertEqual(len(self.my_dataset.TRAIN_DS), 2)
    
    def test_len_train_ds_x(self): 
        self.assertEqual(len(self.my_dataset.TRAIN_DS[0]), 50000)

    def test_len_train_ds_y(self): 
        self.assertEqual(len(self.my_dataset.TRAIN_DS[1]), 50000)

    # Tests for vald_ds
    def test_len_val_ds(self): 
        self.assertEqual(len(self.my_dataset.VAL_DS), 2)

    def test_len_val_ds_x(self): 
        self.assertEqual(len(self.my_dataset.VAL_DS[0]), 10000)

    def test_len_val_ds_y(self): 
        self.assertEqual(len(self.my_dataset.VAL_DS[1]), 10000)

    # Tests for test_ds 
    def test_len_test_ds(self): 
        self.assertEqual(len(self.my_dataset.TEST_DS), 2)

    def test_len_test_ds_x(self): 
        self.assertEqual(len(self.my_dataset.TEST_DS[0]), 10000)

    def test_len_test_ds_y(self): 
        self.assertEqual(len(self.my_dataset.TEST_DS[1]), 10000)

if __name__ == '__main__':
    unittest.main()