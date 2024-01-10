import os
import datasets
import urllib.request as request
from NER.logging import logger
from NER.utils.common import get_size
from NER.entity import (DataIngestionConfig)
from pathlib import Path


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def load_file(self):
        logger.info(f"Loading dataset from huggingface datasets library")
        data = datasets.load_dataset("conll2003")
        data_train = data['train']
        data_test = data['test']
        data_validation = data['validation']
        logger.info(f"printing the first line of tokens")
        print(data['train'][0])
        
        # path of trainfile data
        train_file_path = self.config.train_file
        logger.info(f"path of loaded data : {train_file_path}")
        data_train.to_csv(train_file_path,index=False,header=True)
        
        # path of testfile data
        test_file_path = self.config.test_file
        logger.info(f"path of loaded data : {test_file_path}")
        data_test.to_csv(test_file_path,index=False,header=True)
        
        # path of testfile data
        validation_file_path = self.config.validation_file
        logger.info(f"path of loaded data : {validation_file_path}")
        data_validation.to_csv(validation_file_path,index=False,header=True)

        """# Ensure the directory for the file exists
        directory = os.path.dirname(file_path)
        os.makedirs(directory,exist_ok=True)
        # Save each example individually (you may modify this part based on your requirements)
        with open(file_path, 'w') as file:
             json.dump(data_train, file)
       """
        logger.info(f"Data loaded successfully!!!")

    

    
    