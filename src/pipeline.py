import subprocess


print("Infrastructure Log Monitoring Pipeline Started.")


# Step 1: Data Validation
print("\nStep 1: Running data validation...")

validation_result = subprocess.run(
    ["python", "src/validate_data.py"],
    capture_output=True,
    text=True
)

print(validation_result.stdout)

if validation_result.returncode != 0:
    print("Pipeline stopped: Data validation failed.")
    exit(1)

print("Step 1 completed successfully.")


# Step 2: Data Transformation
print("\nStep 2: Running data transformation...")

transformation_result = subprocess.run(
    ["python", "src/transform_data.py"],
    capture_output=True,
    text=True
)

print(transformation_result.stdout)

if transformation_result.returncode != 0:
    print("Pipeline stopped: Data transformation failed.")
    exit(1)

print("Step 2 completed successfully.")


# Step 3: Load Processed Data
print("\nStep 3: Loading processed data into PostgreSQL...")

load_result = subprocess.run(
    ["python", "src/load_processed.py"],
    capture_output=True,
    text=True
)

print(load_result.stdout)

if load_result.returncode != 0:
    print("Pipeline stopped: Database loading failed.")
    exit(1)

print("Step 3 completed successfully.")


print("\nInfrastructure Log Monitoring Pipeline Completed Successfully.")