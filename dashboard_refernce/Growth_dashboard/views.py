import base64
import numpy as np
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd


def read_excel_data(file_path):
    try:
        # Read data from Excel and skip the specified number of rows
        excel_data = pd.read_excel(file_path, index_col=None)
        return excel_data

    except Exception as e:
        return None


def custom_round(value):
    if isinstance(value, (float, np.float64)):
        # If value is a float or NumPy float64, apply custom_round
        decimal_part = value - int(value)
        if decimal_part >= 0.5:
            return min(int(value) + 1, 100)
        else:
            return min(int(value), 100)
    elif isinstance(value, np.ndarray):
        # If value is a NumPy array, apply custom_round element-wise
        return np.vectorize(custom_round)(value)
    else:
        try:
            return custom_round(float(value))
        except (ValueError, TypeError):
            return value


@login_required
def dashboard_view(request):
    try:
        # Specify the static file path
        excel_file_path = '/home/neosoft/Desktop/dashboard_gene/dashboard_refernce/Growth_dashboard/files/Data_input1.xlsx'

        # Read data from Excel
        excel_data = read_excel_data(excel_file_path)

        if excel_data is not None:
            # Process data as before
            short_name = excel_data['Short Name'].to_list()[1:]
            actual_overall_progress = np.round(excel_data['Actual_Overall Progress'] * 100, 2).apply(
                custom_round).to_list()[1:]
            comp = np.round(excel_data['% Comp'][:1] * 100, 2).astype(float).apply(custom_round).to_list()
            balance = np.round(excel_data['% Balance'][:1] * 100, 2).astype(float).apply(custom_round).to_list()

            # Assuming excel_data is your DataFrame
            actual_batch_data = excel_data.loc[0, 'Actual_Batch01':'Actual_Batch10'] * 100

            # Create separate variables for batch names and values
            batch_names = actual_batch_data.index.to_list()
            batch_values = actual_batch_data.apply(custom_round).to_list()

            # Call the function to get additional values
            months_list, values_list = excel_data_view_data_input_file_2()

            # # Generate the pie chart
            # pie_chart_stream = generate_pie_chart(comp[0], balance[0])
            #
            # # Convert the BytesIO object to a base64-encoded string
            # pie_chart_base64 = base64.b64encode(pie_chart_stream.getvalue()).decode('utf-8')
            #
            # # Generate the bar graph
            # bar_graph_stream = generate_bar_graph(batch_names, batch_values)
            #
            # # Convert the BytesIO object to a base64-encoded string
            # bar_graph_base64 = base64.b64encode(bar_graph_stream.getvalue()).decode('utf-8')
            #
            # # Generate the vertical bar graph
            # vertical_bar_graph_stream = generate_vertical_bar_graph(short_name, actual_overall_progress)
            #
            # # Convert the BytesIO object to a base64-encoded string
            # vertical_bar_graph_base64 = base64.b64encode(vertical_bar_graph_stream.getvalue()).decode('utf-8')
            #
            # # Generate the line plot
            # line_plot_stream = generate_line_plot(months_list, values_list)
            #
            # # Convert the BytesIO object to a base64-encoded string
            # line_plot_base64 = base64.b64encode(line_plot_stream.getvalue()).decode('utf-8')

            # Pass the data to the HTML template
            context = {
                'short_name': short_name,
                'actual_overall_progress': actual_overall_progress,
                'comp': comp[0],
                'balance': balance[0],
                'actual_batch_names': batch_names,
                'actual_batch_values': batch_values,
                'Months': months_list,
                'progress': values_list,
                # 'pie_chart_base64': pie_chart_base64,  # Add the pie chart data to the context
                # 'bar_graph_base64': bar_graph_base64,  # Add the bar graph data to the context
                # 'vertical_bar_graph_base64': vertical_bar_graph_base64,
                # # Add the vertical bar graph data to the context
                # 'line_plot_base64': line_plot_base64,  # Add the line plot data to the context

            }

            return render(request, 'Growth_dashboard/index.html', {'data': context})
        else:
            return HttpResponse("Error reading Excel file. Please check the file format.")

    except Exception as e:
        return HttpResponse(f"Error processing the file: {e}")

    return render(request, 'Growth_dashboard/index.html')


def excel_data_view_data_input_file_2():
    # Excel file path
    excel_file_path = '/home/neosoft/Desktop/dashboard_gene/dashboard_refernce/Growth_dashboard/files/Data_Input-2.xlsx'

    # Read data from Excel
    df = pd.read_excel(excel_file_path)

    # Extracting the column names
    columns = df.columns

    # Extracting the "% Cumulative Plan" row
    cumulative_plan_row = df[df['Month'] == '% Cumulative Plan']

    # Replacing NaN values with 0
    cumulative_plan_values = cumulative_plan_row.values[0][1:]
    cumulative_plan_values = [0 if pd.isna(value) else value for value in cumulative_plan_values]

    # Rounding values to 2 decimal places and multiplying by 100
    rounded_values = [custom_round(value * 100) for value in cumulative_plan_values]

    # Creating separate lists for months and values
    months_list = list(columns[1:len(rounded_values) + 1])  # Exclude the first element (Month)
    values_list = rounded_values

    return months_list, values_list
