import boto3

region = 'us-east-2'
server_tag = 'JEC2nkins'
def get_ec2_instance(region=region, server_tag=server_tag):
    '''this function will return the instance ID of the jenkins server,
    indicated by having the correct tag'''
    ec2 = boto3.resource('ec2', region_name=region)
    for instance in ec2.instances.all():
        if instance.tags:
            for tag in instance.tags:
                if tag['Key'] == 'name' and tag['Value'] == server_tag :
                    return instance.id


def restart_jenkins_server(server):
    '''this function will restart the jenkins server, receives the 
    instance ID from the get_ec2_instance function'''
    ec2 = boto3.resource('ec2', region_name=region)
    instance = ec2.Instance(server)
    instance.start()
    instance.wait_until_running()
    print(instance.public_dns_name)

jenkins_server = get_ec2_instance()
print(jenkins_server)
restart_jenkins_server(jenkins_server)
print('Jenkins server is running')