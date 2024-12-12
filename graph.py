import pandas as pd
import plotly.express as px
#import plotly.figure_factory as ff
import csv

data = {"Sports": ["Basketball", "Tennis", "Hockey", "Football", "Cricket", "Baseball"], 
"Distance(Km)": [4, 4.8, 9, 11.2, 12, 0.6]}

df = pd.DataFrame (data)

fig = px.bar (
    df, 
    x = "Sports", 
    y = "Distance(Km)", 
    title = "Average Distance of Sports",
    labels = {"Distance(Km)": "Distance (Km)", "Sports": "Sports"}
)

fig.show()

