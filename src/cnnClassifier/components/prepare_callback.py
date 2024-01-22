from cnnClassifier.utils import read_yaml , create_directories
from cnnClassifier.constants import  *
from dataclasses import dataclass
from cnnClassifier.entity import PrepareCallbackConfig
import tensorflow as tf
import time 
import os

class PrepareCallback:  
    def __init__(self, config:PrepareCallbackConfig):
        self.config = config
    
    @property
    def _create_tensorboard_callback(self):
        timestamp = time.strftime("%Y-%m-%d-%H-%M-%S")
        tb_log_dir = os.path.join(self.config.tensorboard_root_log_dir, f"tb_log_dir_{timestamp}")

        return tf.keras.callbacks.TensorBoard(log_dir=tb_log_dir)
    
    @property
    def _create_ckpt_callback(self):
        return  tf.keras.callbacks.ModelCheckpoint(
            filepath = self.config.checkpoint_model_filepath,
            save_best_only=True
        )

    
    def get_tb_ckpt_callback(self):
        return [
            self._create_tensorboard_callback,
            self._create_ckpt_callback
        ]
