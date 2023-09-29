import pandas as pd
from dataclasses import dataclass
import os
from sklearn.model_selection import train_test_split # Dividing into X_train, X_test, y_train,y_test


@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts',"train.csv")
    test_data_path: str=os.path.join('artifacts',"test.csv")
    raw_data_path: str=os.path.join('artifacts',"data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
            
            df=pd.read_csv('artifacts/designed_data.csv')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)


            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.drop("Unnamed: 0",axis = 1,inplace=True)
            test_set.drop("Unnamed: 0",axis = 1,inplace=True)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)

            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)


            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
