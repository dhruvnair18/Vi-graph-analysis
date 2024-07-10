# import numpy as np
# import panda as pd
# import pandas as pd 

# df = pd.read_excel(r"C:\Users\naird\OneDrive - Dun and Bradstreet\Documents\VI_Raw_Data_PowerPivot.xlsx") 
# print(df)

# import pandas as pd 

# df = pd.read_excel(r"C:\Users\naird\OneDrive - Dun and Bradstreet\Documents\VI_Raw_Data_PowerPivot.xlsx", 
# 				index_col = 0) 
# print(df) 

# import pandas as pd

# # Define the file path
# file_path = r"C:\Users\naird\OneDrive - Dun and Bradstreet\Documents\VI_Raw_Data_PowerPivot.xlsx"

# # Read the Excel file
# df = pd.read_excel(file_path)

# # Display the first few rows to understand the structure
# print(df.head())

# # Calculate the median and IQR for the 'TOTAL_SCORE' column
# grouped = df.groupby('NO_OF_EMPLOYEE')['TOTAL_SCORE'].agg(['median', 'quantile'])

# # Calculate the IQR specifically for '26-100 employees'
# subset = df[df['NO_OF_EMPLOYEE'] == '26-100 empl']
# Q1 = subset['TOTAL_SCORE'].quantile(0.25)
# Q3 = subset['TOTAL_SCORE'].quantile(0.75)
# IQR = Q3 - Q1

# # Add the IQR calculation to the grouped DataFrame
# grouped['IQR'] = df.groupby('NO_OF_EMPLOYEE')['TOTAL_SCORE'].apply(lambda x: x.quantile(0.75) - x.quantile(0.25))

# # Display the median and IQR for each group
# print(grouped)

# # Display the specific IQR for '26-100 employees'
# print(f"IQR for '26-100 empl': {IQR}")

# # Show the results as required
# print(f"Median TOTAL_SCORE for '26-100 empl': {subset['TOTAL_SCORE'].median()}")
# print(f"IQR for '26-100 empl': {IQR}")
# import pandas as pd

# # Load the Excel file
# file_path = r"C:\Users\naird\OneDrive - Dun and Bradstreet\Documents\VI_Raw_Data_PowerPivot.xlsx"  
# df_dmi_2024 = pd.read_excel(file_path, sheet_name='DMI 2024')

# # Extract the 'TOTAL_SCORE' column, ensuring to handle any non-numeric data properly
# total_score = pd.to_numeric(df_dmi_2024['TOTAL_SCORE'], errors='coerce')

# # Calculate the median
# median_total_score = total_score.median()

# # Calculate the interquartile range (IQR)
# q1 = total_score.quantile(0.25)
# q3 = total_score.quantile(0.75)
# q4=total_score.quantile(1.00)
# iqr_total_score = q3 - q1

# # Print the results
# print("First quartile of TOTAL SCORE: ",q1)
# print("Median of TOTAL_SCORE:", median_total_score)
# print("Third quartile of TOTAL SCORE: ",q3)
# print("Fourth quartile of TOTAL_SCORE: ", q4)
# print("Interquartile Range (IQR) of TOTAL_SCORE:", iqr_total_score)

# import numpy as np
# # import panda as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# dataset=[10,11,12,13,14,15,20,25,70,75,80,100]
# # sns.histplot(dataset)

# q1,q3=np.percentile(dataset,[25,75])
# print(q1,q3)
# iqr=q3-q1
# lower_fence= q1-(1.5*iqr)
# higher_fence= q3+(1.5*iqr)
# print(lower_fence,higher_fence)

# sns.boxplot(data=dataset)
# checkk
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt

# file_path = r"C:\Users\naird\OneDrive - Dun and Bradstreet\Documents\Copy of VI_Raw_Data_PowerPivot (002).xlsx"
# df_dmi_2024 = pd.read_excel(file_path, sheet_name='DMI 2024')

# total_score = pd.to_numeric(df_dmi_2024['TOTAL_SCORE'], errors='coerce')
# #print(df_dmi_2024.columns)
# sns.boxplot(
#     x = "Locations", 
#     y = total_score,
#     showmeans=True,        
#     data=df_dmi_2024
# )
# # sns.stripplot(x="Locations", y=total_score, data=df_dmi_2024, color="grey") 

# plt.xlabel("Location")
# plt.ylabel("Total Score")
# plt.title("DMI")
# plt.xticks(rotation=45)  

# plt.show()
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
# import numpy as np

# file_path = r"C:\Users\naird\OneDrive - Dun and Bradstreet\Documents\Copy of VI_Raw_Data_PowerPivot (002).xlsx"
# df_dmi_2024 = pd.read_excel(file_path, sheet_name='DMI 2024')

# total_score = pd.to_numeric(df_dmi_2024['TOTAL_SCORE'], errors='coerce')

# plt.figure(figsize=(10, 6))
# boxplot = sns.boxplot(
#     x="Locations", 
#     y=total_score,
#     showmeans=True,        
#     data=df_dmi_2024
# )

# def add_quartile_labels(ax, data, locations):
#     loc_list = list(locations) 
#     for loc in loc_list:
#         loc_data = data[data['Locations'] == loc]['TOTAL_SCORE'].dropna()
#         if len(loc_data) > 0:
#             q1 = np.percentile(loc_data, 25)
#             q2 = np.percentile(loc_data, 50)  
#             q3 = np.percentile(loc_data, 75)
#             ax.text(loc_list.index(loc), q1, f'Q1: {q1:.2f}', horizontalalignment='center', size='small', color='black')
#             ax.text(loc_list.index(loc), q2, f'Q2: {q2:.2f}', horizontalalignment='center', size='small', color='black')
#             ax.text(loc_list.index(loc), q3, f'Q3: {q3:.2f}', horizontalalignment='center', size='small', color='black')

# add_quartile_labels(boxplot, df_dmi_2024, df_dmi_2024['Locations'].unique())

# plt.xlabel("Location")
# plt.ylabel("Total Score")
# plt.title("DMI")
# plt.xticks(rotation=45)  

# plt.show()

# import pandas as pd
# # import seaborn as sns
# # import matplotlib.pyplot as plt

# # Read the data from the Excel file
# file_path = r"C:\Users\naird\OneDrive - Dun and Bradstreet\Documents\VI_Raw_Data_PowerPivot.xlsx"
# df_dmi_2024 = pd.read_excel(file_path, sheet_name='DMI 2024')

# # Extract the 'TOTAL_SCORE' column, handling non-numeric data
# # total_score = pd.to_numeric(df_dmi_2024['TOTAL_SCORE'], errors='coerce')

# # # Create the boxplot with respect to location types
# # sns.boxplot(
# #     x = "Locations",  # Set categorical variable on the x-axis
# #     y = total_score,
# #     showmeans=True,        # Show mean as well (optional)
# #     data=df_dmi_2024
# # )

# # # Customize the plot (optional)
# # plt.xlabel("Location Type")
# # plt.ylabel("Total Score")
# # plt.title("Distribution of Total Score by Location Type")
# # plt.xticks(rotation=45)  # Rotate x-axis labels for better readability if many categories

# # # Display the plot
# # plt.show()
# print(df_dmi_2024['Locations'].dtype)


# import matplotlib.pyplot as plt
# import seaborn as sns
# import pandas as pd
# import os

# # Correct file path
# file_path = r'C:\Users\naird\OneDrive - Dun and Bradstreet\Documents\Copy of VI_Raw_Data_PowerPivot (002).xlsx'

# # Check if the file exists and is accessible
# if not os.path.exists(file_path):
#     raise FileNotFoundError(f"The file at {file_path} does not exist.")
# if not os.access(file_path, os.R_OK):
#     raise PermissionError(f"Permission denied to read the file at {file_path}.")

# # Load the necessary columns from the Excel file
# df = pd.read_excel(file_path, sheet_name='DMI 2024', usecols=['TURNOVER', 'TOTAL_SCORE'])

# # Ensure 'TOTAL_SCORE' is numeric
# df['TOTAL_SCORE'] = pd.to_numeric(df['TOTAL_SCORE'], errors='coerce')

# # Define the order for the 'TURNOVER' categories
# turnover_order = ['less than 10 crores', '10 to 50 crores', '50 to 100 crores', '100 to 250 crores', '250 crores']

# # Adjust the 'TURNOVER' values to match the new categories
# df['TURNOVER'] = df['TURNOVER'].replace({
#     '250 to 500 crores': '250 crores',
#     'above 500 crores': '250 crores'
# })

# # Create a box plot
# plt.figure(figsize=(12, 6))
# sns.boxplot(x='TURNOVER', y='TOTAL_SCORE', data=df, order=turnover_order)

# # Add quartile labels
# for turnover in turnover_order:
#     data = df[df['TURNOVER'] == turnover]['TOTAL_SCORE'].dropna()
#     if not data.empty:
#         q1 = data.quantile(0.25)
#         median = data.median()
#         q3 = data.quantile(0.75)
#         plt.text(turnover_order.index(turnover), q1, f'Q1: {q1:.2f}', ha='center', va='center', fontsize=9, color='black', weight='semibold')
#         plt.text(turnover_order.index(turnover), median, f'Median: {median:.2f}', ha='center', va='center', fontsize=9, color='black', weight='semibold')
#         plt.text(turnover_order.index(turnover), q3, f'Q3: {q3:.2f}', ha='center', va='center', fontsize=9, color='black', weight='semibold')

# # Customize plot
# plt.title('Box Plot of TOTAL_SCORE by TURNOVER')
# plt.xlabel('TURNOVER')
# plt.ylabel('TOTAL_SCORE')
# plt.xticks(rotation=45)
# plt.grid(False)

# # Show the plot
# plt.tight_layout()
# plt.show()

# import matplotlib.pyplot as plt
# import seaborn as sns
# import pandas as pd
# import os

# # Correct file path
# file_path = r'C:\Users\naird\OneDrive - Dun and Bradstreet\Documents\Copy of VI_Raw_Data_PowerPivot (002).xlsx'

# # Check if the file exists and is accessible
# if not os.path.exists(file_path):
#     raise FileNotFoundError(f"The file at {file_path} does not exist.")
# if not os.access(file_path, os.R_OK):
#     raise PermissionError(f"Permission denied to read the file at {file_path}.")

# # Load the necessary columns from the Excel file
# df = pd.read_excel(file_path, sheet_name='DMI 2024', usecols=['TURNOVER', 'TOTAL_SCORE'])

# # Ensure 'TOTAL_SCORE' is numeric
# df['TOTAL_SCORE'] = pd.to_numeric(df['TOTAL_SCORE'], errors='coerce')

# # Define the order for the 'TURNOVER' categories
# turnover_order = ['less than 10 crores', '10 to 50 crores', '50 to 100 crores', '100 to 250 crores', '250 crores']

# # Adjust the 'TURNOVER' values to match the new categories
# df['TURNOVER'] = df['TURNOVER'].replace({
#     '250 to 500 crores': '250 crores',
#     'above 500 crores': '250 crores'
# })

# # Create a box plot
# plt.figure(figsize=(12, 6))
# sns.boxplot(x='TURNOVER', y='TOTAL_SCORE', data=df, order=turnover_order, showmeans=True, meanline=True)

# # Add quartile labels
# for turnover in turnover_order:
#     data = df[df['TURNOVER'] == turnover]['TOTAL_SCORE'].dropna()
#     if not data.empty:
#         q1 = round(data.quantile(0.25))
#         median = round(data.median())
#         q3 = round(data.quantile(0.75))
#         plt.text(turnover_order.index(turnover), q1, f'Q1: {q1}', ha='center', va='center', fontsize=10, color='black', weight='bold', bbox=dict(facecolor='white', alpha=0.5))
#         plt.text(turnover_order.index(turnover), median, f'Median: {median}', ha='center', va='center', fontsize=10, color='black', weight='bold', bbox=dict(facecolor='white', alpha=0.5))
#         plt.text(turnover_order.index(turnover), q3, f'Q3: {q3}', ha='center', va='center', fontsize=10, color='black', weight='bold', bbox=dict(facecolor='white', alpha=0.5))

# # Customize plot
# plt.title('Box Plot of TOTAL_SCORE by TURNOVER')
# plt.xlabel('TURNOVER')
# plt.ylabel('TOTAL_SCORE')
# plt.xticks(rotation=45)

# # Show the plot
# plt.tight_layout()
# plt.show()

# import matplotlib.pyplot as plt
# import seaborn as sns
# import pandas as pd
# import os

# # Correct file path
# file_path = r'C:\Users\naird\OneDrive - Dun and Bradstreet\Documents\Copy of VI_Raw_Data_PowerPivot (002).xlsx'

# # Check if the file exists and is accessible
# if not os.path.exists(file_path):
#     raise FileNotFoundError(f"The file at {file_path} does not exist.")
# if not os.access(file_path, os.R_OK):
#     raise PermissionError(f"Permission denied to read the file at {file_path}.")

# # Load the necessary columns from the Excel file
# df = pd.read_excel(file_path, sheet_name='DMI 2024', usecols=['TURNOVER', 'TOTAL_SCORE'])

# # Ensure 'TOTAL_SCORE' is numeric
# df['TOTAL_SCORE'] = pd.to_numeric(df['TOTAL_SCORE'], errors='coerce')

# # Define the new order for the 'TURNOVER' categories
# turnover_order = ['less than 10 crores', '10 to 100 crores', '100 and above']

# # Adjust the 'TURNOVER' values to match the new categories
# df['TURNOVER'] = df['TURNOVER'].replace({
#     '10 to 50 crores': '10 to 100 crores',
#     '50 to 100 crores': '10 to 100 crores',
#     '100 to 250 crores': '100 and above',
#     '250 crores': '100 and above',
#     '250 to 500 crores': '100 and above',
#     'above 500 crores': '100 and above'
# })

# # Create a box plot
# plt.figure(figsize=(12, 6))
# sns.boxplot(x='TURNOVER', y='TOTAL_SCORE', data=df, order=turnover_order, showmeans=True, meanline=True)

# # Add quartile labels
# for turnover in turnover_order:
#     data = df[df['TURNOVER'] == turnover]['TOTAL_SCORE'].dropna()
#     if not data.empty:
#         q1 = round(data.quantile(0.25))
#         median = round(data.median())
#         q3 = round(data.quantile(0.75))
#         plt.text(turnover_order.index(turnover), q1, f'Q1: {q1}', ha='center', va='center', fontsize=10, color='black', weight='bold', bbox=dict(facecolor='white', alpha=0.5))
#         plt.text(turnover_order.index(turnover), median, f'Median: {median}', ha='center', va='center', fontsize=10, color='black', weight='bold', bbox=dict(facecolor='white', alpha=0.5))
#         plt.text(turnover_order.index(turnover), q3, f'Q3: {q3}', ha='center', va='center', fontsize=10, color='black', weight='bold', bbox=dict(facecolor='white', alpha=0.5))

# # Customize plot
# plt.title('Box Plot of TOTAL_SCORE by TURNOVER')
# plt.xlabel('TURNOVER')
# plt.ylabel('TOTAL_SCORE')
# plt.xticks(rotation=45)

# # Show the plot
# plt.tight_layout()
# plt.show()

####
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# Read the data from the uploaded file
file_path =r"C:\Users\naird\OneDrive - Dun and Bradstreet\Documents\Data for Charts.xlsx"
df = pd.read_excel(file_path, sheet_name='Data')

# Cap the scores at 100
df['DMI'] = np.clip(df['DMI'], 0, 100)

# Create a DataFrame for sorting
data = pd.DataFrame({
    'Location': df['locations'],
    'DMI': df['DMI']
})

# Define the desired order for the Location column
location_order = ['Single', '2 to 5', '6 to 25', '25 to 100', 'more than 100']
data['Location'] = pd.Categorical(data['Location'], categories=location_order, ordered=True)

# Sort the DataFrame by the defined order
data_sorted = data.sort_values(by='Location')

fig = go.Figure()

# Adding box plots with no legends
fig.add_trace(go.Box(
    y=data_sorted['DMI'], x=data_sorted['Location'], boxpoints='all', jitter=0.3, pointpos=0, name='DMI',
    marker_size=1, marker=dict(color='#5f004b'), fillcolor='#FFFFFF', line=dict(color='black'),
    showlegend=False
))

# Adding median annotations
def add_median_annotations(fig, x_data, y_data, name, color):
    offset = 2  # Adjust this value to move the annotation slightly above the median
    for industry in sorted(set(x_data)):
        y_vals = [y for x, y in zip(x_data, y_data) if x == industry]
        median_val = pd.Series(y_vals).median()
        fig.add_annotation(
            x=industry,
            y=median_val + offset,
            text=f'{median_val:.2f}',
            showarrow=False,
            font=dict(color=color)  # Removed 'weight' as it is not a valid property
        )

add_median_annotations(fig, data_sorted['Location'], data_sorted['DMI'], 'DMI', '#000000')

# Update layout
fig.update_layout(
    title=dict(text='DMI based on Locations', font=dict(color='black', size=24, family='Arial'), y=0.95, x=0.5, xanchor='center', yanchor='top'),
    yaxis_title='DMI',
    boxmode='group',  # group together boxes of the different traces for each value of x
    template='ggplot2',
    plot_bgcolor='rgba(0, 0, 0, 0)',
    paper_bgcolor='rgba(0, 0, 0, 0)',
    legend=dict(font=dict(color='black')),  # Set legend text color to black
    yaxis=dict(title_font=dict(color='black'), tickfont=dict(color='black')),  # Set y-axis title and tick color to black
    xaxis=dict(
        tickfont=dict(color='black'),
        categoryorder='array',
        categoryarray=location_order  # Set the x-axis categories in the desired order
    ),
    autosize=False,
    width=1600,
    height=900,
    margin=dict(t=40)  # Adjust the top margin
)
