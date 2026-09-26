# Infrastructure Log Monitoring & Data Engineering Pipeline

## Project Overview

This project demonstrates an end-to-end data engineering pipeline for processing and analyzing simulated infrastructure monitoring logs.

The pipeline uses Python and PostgreSQL to perform data validation, transformation, database loading, and SQL-based analysis. The project is designed to simulate a real-world infrastructure monitoring data workflow while demonstrating practical data engineering concepts.

### Key Objectives

* Generate simulated infrastructure monitoring logs
* Validate incoming data for quality and consistency
* Transform raw log data into an analytics-ready format
* Load processed data into PostgreSQL
* Perform SQL-based infrastructure event analysis
* Identify high-severity events and monitoring trends
* Maintain a structured, reproducible data pipeline

## Architecture

```text
Simulated Infrastructure Logs
            |
            v
     Python Data Ingestion
            |
            v
      Data Validation
            |
            v
     Data Transformation
            |
            v
         PostgreSQL
            |
            v
      SQL Analytics
            |
            v
   Monitoring & Incident
         Insights
```

## Technology Stack

| Technology | Purpose                                                                 |
| ---------- | ----------------------------------------------------------------------- |
| Python     | Data generation, validation, transformation, and pipeline orchestration |
| Pandas     | Data processing and transformation                                      |
| PostgreSQL | Data storage and analytical queries                                     |
| SQLAlchemy | Python-to-PostgreSQL database connectivity                              |
| Psycopg2   | PostgreSQL database driver                                              |
| SQL        | Infrastructure log analysis and reporting                               |
| PowerShell | Environment setup and pipeline execution                                |
| Git        | Version control                                                         |
| GitHub     | Source code and project portfolio                                       |
| VS Code    | Development environment                                                 |

## Project Structure

```text
Infrastructure Log Monitoring Project/
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
│   └── pipeline.py
│
├── sql/
│   └── analysis_queries.sql
│
├── logs/
│
├── .gitignore
├── requirements.txt
├── .env
└── README.md
```

## Pipeline Workflow

The pipeline follows a structured ETL workflow:

### 1. Generate Infrastructure Logs

`generate_logs.py` generates simulated infrastructure monitoring events and saves them as a raw CSV file.

**Output:**

`data/raw/infrastructure_logs.csv`

### 2. Ingest Raw Data

`ingest.py` reads the raw CSV file using Pandas and loads the records into the PostgreSQL `infrastructure_logs` table.

### 3. Validate Data

`validate_data.py` performs data quality checks including:

* Missing value validation
* Duplicate event ID detection
* Severity value validation
* Device type validation
* Event type validation

### 4. Transform Data

`transform_data.py` converts the raw data into an analytics-ready format by creating:

* `event_date`
* `event_hour`
* `is_high_severity`

The transformed dataset is saved to:

`data/processed/infrastructure_logs_processed.csv`

### 5. Load Processed Data

`load_processed.py` loads the transformed dataset into the PostgreSQL `infrastructure_logs_processed` table.

### 6. SQL Analytics

`analysis_queries.sql` contains analytical queries to identify:

* High-severity events by host
* High-severity events by event type
* Monthly high-severity event trends
* Overall severity distribution
* Hosts with the highest number of events

### 7. Pipeline Orchestration

`pipeline.py` orchestrates the validation, transformation, and database loading steps and stops execution if a pipeline stage fails.

## Data Quality & Transformation

### Data Validation

The pipeline validates incoming infrastructure log data before processing.

The following checks are performed:

* No missing values
* No duplicate `event_id` values
* Valid severity values: `INFO`, `WARNING`, `ERROR`, `CRITICAL`
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

### Data Flow

```text
Raw CSV
   |
   v
infrastructure_logs
   |
   v
Data Validation
   |
   v
Data Transformation
   |
   v
infrastructure_logs_processed
   |
   v
SQL Analytics
```

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

## How to Run the Project

### Prerequisites

Make sure the following are installed:

* Python 3.12+
* PostgreSQL 18+
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

Create a `.env` file in the project root with the PostgreSQL connection details:

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

### 6. Run Data Ingestion

```powershell
python src\ingest.py
```

### 7. Run the Complete Processing Pipeline

```powershell
python src\pipeline.py
```

The pipeline performs:

```text
Validation
    |
    v
Transformation
    |
    v
PostgreSQL Loading
```

### 8. Run SQL Analytics

```powershell
& "C:\Program Files\PostgreSQL\18\bin\psql.exe" -U postgres -d infrastructure_log_monitoring -f ".\sql\analysis_queries.sql"
```

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
* Environment-based database configuration using `.env`
* Dependency management using `requirements.txt`
* Git-ready project structure for version control

## Future Enhancements

The current project provides a complete local ETL workflow. The following enhancements can be added to make the solution more production-oriented:

* Schedule pipeline execution using Apache Airflow
* Add centralized application and pipeline logging
* Implement incremental data loading
* Add database indexes for frequently queried columns
* Add automated data quality monitoring
* Containerize the application using Docker
* Build a Power BI monitoring dashboard
* Add alerting for critical infrastructure events
* Store processed data in cloud storage
* Extend the pipeline to Azure Data Engineering services

## Data Source & Disclaimer

The infrastructure log data used in this project is **synthetically generated using Python** for learning and portfolio purposes.

The dataset does not contain:

* IBM production data
* Client information
* Customer data
* Confidential infrastructure details
* Real production logs

The project is designed to demonstrate data engineering concepts such as ETL, data validation, transformation, PostgreSQL data loading, and SQL analytics using a simulated infrastructure monitoring scenario.
