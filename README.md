# CSCI461 - Big Data Assignment 1
## Chicago Crimes Data Pipeline

**Team Members:**
- Mostafa Bebars
- Omar Khaled
- Eyad Ahmed
- Mostafa Awad

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
docker run -it --name bigdata-container -v "$(pwd)":/app/pipeline/ bigdata-pipeline
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

**ingest.py** — reads the `.db` SQLite file, loads the crimes table, saves it as `data_raw.csv`

**preprocessing.py** — removes duplicates, fills missing values, scales numeric columns, encodes text columns, applies PCA, and bins one column into intensity levels

**analytics.py** — writes 3 insight files covering dataset size, top crime types and locations, and intensity distribution

**visualize.py** — creates 3 plots and saves them as `summary_plot.png`

**cluster.py** — runs K-Means (k=3) on PCA columns and saves cluster sizes to `clusters.txt`

**summary.sh** — copies all output files from the container to the host, then removes the container

---

## Docker Hub
```bash
docker pull bebars37/bigdata-pipeline:v1
```