import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv')

# Clean data
df = df[((df['value'] <= df['value'].quantile(0.975)) & (df['value'] >= df['value'].quantile(0.025)))]
df['date'] = pd.to_datetime(df['date'])


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(18,6))

    # Plot the line
    ax.plot(df['date'], df['value'])

    # Select 7 evenly spaced tick positions
    xticks = df['date'].iloc[::len(df)//7]

    # Format those tick labels ("2016-05")
    xtick_labels = xticks.dt.strftime('%Y-%m')

    # Apply the ticks and labels
    ax.set_xticks(xticks)
    ax.set_xticklabels(xtick_labels, rotation=45)

    # Optional: Labels & grid
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")

    plt.show()

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.groupby([df['date'].dt.year, df['date'].dt.month])['value'].mean().unstack()

    # Draw bar plot
    # Group by year and month, then calculate the mean page views for each group
    df_bar = df.groupby([df['date'].dt.year, df['date'].dt.month])['value'].mean().unstack()


    # Plotting the bar plot
    fig, ax = plt.subplots(figsize=(10, 6))  # You can adjust the figure size
    df_bar.plot(kind='bar', ax=ax)

    # Set title and labels
    ax.set_xlabel('Years', fontsize=12)
    ax.set_ylabel('Average Page Views', fontsize=12)

    # Customize the x-axis ticks (make sure the years are clearly labeled)
    ax.set_xticklabels(df_bar.index, rotation=0, fontsize=12)

    # Set the legend labels to the full month names
    ax.legend(title='Months', labels=[
        'January', 'February', 'March', 'April', 'May', 'June', 
        'July', 'August', 'September', 'October', 'November', 'December'
    ], loc='upper left', fontsize=10)


    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    # Plot 1: Boxplot for each year with different colors
    plt.figure(figsize=(10, 6))
    sns.boxplot(x="year", y="value", data=df_box, order=[2016, 2017, 2018, 2019], palette='rainbow', hue="year", legend=False)
    plt.title('Year-wise Box Plot (Trend)', fontsize=16)
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('Page Views', fontsize=12)
    plt.xticks(rotation=45)
    plt.show()

    # Plot 2: Boxplot for each month (across all years) with different colors
    plt.figure(figsize=(10, 6))
    sns.boxplot(x="month", y="value", data=df_box, order=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], palette='rainbow', hue="month", legend=False)
    plt.title('PMonth-wise Box Plot (Seasonality)', fontsize=16)
    plt.xlabel('Month', fontsize=12)
    plt.ylabel('Page Views', fontsize=12)
    plt.xticks(rotation=45)


    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
