import boto3
import os

def lambda_handler(event, context):
    environment = os.environ['environment']
    client = boto3.client('elasticbeanstalk')

    client.terminate_environment(EnvironmentName=environment)

    return 'Beanstalk Environment: ' + environment + ' Stopped'
