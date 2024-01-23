import matplotlib.pyplot as plt
from io import BytesIO
import base64


def generate_pie_chart(comp, balance):
    labels = ['Completed', 'Balance']
    sizes = [comp, balance]

    fig, ax = plt.subplots(figsize=(8, 8))  # Set a larger figure size
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=['#66b3ff', '#99ff99'])
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    # Save the figure to a BytesIO object
    image_stream = BytesIO()
    plt.savefig(image_stream, format='png')
    image_stream.seek(0)

    # Return the BytesIO object
    return image_stream


def generate_bar_graph(batch_names, batch_values):
    rounded_values = [round(value) for value in batch_values]

    # Extracting the relevant part of the batch names
    modified_batch_names = [name.split('_')[-1] for name in batch_names]

    fig, ax = plt.subplots(figsize=(10, 6))  # Set a larger figure size
    bars = ax.bar(modified_batch_names, batch_values, color='blue')
    ax.set_ylim(0, 100)  # Set y-axis limit to 100%
    ax.set_xlabel('Batch Names')
    ax.set_ylabel('Values (%)')
    ax.set_title('Actual Batch Values')

    # Add rounded text annotations on top of the bars
    for bar, value in zip(bars, rounded_values):
        ax.text(bar.get_x() + bar.get_width() / 2, value + 1, f'{value}%', ha='center', va='bottom')

    # Save the figure to a BytesIO object
    image_stream = BytesIO()
    plt.savefig(image_stream, format='png')
    image_stream.seek(0)

    # Return the BytesIO object
    return image_stream


def generate_vertical_bar_graph(short_names, overall_progress_values):
    rounded_values = [round(value) for value in overall_progress_values]

    fig, ax = plt.subplots(figsize=(10, 10))  # Set a larger figure size
    bars = ax.bar(short_names, overall_progress_values, color='green')
    ax.set_ylabel('Values (%)')
    ax.set_xlabel('Short Names')
    ax.set_title('Actual Overall Progress')

    # Rotate x-axis labels vertically
    plt.xticks(rotation='vertical')

    # Add rounded text annotations beside the bars
    for bar, value in zip(bars, rounded_values):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1, f'{value}%', ha='center', va='bottom')

    # Save the figure to a BytesIO object
    image_stream = BytesIO()
    plt.savefig(image_stream, format='png')
    image_stream.seek(0)

    # Return the BytesIO object
    return image_stream


def generate_line_plot(months_list, values_list):
    rounded_values = [round(value) for value in values_list]

    fig, ax = plt.subplots(figsize=(15, 6))  # Set a larger figure size
    ax.plot(months_list, rounded_values, marker='o', linestyle='-')
    ax.set_ylabel('progress (%)')
    ax.set_xlabel('Months')
    ax.set_title('NC Planned Progress Path')

    # Add rounded text annotations above the points
    for month, value in zip(months_list, rounded_values):
        ax.text(month, value + 1, f'{value}%', ha='center', va='bottom')

    ax.set_ylim(0, 100)  # Set y-axis limit to 100%
    plt.xticks(rotation='vertical')  # Rotate x-axis labels vertically

    # Save the figure to a BytesIO object
    image_stream = BytesIO()
    plt.savefig(image_stream, format='png')
    image_stream.seek(0)

    # Return the BytesIO object
    return image_stream
