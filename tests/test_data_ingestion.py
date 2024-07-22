import unittest
from scripts.data_ingestion import Data_Ingestion

class TestDataIngestion(unittest.TestCase):
    def setUp(self):
        self.data_ingestion = Data_Ingestion()

    def test_data_ingestion(self):
        df = self.data_ingestion.initiate_data_ingestion(num_users=50, num_posts=100)
        self.assertFalse(df.empty)
        self.assertIn('user_id', df.columns)
        self.assertIn('post_id', df.columns)
        self.assertIn('post_timestamp', df.columns)
        self.assertIn('comment_timestamp', df.columns)
        self.assertIn('post_content', df.columns)
        self.assertIn('comment_content', df.columns)
        self.assertIn('view_count', df.columns)
        self.assertIn('comment_count', df.columns)

if __name__ == "__main__":
    unittest.main()
