# Clustering Similar Users and Social Network

This project aims to ingest, transform, and visualize synthetic user activity data, followed by clustering users based on their activity patterns using K-Means clustering. The project leverages PySpark for data processing, Airflow for workflow orchestration, MLflow for experiment tracking, and AWS for deployment and storage.

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
  - [Integration with PySpark](#integration-with-pyspark)
  - [Integration with Airflow](#integration-with-airflow)
  - [Integration with MLflow](#integration-with-mlflow)
  - [Integration with AWS](#integration-with-aws)
  - [Example](#example)
  - [License](#license)

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/CC-KEH/user-activity-clustering.git
    ```

2. Navigate to the project directory:

    ```sh
    cd user-activity-clustering
    ```

3. Create a virtual environment and activate it:

    ```sh
    conda create -p venv python=3.9
    conda activate venv/
    ```

4. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

## Usage

To run the project, execute the `main.py` script:

```sh
python main.py
```

## Project Structure

The project directory is organized as follows:

```plaintext
user-activity-clustering/
│
├── dags/
│   └── user_activity_dag.py
├── scripts/
│   ├── data_ingestion.py
│   ├── data_transformation.py
│   ├── model_trainer.py
│   └── visualizer.py
├── main.py
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

## Integration with PySpark

To handle large datasets efficiently, we use PySpark for data processing.

1. Install PySpark:

    ```sh
    pip install pyspark
    ```

2. Update your data ingestion and transformation scripts to use PySpark DataFrames.

## Integration with Airflow

Airflow is used for orchestrating the workflow of data ingestion, transformation, and model training.

1. Install Airflow:

    ```sh
    pip install apache-airflow
    ```

2. Create a DAG file (`user_activity_dag.py`) under the `dags/` directory.

3. Define tasks for each step in the workflow and set up task dependencies.

## Integration with MLflow

MLflow is used for experiment tracking and model management.

1. Install MLflow:

    ```sh
    pip install mlflow
    ```

2. Update your model training script to log metrics and models with MLflow.

## Integration with AWS

AWS is used for deployment and storage.

1. Install the AWS SDK:

    ```sh
    pip install boto3
    ```

2. Set up AWS credentials and configure services like S3 for storage and EC2 for deployment.

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
