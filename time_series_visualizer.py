import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Importer les données
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=["date"], index_col="date")

# Nettoyer les données en supprimant les 2.5% les plus hauts et les plus bas
df = df[
    (df['value'] >= df['value'].quantile(0.025)) &
    (df['value'] <= df['value'].quantile(0.975))
]
def draw_line_plot():
    # Configurer la figure
    fig, ax = plt.subplots(figsize=(12, 6))

    # Tracer le graphique
    ax.plot(df.index, df['value'], color='red', linewidth=1)

    # Ajouter un titre et des étiquettes
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")

    # Sauvegarder et retourner la figure
    fig.savefig('line_plot.png')
    return fig

draw_line_plot()
def draw_bar_plot():
    # Préparer les données pour le graphique en barres
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month

    # Grouper les données par année et par mois
    df_bar = df_bar.groupby(['year', 'month'])['value'].mean().unstack()

    # Configurer la figure
    fig = df_bar.plot(kind='bar', figsize=(12, 8)).figure
    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    plt.title("Monthly Average Page Views per Year")
    plt.legend(title="Months", labels=[
        "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
    ])

    # Sauvegarder et retourner la figure
    fig.savefig('bar_plot.png')
    return fig

draw_bar_plot()
def draw_box_plot():
    # Préparer les données pour les box plots
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = df_box['date'].dt.year
    df_box['month'] = df_box['date'].dt.strftime('%b')

    # Trier les mois pour le box plot
    month_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    # Configurer la figure et les sous-plots
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))

    # Box plot par année
    sns.boxplot(x="year", y="value", data=df_box, ax=axes[0])
    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")

    # Box plot par mois
    sns.boxplot(x="month", y="value", data=df_box, order=month_order, ax=axes[1])
    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")

    # Sauvegarder et retourner la figure
    fig.savefig('box_plot.png')
    return fig

draw_box_plot()
