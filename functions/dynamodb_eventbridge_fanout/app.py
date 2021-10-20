import boto3
import json
import os

client = boto3.client('events')


EVENT_SOURCE = os.environ.get('AWS_LAMBDA_FUNCTION_NAME')
EVENT_DETAIL_TYPE = 'dynamodb-stream-event'


def build_event(dynamodb_event):
    return {
        'Source': EVENT_SOURCE,
        'Resources': [dynamodb_event['eventSourceARN']],
        'DetailType': EVENT_DETAIL_TYPE,
        'Detail': json.dumps(dynamodb_event)
    }


def lambda_handler(event, context):
    client.put_events(
        Entries=list(map(build_event, event['Records']))
    )
