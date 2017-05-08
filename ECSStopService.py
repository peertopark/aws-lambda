import boto3
import os


def lambda_handler(event, context):
    client = boto3.client('ecs')
    client.update_service(
        cluster=os.environ['cluster'],
        service=os.environ['service'],
        desiredCount=0
    )
    return "Stopped service: " + os.environ['service'] + " in cluster: " + os.environ['cluster']