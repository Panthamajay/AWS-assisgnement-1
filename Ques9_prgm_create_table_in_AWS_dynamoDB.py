import boto3

# Get the service resource.
dynamodb = boto3.resource('dynamodb')

# Creating the DynamoDB table.

table = dynamodb.create_table(    #table is the response for the create_table
    TableName='Games',            #tablename must be unique in a region..i have used table name as Hello.
    KeySchema=[
        {
            'AttributeName': 'gname',     #hash attribute (a partition key)
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'gid',       #range attribute (a sort key)
            'KeyType': 'RANGE'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'gname',
            'AttributeType': 'S'          # S refers string type
        },
        {
            'AttributeName': 'gid',
            'AttributeType': 'N'          # N refers number type
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

table.meta.client.get_waiter('table_exists').wait(TableName='Games')       # Wait until the table exists.
.
print(table.item_count)          # Printing the no. of items in the table

                                 #if result=0 then it meant creation of table is success and there is no content

print('Table has been created, continuing to insert data.')


table.put_item(
   Item={
           'gname': 'cricket',
         'gid': 1,
        'publisher': 'Ajay',
        'rating': '10',
        'release_date': '21-06-2001',
        'genres': ['interesting' , 'focus']

    }                                                            #items are loaded into table 'Games'
)


table.put_item(
   Item={
           'gname': 'carrom',
           'gid': 2,
        'publisher': 'kumar',
        'rating': '8',
        'release_date': '30-08-2005',
        'genres': ['focus' , 'practise']

    }                                                           #items are loaded into table 'Games'
)

table.put_item(
   Item={
           'gname': 'chess',
           'gid': 3,
        'publisher': 'naresh',
        'rating': '9',
        'release_date': '5-04-2003',
        'genres': ['focus' , 'strategy']

    }                                                             #items are loaded into table 'Games'
)




