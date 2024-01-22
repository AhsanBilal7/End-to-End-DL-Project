from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier import logger
STORAGE_NAME = 'Data Ingestion stage'

try:
    logger.info(f' >>>>>>>>>> {STORAGE_NAME} started <<<<<<<<<<<')
    data_ingestion_pipeline = DataIngestionTrainingPipeline()
    data_ingestion_pipeline.main()
    logger.info(f'{STORAGE_NAME} completed')
except Exception as e:
    logger.error(f'{STORAGE_NAME} failed with error: {e}')
    raise e