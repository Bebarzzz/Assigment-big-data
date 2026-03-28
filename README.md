# CSCI461 - Big Data Assignment 1
## Chicago Crimes Data Pipeline

**Team Members:**
- Mostafa Bebars - 231000161
- Omar Khaled    - 231000114
- Eyad Ahmed     - 231000644
- Moustafa Awaad - 231000677


---

## Dataset

Chicago Crimes dataset with over 7.6 million crime records including
crime type, location, date, and arrest status.

Source: https://www.kaggle.com/datasets/salikhussaini49/chicago-crimes

---

## Project Structure
```
.
├── README.md
├── .gitignore
└── customer-analytics/
    ├── Dockerfile
    ├── ingest.py
    ├── preprocessing.py
    ├── analytics.py
    ├── visualize.py
    ├── cluster.py
    ├── summary.sh
    └── results/
        ├── data_raw.csv
        ├── data_preprocessed.csv
        ├── insight1.txt
        ├── insight2.txt
        ├── insight3.txt
        ├── summary_plot.png
        └── clusters.txt
```

---

## Pipeline Flow
```
ingest.py → preprocessing.py → analytics.py → visualize.py → cluster.py
```

Each script calls the next one automatically when it finishes.

---

## How to Run

### 1. Navigate to the project folder
```bash
cd customer-analytics
```

### 2. Build the image
```bash
docker build -t bigdata-pipeline .
```

### 3. Run the container
```bash
docker run -it --name bigdata-container -v "${PWD}:/app/pipeline/" bigdata-pipeline
```

### 4. Inside the container, start the pipeline
```bash
python3 ingest.py chicago.db
```

### 5. In a new terminal, copy results and clean up
```bash
bash summary.sh
```

---

## What Each Script Does

**ingest.py** — connects to the SQLite `.db` file, detects the table automatically, loads all records and saves them as `data_raw.csv`

**preprocessing.py** — removes duplicates, fills missing values, scales numeric columns, encodes text columns into integers, applies PCA to reduce dimensions to 2 components, and bins one column into intensity levels

**analytics.py** — writes 3 insight files covering dataset size, top crime types and locations, and the intensity bin distribution

**visualize.py** — creates 3 plots (PCA distribution histogram, correlation heatmap, intensity bin bar chart) and saves them as `summary_plot.png`

**cluster.py** — runs K-Means clustering (k=3) on the two PCA columns and saves cluster sizes to `clusters.txt`

**summary.sh** — copies all output files from the container to the host machine, then stops and removes the container

---

## Sample Output

**Pipeline execution log:**
```
Loading dataset from: chicago.db
Tables found: ['Crimes']
Saved as data_raw.csv - 7655273 rows loaded
Starting preprocessing on: data_raw.csv
Preprocessing done, saved to data_preprocessed.csv
Generating insights from: data_preprocessed.csv
Insights saved to insight1.txt, insight2.txt, insight3.txt
Creating plots from: data_preprocessed.csv
Plot saved as summary_plot.png
Running clustering on: data_preprocessed.csv
Cluster sizes saved to clusters.txt
```

**insight1.txt:**
```
INSIGHT 1: DATASET INVENTORY
------------------------------
Total Crimes Logged: 7655273
Number of Columns: 26
```

**insight2.txt:**
```
INSIGHT 2: FREQUENCY ANALYSIS
------------------------------
Top 5 Crime Type Codes:
Primary Type
 1.3906    1614676
-1.0713    1402829
-0.7636     872709
 0.2366     744269
-1.1483     496882

Top 5 Location Codes:
Location Description
 0.7762    1988236
 0.3237    1289399
-1.9710     855088
 0.6954     723474
 0.0005     270044
```

**insight3.txt:**
```
INSIGHT 3: CRIME INTENSITY DISTRIBUTION
------------------------------
level_bin
0    2551758
1    2551757
2    2551758
```

**clusters.txt:**
```
K-Means Clustering Results (k=3)
===================================
Cluster 0: 3448333 samples
Cluster 1: 81324 samples
Cluster 2: 4125616 samples
```

---

## Docker Hub
```bash
docker pull bebars37/bigdata-pipeline:v2
```
