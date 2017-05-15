import boto3
import time
import random

client = boto3.client('sdb')

#TODO:
#add function to take new domain name as input and create it
#add fucntion to display current domain info
#add function to delete domain by name
#in test script, add a fucntion that calls the above in sequence

def sdb_comments():
	response = client.domain_metadata(
		DomainName='comments'
	)
	return response

def save_comments(comments):
	etime = str(time.time())
	s_comment = str(comments)
	comment_id = str(random.randint(1, 1000))

	response = client.put_attributes(
		DomainName='comments',
		ItemName=comment_id,
		Attributes=[
			{
				'Name': 'comment ID',
				'Value': comment_id,
				'Replace': True
			},
			{
				'Name': 'text',
				'Value': s_comment,
				'Replace': True
			},
			{
				'Name': 'submit-time',
				'Value': etime,
				'Replace': True
			}
		]
	)
	return response

def get_comments():
	resp = client.select(
		SelectExpression='select * from comments')
	return resp
