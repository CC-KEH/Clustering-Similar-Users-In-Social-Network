import tweepy
import pandas as pd
import s3fs
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

import os
import re
from dotenv import load_dotenv

load_dotenv()

class Data_Ingestion:
    def __init__(self):
        self.api_key = os.getenv('API_KEY')
        self.api_key_secret = os.getenv('API_KEY_SECRET')
        self.access_token = os.getenv('ACCESS_TOKEN')
        self.access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')
        self.raw_filename = 'raw_post_data.csv'
        
    def connect(self):
        auth = tweepy.OAuthHandler(self.api_key, self.api_key_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        self.api = tweepy.API(auth)
    
    def fetch_tweets(self, post_id, count):
        # Fetch the original post
        post = self.api.get_status(post_id)

        # Fetch comments on the post
        comments = tweepy.Cursor(self.api.search_tweets, q=f'to:{post.user.screen_name}', since_id=post_id, tweet_mode='extended').items(count)

        # Process post and comments
        data_list = [[post.user.screen_name, post.text, post.user.followers_count, 'post']]
        
        for comment in comments:
            if hasattr(comment, 'in_reply_to_status_id_str') and comment.in_reply_to_status_id_str == post_id:
                data_list.append([comment.user.screen_name, comment.full_text, comment.user.followers_count, 'comment'])

        # Create DataFrame for raw data
        raw_df = pd.DataFrame(data_list, columns=["user", "text", "followers_count", "type"])

        # Save raw data to CSV
        raw_df.to_csv(self.raw_filename, index=False)

        return raw_df
    
    def initiate_data_ingestion(self, post_id, count=10):
        self.connect()
        data = self.fetch_tweets(post_id, count)
        return data

class Data_Transformation:
    def __init__(self):
        pass

    def clean_text(self,text):
        text = re.sub(r'http\S+', '', text)
        text = re.sub(r'@\w+', '', text)
        text = re.sub(r'#\w+', '', text)
        text = re.sub(r'\n', '', text)
        text = re.sub(r'\W', ' ', text)
        text = text.lower()
        return text
    
    def initiate_data_transformation(self, data):
        data['clean_text'] = data['text'].apply(self.clean_text)
        return data

class Model_Trainer:
    def __init__(self,n_clusters=5):
        self.vectorizer = TfidfVectorizer(stop_words='english', max_features=1000)
        self.kmeans = KMeans(n_clusters=n_clusters, random_state=42)
        
    def initiate_model_trainer(self, data):
        X = self.vectorizer.fit_transform(data['clean_text'])
        data['cluster'] = self.kmeans.fit_predict(X)
        
        return data

class Analysis:
    def __init__(self):
        pass
    
    def analyze_clusters(self):
        #* Analysis
        cluster_analysis = data.groupby('cluster').agg({
        'user': 'count',
        'followers_count': 'mean'
        }).reset_index()
        print(cluster_analysis)
    
    def visualize_clusters(self):
        #* Visualization
        pca = PCA(n_components=2)
        X_pca = pca.fit_transform(X.toarray())

        plt.scatter(X_pca[:, 0], X_pca[:, 1], c=data['cluster'], cmap='viridis')
        plt.title('K-Means Clustering of Social Media Users')
        plt.xlabel('PCA Component 1')
        plt.ylabel('PCA Component 2')
        plt.show()
        
if __name__ == "__main__":
    print("Data Ingestion in progress...")
    #* Data Ingestion 
    data_ingestion = Data_Ingestion()
    post_id = '1732037140111102460'
    data = data_ingestion.initiate_data_ingestion(post_id)
    data.to_csv('raw_data_other.csv', index=False)
    print("Data fetched successfully!")
            
    print("Data Transformation in progress...")
    #* Data Transformation 
    transformer = Data_Transformation()
    data = transformer.initiate_data_transformation(data)
    print("Data Transformation completed!")
    
    print("Model Training in progress...")
    #* Model Trainer 
    model_trainer = Model_Trainer()
    model_trainer.initiate_model_trainer(data)
    print("Model Training completed!")