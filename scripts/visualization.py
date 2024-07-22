import seaborn as sns
import matplotlib.pyplot as plt

class Visualizer:
    def __init__(self):
        pass

    def visualize(self, pca_features, user_activity):
        plt.figure(figsize=(10, 6))
        sns.scatterplot(
            x=pca_features[:, 0],
            y=pca_features[:, 1],
            hue=user_activity["cluster"],
            palette="viridis",
            s=100,
            alpha=0.7,
        )
        plt.xlabel("PCA Feature 1")
        plt.ylabel("PCA Feature 2")
        plt.title("User Clusters")
        plt.legend(title="Cluster")
        plt.savefig('static/visualization.png')
        plt.show()
    
    def analyze_clusters(self, user_activity):
        cluster_analysis = user_activity.groupby("cluster").mean()
        print(cluster_analysis)
        return cluster_analysis