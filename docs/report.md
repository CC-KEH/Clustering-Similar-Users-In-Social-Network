# Project Report: Social Media Community Using Optimized Clustering Algorithm

## 1. Introduction

### 1.1 Project Background

In the era of social media, understanding user behavior is crucial for targeted marketing, improving user experience, and enhancing community engagement. This project focuses on clustering users in a social network based on their activity data using a Big Data approach. By applying clustering techniques, we can identify distinct groups of users with similar behaviors.

### 1.2 Objectives

- To generate and process synthetic user activity data for a social network.
- To perform clustering on users based on their activity patterns using Big Data tools and techniques.
- To visualize the resulting clusters to gain insights into user behavior.

### 1.3 Scope

The scope of this project includes data ingestion, transformation, clustering, and visualization. The project utilizes Apache Spark for handling large datasets, Scikit-learn for clustering, and Plotly for visualizations, with a web interface developed using Flask and Flask-SocketIO for real-time interactions.

## 2. Methodology

### 2.1 Data Ingestion

Synthetic data is generated using the `Faker` library. The data includes user IDs, post IDs, timestamps, content, and interaction counts. This data simulates user activities such as posting, viewing, and commenting.

- **Tools Used**: Faker, Apache Spark
- **Data Attributes**:
  - `user_id`: Unique identifier for each user.
  - `post_id`: Unique identifier for each post.
  - `post_timestamp`: Timestamp of post creation.
  - `comment_timestamp`: Timestamp of comment creation.
  - `post_content`: Content of the post.
  - `comment_content`: Content of the comment.
  - `view_count`: Number of views for the post.
  - `comment_count`: Number of comments on the post.

### 2.2 Data Transformation

Data is aggregated to calculate user activity metrics such as unique posts, total views, and total comments. Features are scaled, and Principal Component Analysis (PCA) is applied to reduce dimensionality.

- **Tools Used**: Apache Spark, PCA
- **Transformation Steps**:
  - Aggregate data by `user_id`.
  - Calculate `comment_to_view_ratio`.
  - Scale features using `StandardScaler`.
  - Reduce dimensions with PCA to extract two principal components.

### 2.3 Model Training

The K-Means clustering algorithm is applied to group users based on their activity patterns. The elbow method is used to determine the optimal number of clusters.

- **Tools Used**: Scikit-learn
- **Modeling Steps**:
  - Calculate WCSS for different numbers of clusters.
  - Determine the optimal number of clusters using the elbow method.
  - Train the K-Means model and assign cluster labels to users.

### 2.4 Visualization

The clustered data is visualized using Plotly, creating an interactive scatter plot to display user clusters.

- **Tools Used**: Plotly
- **Visualization Steps**:
  - Plot PCA features on a 2D scatter plot.
  - Color code points based on cluster assignments.
  - Export the plot as an interactive HTML file.

### 2.5 Web Application

A web interface is created using Flask and Flask-SocketIO to run the pipeline and display results with real-time updates.

- **Tools Used**: Flask, Flask-SocketIO
- **Application Features**:
  - Endpoint to initiate the pipeline.
  - Real-time updates during pipeline execution.
  - Display of clustering results.

## 3. Results

- **Data Ingestion**: Successfully generated and ingested synthetic data for 1,000 users and 10,000 posts.
- **Data Transformation**: Reduced dimensions from 4 features to 2 principal components.
- **Model Training**: Identified optimal clusters and assigned cluster labels to users.
- **Visualization**: Created an interactive plot displaying user clusters.
- **Web Application**: Provided a functional interface for running and visualizing the pipeline.

## 4. Conclusion

The project successfully implemented a pipeline to cluster users in a social network based on their activity data. The use of Big Data tools like Apache Spark enabled efficient data processing, and the K-Means algorithm effectively grouped users into meaningful clusters. The visualization provided insights into user behavior, which can be leveraged for various applications such as targeted marketing and user segmentation.

## 5. Future Work

- **Real Data Integration**: Apply the pipeline to real social network data for more accurate clustering results.
- **Advanced Clustering Techniques**: Explore other clustering algorithms like DBSCAN or hierarchical clustering for comparison.
- **Feature Expansion**: Incorporate additional features such as user demographics and network connections.
- **Scalability**: Optimize the pipeline for larger datasets and real-time processing.

## 6. References

- [Apache Spark Documentation](https://spark.apache.org/docs/latest/)
- [Scikit-learn Documentation](https://scikit-learn.org/stable/documentation.html)
- [Faker Library](https://faker.readthedocs.io/en/master/)
- [Plotly Documentation](https://plotly.com/python/)
- [Flask Documentation](https://flask.palletsprojects.com/en/2.0.x/)
- [Flask-SocketIO Documentation](https://flask-socketio.readthedocs.io/en/latest/)

---
