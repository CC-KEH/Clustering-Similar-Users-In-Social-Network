from src.utils import logger
from src.pipelines.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.pipelines.stage_02_data_transformation import DataTransformationTrainingPipeline
from src.pipelines.stage_03_model_trainer import ModelTrainerTrainingPipeline
from src.pipelines.stage_04_visualization import VisualizationTrainingPipeline

def data_ingestion(num_users=10, num_posts=30):
    STAGE_NAME = 'Data Ingestion Stage'
    try:
        logger.info(f'>>>>>>> STAGE {STAGE_NAME} Started <<<<<<<')
        obj = DataIngestionTrainingPipeline()
        spark_df = obj.main(num_users=10, num_posts=30)
        logger.info(spark_df.show(5))
        logger.info(f'>>>>>>> STAGE {STAGE_NAME} Completed <<<<<<<\n\nx============================x')
        return spark_df
    except Exception as e:
        logger.exception(e)
        raise e

def data_transformation(spark_df):
    STAGE_NAME = 'Data Transformation'

    try:
        logger.info(f'>>>>>>> STAGE {STAGE_NAME} Started <<<<<<<')
        obj = DataTransformationTrainingPipeline()
        pca_features,user_activity = obj.main(spark_df=spark_df)
        logger.info(f'>>>>>>> STAGE {STAGE_NAME} Completed <<<<<<<\n\nx============================x')
        return pca_features, user_activity
    except Exception as e:
        logger.exception(e)
        raise e

def model_trainer(pca_features, user_activity):
    STAGE_NAME = 'Model Trainer Stage'

    try:
        logger.info(f'>>>>>>> STAGE {STAGE_NAME} Started <<<<<<<')
        obj = ModelTrainerTrainingPipeline()
        user_activity = obj.main(pca_features, user_activity)
        logger.info(f'>>>>>>> STAGE {STAGE_NAME} Completed <<<<<<<\n\nx============================x')
        return pca_features,user_activity
    except Exception as e:
        logger.exception(e)
        raise e


def visualize(pca_features, user_activity):
    STAGE_NAME = 'Visualization Stage'

    try:
        logger.info(f'>>>>>>> STAGE {STAGE_NAME} Started <<<<<<<')
        obj = VisualizationTrainingPipeline()
        obj.main(pca_features, user_activity)
        logger.info(f'>>>>>>> STAGE {STAGE_NAME} Completed <<<<<<<\n\nx=============x')
    except Exception as e:
        logger.exception(e)
        raise e

if __name__ == '__main__':
    spark_df = data_ingestion(num_users=30,num_posts=10)
    pca_features, user_activity = data_transformation(spark_df)
    pca_features, user_activity = model_trainer(pca_features, user_activity)
    visualize(pca_features, user_activity)