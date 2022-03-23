from urllib import response
import boto3

client = boto3.client('rds')


def get_db_arn():
    rds_paginator = client.get_paginator('describe_db_instances')
    response_iterator = rds_paginator.paginate()
    #database_arn = []
    for db in response_iterator:
        db_instances = db['DBInstances']
        
        '''Make this a func -- Finds all non tagged dbs -- then return the array of non-tagged'''
        for identifier in db_instances:
            database_arn = (identifier['DBInstanceArn'])
            database_tag = (identifier['TagList'])
            print(database_arn, database_tag)
            
get_db_arn()


'''
Then this func would go thrugh the array and tag 
def id_tagging(database_arn):
    for each in x:
        client.list_tags_for_resource()
        '''

