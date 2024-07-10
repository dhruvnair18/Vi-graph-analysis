import pandas as pd
import numpy as np
import plotly.graph_objects as go

# Read the data
df = pd.read_excel(r"C:\Users\naird\OneDrive - Dun and Bradstreet\Documents\Data for Charts.xlsx", sheet_name='Data')

# Cap the scores at 100
df['DMI'] = np.clip(df['DMI'], 0, 100)

# Create a DataFrame for sorting
data = pd.DataFrame({
    'Industry': df['industry'],
    'DMI': df['DMI']
})

# Sort the DataFrame by Industry
data_sorted = data.sort_values(by='DMI')

fig = go.Figure()

# Adding box plots with no legends
fig.add_trace(go.Box(
    y=data_sorted['DMI'], x=data_sorted['Industry'], boxpoints='all', jitter=0.3, pointpos=0, name='DMI',
    marker_size=1, marker=dict(color='#ee2938'), fillcolor='#FFFFFF', line=dict(color='black'),
    showlegend=False
))

# Adding dummy scatter traces for legends


def add_median_annotations(fig, x_data, y_data, name, color):
    offset = 2  # Adjust this value to move the annotation slightly above the median
    for industry in sorted(set(x_data)):
        y_vals = [y for x, y in zip(x_data, y_data) if x == industry]
        median_val = pd.Series(y_vals).median()
        fig.add_annotation(
            x=industry,
            y=median_val + offset,
            text=f'{median_val:.1f}',
            showarrow=False,
            font=dict(color=color, family='Arial Black', size=14),  # Set font to Arial Black and increase size
            align='center'
        )

add_median_annotations(fig, data_sorted['Industry'], data_sorted['DMI'], 'DMI', '#000000')

# Update layout
fig.update_layout(
    title=dict(text='DMI based on Industries', font=dict(color='black', size=24, family='Arial Black'), y=0.95, x=0.5, xanchor='center', yanchor='top'),
    yaxis_title='DMI',
    boxmode='group',  # group together boxes of the different traces for each value of x
    template='ggplot2',
    plot_bgcolor='rgba(0, 0, 0, 0)',
    paper_bgcolor='rgba(0, 0, 0, 0)',
    legend=dict(font=dict(color='black')),  # Set legend text color to black
    yaxis=dict(title_font=dict(color='black'), tickfont=dict(color='black')),  # Set y-axis title and tick color to black
    xaxis=dict(tickfont=dict(color='black'), categoryorder='category ascending'),  # Arrange x-axis in ascending order
    autosize=False,
    width=1600,
    height=900,
    margin=dict(t=40)  # Adjust the top margin
)

fig.show()
