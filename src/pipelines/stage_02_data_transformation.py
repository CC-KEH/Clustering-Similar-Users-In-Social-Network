from src.components.data_transformation import Data_Transformation
from src.utils import logger

STAGE_NAME = 'Starting Data Transformation Training Pipeline'

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self, spark_df):
        data_transformation = Data_Transformation()
        pca_features, user_activity = data_transformation.initiate_data_transformation(spark_df)
        return pca_features, user_activity
    
if __name__ == '__main__':
    try:
        logger.info(f">>>>>> {STAGE_NAME} Started <<<<<<")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> {STAGE_NAME} Started <<<<<<")
        
    except Exception as e:
        logger.exception(e)
        raise e