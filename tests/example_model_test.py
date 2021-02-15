import unittest 
from src.model import ExampleModel
from src.configs.config import example_config
from src.utils.helpers import MNISTdataset as Dataset

class TestExampleModel(unittest.TestCase): 

    def setUp(self): 
        self.my_dataset = Dataset()
        self.my_model = ExampleModel(example_config) 

    def test_generated_model_first_layer_input_shape(self): 
        self.my_model.generate_model()
        
        self.assertEqual(self.my_model.MODEL.layers[0].input_shape[0], None)
        self.assertEqual(self.my_model.MODEL.layers[0].input_shape[1], len(self.my_dataset.TRAIN_DS[0][0]))
        self.assertEqual(self.my_model.MODEL.layers[0].input_shape[2], len(self.my_dataset.TRAIN_DS[0][0][0]))

if __name__ == '__main__':
    unittest.main()