from sklearn.cluster import KMeans
from kneed import KneeLocator
import numpy as np
import os

os.environ['OMP_NUM_THREADS'] = '1'

class Model_Trainer:
    def __init__(self):
        pass
    
    def initiate_model_trainer(self, pca_features, user_activity):
        os.environ['OMP_NUM_THREADS'] = '1'
        # Extract the PCA features as a numpy array
        pca_data = np.array(pca_features['pca_features'].tolist())

        # Calculate WCSS (Within-Cluster Sum of Squares) for different numbers of clusters
        wcs = []
        for k in range(1, 11):
            kmeans = KMeans(n_clusters=k, init='k-means++', random_state=44)
            kmeans.fit(pca_data)
            wcs.append(kmeans.inertia_)

        # Determine the optimal number of clusters using the elbow method
        kneedle = KneeLocator(range(1, 11), wcs, curve='convex', direction='decreasing')
        optimal_k = kneedle.elbow

        print(f'Optimal number of clusters: {optimal_k}')

        # Train the KMeans model with the optimal number of clusters
        kmeans = KMeans(n_clusters=optimal_k, init='k-means++', random_state=44)
        clusters = kmeans.fit_predict(pca_data)

        # Add the cluster assignments to the user_activity DataFrame
        user_activity['cluster'] = clusters

        return user_activity
    