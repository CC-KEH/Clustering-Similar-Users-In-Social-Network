from src.utils import logger
from src.pipelines.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.pipelines.stage_02_data_transformation import DataTransformationTrainingPipeline
from src.pipelines.stage_03_model_trainer import ModelTrainerTrainingPipeline
from src.pipelines.stage_04_visualization import VisualizerTrainingPipeline


class PredictionPipeline:
    def __init__(self):
        self.data_ingestion = DataIngestionTrainingPipeline()
        self.data_transformation = DataTransformationTrainingPipeline()
        self.model_trainer = ModelTrainerTrainingPipeline()
        self.visualizer = VisualizerTrainingPipeline()

    def predict(self, num_users=10, num_posts=30):
        try:
            logger.info('>>>>>> Prediction Pipeline Started <<<<<<')
            df = self.data_ingestion.main(num_users, num_posts)
            self.data_transformation.main(df)
            pca_features, user_activity = self.model_trainer.main(pca_features,user_activity)
            pca_features, user_activity = self.visualizer.main(pca_features,user_activity)
            logger.info('>>>>>> Prediction Pipeline Completed <<<<<<')

        except Exception as e:
            logger.exception(e)
            raise e
        
if __name__ == '__main__':
    obj = PredictionPipeline()
    obj.predict()