import unittest
from scripts.model_training import Model_Trainer
import numpy as np
import pandas as pd

class TestModelTraining(unittest.TestCase):
    def setUp(self):
        self.model_trainer = Model_Trainer()
        # Example PCA features and user_activity for testing
        self.pca_features = np.random.rand(50, 2)
        self.user_activity = pd.DataFrame({
            'user_id': [f'user{i}' for i in range(50)],
            'post_id': np.random.randint(0, 100, 50),
            'view_count': np.random.randint(1, 10, 50),
            'comment_count': np.random.randint(0, 5, 50),
            'comment_to_view_ratio': np.random.rand(50)
        })

    def test_model_trainer(self):
        self.model_trainer.initiate_model_trainer(self.pca_features, self.user_activity)
        self.assertIn('cluster', self.user_activity.columns)

if __name__ == "__main__":
    unittest.main()
