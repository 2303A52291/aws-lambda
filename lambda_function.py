import boto3
import os
import json

def lambda_handler(event, context):
    sns = boto3.client('sns')
    topic_arn = os.environ.get('ALERT_TOPIC_ARN')
    
    # Extract S3 info from event
    try:
        record = event['Records'][0]
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        message = f"New object created in bucket {bucket}: {key}"
    except Exception as e:
        message = f"Error parsing event: {str(e)}"
    
    # Publish to SNS
    if topic_arn:
        sns.publish(TopicArn=topic_arn, Message=message, Subject='S3 Alert')
    else:
        print('ALERT_TOPIC_ARN not set')
    
    return {
        'statusCode': 200,
        'body': json.dumps('Alert sent!')
    }
