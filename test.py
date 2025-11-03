import sys
import subprocess

# Install prefect with databricks if not already installed
subprocess.check_call([sys.executable, "-m", "pip", "install", "-U","prefect[databricks]"])

from prefect import flow
from prefect_databricks import DatabricksCredentials, jobs_list

@flow
def example_execute_endpoint_flow():
    databricks_credentials = DatabricksCredentials.load("test")
    jobs = jobs_list(
        databricks_credentials=databricks_credentials,
        limit=5
    )
    return jobs

if __name__ == "__main__":
    result = example_execute_endpoint_flow()
    print(result)
