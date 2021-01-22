from prefect import task, Flow
from prefect.environments.storage import GitHub
from prefect.run_configs import DockerRun
from prefect.engine.executors.dask import LocalDaskExecutor


@task
def extract():
    """Get a list of data"""
    return [i for i in range(1, 100)]


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
        repo="<my_github_org/repo_name>",
        path="src/flow.py",
        secrets=["<GITHUB_ACCESS_TOKEN>"],
    ),
    run_config=DockerRun(image="prefecthq/prefect:all_extras"),
    executor=LocalDaskExecutor(scheduler="threads", num_workers=3),
) as flow:
    e = extract()
    t = transform.map(e)
    l = load(t)