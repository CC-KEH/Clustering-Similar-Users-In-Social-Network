from pyspark.sql import SparkSession
from pyspark.sql.functions import col, countDistinct, sum as spark_sum
from pyspark.ml.feature import VectorAssembler,StandardScaler, PCA as SparkPCA
from pyspark.ml import Pipeline
from pyspark.sql.functions import when

class Data_Transformation:
    def __init__(self):
        # Initialize a Spark session
        self.spark = SparkSession.builder.appName("DataTransformation").getOrCreate()

    def initiate_data_transformation(self,spark_df):
        # Aggregate data by user_id
        user_activity = spark_df.groupBy("user_id").agg(
            countDistinct("post_id").alias("unique_posts"),
            spark_sum("view_count").alias("total_views"),
            spark_sum("comment_count").alias("total_comments")
        )
        # Calculate comment_to_view_ratio
        user_activity = user_activity.withColumn(
            "comment_to_view_ratio",
            when(col("total_views") != 0, col("total_comments") / col("total_views")).otherwise(0)
        )
        # Features to scale
        feature_columns = ["unique_posts", "total_views", "total_comments", "comment_to_view_ratio"]
        # Vector assembler
        assembler = VectorAssembler(inputCols=feature_columns, outputCol="features")
        # Standard Scaler
        scaler = StandardScaler(inputCol="features", outputCol="scaled_features")
        # PCA
        pca = SparkPCA(k=2, inputCol="scaled_features", outputCol="pca_features")
        # Create a pipeline
        pipeline = Pipeline(stages=[assembler, scaler, pca])
        # Fit and transform the data
        pipeline_model = pipeline.fit(user_activity)
        transformed_data = pipeline_model.transform(user_activity)
        # Select the required columns
        result_df = transformed_data.select("user_id", "pca_features")
        # Convert Spark DataFrame to Pandas DataFrame for further use
        pca_features = result_df.toPandas()
        return pca_features, user_activity.toPandas()
