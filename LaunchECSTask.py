import boto3
import os

def lambda_handler(event, context):
    client = boto3.client('ecs')
    client.run_task(
       cluster=os.environ['cluster'],
       taskDefinition=os.environ['task']
    )
    return "Launched task: " + os.environ['task'] + " in cluster: " + os.environ['cluster']
