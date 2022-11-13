import boto3
import connection

con = connection.instance()

print(con.stop_instance())