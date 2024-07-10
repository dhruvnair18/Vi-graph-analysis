# import pandas as pd
# df=pd.read_excel( r'C:\Users\naird\OneDrive - Dun and Bradstreet\Documents\Copy of VI_Raw_Data_PowerPivot (002).xlsx', sheet_name='DMI 2024')
 
# ls_indus=df['INDUSTRY(Client)'].tolist()
# ls_cust=df['CUSTOMER_SCORE'].tolist()
# ls_buss=df['BUSINESS_SCORE'].tolist()
# ls_work=df['WORKSPACE_SCORE'].tolist()
 
# import plotly.graph_objects as go
# x = ls_indus
# fig = go.Figure()
# fig.add_trace(go.Box(y=ls_cust,x=ls_indus,boxpoints='all',jitter=0.3,pointpos=0,name='Customer',marker_size=1,marker_color='#3D9970'))
# fig.add_trace(go.Box(y=ls_buss,x=ls_indus,name='Business',boxpoints='all',jitter=0.3,pointpos=0,marker_size=1,marker_color='#FF4136'))
# fig.add_trace(go.Box(y=ls_work,x=ls_indus,name='Workspace',boxpoints='all',jitter=0.3,pointpos=0,marker_size=1,marker_color='#FF851B'))
# fig.update_layout(yaxis_title='Scores at Turnover Level',boxmode='group') # group together boxes of the different traces for each value of x)
# fig.update_layout(autosize=False,width=1600,height=900)
 
# fig.show()

# import pandas as pd
# df=pd.read_excel( r'C:\Users\naird\OneDrive - Dun and Bradstreet\Documents\Copy of VI_Raw_Data_PowerPivot (002).xlsx', sheet_name='DMI 2024')
 
# ls_indus=df['INDUSTRY(Client)'].tolist()
# ls_cust=df['CUSTOMER_SCORE'].tolist()
# ls_buss=df['BUSINESS_SCORE'].tolist()
# ls_work=df['WORKSPACE_SCORE'].tolist()
 
# import plotly.graph_objects as go
# x = ls_indus
# fig = go.Figure()
# fig.add_trace(go.Box(y=ls_cust,x=ls_indus,boxpoints='all',jitter=0.3,pointpos=0,name='Customer',marker_size=1,marker_color='#3D9970'))
# fig.add_trace(go.Box(y=ls_buss,x=ls_indus,name='Business',boxpoints='all',jitter=0.3,pointpos=0,marker_size=1,marker_color='#FF4136'))
# fig.add_trace(go.Box(y=ls_work,x=ls_indus,name='Workspace',boxpoints='all',jitter=0.3,pointpos=0,marker_size=1,marker_color='#FF851B'))
# fig.update_layout(yaxis_title='Scores at Turnover Level',boxmode='group') # group together boxes of the different traces for each value of x)
# fig.update_layout(autosize=False,width=1600,height=900)
 
# fig.show()

# import pandas as pd
# import plotly.graph_objects as go

# df = pd.read_excel(r'C:\Users\naird\OneDrive - Dun and Bradstreet\Documents\Copy of VI_Raw_Data_PowerPivot (002).xlsx', sheet_name='DMI 2024')

# ls_indus = df['INDUSTRY(Client)'].tolist()
# ls_cust = df['CUSTOMER_SCORE'].tolist()

# fig = go.Figure()

# fig.add_trace(go.Box(
#     y=ls_cust, x=ls_indus, boxpoints='all', jitter=0.3, pointpos=0, name='Customer',
#     marker_size=1, marker=dict(color='#FF5733'), fillcolor='#FFFFFF', line=dict(color='black'),
#     showlegend=False
# ))

# fig.add_trace(go.Scatter(
#     x=[None], y=[None], mode='markers', marker=dict(size=10, color='#FF5733'),
#     legendgroup='Customer', showlegend=True, name='Customer'
# ))

# annotations = []
# for ind, score in zip(ls_indus, ls_cust):
#     annotations.append(dict(
#         x=ind,
#         y=score,
#         text=str(score),
#         showarrow=False,
#         font=dict(color='black', size=10)
#     ))

# fig.update_layout(
#     yaxis_title='Scores at Industry Level',
#     boxmode='group',  # group together boxes of the different traces for each value of x
#     template='plotly_dark',
#     plot_bgcolor='rgba(0, 0, 0, 0)',
#     paper_bgcolor='rgba(0, 0, 0, 0)',
#     legend=dict(font=dict(color='black')),  # Set legend text color to black
#     yaxis=dict(title_font=dict(color='black'), tickfont=dict(color='black')),  # Set y-axis title and tick color to black
#     xaxis=dict(tickfont=dict(color='black')),
#     autosize=False,
#     width=1600,
#     height=900,
#     annotations=annotations
# )

# # Show the figure
# fig.show()
# import pandas as pd
# df=pd.read_excel( r'C:\Users\naird\OneDrive - Dun and Bradstreet\Documents\Copy of VI_Raw_Data_PowerPivot (002).xlsx', sheet_name='DMI 2024')
 
# ls_indus=df['INDUSTRY(Client)'].tolist()
# ls_cust=df['CUSTOMER_SCORE'].tolist()
# ls_buss=df['BUSINESS_SCORE'].tolist()
# ls_work=df['WORKSPACE_SCORE'].tolist()
 
# import plotly.graph_objects as go
# x = ls_indus
# fig = go.Figure()
# fig.add_trace(go.Box(y=ls_cust,x=ls_indus,boxpoints='all',jitter=0.3,pointpos=0,name='Customer',marker_size=1,marker_color='#3D9970'))
# fig.add_trace(go.Box(y=ls_buss,x=ls_indus,name='Business',boxpoints='all',jitter=0.3,pointpos=0,marker_size=1,marker_color='#FF4136'))
# fig.add_trace(go.Box(y=ls_work,x=ls_indus,name='Workspace',boxpoints='all',jitter=0.3,pointpos=0,marker_size=1,marker_color='#FF851B'))
# fig.update_layout(yaxis_title='Scores at Turnover Level',boxmode='group') # group together boxes of the different traces for each value of x)
# fig.update_layout(autosize=False,width=1600,height=900)
 
# fig.show()
#####
# import pandas as pd
# df=pd.read_excel( r'C:\Users\naird\OneDrive - Dun and Bradstreet\Documents\Copy of VI_Raw_Data_PowerPivot (002).xlsx', sheet_name='DMI 2024')
 
# ls_indus=df['INDUSTRY(Client)'].tolist()
# ls_cust=df['CUSTOMER_SCORE'].tolist()
# ls_buss=df['BUSINESS_SCORE'].tolist()
# ls_work=df['WORKSPACE_SCORE'].tolist()

# import plotly.graph_objects as go
 
# fig = go.Figure()
 
# # Adding box plots with no legends
# fig.add_trace(go.Box(
#     y=ls_cust, x=ls_indus, boxpoints='all', jitter=0.3, pointpos=0, name='Customer',
#     marker_size=1, marker=dict(color='#FF5733'), fillcolor='#FFFFFF', line=dict(color='black'),
#     showlegend=False
# ))
# fig.add_trace(go.Box(
#     y=ls_buss, x=ls_indus, boxpoints='all', jitter=0.3, pointpos=0, name='Business',
#     marker_size=1, marker=dict(color='#FF4136'), fillcolor='#FFFFFF', line=dict(color='black'),
#     showlegend=False
# ))
# fig.add_trace(go.Box(
#     y=ls_work, x=ls_indus, boxpoints='all', jitter=0.3, pointpos=0, name='Workspace',
#     marker_size=1, marker=dict(color='#FF851B'), fillcolor='#FFFFFF', line=dict(color='black'),
#     showlegend=False
# ))
 
# # Adding dummy scatter traces for legends
# fig.add_trace(go.Scatter(
#     x=[None], y=[None], mode='markers', marker=dict(size=10, color='#FF5733'),
#     legendgroup='Customer', showlegend=True, name='Customer'
# ))
# fig.add_trace(go.Scatter(
#     x=[None], y=[None], mode='markers', marker=dict(size=10, color='#FF4136'),
#     legendgroup='Business', showlegend=True, name='Business'
# ))
# fig.add_trace(go.Scatter(
#     x=[None], y=[None], mode='markers', marker=dict(size=10, color='#FF851B'),
#     legendgroup='Workspace', showlegend=True, name='Workspace'
# ))
 
# # Update layout
# fig.update_layout(
#     yaxis_title='Scores at Industry Level',
#     boxmode='group',  # group together boxes of the different traces for each value of x
#     template='plotly_dark',
#     plot_bgcolor='rgba(0, 0, 0, 0)',
#     paper_bgcolor='rgba(0, 0, 0, 0)',
#     legend=dict(font=dict(color='black')),# Set legend text color to black
#     yaxis=dict(title_font=dict(color='black'), tickfont=dict(color='black')),  # Set y-axis title and tick color to black
#     xaxis=dict(tickfont=dict(color='black')),
#     autosize=False,
#     width=1600,
#     height=900
# )
 
# fig.show()

# import pandas as pd
# df=pd.read_excel( r'C:\Users\naird\OneDrive - Dun and Bradstreet\Documents\Copy of VI_Raw_Data_PowerPivot (002).xlsx', sheet_name='DMI 2024')
 
# ls_indus=df['INDUSTRY(Client)'].tolist()
# ls_cust=df['CUSTOMER_SCORE'].tolist()
# ls_buss=df['BUSINESS_SCORE'].tolist()
# ls_work=df['WORKSPACE_SCORE'].tolist()
 
# import plotly.graph_objects as go
# x = ls_indus
# fig = go.Figure()
# fig.add_trace(go.Box(y=ls_cust,x=ls_indus,boxpoints='all',jitter=0.3,pointpos=0,name='Customer',marker_size=1,marker_color='#3D9970'))
# fig.add_trace(go.Box(y=ls_buss,x=ls_indus,name='Business',boxpoints='all',jitter=0.3,pointpos=0,marker_size=1,marker_color='#FF4136'))
# fig.add_trace(go.Box(y=ls_work,x=ls_indus,name='Workspace',boxpoints='all',jitter=0.3,pointpos=0,marker_size=1,marker_color='#FF851B'))
# fig.update_layout(yaxis_title='Scores at Turnover Level',boxmode='group') # group together boxes of the different traces for each value of x)
# fig.update_layout(autosize=False,width=1600,height=900)
 
# fig.show()

# import pandas as pd
# df=pd.read_excel( r'C:\Users\naird\OneDrive - Dun and Bradstreet\Documents\Copy of VI_Raw_Data_PowerPivot (002).xlsx', sheet_name='DMI 2024')
 
# ls_indus=df['INDUSTRY(Client)'].tolist()

# ls_buss=df['BUSINESS_SCORE'].tolist()


# import plotly.graph_objects as go
 
# fig = go.Figure()
 
# # Adding box plots with no legends

# fig.add_trace(go.Box(
#     y=ls_buss, x=ls_indus, boxpoints='all', jitter=0.3, pointpos=0, name='Business',
#     marker_size=1, marker=dict(color='#FF4136'), fillcolor='#FFFFFF', line=dict(color='black'),
#     showlegend=False
# ))

# # Adding dummy scatter traces for legends

# fig.add_trace(go.Scatter(
#     x=[None], y=[None], mode='markers', marker=dict(size=10, color='#FF4136'),
#     legendgroup='Business', showlegend=True, name='Business'
# ))

# # Update layout
# fig.update_layout(
#     yaxis_title='Scores at Industry Level',
#     boxmode='group',  # group together boxes of the different traces for each value of x
#     template='plotly_dark',
#     plot_bgcolor='rgba(0, 0, 0, 0)',
#     paper_bgcolor='rgba(0, 0, 0, 0)',
#     legend=dict(font=dict(color='black')),# Set legend text color to black
#     yaxis=dict(title_font=dict(color='black'), tickfont=dict(color='black')),  # Set y-axis title and tick color to black
#     xaxis=dict(tickfont=dict(color='black')),
#     autosize=False,
#     width=1600,
#     height=900
# )
 
# fig.show()



# import pandas as pd
# df=pd.read_excel( r'C:\Users\naird\OneDrive - Dun and Bradstreet\Documents\Copy of VI_Raw_Data_PowerPivot (002).xlsx', sheet_name='DMI 2024')
 
# ls_indus=df['INDUSTRY(Client)'].tolist()
# ls_cust=df['CUSTOMER_SCORE'].tolist()
# ls_buss=df['BUSINESS_SCORE'].tolist()
# ls_work=df['WORKSPACE_SCORE'].tolist()

# import plotly.graph_objects as go
 
# fig = go.Figure()
 
# # Adding box plots with no legends

# fig.add_trace(go.Box(
#     y=ls_work, x=ls_indus, boxpoints='all', jitter=0.3, pointpos=0, name='Workspace',
#     marker_size=1, marker=dict(color='#FF851B'), fillcolor='#FFFFFF', line=dict(color='black'),
#     showlegend=False
# ))
 
# # Adding dummy scatter traces for legends

# fig.add_trace(go.Scatter(
#     x=[None], y=[None], mode='markers', marker=dict(size=10, color='#FF851B'),
#     legendgroup='Workspace', showlegend=True, name='Workspace'
# ))
 
# # Update layout
# fig.update_layout(
#     yaxis_title='Scores at Industry Level',
#     boxmode='group',  # group together boxes of the different traces for each value of x
#     template='plotly_dark',
#     plot_bgcolor='rgba(0, 0, 0, 0)',
#     paper_bgcolor='rgba(0, 0, 0, 0)',
#     legend=dict(font=dict(color='black')),# Set legend text color to black
#     yaxis=dict(title_font=dict(color='black'), tickfont=dict(color='black')),  # Set y-axis title and tick color to black
#     xaxis=dict(tickfont=dict(color='black')),
#     autosize=False,
#     width=1600,
#     height=900
# )
 
# fig.show()

# import pandas as pd
# import plotly.graph_objects as go

# # Load the Excel file
# file_path = r'C:\Users\naird\OneDrive - Dun and Bradstreet\Documents\Copy of VI_Raw_Data_PowerPivot (002).xlsx'
# df = pd.read_excel(file_path, sheet_name='DMI 2024')

# # Extract the relevant columns into lists
# ls_indus = df['INDUSTRY(Client)'].tolist()
# ls_cust = df['CUSTOMER_SCORE'].tolist()
# ls_buss = df['BUSINESS_SCORE'].tolist()
# ls_work = df['WORKSPACE_SCORE'].tolist()

# # Create a Plotly figure
# fig = go.Figure()

# # Add box plots with no legends
# fig.add_trace(go.Box(
#     y=ls_work, x=ls_indus, boxpoints='all', jitter=0.3, pointpos=0, name='Workspace',
#     marker_size=1, marker=dict(color='#FF851B'), fillcolor='#FFFFFF', line=dict(color='black'),
#     showlegend=False
# ))

# # Add dummy scatter traces for legends
# fig.add_trace(go.Scatter(
#     x=[None], y=[None], mode='markers', marker=dict(size=10, color='#FF851B'),
#     legendgroup='Workspace', showlegend=True, name='Workspace'
# ))

# # Update layout
# fig.update_layout(
#     title='Scores at Industry Level',  # Add the graph title
#     yaxis_title='Scores',
#     xaxis_title='Industry',
#     boxmode='group',  # Group together boxes of the different traces for each value of x
#     template='ggplot2',
#     plot_bgcolor='rgba(0, 0, 0, 0)',
#     paper_bgcolor='rgba(0, 0, 0, 0)',
#     legend=dict(font=dict(color='black')),  # Set legend text color to black
#     yaxis=dict(title_font=dict(color='black'), tickfont=dict(color='black')),  # Set y-axis title and tick color to black
#     xaxis=dict(tickfont=dict(color='black')),  # Set x-axis tick color to black
#     autosize=False,
#     width=1600,
#     height=900
# )

# # Show the figure
# fig.show()

# import pandas as pd
# import plotly.graph_objects as go

# df = pd.read_excel(r'C:\Users\naird\OneDrive - Dun and Bradstreet\Documents\Copy of VI_Raw_Data_PowerPivot (002).xlsx', sheet_name='DMI 2024')

# ls_indus = df['INDUSTRY(Client)'].tolist()
# ls_cust = df['CUSTOMER_SCORE'].tolist()
# ls_buss = df['BUSINESS_SCORE'].tolist()
# ls_work = df['WORKSPACE_SCORE'].tolist()

# fig = go.Figure()

# # Adding box plots with no legends
# fig.add_trace(go.Box(
#     y=ls_cust, x=ls_indus, boxpoints='all', jitter=0.3, pointpos=0, name='Customer',
#     marker_size=1, marker=dict(color='#FF5733'), fillcolor='#FFFFFF', line=dict(color='black'),
#     showlegend=False
# ))
# fig.add_trace(go.Box(
#     y=ls_buss, x=ls_indus, boxpoints='all', jitter=0.3, pointpos=0, name='Business',
#     marker_size=1, marker=dict(color='#FF4136'), fillcolor='#FFFFFF', line=dict(color='black'),
#     showlegend=False
# ))
# fig.add_trace(go.Box(
#     y=ls_work, x=ls_indus, boxpoints='all', jitter=0.3, pointpos=0, name='Workspace',
#     marker_size=1, marker=dict(color='#FF851B'), fillcolor='#FFFFFF', line=dict(color='black'),
#     showlegend=False
# ))

# # Adding dummy scatter traces for legends
# fig.add_trace(go.Scatter(
#     x=[None], y=[None], mode='markers', marker=dict(size=10, color='#FF4500'),
#     legendgroup='Customer', showlegend=True, name='Customer'
# ))
# fig.add_trace(go.Scatter(
#     x=[None], y=[None], mode='markers', marker=dict(size=10, color='#00FFFF'),
#     legendgroup='Business', showlegend=True, name='Business'
# ))
# fig.add_trace(go.Scatter(
#     x=[None], y=[None], mode='markers', marker=dict(size=10, color='#32CD32'),
#     legendgroup='Workspace', showlegend=True, name='Workspace'
# ))

# # Adding annotations for the median values
# def add_median_annotations(fig, x_data, y_data, name, color):
#     for industry in set(x_data):
#         y_vals = [y for x, y in zip(x_data, y_data) if x == industry]
#         median_val = pd.Series(y_vals).median()
#         fig.add_annotation(
#             x=industry,
#             y=median_val,
#             text=f'{median_val:.2f}',
#             showarrow=False,
#             font=dict(color=color)
#         )

# add_median_annotations(fig, ls_indus, ls_cust, 'Customer', '#000000')
# add_median_annotations(fig, ls_indus, ls_buss, 'Business', '#000000')
# add_median_annotations(fig, ls_indus, ls_work, 'Workspace', '#000000')

# # Update layout
# fig.update_layout(
#     title='DMI by Number of Operating Locations',
#     yaxis_title='Scores at Industry Level',
#     boxmode='group',  # group together boxes of the different traces for each value of x
#     template='ggplot2',
#     plot_bgcolor='rgba(0, 0, 0, 0)',
#     paper_bgcolor='rgba(0, 0, 0, 0)',
#     legend=dict(font=dict(color='black')),  # Set legend text color to black
#     yaxis=dict(title_font=dict(color='black'), tickfont=dict(color='black')),  # Set y-axis title and tick color to black
#     xaxis=dict(tickfont=dict(color='black')),
#     autosize=False,
#     width=1600,
#     height=900
# )

# fig.show()

# import pandas as pd
# import plotly.graph_objects as go

# df = pd.read_excel(r'C:\Users\naird\OneDrive - Dun and Bradstreet\Documents\Copy of VI_Raw_Data_PowerPivot (002).xlsx', sheet_name='DMI 2024')

# ls_indus = df['INDUSTRY(Client)'].tolist()
# ls_cust = df['CUSTOMER_SCORE'].tolist()
# ls_buss = df['BUSINESS_SCORE'].tolist()
# ls_work = df['WORKSPACE_SCORE'].tolist()

# # Create a DataFrame for sorting
# data = pd.DataFrame({'Industry': ls_indus, 'Customer': ls_cust, 'Business': ls_buss, 'Workspace': ls_work})

# # Sort the DataFrame by Industry
# data_sorted = data.sort_values(by='Industry')

# fig = go.Figure()

# # Adding box plots with no legends
# fig.add_trace(go.Box(
#     y=data_sorted['Customer'], x=data_sorted['Industry'], boxpoints='all', jitter=0.3, pointpos=0, name='Customer',
#     marker_size=1, marker=dict(color='#ee2938'), fillcolor='#FFFFFF', line=dict(color='black'),
#     showlegend=False
# ))
# fig.add_trace(go.Box(
#     y=data_sorted['Business'], x=data_sorted['Industry'], boxpoints='all', jitter=0.3, pointpos=0, name='Business',
#     marker_size=1, marker=dict(color='#ffc70a'), fillcolor='#FFFFFF', line=dict(color='black'),
#     showlegend=False
# ))
# fig.add_trace(go.Box(
#     y=data_sorted['Workspace'], x=data_sorted['Industry'], boxpoints='all', jitter=0.3, pointpos=0, name='Workspace',
#     marker_size=1, marker=dict(color='#5f004b'), fillcolor='#FFFFFF', line=dict(color='black'),
#     showlegend=False
# ))

# # Adding dummy scatter traces for legends
# fig.add_trace(go.Scatter(
#     x=[None], y=[None], mode='markers', marker=dict(size=10, color='#ee2938'),
#     legendgroup='Customer', showlegend=True, name='Customer'
# ))
# fig.add_trace(go.Scatter(
#     x=[None], y=[None], mode='markers', marker=dict(size=10, color='#ffc70a'),
#     legendgroup='Business', showlegend=True, name='Business'
# ))
# fig.add_trace(go.Scatter(
#     x=[None], y=[None], mode='markers', marker=dict(size=10, color='#5f004b'),
#     legendgroup='Workspace', showlegend=True, name='Workspace'
# ))

# # Adding annotations for the median values
# # def add_median_annotations(fig, x_data, y_data, name, color):
# #     for industry in sorted(set(x_data)):
# #         y_vals = [y for x, y in zip(x_data, y_data) if x == industry]
# #         median_val = pd.Series(y_vals).median()
# #         fig.add_annotation(
# #             x=industry,
# #             y=median_val,
# #             text=f'{median_val:.2f}',
# #             showarrow=False,
# #             font=dict(color=color)
# #         )

# # add_median_annotations(fig, data_sorted['Industry'], data_sorted['Customer'], 'Customer', '#000000')
# # add_median_annotations(fig, data_sorted['Industry'], data_sorted['Business'], 'Business', '#000000')
# # add_median_annotations(fig, data_sorted['Industry'], data_sorted['Workspace'], 'Workspace', '#000000')

# # Update layout
# fig.update_layout(
#     title=dict(text='DMI by Number of Operating Locations', font=dict(color='black', size=24, family='Arial', bold=True)),
#     yaxis_title='Scores at Industry Level',
#     boxmode='group',  # group together boxes of the different traces for each value of x
#     template='ggplot2',
#     plot_bgcolor='rgba(0, 0, 0, 0)',
#     paper_bgcolor='rgba(0, 0, 0, 0)',
#     legend=dict(font=dict(color='black')),  # Set legend text color to black
#     yaxis=dict(title_font=dict(color='black'), tickfont=dict(color='black')),  # Set y-axis title and tick color to black
#     xaxis=dict(tickfont=dict(color='black'), categoryorder='category ascending'),  # Arrange x-axis in ascending order
#     autosize=False,
#     width=1600,
#     height=900
# )

# fig.show()

import pandas as pd
import numpy as np
import plotly.graph_objects as go

df = pd.read_excel(r"C:\Users\naird\OneDrive - Dun and Bradstreet\Documents\Data for Charts.xlsx", sheet_name='DMI 2024')

# Cap the scores at 100
df['customer'] = np.clip(df['customer'], 0, 100)
df['business'] = np.clip(df['business'], 0, 100)
df['workspace'] = np.clip(df['workspace'], 0, 100)

# Create a DataFrame for sorting
data = pd.DataFrame({
    'Industry': df['industry'],
    'Customer': df['customer'],
    'Business': df['business'],
    'Workspace': df['workspace']
})

# Sort the DataFrame by Industry
data_sorted = data.sort_values(by='Industry')

fig = go.Figure()

# Adding box plots with no legends
fig.add_trace(go.Box(
    y=data_sorted['Customer'], x=data_sorted['Industry'], boxpoints='all', jitter=0.3, pointpos=0, name='Customer',
    marker_size=0.5, marker=dict(color='#ee2938'), fillcolor='#FFFFFF', line=dict(color='black'),
    showlegend=False
))
fig.add_trace(go.Box(
    y=data_sorted['Business'], x=data_sorted['Industry'], boxpoints='all', jitter=0.3, pointpos=0, name='Business',
    marker_size=0.5, marker=dict(color='#ffc70a'), fillcolor='#FFFFFF', line=dict(color='black'),
    showlegend=False
))
fig.add_trace(go.Box(
    y=data_sorted['Workspace'], x=data_sorted['Industry'], boxpoints='all', jitter=0.3, pointpos=0, name='Workspace',
    marker_size=0.5, marker=dict(color='#5f004b'), fillcolor='#FFFFFF', line=dict(color='black'),
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
    title=dict(text='DMI by Number of Operating Locations', font=dict(color='black', size=24, family='Arial', weight='bold')),
    yaxis_title='Scores at Industry Level',
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