import pandas as pd
import plotly.express as px

class Visualizer:
    def __init__(self):
        pass

    def visualize(self, pca_features, user_activity):
        # Ensure the PCA features are properly extracted
        pca_data = pd.DataFrame(pca_features['pca_features'].tolist(), columns=['pca_x', 'pca_y'])

        pca_data['cluster'] = user_activity['cluster']

        fig = px.scatter(
            pca_data, 
            x='pca_x', 
            y='pca_y', 
            color='cluster',
            title='User Clusters Visualization',
            labels={'cluster': 'Cluster'},
            color_continuous_scale=px.colors.qualitative.T10
        )

        fig.update_layout(
            xaxis_title='PCA Feature 1',
            yaxis_title='PCA Feature 2',
            legend_title='Cluster',
            template='plotly_dark',
            width=800,
            height=600
        )

        # fig.show()

        fig.write_html('static/clusters_plot.html')
        
    