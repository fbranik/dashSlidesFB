import requests
import random
import bs4 as bs
from dash import html
# file for custom functions
import pandas as pd


def my_function():
    return 0


def print_lorem_ipsum():
    r = requests.get(
            "https://baconipsum.com/api/?type=meat-and-filler&paras=5&start-with-lorem=1"
    )
    # r = requests.get('https://loripsum.net/api/20/medium/plaintext')
    return r.json()


def new_random_colors():
    return dict(
            background="rgba({},{},{},.9)".format(
                    *[random.randint(100, 255) for x in range(3)]
            ),
            maxWidth="700px",
            textAlign="center",
            margin="auto",
    )


def create_table(df):
    columns, values = df.columns, df.values
    header = [html.Tr([html.Th(col) for col in columns])]
    rows = [html.Tr([html.Td(cell) for cell in row]) for row in values]
    table = [html.Thead(header), html.Tbody(rows)]
    return table
