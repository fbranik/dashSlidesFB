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
modelScenario = "messageSizeScalesModel"

arisDatasetToTrainBig = pd.read_csv(f'assets/{modelScenario}/bigMessageModelData.csv', sep=',')
arisDatasetToTrainSmall = pd.read_csv(f'assets/{modelScenario}/smallMessageModelData.csv', sep=',')

bigImportances = pd.read_csv(f'assets/{modelScenario}/bigMessageModelImportances.csv', sep=',')
smallImportances = pd.read_csv(f'assets/{modelScenario}/smallMessageModelImportances.csv', sep=',')

arisDatasetToTrainBig['Computational_Load_Type'] = arisDatasetToTrainBig['Computational_Load_Type'].str.replace('_',
                                                                                                                ' ')
arisDatasetToTrainBig.columns = arisDatasetToTrainBig.columns.str.replace('_', ' ')

arisDatasetToTrainSmall['Computational_Load_Type'] = arisDatasetToTrainSmall['Computational_Load_Type'].str.replace('_',
                                                                                                                    ' ')
arisDatasetToTrainSmall.columns = arisDatasetToTrainSmall.columns.str.replace('_', ' ')
modelResults = dbc.Row(
        children=[

                dbc.Row([
                        dbc.Col([
                                html.P('Message Size Scale', style={"font-size": "20px"}),
                                dmc.Select(
                                        id='messageSizeScale',
                                        value='Big Messages',

                                        data=['Big Messages', 'Small Messages'],
                                        style={'text-align'   : 'left',
                                               'padding-right': '10px'},
                                        clearable=False
                                )
                        ], style={"width": "450px", "padding-right": "20px", "padding-left": "30px"}),
                        dbc.Col([
                                html.P('Colored Feature', style={"font-size": "20px"}),
                                dmc.Select(
                                        id='colorMeasurementsComparison',
                                        value='Processes per Node',
                                        data=features,
                                        style={'text-align'   : 'left',
                                               'padding-right': '10px'},
                                        clearable=False
                                )
                        ], style={"width": "450px", "padding-right": "20px", "padding-left": "30px"}),

                ]),
                dbc.Row([

                        dbc.Col([dcc.Graph(id="graphMeasurementsComparison")],
                                style={"padding"    : "20px", "textAlign": "center", "display": "flex",
                                       "align-items": "center", "justify-content": "center"}),
                        dbc.Col([html.Table(id="featureImportancesMessageSizeScale", )],
                                style={"padding"    : "20px", "textAlign": "left", "display": "flex",
                                       "align-items": "center", "justify-content": "center"}),
                ]),

        ])

title = 'Message Size Models'
titleBar = html.H4(title, className="text-white p-4 mb-2 text-left", style={"font-size" : "30px",
                                                                            "background": "slategray"})

introExp = ["The available dataset, was used in three different ways to create Gradient Boosting models."]

experiments = html.Dl([
        html.Dt(["Message Size Models"]),
        html.Dd(["- Two different sub-models were compiled, one for each message size scale. This was"
                 " done after seeing the difference in performance in the preliminary experiments"]),
        html.Dt(["Train Small/Test Big Model"]),
        html.Dd(["- The model is trained only on data from [4, 8, 16] nodes (this subset"
                 " is also split for training/testing), and performance is checked for"
                 " the larger setups of [32, 64] nodes."]),
        html.Dt(["Main Model"]), html.Dd(["- This model uses the whole dataset."]),
])
text1 = html.Div(
        [
                dbc.Row(
                        [
                                dbc.Col(html.Div(dbc.Card(
                                        [

                                                dbc.CardBody(
                                                        [
                                                                html.P(introExp),
                                                        ]
                                                ),
                                        ],
                                        className="mb-3", style={"color": "black", "background": "ghostwhite"},
                                        outline=True
                                ))),

                        ], style={"padding-left": "50px", "padding-right": "50px", "width": "100%"}
                ),
        ], style={"textAlign"  : "justify", "display": "flex",
                  "align-items": "left", "justify-content": "left"}
)
text2 = html.Div(
        [
                dbc.Row(
                        [
                                dbc.Col(html.Div(dbc.Card(
                                        [
                                                dbc.CardHeader("Scenarios",
                                                               style={"background": "slategray", "color": "white"}),
                                                dbc.CardBody(
                                                        [
                                                                experiments,
                                                        ]
                                                ),
                                        ],
                                        className="mb-3", style={"color": "black", "background": "ghostwhite"},
                                        outline=True
                                ))),

                        ], style={"padding-left": "50px", "padding-right": "50px", "width": "100%"}
                ),
        ], style={"textAlign"  : "justify", "display": "flex",
                  "align-items": "left", "justify-content": "left"}
)

content = [
        titleBar,
        html.Br(),
        modelResults

]


@app.callback(
        Output("graphMeasurementsComparison", "figure"),
        Input("colorMeasurementsComparison", "value"),
        Input("messageSizeScale", "value"),
)
def generateMeasurementsComparisonChart(colorMeasurementsComparison, messageSizeScale):
    if messageSizeScale == "Big Messages":
        plottedDataDf = arisDatasetToTrainBig.copy(deep=True)
    else:
        plottedDataDf = arisDatasetToTrainSmall.copy(deep=True)

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
             max(plottedDataDf['Tuned Gradient Boosting Model Communication Time']))
    p2 = min(min(plottedDataDf['Measured Communication Time']),
             min(plottedDataDf['Tuned Gradient Boosting Model Communication Time']))

    fig2 = px.line(x=[p2, p1], y=[p2, p1])
    fig2.update_traces(line_color='#b8cff5', line_width=2)

    fig1 = px.scatter(plottedDataDf, x=plottedDataDf['Measured Communication Time'],
                      y=plottedDataDf['Tuned Gradient Boosting Model Communication Time'],
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


@app.callback(
        Output("featureImportancesMessageSizeScale", "children"),
        Input("messageSizeScale", "value"),
)
def generateMeasurementsComparisonChart(messageSizeScale):
    if messageSizeScale == "Big Messages":
        importances = bigImportances
    else:
        importances = smallImportances
    condition = (
            (importances["Model"] == "Tuned Gradient Boosting")
    )
    importances = importances[condition].drop(['Model'], axis=1).transpose()
    importances["Feature"] = importances.index

    importances.rename(columns={2: " ", 'Feature': "Feature Importances"}, inplace=True)
    importances = importances.loc[:, ['Feature Importances', ' ']]
    importances[" "] = importances[" "].apply(lambda x: round(x, 2))
    importances["Feature Importances"] = importances["Feature Importances"].apply(lambda x: x.replace("_", " "))
    importances.sort_values(by=" ", inplace=True, ascending=False)

    return create_table(importances)
