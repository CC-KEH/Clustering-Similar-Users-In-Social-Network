from flask import Flask, render_template, jsonify, send_from_directory
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/run_pipeline')
def run_pipeline():
    airflow_url = "http://localhost:8080/api/v1/dags/data_pipeline/dag_runs"
    response = requests.post(airflow_url, json={"conf": {}})
    if response.status_code == 200:
        return jsonify({"message": "Pipeline triggered successfully"})
    else:
        return jsonify({"message": "Failed to trigger pipeline"}), 500

@app.route('/visualization')
def visualization():
    return send_from_directory('static', 'visualization.png')

if __name__ == '__main__':
    app.run(debug=True)