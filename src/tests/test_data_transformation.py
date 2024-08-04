import unittest
import pandas as pd
from src.components.data_transformation import Data_Transformation

class TestDataTransformation(unittest.TestCase):
    def setUp(self):
        self.data_transformation = Data_Transformation()
        # Small DataFrame for testing
        self.df = pd.DataFrame({
            'user_id': ['user1', 'user2', 'user1'],
            'post_id': ['post1', 'post2', 'post3'],
            'view_count': [1, 1, 1],
            'comment_count': [2, 1, 0]
        })

    def test_data_transformation(self):
        pca_features, user_activity = self.data_transformation.initiate_data_transformation(self.df)
        self.assertEqual(len(pca_features), user_activity.shape[0])
        self.assertIn('user_id', user_activity.columns)
        self.assertIn('comment_to_view_ratio', user_activity.columns)

if __name__ == "__main__":
    unittest.main()
