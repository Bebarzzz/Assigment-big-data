# CSCI461 - Big Data Assignment 1
## Chicago Crimes Data Pipeline

**Team Members:**
- Mostafa Bebars - 231000161
- Omar Khaled    - 231000
- Eyad Ahmed     - 231000644
- Mostafa Awad   - 231000


---

## Dataset

Chicago Crimes dataset with over 7.6 million crime records including
crime type, location, date, and arrest status.

Source: https://data.cityofchicago.org/

---

## Project Structure
```
customer-analytics/
├── Dockerfile
├── ingest.py
├── preprocessing.py
├── analytics.py
├── visualize.py
├── cluster.py
├── summary.sh
├── README.md
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

### 1. Build the image
```bash
docker build -t bigdata-pipeline .
```

### 2. Run the container
```bash
docker run -it --name bigdata-container -v "${PWD}:/app/pipeline/" bigdata-pipeline
```

### 3. Inside the container, start the pipeline
```bash
python3 ingest.py chicago.db
```

### 4. In a new terminal, copy results and clean up
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
loading data...
preprocessing done
analytics done
visualization done
clustering done
ALL DONE
```

**insight1.txt:**
```
INSIGHT 1: DATASET INVENTORY
------------------------------
Total Crimes Logged: 7655273
Number of Columns: 28
```

**clusters.txt:**
```
K-Means Clustering Results (k=3)
===================================
Cluster 0: XXXX samples
Cluster 1: XXXX samples
Cluster 2: XXXX samples
```

---

## Docker Hub
```bash
docker pull bebars37/bigdata-pipeline:v2
```
