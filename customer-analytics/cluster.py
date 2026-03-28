import sys
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

def cluster(input_csv):
    print("Running clustering on:", input_csv)

    df = pd.read_csv(input_csv, low_memory=False)

    # use PCA columns since they already summarize the data well
    features = df[['pca_1', 'pca_2']].dropna()

    scaler = StandardScaler()
    X = scaler.fit_transform(features)

    # 3 clusters to match the 3 intensity levels
    kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
    labels = kmeans.fit_predict(X)

    counts = pd.Series(labels).value_counts().sort_index()

    with open("clusters.txt", "w") as f:
        f.write("K-Means Clustering Results (k=3)\n")
        f.write("=" * 35 + "\n")
        for cluster_id, count in counts.items():
            f.write("Cluster " + str(cluster_id) + ": " + str(count) + " samples\n")

    print("Cluster sizes saved to clusters.txt")
    print(counts)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        cluster(sys.argv[1])
    else:
        cluster("data_preprocessed.csv")