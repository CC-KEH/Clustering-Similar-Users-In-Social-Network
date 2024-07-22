from sklearn.cluster import KMeans
from kneed import KneeLocator

class Model_Trainer:
    def __init__(self):
        pass

    def initiate_model_trainer(self, pca_features, user_activity):
        wcs = []
        for k in range(1, 11):
            kmeans = KMeans(n_clusters=k, init='k-means++', random_state=44)
            kmeans.fit(pca_features)
            wcs.append(kmeans.inertia_)

        kneedle = KneeLocator(range(1, 11), wcs, curve='convex', direction='decreasing')
        optimal_k = kneedle.elbow
        print(f'Optimal number of clusters: {optimal_k}')

        kmeans = KMeans(n_clusters=optimal_k, init='k-means++', random_state=44)
        clusters = kmeans.fit_predict(pca_features)
        user_activity['cluster'] = clusters
        return user_activity