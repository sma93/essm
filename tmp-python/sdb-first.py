import boto3
import time

client = boto3.client('sdb')

#create domain, show response

#commented out because the domain already exists

#print("test - creating blog_posts domain")
#response = client.create_domain(
#    DomainName='blog_posts'
#)
print response

#wait 10 seconds, try to get domain metadata
time.sleep(10)
response = client.domain_metadata(
    DomainName='blog_posts'
)
for k, v in response.iteritems():
    print k, v

