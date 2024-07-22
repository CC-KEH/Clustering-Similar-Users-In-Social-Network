import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

class Data_Transformation:
    def __init__(self):
        pass
    
    def reduce_dimensions(self, user_activity):
        scaler = StandardScaler()
        features = user_activity.drop(["user_id"], axis=1)  # Drop non-numeric columns
        scaled_features = scaler.fit_transform(features)
        pca = PCA(n_components=2)
        pca_features = pca.fit_transform(scaled_features)
        return pca_features, user_activity

    def initiate_data_transformation(self, df):
        df["post_timestamp"] = pd.to_datetime(df["post_timestamp"])
        df["comment_timestamp"] = pd.to_datetime(df["comment_timestamp"])

        # Handle missing comment_timestamp and comment_content
        df["comment_timestamp"] = df["comment_timestamp"].fillna(pd.NaT)
        df["comment_content"] = df["comment_content"].fillna("")
        
        user_activity = df.groupby("user_id").agg(
            {
                "post_id": "nunique",  # Number of unique posts viewed
                "view_count": "sum",  # Total number of post views
                "comment_count": "sum",  # Total number of comments made
            }
        ).reset_index()
        user_activity["comment_to_view_ratio"] = (
            user_activity["comment_count"] / user_activity["view_count"]
        )
        user_activity["comment_to_view_ratio"].fillna(0, inplace=True)
        pca_features, user_activity = self.reduce_dimensions(user_activity)
        return pca_features, user_activity