from cnnClassifier.config import ConfigurationManager
from cnnClassifier.components import DataIngestion, BaseModel, Training, PrepareCallback


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


class ModelTrainingPipeline:
    def __init__(self):
        pass    
    def main(self):
        
        try:
            config_manager = ConfigurationManager()
            callback_config = config_manager.get_prepare_callback_config()
            prepare_callbacks = PrepareCallback(config = callback_config)
            callback = prepare_callbacks.get_tb_ckpt_callback()
            training_config = config_manager.get_training_configuration()
            training = Training(config = training_config)
            training.get_base_model()
            training.train_valid_generator()

            training.train(callback_list=callback)

        except Exception as e:
            print(e)
            # logging(e)