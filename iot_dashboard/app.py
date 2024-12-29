import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go

from database.db import get_topics, get_fields_for_topic, get_data_for_topic_and_field


# Initialize the Dash app
app = dash.Dash(__name__)

# Create a layout
app.layout = html.Div(children=[
    html.H1(children='InfluxDB Data Visualization'),

    dcc.Dropdown(
        id='topic-dropdown',
        options=[{'label': topic, 'value': topic} for topic in get_topics()],
        placeholder='Select a topic'
    ),

    dcc.Dropdown(
        id='field-dropdown',
        placeholder='Select a field'
    ),

    dcc.Graph(
        id='example-graph'
    )
])

# Callback to update the field dropdown based on selected topic
@app.callback(
    Output('field-dropdown', 'options'),
    Input('topic-dropdown', 'value')
)
def set_fields_options(selected_topic):
    if selected_topic is None:
        return []
    fields = get_fields_for_topic(selected_topic)
    return [{'label': field, 'value': field} for field in fields]

# Callback to update the graph based on selected topic and field
@app.callback(
    Output('example-graph', 'figure'),
    [Input('topic-dropdown', 'value'),
     Input('field-dropdown', 'value')]
)
def update_graph(selected_topic, selected_field):
    if selected_topic is None or selected_field is None:
        return {'data': [], 'layout': {'title': 'Data from InfluxDB'}}
    
    filtered_data = get_data_for_topic_and_field(selected_topic, selected_field)
    
    return {
        'data': [
            go.Scatter(
                x=[record[0] for record in filtered_data],
                y=[record[1] for record in filtered_data],
                mode='lines+markers'
            )
        ],
        'layout': {
            'title': f'Data for {selected_topic} - {selected_field}'
        }
    }

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)