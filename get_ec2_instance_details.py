import boto3
import pprint

ec2 = boto3.client('ec2')
responses = ec2.describe_instances()['Reservations']

for response in responses:
    data = response['Instances']
    for get_data in data:
        instance_id = get_data['InstanceId']
        instance_Type = get_data['InstanceType']
        publicDns_Name = get_data['PublicDnsName']
        publicIp_Address = get_data['PublicIpAddress']
        get_private_ip = get_data['NetworkInterfaces'][0]
        pr_ip = get_private_ip['PrivateIpAddress']

        print("------------------------")
        print("Instance id - ", instance_id)
        print("Instance Type - ", instance_Type)
        print("Instance public IP - ", publicIp_Address)
        print("Instance private IP - ", pr_ip)
        print("Instance Public DnsName ", publicDns_Name)
        print("------------------------")
