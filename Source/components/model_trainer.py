import os
import sys
from dataclasses import dataclass


from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor
from sklearn.ensemble import AdaBoostRegressor , GradientBoostingRegressor , RandomForestRegressor
from sklearn.metrics import r2_score,mean_squared_error

from Source.exception import CustomException
from Source.logger import logging

from Source.utils import save_object , evaluate_models


@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join("Created_data" , "model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()


    def initiate_model_trainer(self , train_array ,test_array):
        try:
            print("Spliting Training and Testing data.........")
            logging.info("Spliting training and testing ........")
            X_train, y_train, X_test ,y_test = (
                train_array[:,:-1] , train_array[:,-1] ,
                test_array[:,:-1] , test_array[:,-1]
            )

            models = {
                "Random Forest": RandomForestRegressor(),
                "Decision Tree": DecisionTreeRegressor(),
                "Gradient Boosting": GradientBoostingRegressor(),
                "Linear Regression": LinearRegression(),
                "XGBRegressor": XGBRegressor(),
                "AdaBoost Regressor": AdaBoostRegressor(),
            }

            model_report:dict = evaluate_models(X_train = X_train , y_train = y_train ,
                                                X_test = X_test , y_test=y_test ,
                                                models = models)
            
            best_model_score = max(sorted(model_report.values()))
            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]

            best_model = models[best_model_name]

            if best_model_score < 0.6 :
                print("No best model found on both training & testing....")
                raise CustomException("No best model Found")
            
            print("Best model found on both training & testing....")

            save_object(
                file_path = self.model_trainer_config.trained_model_file_path ,
                obj = best_model
            )

            y_predict = best_model.predict(X_test)
            score = r2_score(y_test , y_predict)

            print(f"Best Model is : {best_model} ,with {score * 100 : .2f}% accuracy")
            return score

        except Exception as e:
            raise CustomException(e, sys)