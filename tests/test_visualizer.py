import unittest
from scripts.visualization import Visualizer
import numpy as np
import pandas as pd

class TestVisualization(unittest.TestCase):
    def setUp(self):
        self.visualizer = Visualizer()
        self.pca_features = np.random.rand(50, 2)
        self.user_activity = pd.DataFrame({
            'user_id': [f'user{i}' for i in range(50)],
            'cluster': np.random.randint(0, 5, 50)
        })

    def test_visualization(self):
        self.visualizer.visualize(self.pca_features, self.user_activity)

if __name__ == "__main__":
    unittest.main()