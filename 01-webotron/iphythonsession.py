# coding: utf-8
import boto3
get_ipython().run_line_magic('cat', '~/.aws/config')
session = boto3.Session(profile_name='pythonAutomation')
s3 = session.resource('s3')
for bucket in s3.buckets.all():
    print(bucket)
    
new_bucket = s3.create_bucket(Bucket='automatingawsshibani-boto3', CreateBucketConfiguration={'LocationConstraint':'us-east-1'})
new_bucket = s3.create_bucket(Bucket='automatingawsshibani-boto3', CreateBucketConfiguration={'LocationConstraint':'us-east-1'})
new_bucket = s3.create_bucket(Bucket='automatingawsshibani-boto3')
for bucket in s3.buckets.all():
    print(bucket)
    
ec2_client = session.client('ec2')
ec2_client.allocate_
get_ipython().run_line_magic('history', '')
