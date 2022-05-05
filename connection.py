import boto3
from botocore.exceptions import ClientError

ec2 = boto3.resource('ec2')

class instance():
    def __init__(self, id, **options):
        super().__init__(**options)
        self.instance = ec2.Instance(id)

    def get_status(self):
        try:
            self.instance.reload()
            res = self.instance.state
        except ClientError:
            print("Couldn't reach instance %s", self.instance.instance-id)
        else:
            return res

    def describe_instance(self):
        try:
            res = self.instance.describe_attribute(Attribute='instanceType', DryRun=False)
        except:
            print("Couldn't describe instance %s", self.instance.instance-id)
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
            print("Instance started")
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