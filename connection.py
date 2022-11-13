import boto3
from botocore.exceptions import ClientError

ec2 = boto3.resource('ec2')
client = boto3.client('ec2')

class instance():
    def __init__(self, **options):
        super().__init__(**options)

        #get the last instance id of all instances tagged mcServer
        filter = [{'Name':'tag:Name','Values':['mcServer']}]
        for i in client.describe_instances(Filters=filter).get('Reservations'):
            for j in i.get('Instances'):
                instanceId = j.get('InstanceId')
        self.instance = ec2.Instance(instanceId)

    def get_instance(self):
        return self.instance

    def get_status(self):
        try:
            self.instance.reload()
            res = self.instance.state
        except ClientError:
            print("Couldn't reach instance %s", self.instance.instance_id)
        else:
            return res

    def describe_instance(self):
        try:
            res = self.instance.public_ip_address
        except:
            print("Couldn't describe instance %s", self.instance.instance_id)
            raise
        else:
            return res

    def start_instance(self):
        """
        Starts an instance. The request returns immediately. To wait for the instance
        to start, use the Instance.wait_until_running() function.

        :param instance_id: The ID of the instance to start.
        :return: The response to the start request. This includes both the previous and
                current state of the instance.
        """
        try:
            response = self.instance.start()
            print("Starting instance %s.", self.instance.instance_id)
            self.instance.wait_until_running()
            self.instance.reload()
            print("Instance started with ip:%s", self.instance.public_ip_address)
        except ClientError:
            print("Couldn't start instance %s.", self.instance.instance_id)
            raise
        except Exception as e:
            print(e)
            raise
        else:
            return response

    def stop_instance(self):
        """
        Stops an instance. The request returns immediately. To wait for the instance
        to stop, use the Instance.wait_until_stopped() function.

        :param instance_id: The ID of the instance to stop.
        :return: The response to the stop request. This includes both the previous and
                current state of the instance.
        """
        try:
            response = self.instance.stop()
            print("Stopped instance %s.", self.instance.instance_id)
            self.instance.wait_until_stopped()
            print("Instance stopped")
        except ClientError:
            print("Couldn't stop instance %s.", self.instance.instance_id)
            raise
        except Exception as e:
            print(e)
            raise
        else:
            return response