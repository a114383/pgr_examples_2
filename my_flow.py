import os

import prefect
from prefect import task, Flow
from prefect.storage import GitHub
from prefect.run_configs import DockerRun
from prefect.executors import LocalDaskExecutor


@task
def extract():
    """Get a list of data"""
    logger = prefect.context.get("logger")
    logger.info("We're in Dev")
    return [i for i in range(1, 10)]


@task
def transform(datum):
    """Multiply the input by 10"""
    return datum * 10


@task
def load(data):
    """Print the data to indicate it was received"""
    print("Here's your data: {}".format(data))


# Some configuration is required, see https://docs.prefect.io/orchestration/flow_config/overview.html
with Flow(
    "ETL",
    storage=GitHub(
        repo="dylanbhughes/pgr_examples_2",
        path="my_flow.py",
        secrets=["GITHUB_ACCESS_TOKEN"],
        ref=os.environ["PREFECT_FLOW_BRANCH_NAME"],
    ),
    run_config=DockerRun(
        image="prefecthq/prefect:latest",
        labels=[os.environ["PREFECT_FLOW_LABEL"]],
        env={
            "PREFECT_FLOW_BRANCH_NAME": os.environ["PREFECT_FLOW_BRANCH_NAME"],
            "PREFECT_FLOW_LABEL": os.environ["PREFECT_FLOW_LABEL"],
            "PREFECT_PROJECT_NAME": os.environ["PREFECT_PROJECT_NAME"],
        },
    ),
    executor=LocalDaskExecutor(scheduler="threads", num_workers=3),
) as flow:
    e = extract()
    t = transform.map(e)
    l = load(t)

if __name__ == "__main__":
    flow.register(os.environ["PREFECT_PROJECT_NAME"])
