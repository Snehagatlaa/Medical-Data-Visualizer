import matplotlib
matplotlib.use('Agg')  # Non-interactive backend
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

# Import data
# Make sure medical_examination.csv is in the same directory as this file.
df = pd.read_csv('medical_examination.csv')

# 1) Add 'overweight' column
# BMI = weight(kg) / (height(m))^2. If BMI > 25 => overweight (1) else 0
height_m = df['height'] / 100
bmi = df['weight'] / (height_m ** 2)
df['overweight'] = (bmi > 25).astype(int)

# 2) Normalize data: make 0 always good and 1 always bad for 'cholesterol' and 'gluc'
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)


def draw_cat_plot():
    """Draw the categorical plot as described in the project instructions.

    Returns
    -------
    fig : matplotlib.figure.Figure
        The matplotlib Figure object containing the categorical plot.
    """
    # Create DataFrame for cat plot using pd.melt
    df_cat = pd.melt(df,
                     id_vars=['cardio'],
                     value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # We want counts of each feature split by cardio, variable and value
    # seaborn.catplot with kind='count' can take the melted df directly.

    # Draw the catplot
    catplot = sns.catplot(
        data=df_cat,
        kind='count',
        x='variable',
        hue='value',
        col='cardio'
    )

    fig = catplot.fig
    # Ensure tight layout
    fig.tight_layout()
    return fig


def draw_heat_map():
    """Clean the data and draw a heatmap of the correlation matrix.

    Returns
    -------
    fig : matplotlib.figure.Figure
        The matplotlib Figure object containing the heatmap.
    """
    # Clean the data
    df_heat = df.copy()

    # 1) Keep rows where ap_lo <= ap_hi
    df_heat = df_heat[df_heat['ap_lo'] <= df_heat['ap_hi']]

    # 2) Keep rows with height between 2.5th and 97.5th percentiles
    h_low = df_heat['height'].quantile(0.025)
    h_high = df_heat['height'].quantile(0.975)
    df_heat = df_heat[(df_heat['height'] >= h_low) & (df_heat['height'] <= h_high)]

    # 3) Keep rows with weight between 2.5th and 97.5th percentiles
    w_low = df_heat['weight'].quantile(0.025)
    w_high = df_heat['weight'].quantile(0.975)
    df_heat = df_heat[(df_heat['weight'] >= w_low) & (df_heat['weight'] <= w_high)]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 10))

    # Draw the heatmap with seaborn
    sns.heatmap(
        corr,
        mask=mask,
        annot=True,
        fmt='.1f',
        square=True,
        linewidths=0.5,
        cbar_kws={"shrink": 0.5},
        center=0,
        vmax=0.3,
        ax=ax
    )

    fig.tight_layout()
    return fig


# If run as a script, produce and save the figures (useful during development)
if __name__ == '__main__':
    fig1 = draw_cat_plot()
    fig1.savefig('catplot.png')

    fig2 = draw_heat_map()
    fig2.savefig('heatmap.png')

    plt.close('all')
