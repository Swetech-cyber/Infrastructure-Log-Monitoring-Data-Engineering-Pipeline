# Infrastructure Log Monitoring & Data Engineering Pipeline

## Project Overview

This project demonstrates an end-to-end data engineering pipeline for processing and analyzing simulated infrastructure monitoring logs.

The pipeline uses Python, Pandas, PostgreSQL, SQL, Apache Airflow, and Docker to perform data ingestion, validation, transformation, database loading, data quality monitoring, and SQL-based analysis.

The project is designed to simulate a real-world infrastructure monitoring data workflow while demonstrating practical data engineering concepts such as ETL, workflow orchestration, containerization, database management, and data quality monitoring.

### Key Objectives

* Generate simulated infrastructure monitoring logs
* Validate incoming data for quality and consistency
* Transform raw log data into an analytics-ready format
* Load processed data into PostgreSQL
* Perform SQL-based infrastructure event analysis
* Identify high-severity events and monitoring trends
* Implement data quality monitoring
* Orchestrate the ETL workflow using Apache Airflow
* Run Airflow components in Docker containers
* Maintain a structured and reproducible data pipeline

---

## Architecture

```text
Simulated Infrastructure Logs
            |
            v
      Airflow DAG
            |
            v
       Ingest Data
            |
            v
      Validate Data
            |
            v
     Transform Data
            |
            v
  Load to PostgreSQL
            |
            v
    Data Quality Check
            |
            v
       SQL Analytics
            |
            v
 Monitoring & Incident
       Insights
```

The Airflow DAG orchestrates the pipeline using the following task dependency:

```text
ingest_data
      |
      v
validate_data
      |
      v
transform_data
      |
      v
load_to_postgresql
      |
      v
data_quality
```

Apache Airflow runs inside Docker containers, while the PostgreSQL database is hosted on the local Windows environment.

---

## Technology Stack

| Technology     | Purpose                                                                        |
| -------------- | ------------------------------------------------------------------------------ |
| Python         | Data generation, ingestion, validation, transformation, and pipeline execution |
| Pandas         | Data processing and transformation                                             |
| PostgreSQL     | Raw and processed data storage                                                 |
| SQLAlchemy     | Python-to-PostgreSQL database connectivity                                     |
| Psycopg2       | PostgreSQL database driver                                                     |
| SQL            | Infrastructure log analysis and reporting                                      |
| Apache Airflow | Workflow orchestration and task scheduling                                     |
| Docker         | Containerized Airflow environment                                              |
| Docker Compose | Management of Airflow services                                                 |
| PowerShell     | Environment setup and pipeline execution                                       |
| Git            | Version control                                                                |
| GitHub         | Source code and project portfolio                                              |
| VS Code        | Development environment                                                        |

---

## Project Structure

```text
Infrastructure Log Monitoring Project/
│
├── airflow/
│   ├── dags/
│   │   └── infrastructure_log_pipeline.py
│   ├── logs/
│   ├── plugins/
│   ├── config/
│   ├── .env
│   └── docker-compose.yaml
│
├── data/
│   ├── raw/
│   │   └── infrastructure_logs.csv
│   └── processed/
│       └── infrastructure_logs_processed.csv
│
├── src/
│   ├── generate_logs.py
│   ├── ingest.py
│   ├── validate_data.py
│   ├── transform_data.py
│   ├── load_processed.py
│   ├── data_quality.py
│   └── pipeline.py
│
├── sql/
│   ├── analysis_queries.sql
│   └── create_indexes.sql
│
├── logs/
│   └── pipeline.log
│
├── .gitignore
├── requirements.txt
├── .env
└── README.md
```

---

## Pipeline Workflow

The project follows a structured ETL workflow orchestrated through Apache Airflow.

### 1. Generate Infrastructure Logs

`generate_logs.py` generates simulated infrastructure monitoring events and saves them as a raw CSV file.

**Output:**

```text
data/raw/infrastructure_logs.csv
```

The generated dataset contains 1,000 infrastructure monitoring events.

---

### 2. Ingest Raw Data

`ingest.py` reads the raw CSV file using Pandas and loads the records into the PostgreSQL `infrastructure_logs` table.

The ingestion process clears previous raw records before loading the latest dataset, making the pipeline rerunnable.

---

### 3. Validate Data

`validate_data.py` performs data quality checks including:

* Missing value validation
* Duplicate event ID detection
* Severity value validation
* Device type validation
* Event type validation

The pipeline stops if validation fails.

---

### 4. Transform Data

`transform_data.py` converts the raw data into an analytics-ready format by creating:

* `event_date`
* `event_hour`
* `is_high_severity`

The transformed dataset is saved to:

```text
data/processed/infrastructure_logs_processed.csv
```

---

### 5. Load Processed Data

`load_processed.py` loads the transformed dataset into the PostgreSQL:

```text
infrastructure_logs_processed
```

table.

The processed table contains 1,000 records after successful pipeline execution.

---

### 6. Data Quality Monitoring

`data_quality.py` performs post-processing quality checks including:

* Total record count
* Missing value count
* Duplicate event ID detection
* High-severity event count
* Severity distribution

The latest pipeline execution reported:

```text
Total records: 1000
Missing values: 0
Duplicate event IDs: 0
High-severity events: 149
Data Quality Status: PASSED
```

---

### 7. SQL Analytics

`analysis_queries.sql` contains analytical queries to identify:

* High-severity events by host
* High-severity events by event type
* Monthly high-severity event trends
* Overall severity distribution
* Hosts with the highest number of events

---

## Apache Airflow Orchestration

Apache Airflow is used to orchestrate the complete data pipeline.

The DAG is defined in:

```text
airflow/dags/infrastructure_log_pipeline.py
```

### DAG

```text
infrastructure_log_monitoring_pipeline
```

### Task Dependency

```text
ingest_data
      ↓
validate_data
      ↓
transform_data
      ↓
load_to_postgresql
      ↓
data_quality
```

Each task executes only after the previous task completes successfully.

The DAG is configured with retry handling so failed tasks can be retried automatically.

### Airflow and PostgreSQL Connectivity

Airflow runs inside Docker containers, while PostgreSQL runs on the Windows host machine.

The Airflow worker connects to PostgreSQL using:

```text
host.docker.internal
```

This allows the Dockerized Airflow environment to communicate with the PostgreSQL server running on the host machine.

### Verified Airflow Execution

The complete DAG was successfully executed through Airflow.

The final DAG state was:

```text
success
```

PostgreSQL verification after the Airflow run:

```text
processed_records
-----------------
1000
```

This confirms that the complete orchestrated workflow successfully processed and loaded the dataset.

---

## Docker Environment

Docker Desktop is used to run the Apache Airflow environment.

The project uses Docker Compose to manage the Airflow services.

The Airflow environment includes services such as:

* Airflow API server
* Airflow scheduler
* Airflow worker
* Airflow DAG processor
* Airflow triggerer
* Redis
* PostgreSQL service used internally by Airflow

The project PostgreSQL database remains on the Windows host environment and is accessed by Airflow through `host.docker.internal`.

---

## Data Quality & Transformation

### Data Validation

The pipeline validates incoming infrastructure log data before processing.

The following checks are performed:

* No missing values
* No duplicate `event_id` values
* Valid severity values:
  `INFO`, `WARNING`, `ERROR`, `CRITICAL`
* Valid device types
* Valid event types

The pipeline proceeds to transformation only when validation is successful.

### Data Transformation

The transformation stage creates additional fields required for analysis:

| Field              | Description                                            |
| ------------------ | ------------------------------------------------------ |
| `event_date`       | Date extracted from the event timestamp                |
| `event_hour`       | Hour extracted from the event timestamp                |
| `is_high_severity` | Boolean flag identifying `ERROR` and `CRITICAL` events |

These transformations make the data easier to analyze using SQL and reporting tools.

---

## Database Design

The project uses PostgreSQL to store both raw and processed infrastructure log data.

### Raw Table

**Table:** `infrastructure_logs`

This table stores the original log records received from the ingestion stage.

Key columns include:

* `event_id`
* `event_timestamp`
* `host_name`
* `device_type`
* `event_type`
* `severity`
* `source_ip`
* `message`

### Processed Table

**Table:** `infrastructure_logs_processed`

This table stores the transformed, analytics-ready records.

In addition to the original log fields, it contains:

* `event_date`
* `event_hour`
* `is_high_severity`

### Database Indexes

Indexes were created on frequently queried columns to support infrastructure log analysis as data volume grows.

Indexed columns include:

* `event_timestamp`
* `is_high_severity`
* `host_name`
* `event_type`

---

## SQL Analytics & Results

The project includes SQL queries for monitoring infrastructure events and identifying high-severity activity.

### Key Results

* **Total infrastructure events:** 1,000
* **High-severity events:** 149
* **INFO events:** 599
* **WARNING events:** 252
* **ERROR events:** 119
* **CRITICAL events:** 30

### High-Severity Events by Host

| Host          | High-Severity Events |
| ------------- | -------------------: |
| DB-SERVER-02  |                   22 |
| WEB-SERVER-02 |                   22 |
| APP-SERVER-02 |                   19 |
| APP-SERVER-01 |                   18 |
| WEB-SERVER-01 |                   18 |
| SWITCH-01     |                   18 |
| ROUTER-01     |                   17 |
| DB-SERVER-01  |                   15 |

### High-Severity Events by Event Type

| Event Type        | High-Severity Events |
| ----------------- | -------------------: |
| CPU Monitoring    |                   30 |
| Memory Monitoring |                   26 |
| Network           |                   25 |
| Authentication    |                   24 |
| System            |                   23 |
| Application       |                   21 |

These queries demonstrate the use of SQL aggregation, filtering, grouping, sorting, and date-based analysis for infrastructure monitoring.

---

## How to Run the Project

### Prerequisites

Make sure the following are installed:

* Python 3.12+
* PostgreSQL 18+
* Docker Desktop
* Git
* Visual Studio Code

### 1. Clone the Repository

```bash
git clone <repository-url>
cd "Infrastructure Log Monitoring Project"
```

### 2. Create and Activate Virtual Environment

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```powershell
pip install -r requirements.txt
```

### 4. Configure Database Connection

Create a `.env` file in the project root:

```text
DB_USER=postgres
DB_PASSWORD=<your-password>
DB_HOST=localhost
DB_PORT=5432
DB_NAME=infrastructure_log_monitoring
```

### 5. Generate Sample Infrastructure Logs

```powershell
python src\generate_logs.py
```

### 6. Run the Local Python Pipeline

```powershell
python src\pipeline.py
```

The local Python pipeline performs:

```text
Validation
    ↓
Transformation
    ↓
PostgreSQL Loading
    ↓
Data Quality Monitoring
```

### 7. Start Airflow Using Docker

From the project root:

```powershell
docker compose -f .\airflow\docker-compose.yaml up -d
```

### 8. Trigger the Airflow Pipeline

```powershell
docker compose -f .\airflow\docker-compose.yaml exec airflow-worker airflow dags trigger infrastructure_log_monitoring_pipeline
```

The Airflow DAG executes:

```text
Ingestion
    ↓
Validation
    ↓
Transformation
    ↓
PostgreSQL Loading
    ↓
Data Quality Monitoring
```

### 9. Verify PostgreSQL Records

```powershell
& "C:\Program Files\PostgreSQL\18\bin\psql.exe" -U postgres -d infrastructure_log_monitoring -c "SELECT COUNT(*) AS processed_records FROM infrastructure_logs_processed;"
```

Expected result:

```text
processed_records
-----------------
1000
```

### 10. Run SQL Analytics

```powershell
& "C:\Program Files\PostgreSQL\18\bin\psql.exe" -U postgres -d infrastructure_log_monitoring -f ".\sql\analysis_queries.sql"
```

---

## Project Features

* Simulated infrastructure log generation using Python
* Automated data ingestion using Pandas and SQLAlchemy
* Data quality validation before processing
* Duplicate and missing-value detection
* Severity and event-type validation
* Data transformation for analytics
* PostgreSQL-based raw and processed data storage
* Automated ETL pipeline execution
* SQL-based infrastructure monitoring analytics
* High-severity event identification
* Host-level and event-type analysis
* Monthly high-severity trend analysis
* Post-processing data quality monitoring
* Database indexing for frequently queried columns
* Apache Airflow workflow orchestration
* Docker-based Airflow environment
* Airflow task retries and dependency management
* Environment-based database configuration using `.env`
* Dependency management using `requirements.txt`
* Git-ready project structure for version control

---

## Future Enhancements

The current project provides a complete local ETL workflow with Airflow orchestration and Docker-based execution.

Potential future enhancements include:

* Implement incremental data loading
* Build a Power BI infrastructure monitoring dashboard
* Add alerting for critical infrastructure events
* Store processed data in cloud storage
* Extend the pipeline to Azure Data Engineering services
* Add centralized monitoring and alerting
* Implement production-scale data ingestion
* Introduce cloud-based Airflow orchestration

---

## Data Source & Disclaimer

The infrastructure log data used in this project is **synthetically generated using Python** for learning and portfolio purposes.

The dataset does not contain:

* IBM production data
* Client information
* Customer data
* Confidential infrastructure details
* Real production logs

The project is designed to demonstrate data engineering concepts such as ETL, data validation, transformation, PostgreSQL data loading, SQL analytics, workflow orchestration, Docker, and data quality monitoring using a simulated infrastructure monitoring scenario.
