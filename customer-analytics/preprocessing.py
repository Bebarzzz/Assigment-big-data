import sys
import subprocess
import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.decomposition import PCA

def preprocess(input_path):
    print("Starting preprocessing on:", input_path)

    try:
        df = pd.read_csv(input_path)
    except UnicodeDecodeError:
        df = pd.read_csv(input_path, encoding='latin1')

    # --- Data Cleaning ---
    df.drop_duplicates(inplace=True)

    # fix: handle numeric and text columns separately
    for col in df.columns:
        if df[col].dtype == 'object':
            df[col] = df[col].fillna("Unknown")
        else:
            df[col] = df[col].fillna(df[col].median())

    # --- Feature Transformation ---
    # only scale columns that are actually numeric
    num_cols = df.select_dtypes(include=['float64', 'int64']).columns.tolist()

    scaler = StandardScaler()
    if len(num_cols) > 0:
        df[num_cols] = scaler.fit_transform(df[num_cols])

    # encode text columns into numbers
    le = LabelEncoder()
    cat_cols = df.select_dtypes(include=['object']).columns.tolist()
    for col in cat_cols:
        df[col] = le.fit_transform(df[col].astype(str))

    # --- Dimensionality Reduction ---
    if len(num_cols) >= 2:
        pca = PCA(n_components=2)
        result = pca.fit_transform(df[num_cols])
        df['pca_1'] = result[:, 0]
        df['pca_2'] = result[:, 1]

    # --- Discretization ---
    if len(num_cols) > 0:
        df['level_bin'] = pd.cut(df[num_cols[0]], bins=3, labels=[0, 1, 2])

    df = df.round(4)

    output_file = "data_preprocessed.csv"
    df.to_csv(output_file, index=False)
    print("Preprocessing done, saved to", output_file)

    subprocess.run(["python3", "analytics.py", output_file])


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] != "-f":
        preprocess(sys.argv[1])
    else:
        preprocess("data_raw.csv")