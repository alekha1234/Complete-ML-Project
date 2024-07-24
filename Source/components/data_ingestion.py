import os
import sys
import pandas as pd
from dataclasses import dataclass
from sklearn.model_selection import train_test_split

# Import custom exception and logging configurations
from Source.exception import CustomException
from Source.logger import logging

# import data transformation
from Source.components.data_transformation import DataTransformation
from Source.components.data_transformation import DataTransformationConfig

# import model trainer
from Source.components.model_trainer import ModelTrainerConfig
from Source.components.model_trainer import ModelTrainer

@dataclass
class DataIngestionConfig:
    """
    Configuration for data ingestion process.

    Attributes:
        train_data_path (str): Path where the training data will be stored.
        test_data_path (str): Path where the test data will be stored.
        raw_data_path (str): Path where the raw data will be stored.
    """
    train_data_path: str = os.path.join('Created_data', "train.csv")
    test_data_path: str = os.path.join('Created_data', "test.csv")
    raw_data_path: str = os.path.join('Created_data', "data.csv")


class DataIngestion:
    """
    Class for handling data ingestion process.

    Methods:
        initiate_data_ingestion: Reads the dataset, splits it into train and test sets, and saves them to specified paths.
    """
    def __init__(self):
        """
        Initializes the DataIngestion instance with default configuration.
        """
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        """
        Reads the dataset from a CSV file, splits it into training and test sets, 
        and saves the splits to specified paths.

        Returns:
            tuple: Paths to the training and test data files.

        Raises:
            CustomException: If an error occurs during the data ingestion process.
        """
        logging.info("Entered the data ingestion method or component")
        try:
            # Read the dataset
            df = pd.read_csv('notebook\stud.csv')
            logging.info('Read the dataset as dataframe')
            print("Reading the data........")
            print(df.head())

            # Create directory if it doesn't exist
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            # Save raw data to specified path
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            logging.info("Train test split initiated")
            print("Spliting the data into train & test ......")

            # Split the data into training and test sets
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            # Save the training set to the specified path
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)

            # Save the test set to the specified path
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Ingestion of the data is completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e, sys)

if __name__ == "__main__":
    # Create an instance of DataIngestion
    obj = DataIngestion()
    train_data , test_data = obj.initiate_data_ingestion()
    print("data ingestion is Completed.............")

    data_transformation = DataTransformation()
    train_arr , test_arr , _ = data_transformation.initiate_data_transformation(train_path=train_data , test_path=test_data)

    print("train_arr : " ,train_arr.shape)
    print("test_arr : " ,test_arr.shape)

    model_trainer = ModelTrainer()
    print("Model training is Started ...............")
    print(model_trainer.initiate_model_trainer(train_array=train_arr ,test_array=test_arr))
    