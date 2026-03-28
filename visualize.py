import sys
import subprocess
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def visualize(input_csv):
    print("Creating plots from:", input_csv)

    df = pd.read_csv(input_csv, low_memory=False)

    fig, axes = plt.subplots(1, 3, figsize=(18, 5))

    # plot 1 - distribution of first PCA component
    axes[0].hist(df['pca_1'].dropna(), bins=50, color='steelblue', edgecolor='black')
    axes[0].set_title('PCA Component 1 Distribution')
    axes[0].set_xlabel('pca_1')
    axes[0].set_ylabel('Count')

    # plot 2 - correlation between numeric columns
    num_cols = df.select_dtypes(include='number').columns
    corr = df[num_cols].corr()
    sns.heatmap(corr, ax=axes[1], annot=False, cmap='coolwarm')
    axes[1].set_title('Correlation Heatmap')

    # plot 3 - crime counts per intensity bin
    bin_counts = df['level_bin'].value_counts().sort_index()
    axes[2].bar(bin_counts.index.astype(str), bin_counts.values, color='coral', edgecolor='black')
    axes[2].set_title('Crime Intensity Bins')
    axes[2].set_xlabel('Bin (0=Low, 1=Med, 2=High)')
    axes[2].set_ylabel('Count')

    plt.tight_layout()
    plt.savefig('summary_plot.png')
    print("Plot saved as summary_plot.png")

    subprocess.run(["python3", "cluster.py", input_csv])


if __name__ == "__main__":
    if len(sys.argv) > 1:
        visualize(sys.argv[1])
    else:
        visualize("data_preprocessed.csv")