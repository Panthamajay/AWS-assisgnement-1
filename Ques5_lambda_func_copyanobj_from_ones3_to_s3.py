import boto3
import json
s3 = boto3.resource('s3')


def lambda_handler(event, context):
    bucket = s3.Bucket('source-j')
    dest_bucket = s3.Bucket('destination-j')
    print(bucket)
    print(dest_bucket)
    copy='sales.txt'    #enter the specific obj which you want to copy from source s3 to destination s3
    for obj in bucket.objects.all():
        dest_key = obj.key
        if dest_key == copy:
            print(dest_key)
            s3.Object(dest_bucket.name, dest_key).copy_from(CopySource = {'Bucket': obj.bucket_name, 'Key': obj.key})

