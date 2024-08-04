from src.components.model_trainer import Model_Trainer
from src.utils import logger

STAGE_NAME = 'Starting Model Trainer Training Pipeline'


class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self,pca_features,user_activity):
        model_trainer = Model_Trainer()
        user_activity = model_trainer.initiate_model_trainer(pca_features,user_activity)
        return user_activity
    
if __name__ == '__main__':
    try:
        logger.info(f">>>>>> {STAGE_NAME} Started <<<<<<")
        obj = ModelTrainerTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> {STAGE_NAME} Started <<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e