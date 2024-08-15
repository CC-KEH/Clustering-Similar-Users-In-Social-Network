# Clustering Similar Users and Social Network

This project aims to ingest, transform, and visualize synthetic user activity data, followed by clustering users based on their activity patterns using K-Means clustering. The project leverages PySpark for data processing and Flask for local deployment.

## Table of Contents

- [Clustering Similar Users and Social Network](#clustering-similar-users-and-social-network)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Project Structure](#project-structure)
  - [Classes and Methods](#classes-and-methods)
    - [Data\_Ingestion](#data_ingestion)
    - [Data\_Transformation](#data_transformation)
    - [Model\_Trainer](#model_trainer)
    - [Visualizer](#visualizer)
  - [Example](#example)
  - [License](#license)

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/CC-KEH/Clustering-Similar-Users-In-Social-Network.git
    ```

2. Create a virtual environment and activate it:

    ```sh
    conda create -p venv python=3.9
    conda activate venv/
    ```

3. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. To run the project, execute the `setup.py` script this will create the package:

```sh
    python setup.py
```

2. Now, execute `application.py` script:

```sh
    python application.py
```

## Project Structure

The project directory is organized as follows:

```plaintext

├── src/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   ├── model_trainer.py
│   │   └── visualization.py
│   ├── pipelines/
│   │   └── prediction.py
│   │   └── stage_01_data_ingestion.py
│   │   └── stage_02_data_transformation.py
│   │   └── stage_03_model_trainer.py
│   │   └── stage_04_visualization.py
│   ├── tests/
│   │   ├── test_data_ingestion.py
│   │   ├── test_data_transformation.py
│   │   ├── test_model_trainer.py
│   │   └── test_web_app.py
│   │   └── testing_pipeline.py
│   └── utils/
│       ├── __init__.py
│       └── common.py
├── application.py
├── main.py
├── setup.py
├── requirements.txt
├── README.md
└── ...
```

## Classes and Methods

### Data_Ingestion

Handles the generation of synthetic data.

- `initiate_data_ingestion(self, num_users, num_posts)`: Generates synthetic data for a specified number of users and posts.

### Data_Transformation

Handles the transformation of the ingested data.

- `reduce_dimensions(self, user_activity)`: Applies PCA to reduce data dimensions.
- `initiate_data_transformation(self, df)`: Aggregates user activity data and applies PCA.

### Model_Trainer

Handles the training of the clustering model.

- `initiate_model_trainer(self, pca_features, user_activity)`: Determines the optimal number of clusters using the elbow method and trains the K-Means model.

### Visualizer

Handles the visualization of the results.

- `visualize(self, pca_features, user_activity)`: Visualizes the user clusters in a scatter plot.
- `analyze_clusters(self, user_activity)`: Analyzes and prints the mean characteristics of each cluster.

## Example

The `main.py` script provides an example of how to use the classes and methods. Here is a brief overview:

1. Ingest synthetic data:

    ```python
    data_ingestion = Data_Ingestion()
    df = data_ingestion.initiate_data_ingestion(num_users=50, num_posts=100)
    ```

2. Transform the data:

    ```python
    data_transformation = Data_Transformation()
    pca_features, user_activity = data_transformation.initiate_data_transformation(df)
    ```

3. Train the clustering model:

    ```python
    model_trainer = Model_Trainer()
    user_activity = model_trainer.initiate_model_trainer(pca_features, user_activity)
    ```

4. Visualize the results:

    ```python
    data_visualizer = Visualizer()
    data_visualizer.visualize(pca_features, user_activity)
    cluster_analysis = data_visualizer.analyze_clusters(user_activity)
    ```

## License

This project is licensed under the MIT License.

---
