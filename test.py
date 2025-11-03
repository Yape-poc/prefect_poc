pip install "prefect[databricks]"

from prefect_databricks import DatabricksCredentials
databricks_credentials_block = DatabricksCredentials.load("test")


@flow
def example_execute_endpoint_flow():
    databricks_credentials = DatabricksCredentials.load("test")
    jobs = jobs_list(
        databricks_credentials,
        limit=5
    )
    return jobs

if __name__ == "__main__":
    example_execute_endpoint_flow()
