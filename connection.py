import json

import boto3



class Connector():
# Creates a connection to a dynamo DB via Boto3
    def __init__(self, db, conn_json):
        self.db = db
        self.json = conn_json

    def connect(self):
        with open(self.json) as fi:
            dicto = json.load(fi)
        session = boto3.Session(
           aws_access_key_id = dicto['aws_key'],
           aws_secret_access_key = dicto['aws_pw'],
        )


        dynamo_resource = session.resource(
            self.db,
            region_name='eu-west-1'
        )

        return dynamo_resource

