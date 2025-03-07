from textsummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textsummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from textsummarizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from textsummarizer.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline

from textsummarizer.logging import logger

STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f">>>>>>> Starting {STAGE_NAME} <<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>> {STAGE_NAME} completed successfully <<<<<<< ")

except Exception as e:
    logger.error(f"An error occurred during {STAGE_NAME}: {str(e)}")
    raise e

STAGE_NAME = "Data Validation stage"

try:
    logger.info(f">>>>>>> Starting {STAGE_NAME} <<<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>>> {STAGE_NAME} completed successfully <<<<<<< ")

except Exception as e:
    logger.error(f"An error occurred during {STAGE_NAME}: {str(e)}")
    raise e

STAGE_NAME = "Data Transformation stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
         logger.exception(e)
         raise e
 
STAGE_NAME = "Model trainer stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
    model_trainer = ModelTrainerTrainingPipeline()
    model_trainer.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
         logger.exception(e)
         raise e
 