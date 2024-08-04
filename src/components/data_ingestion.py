import random
from src.utils import logger
import pandas as pd
from faker import Faker
from datetime import datetime
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, TimestampType, IntegerType
from src.utils.common import plot_data_points

class Data_Ingestion:
    def __init__(self):
        self.faker = Faker()
        self.spark = SparkSession.builder.appName("DataIngestion").getOrCreate()
        
    def initiate_data_ingestion(self, num_users, num_posts):
        schema = StructType([
            StructField("user_id", StringType(), True),
            StructField("post_id", StringType(), True),
            StructField("post_timestamp", TimestampType(), True),
            StructField("comment_timestamp", TimestampType(), True),
            StructField("post_content", StringType(), True),
            StructField("comment_content", StringType(), True),
            StructField("view_count", IntegerType(), True),
            StructField("comment_count", IntegerType(), True),
        ])
        data = []
        user_ids = [self.faker.uuid4() for _ in range(num_users)]
        post_ids = [self.faker.uuid4() for _ in range(num_posts)]
        for user_id in user_ids:
            num_views = random.randint(1, num_posts)
            viewed_posts = random.sample(post_ids, num_views)
            for post_id in viewed_posts:
                post_timestamp = self.faker.date_time_between(start_date="-30d", end_date="now")
                post_content = self.faker.paragraph()
                num_comments = random.randint(0, 3)
                comment_timestamps = [
                    self.faker.date_time_between_dates(datetime_start=post_timestamp, datetime_end=datetime.now())
                    for _ in range(num_comments)
                ]
                comment_contents = [self.faker.paragraph() for _ in range(num_comments)]
                data.append((user_id, post_id, post_timestamp, None if num_comments == 0 else comment_timestamps[0], post_content, "" if num_comments == 0 else comment_contents[0], 1, num_comments))

                for i in range(1, num_comments):
                    data.append((user_id, post_id, post_timestamp, comment_timestamps[i], post_content, comment_contents[i], 0, 0))
        df = self.spark.createDataFrame(data, schema)
        plot_data_points(df)
        return df

def save_to_csv(df, file_path):
    df.write.save(file_path,'csv','append')
    
if __name__ == '__main__':
    data_ingestion = Data_Ingestion()
    synthetic_data = data_ingestion.generate_synthetic_data(10, 100)
    synthetic_data.to_csv('synthetic_data.csv', index=False)
    print('Synthetic data generated and saved to synthetic_data.csv')