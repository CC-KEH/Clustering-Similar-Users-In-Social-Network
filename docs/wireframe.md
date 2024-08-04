# Wireframe

1. **Homepage**
   - **Title**: "Social Network User Clustering"
   - **Description**: Brief explanation of the project's purpose and functionality.
   - **Button**: "Run Pipeline"
   - **Status Area**: Displays real-time updates of the pipeline progress using Flask-SocketIO.

2. **Visualization Page**
   - **Title**: "User Clusters Visualization"
   - **Plot Area**: Displays the interactive scatter plot of clustered users.
   - **Legend**: Shows cluster color coding.
   - **Button**: "Back to Homepage"

## Wireframe Details

### Homepage

```
+-----------------------------------------------------+
|          Social Network User Clustering             |
|                                                     |
|   This application clusters users based on their    |
|   activity data in a social network. Click the      |
|   button below to run the clustering pipeline.      |
|                                                     |
|   [Run Pipeline]                                    |
|                                                     |
|   ------------------------------------------------  |
|   Status:                                           |
|   - Pipeline Initialized                            |
|   - Data Ingestion Started                          |
|   - Data Transformation in Progress...              |
|   - Model Training Completed                        |
|   - Visualization Generated                         |
|                                                     |
+-----------------------------------------------------+
```

### Visualization Page

```
+-----------------------------------------------------+
|          User Clusters Visualization                |
|                                                     |
|   [Back to Homepage]                                |
|                                                     |
|   ------------------------------------------------  |
|   |                                               | |
|   |                [ Scatter Plot ]               | |
|   |                                               | |
|   ------------------------------------------------  |
|                                                     |
|   Legend:                                           |
|   - Cluster 0: Blue                                 |
|   - Cluster 1: Red                                  |
|   - Cluster 2: Green                                |
|   - ...                                             |
|                                                     |
+-----------------------------------------------------+
```

### Wireframe Explanation

1. **Homepage**:
   - The homepage provides a simple interface to introduce the project and allow users to start the clustering pipeline. The "Run Pipeline" button initiates the process, and a status area provides real-time feedback about each step of the pipeline, such as data ingestion, transformation, and model training.

2. **Visualization Page**:
   - After the pipeline completes, users are directed to a visualization page where they can see the clustering results. An interactive scatter plot displays the clusters, with each point representing a user. The legend helps identify which color corresponds to which cluster.

---
