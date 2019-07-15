import boto3
import boto3.dynamodb.conditions                # Library for including the key conditions

# Get the service resource.
dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('Games')                 #Reading the Games DynamoDB table
response = table.query(
	KeyConditionExpression=Key('gid').eq(2)     #Returns only the game where ‘gid=2
)
items = response['Items']
print(items['gname'], ":", items['rating'])      #Printing the ‘gname’ and ‘rating’ only.
