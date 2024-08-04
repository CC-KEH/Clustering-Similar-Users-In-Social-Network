from src.components.data_ingestion import Data_Ingestion
from src.utils import logger


STAGE_NAME = 'Starting Data Ingestion Training Pipeline'

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self, num_users, num_posts):
        data_ingestion = Data_Ingestion()
        spark_df = data_ingestion.initiate_data_ingestion(num_users, num_posts)
        return spark_df
    
if __name__ == '__main__':
    try:
        logger.info(f">>>>>> {STAGE_NAME} Started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> {STAGE_NAME} Completed <<<<<<")
        
    except Exception as e:
        logger.exception(e)
        raise e