import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('cloud-resume-stats')

def lambda_handler(event, context):
    # Retrieve current count and increment by 1
    response = table.update_item(
        Key={'id': 'visitors'},
        UpdateExpression='SET #v = #v + :val',
        ExpressionAttributeNames={'#v': 'views'},
        ExpressionAttributeValues={':val': 1},
        ReturnValues='UPDATED_NEW'
    )
    
    views = int(response['Attributes']['views'])
    
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Allow-Methods': '*'
        },
        'body': json.dumps({'views': views})
    }