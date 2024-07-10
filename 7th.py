import pandas as pd
import numpy as np
import plotly.graph_objects as go

df = pd.read_excel(r"C:\Users\naird\OneDrive - Dun and Bradstreet\Documents\Data for Charts.xlsx", sheet_name='Data')

# Cap the scores at 100
df['customer'] = np.clip(df['customer'], 0, 100)
df['business'] = np.clip(df['business'], 0, 100)
df['workspace'] = np.clip(df['workspace'], 0, 100)

# Create a DataFrame for sorting
data = pd.DataFrame({
    'Location': df['locations'],
    'Customer': df['customer'],
    'Business': df['business'],
    'Workspace': df['workspace']
})

# Sort the DataFrame by Industry
location_order = ['Single', '2 to 5', '6 to 25', '25 to 100', 'more than 100']
data['Location'] = pd.Categorical(data['Location'], categories=location_order, ordered=True)

# Sort the DataFrame by the defined order
data_sorted = data.sort_values(by='Location')

fig = go.Figure()

# Adding box plots with grey frames
fig.add_trace(go.Box(
    y=data_sorted['Customer'], x=data_sorted['Location'], boxpoints='all', jitter=0.3, pointpos=0, name='Customer',
    marker_size=1, marker=dict(color='#ee2938'), fillcolor='#FFFFFF', line=dict(color='black'),
    showlegend=False
))
fig.add_trace(go.Box(
    y=data_sorted['Business'], x=data_sorted['Location'], boxpoints='all', jitter=0.3, pointpos=0, name='Business',
    marker_size=1, marker=dict(color='#ffc70a'), fillcolor='#FFFFFF', line=dict(color='black'),
    showlegend=False
))
fig.add_trace(go.Box(
    y=data_sorted['Workspace'], x=data_sorted['Location'], boxpoints='all', jitter=0.3, pointpos=0, name='Workspace',
    marker_size=1, marker=dict(color='#5f004b'), fillcolor='#FFFFFF', line=dict(color='black'),
    showlegend=False
))

# Adding dummy scatter traces for legends
fig.add_trace(go.Scatter(
    x=[None], y=[None], mode='markers', marker=dict(size=10, color='#ee2938'),
    legendgroup='Customer', showlegend=True, name='Customer'
))
fig.add_trace(go.Scatter(
    x=[None], y=[None], mode='markers', marker=dict(size=10, color='#ffc70a'),
    legendgroup='Business', showlegend=True, name='Business'
))
fig.add_trace(go.Scatter(
    x=[None], y=[None], mode='markers', marker=dict(size=10, color='#5f004b'),
    legendgroup='Workspace', showlegend=True, name='Workspace'
))

# Update layout
fig.update_layout(
    title=dict(text='DMI based on Location', font=dict(color='black', size=24, family='Arial', weight='bold')),
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
    height=900
)

fig.show()
