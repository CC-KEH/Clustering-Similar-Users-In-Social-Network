import os
import random
from datetime import datetime
from faker import Faker
import pandas as pd
import boto3
from dotenv import load_dotenv
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, TimestampType, IntegerType

load_dotenv()

access_key = os.getenv("AWS_ACCESS_KEY")
secret_key = os.getenv("AWS_SECRET_KEY")

class Data_Ingestion:
    def __init__(self):
        self.faker = Faker()
        self.spark = SparkSession.builder.appName("DataIngestion") \
    .config("spark.hadoop.fs.s3a.access.key", access_key) \
    .config("spark.hadoop.fs.s3a.secret.key", secret_key) \
    .config("spark.hadoop.fs.s3a.endpoint", "s3.amazonaws.com").getOrCreate()
        
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
        return df

    def save_to_s3(self, df, bucket_name, file_path):
        df.write.mode('overwrite').parquet(f"s3a://{bucket_name}/{file_path}")

# Example usage
data_ingestion = Data_Ingestion()
df = data_ingestion.initiate_data_ingestion(num_users=10, num_posts=5)
data_ingestion.save_to_s3(df, "your-bucket-name", "path/to/save/data")
