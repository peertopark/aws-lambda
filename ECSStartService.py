import boto3
import os


def lambda_handler(event, context):
    client = boto3.client('ecs')
    client.update_service(
        cluster=os.environ['cluster'],
        service=os.environ['service'],
        desiredCount=int(os.environ['tasks'])
    )
    return "Started service: " + os.environ['service'] + " in cluster: " + os.environ['cluster']