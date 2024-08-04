import os
import pandas as pd
import plotly.express as px


def plot_data_points(spark_df):
    df = spark_df.toPandas()
    
    # Scatter plot of post timestamps and comment timestamps by user_id
    fig = px.scatter(df, x='post_timestamp', y='comment_timestamp', color='user_id', 
                     title='User Activity: Posts vs. Comments',
                     labels={'post_timestamp': 'Post Timestamp', 'comment_timestamp': 'Comment Timestamp'})
    
    # Set plot layout for better visualization
    fig.update_layout(autosize=False, width=800, height=600,
                      margin=dict(l=50, r=50, b=100, t=100, pad=4))
    
    # Convert Plotly figure to HTML for rendering
    return fig.write_html('ingested_data_plot.html')