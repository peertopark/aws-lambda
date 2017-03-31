import boto3
import os


def lambda_handler(event, context):
    client = boto3.client('ecs')
    cluster = os.environ['cluster']
    response = client.list_tasks(
        cluster=cluster,
        family=os.environ['task']
    )

    tasks = response['taskArns']
    for task in tasks:
        client.stop_task(
            cluster=cluster,
            task=task
        )

    return "Stopped task: " + os.environ['task'] + " in cluster: " + os.environ['cluster']
