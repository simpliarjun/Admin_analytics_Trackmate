import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt

def plot_pie(series, title):
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.pie(series.values, labels=series.index, autopct="%1.1f%%", startangle=90)
    ax.set_title(title)
    plt.tight_layout()
    return fig

def plot_line(series, title, xlabel, ylabel):
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(series.index.astype(str), series.values, marker="o")
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    plt.xticks(rotation=45)
    plt.tight_layout()
    return fig

def plot_single_value(value, title, ylabel):
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.bar(["Value"], [value])
    ax.set_title(title)
    ax.set_ylabel(ylabel)
    plt.tight_layout()
    return fig

def plot_bar(series, title, xlabel, ylabel):
    fig, ax = plt.subplots(figsize=(10, 5))
    series.plot(kind="bar", ax=ax)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    return fig
