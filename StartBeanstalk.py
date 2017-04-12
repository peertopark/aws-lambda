import boto3
import os
import re

def lambda_handler(event, context):

    applicationName = os.environ['application']
    environmentName = os.environ['environment']
    templateName = os.environ['template']
    appRegex = os.environ['appregex']

    client = boto3.client('elasticbeanstalk')

    response = client.describe_application_versions(ApplicationName=applicationName)
    applications = response.get('ApplicationVersions')
    selectedApplications = []

    for application in applications:
        appVersion = application[u'VersionLabel']
        if re.match(appRegex, appVersion):
            selectedApplications.append(application)

    selectedApplications.sort(key=lambda r: r['DateCreated'], reverse=True)

    selectedApplicationVersion = selectedApplications[0]['VersionLabel']

    client.create_environment(
        ApplicationName=applicationName,
        EnvironmentName=environmentName,
        CNAMEPrefix=environmentName,
        VersionLabel=selectedApplicationVersion,
        TemplateName=templateName)

    return 'Beanstalk Environment: ' + environmentName + ' Started'