import boto3
import time
import random

client = boto3.client('sdb')

#create domain, show response

#commented out because the domain already exists

#print("test - creating blog_posts domain")
#response = client.create_domain(
#    DomainName='blog_posts'
#)
#print response

#wait 10 seconds, try to get domain metadata
def sdb_blog_posts():
	response = client.domain_metadata(
		DomainName='blog_posts'
	)
	return response
	#for k, v in response.iteritems():
  #  print k, v
def save_post(title, author, text):
	etime = str(time.time())
	post_id = str(random.randint(1, 1000))
	s_title = str(title)
	s_author = str(author)
	s_text = str(text)

	response = client.put_attributes(
		DomainName='blog_posts',
		ItemName=post_id,
		Attributes=[
			{
				'Name': 'title',
				'Value': s_title,
				'Replace': True
			},
			{
				'Name': 'author',
				'Value': s_author,
				'Replace': True
			},
			{
				'Name': 'text',
				'Value': s_text,
				'Replace': True
			},
			{
				'Name': 'last-modified',
				'Value': etime,
				'Replace': True
			}
		]
	)
	return response

def get_posts():
	resp = client.select(
		SelectExpression='select * from blog_posts')
	return resp
	#read docs for put attrib
	# send all attributes to simpleDB
