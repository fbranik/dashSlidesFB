# no need to delete this - it won't show up in the presentation unless you add it to presentation.py

# necessary imports - do not change
from dash import html, dcc, Input, Output, State
from server import app
import dash_bootstrap_components as dbc

# custom imports
# ...
# red: #9c1000, main-blue: #325d88, dark-orange: #6e2600

import dash_mantine_components as dmc
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from fs.filesize import binary as binarySize
import pandas as pd

from custom_utilities.custom_functions import create_table
from time import sleep

mediaFolder = "/Users/fbran/Desktop/"
features = ['Working Set Size', 'Computational Load Type', 'Message Size', 'Number of Messages',
            'Number of Nodes', 'Processes per Node']
times = ['Computation Time', 'Measured Communication Time',
         'Derived Communication Time', 'Total Time', 'Communication to Total Time Ratio']

modelScenario = "BtPredict"

arisDatasetToTrain = pd.read_csv(f'assets/btPredictionsMaximum.csv', sep=',')

arisDatasetToTrain['Computational_Load_Type'] = arisDatasetToTrain['Computational_Load_Type'].str.replace('_', ' ')
arisDatasetToTrain.columns = arisDatasetToTrain.columns.str.replace('_', ' ')

modelResults = dbc.Row(
        children=[

                dbc.Row([
                        dbc.Col([
                                html.P('Colored Feature', style={"font-size": "20px"}),
                                dmc.Select(
                                        id='colorMeasurementsComparisonBtPredict',
                                        value='Number of Nodes',
                                        data=features,
                                        style={'text-align'   : 'left',
                                               'padding-right': '10px'},
                                        clearable=False
                                )
                        ], style={"width": "450px", "padding-right": "20px", "padding-left": "30px"}),

                ]),
                dbc.Row([

                        dbc.Col([dcc.Graph(id="graphMeasurementsComparisonBtPredict")],
                                style={"padding"    : "20px", "textAlign": "center", "display": "flex",
                                       "align-items": "center", "justify-content": "center"}),
                ]),

        ])

title = 'NAS BT Prediction'
titleBar = html.H4(title, className="text-white p-4 mb-2 text-left", style={"font-size" : "30px",
                                                                            "background": "slategray"})

content = [
        titleBar,
        html.Br(),
        modelResults

]


@app.callback(
        Output("graphMeasurementsComparisonBtPredict", "figure"),
        Input("colorMeasurementsComparisonBtPredict", "value"),
)
def generateMeasurementsComparisonChart(colorMeasurementsComparison):
    plottedDataDf = arisDatasetToTrain.copy(deep=True)

    categoryOrders = {
            'Working Set Size':
                list(plottedDataDf.sort_values(by='Working Set Size (Bytes)')['Working Set Size'].unique()),
            'Message Size'    :
                list(plottedDataDf.sort_values(by='Message Size (Bytes)')['Message Size'].unique()),
    }

    if colorMeasurementsComparison != 'Working Set Size' and colorMeasurementsComparison != 'Message Size':
        categoryOrders[colorMeasurementsComparison] = (
                list(plottedDataDf.sort_values(by=colorMeasurementsComparison)[colorMeasurementsComparison].unique()))

    plottedDataDf.sort_values(by=colorMeasurementsComparison, inplace=True)

    plottedDataDf[colorMeasurementsComparison] = plottedDataDf[colorMeasurementsComparison].astype(str)

    p1 = max(max(plottedDataDf['Measured Communication Time']),
             max(plottedDataDf['Tuned Gradient Boosting Model SUM']))
    p2 = min(min(plottedDataDf['Measured Communication Time']),
             min(plottedDataDf['Tuned Gradient Boosting Model SUM']))

    fig2 = px.line(x=[p2, p1], y=[p2, p1])
    fig2.update_traces(line_color='#b8cff5', line_width=2)

    fig1 = px.scatter(plottedDataDf, x=plottedDataDf['Measured Communication Time'],
                      y=plottedDataDf['Tuned Gradient Boosting Model SUM'],
                      color=plottedDataDf[colorMeasurementsComparison],
                      color_discrete_sequence=px.colors.qualitative.Vivid, hover_data=features,
                      category_orders=categoryOrders)
    fig1.update_traces(marker=dict(size=12, ))

    figMeasurementsComparison = go.Figure(data=fig2.data + fig1.data)

    figMeasurementsComparison.update_layout(
            uirevision=True,
            autosize=False,
            width=1600,
            height=1500,
            xaxis_title='Measured Communication Time', font_family="CMU Serif",

            yaxis_title='Predicted Time', template="ggplot2",
            coloraxis={"colorscale": [(0, "blue"), (0.5, "purple"), (1, "red")]},
            font=dict(size=30),
    )
    figMeasurementsComparison.update_layout({
            "paper_bgcolor": "rgba(0, 0, 0, 0)",
    })
    figMeasurementsComparison.update_layout(
            legend=dict(traceorder='normal',
                        title_text=colorMeasurementsComparison,
                        font_size=25,
                        orientation="h",
                        yanchor="bottom",
                        y=1.02,
                        xanchor="left",
                        x=0)
    )

    figMeasurementsComparison.update_layout(
            uirevision=True,
            autosize=False,
            width=800,
            height=700,
            xaxis_title='Measured Communication Time', font_family="CMU Serif",

            yaxis_title='Predicted Time', template="ggplot2",
            coloraxis={"colorscale": [(0, "blue"), (0.5, "purple"), (1, "red")]},
            font=dict(size=16),
    )
    figMeasurementsComparison.update_layout({
            "paper_bgcolor": "rgba(0, 0, 0, 0)",
    })
    figMeasurementsComparison.update_layout(
            legend=dict(traceorder='normal',
                        title_text=colorMeasurementsComparison,
                        font_size=14,
                        orientation="h",
                        yanchor="bottom",
                        y=1.02,
                        xanchor="left",
                        x=0)
    )

    return figMeasurementsComparison
