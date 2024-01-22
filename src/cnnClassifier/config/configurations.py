from cnnClassifier.utils import read_yaml , create_directories
from cnnClassifier.constants import  *
from dataclasses import dataclass
from pathlib import Path
import os
from dataclasses import dataclass
from cnnClassifier.entity import PrepareBaseModelConfig, DataIngestionConfig, PrepareCallbackConfig



class ConfigurationManager:
    def __init__(self,
        config_file_path = CONFIG_FILE_PATH,
        params_file_path = PARAMS_FILE_PATH):
        self.config_file = read_yaml(config_file_path)
        self.params = read_yaml(params_file_path)
        create_directories([self.config_file.artifacts_root])


    # Data Ingestion
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config_file.data_ingestion
        create_directories([config.root_dir])
        
        data_ingestion_config = DataIngestionConfig(
            root_dir = config.root_dir,
            source_URL = config.source_URL,
            local_data_file = config.local_data_file,
            unzip_dir = config.unzip_dir
        )
        return data_ingestion_config
    
    # Prepare Base Model
    def get_prepare_model_config(self) -> PrepareBaseModelConfig:
        config = self.config_file.prepare_base_model
        create_directories([config.root_dir])
        
        # prepare_base_model_config = PrepareBaseModelConfig(
        #     root_dir = Path(config.root_dir),
        #     base_model_path = Path(config.base_model_path),
        #     update_base_model_path = Path(config.update_base_model_path),
        #     params_image_size= self.params_file.IMAGE_SIZE,
        #     params_learning_rate= self.params_file.LEARNING_RATE,
        #     params_include_top= self.params_file.INCLUDE_TOP,
        #     params_classes = self.params_file.CLASSES,
        #     params_weights = self.params_file.WEIGHTS
        # )
        prepare_base_model_config = PrepareBaseModelConfig(
            root_dir=Path(config.root_dir),
            base_model_path=Path(config.base_model_path),
            update_base_model_path=Path(config.update_base_model_path),
            params_image_size=self.params.IMAGE_SIZE,
            params_learning_rate=self.params.LEARNING_RATE,
            params_include_top=self.params.INCLUDE_TOP,
            params_weights=self.params.WEIGHTS,
            params_classes=self.params.CLASSES
        )
        return prepare_base_model_config
    

    # Prepare Callbackk
    def get_prepare_callback_config(self) -> PrepareCallbackConfig:
        config = self.config_file.prepare_callbacks
        
        model_ckp = os.path.dirname(config.checkpoint_model_filepath)


        create_directories([Path(model_ckp) , Path(config.tensorboard_root_log_dir)])
        
        prepare_callback_config = PrepareCallbackConfig(
            root_dir=Path(config.root_dir),
            tensorboard_root_log_dir=Path(config.tensorboard_root_log_dir),
            checkpoint_model_filepath=Path(config.checkpoint_model_filepath)
        )
        return prepare_callback_config
    