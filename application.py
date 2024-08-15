from flask import Flask, request, jsonify, render_template, url_for
import plotly.express as px
import plotly.io as pio
from main import *


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    num_users = int(data['num_users'])
    num_posts = int(data['num_posts'])

    spark_df = data_ingestion(num_users, num_posts)
    pca_features, user_activity = data_transformation(spark_df=spark_df)
    pca_features, user_activity = model_trainer(pca_features, user_activity)
    visualize(pca_features, user_activity)

    return jsonify({
        'initial_plot_url': url_for('static', filename='ingested_data_plot.html'),
        'clustered_plot_url': url_for('static', filename='clusters_plot.html')
    })

if __name__ == '__main__':
    app.run(debug=True)
