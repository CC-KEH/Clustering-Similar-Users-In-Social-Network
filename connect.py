import pandas as pd

if __name__ == "__main__":
    data_ingestion = Data_Ingestion()
    df = data_ingestion.initiate_data_ingestion(num_users=50,num_posts=100)
   
    df["post_timestamp"] = pd.to_datetime(df["post_timestamp"])
    df["comment_timestamp"] = pd.to_datetime(df["comment_timestamp"])

    # Handle missing comment_timestamp and comment_content
    df["comment_timestamp"] = df["comment_timestamp"].fillna(pd.NaT)
    df["comment_content"] = df["comment_content"].fillna("")

   
    data_transformation = Data_Transformation()
    pca_features,user_activity = data_transformation.initiate_data_transformation(df)
    
    print(pca_features)
    
    model_trainer = Model_Trainer()
    model_trainer.initiate_model_trainer(pca_features,user_activity)

    data_visualizer = Visualizer()
    data_visualizer.visualize(pca_features=pca_features, user_activity=user_activity)