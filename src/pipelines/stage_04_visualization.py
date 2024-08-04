from src.components.visualization import Visualizer
from src.utils import logger

STAGE_NAME = 'Starting Visualization Training Pipeline'

class VisualizationTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self,pca_features,user_activity):
        visualizer = Visualizer()
        visualizer.visualize(pca_features,user_activity)

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> {STAGE_NAME} Started <<<<<<")
        obj = VisualizationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> {STAGE_NAME} Started <<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e