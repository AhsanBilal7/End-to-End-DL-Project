from cnnClassifier.config import ConfigurationManager
from cnnClassifier.components import DataIngestion, BaseModel
from cnnClassifier import logger


# Stage-1 Pipeline

class PrepareBaseTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        prepare_model_config = config.get_prepare_model_config()
        base_model = BaseModel(config=prepare_model_config)
        base_model.get_base_model()
        base_model.update_base_model()