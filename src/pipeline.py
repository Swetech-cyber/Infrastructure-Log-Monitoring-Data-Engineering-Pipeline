import logging
import subprocess


# Configure logging
logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


logger.info("Infrastructure Log Monitoring Pipeline Started.")
print("Infrastructure Log Monitoring Pipeline Started.")


# Step 1: Data Validation
logger.info("Step 1: Running data validation...")
print("\nStep 1: Running data validation...")

validation_result = subprocess.run(
    ["python", "src/validate_data.py"],
    capture_output=True,
    text=True
)

print(validation_result.stdout)

if validation_result.returncode != 0:
    logger.error("Data validation failed.")
    logger.error(validation_result.stderr)
    print("Pipeline stopped: Data validation failed.")
    exit(1)

logger.info("Step 1 completed successfully.")
print("Step 1 completed successfully.")


# Step 2: Data Transformation
logger.info("Step 2: Running data transformation...")
print("\nStep 2: Running data transformation...")

transformation_result = subprocess.run(
    ["python", "src/transform_data.py"],
    capture_output=True,
    text=True
)

print(transformation_result.stdout)

if transformation_result.returncode != 0:
    logger.error("Data transformation failed.")
    logger.error(transformation_result.stderr)
    print("Pipeline stopped: Data transformation failed.")
    exit(1)

logger.info("Step 2 completed successfully.")
print("Step 2 completed successfully.")


# Step 3: Load Processed Data
logger.info("Step 3: Loading processed data into PostgreSQL...")
print("\nStep 3: Loading processed data into PostgreSQL...")

load_result = subprocess.run(
    ["python", "src/load_processed.py"],
    capture_output=True,
    text=True
)

print(load_result.stdout)

if load_result.returncode != 0:
    logger.error("Database loading failed.")
    logger.error(load_result.stderr)
    print("Pipeline stopped: Database loading failed.")
    exit(1)

logger.info("Step 3 completed successfully.")
print("Step 3 completed successfully.")


logger.info("Infrastructure Log Monitoring Pipeline Completed Successfully.")
print("\nInfrastructure Log Monitoring Pipeline Completed Successfully.")