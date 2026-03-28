import sys
import os
import subprocess
import pandas as pd

def run_analytics(input_csv="data_preprocessed.csv"):
    print("Generating insights from:", input_csv)

    if not os.path.exists(input_csv):
        print("File not found:", input_csv)
        return

    df = pd.read_csv(input_csv, low_memory=False)

    # insight 1 - basic dataset info
    with open("insight1.txt", "w") as f:
        f.write("INSIGHT 1: DATASET INVENTORY\n")
        f.write("-" * 30 + "\n")
        f.write("Total Crimes Logged: " + str(len(df)) + "\n")
        f.write("Number of Columns: " + str(len(df.columns)) + "\n")
        f.write("File Size Status: Optimized and Scaled\n")

    # insight 2 - most common crime types and locations
    with open("insight2.txt", "w") as f:
        f.write("INSIGHT 2: FREQUENCY ANALYSIS\n")
        f.write("-" * 30 + "\n")

        if 'Primary Type' in df.columns:
            top_crimes = df['Primary Type'].value_counts().head(5)
            f.write("Top 5 Crime Type Codes:\n")
            f.write(top_crimes.to_string() + "\n\n")

        if 'Location Description' in df.columns:
            top_locs = df['Location Description'].value_counts().head(5)
            f.write("Top 5 Location Codes:\n")
            f.write(top_locs.to_string() + "\n\n")

        f.write("Note: columns are label-encoded integers\n")

    # insight 3 - crime intensity bin distribution
    with open("insight3.txt", "w") as f:
        f.write("INSIGHT 3: CRIME INTENSITY DISTRIBUTION\n")
        f.write("-" * 30 + "\n")
        if 'level_bin' in df.columns:
            f.write("Low(0), Medium(1), High(2) counts:\n")
            f.write(df['level_bin'].value_counts().sort_index().to_string() + "\n")

    print("Insights saved to insight1.txt, insight2.txt, insight3.txt")

    subprocess.run(["python3", "visualize.py", input_csv])


if __name__ == "__main__":
    if len(sys.argv) > 1:
        run_analytics(sys.argv[1])
    else:
        run_analytics()