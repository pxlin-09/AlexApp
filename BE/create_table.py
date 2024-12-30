# create_table.py

import boto3
from botocore.exceptions import ClientError
from schema import TABLE_SCHEMAS

# Configuration for LocalStack
DYNAMODB_ENDPOINT = "http://localhost:4566"

# Define the DynamoDB client
dynamodb = boto3.resource(
    'dynamodb',
    endpoint_url=DYNAMODB_ENDPOINT,
    region_name='us-east-1',  # Use any region name for LocalStack
    aws_access_key_id="fakeAccessKey",  # Dummy credentials for LocalStack
    aws_secret_access_key="fakeSecretKey"
)

def create_table(table_name, schema):
    """Creates a table in DynamoDB using the provided schema."""
    try:
        print(f"Creating table {table_name}...")
        table = dynamodb.create_table(
            TableName=table_name,
            KeySchema=schema["key_schema"],
            AttributeDefinitions=schema["attribute_definitions"],
            ProvisionedThroughput=schema["provisioned_throughput"]
        )
        table.meta.client.get_waiter('table_exists').wait(TableName=table_name)
        print(f"Table {table_name} created successfully!")
    except ClientError as e:
        if e.response['Error']['Code'] == 'ResourceInUseException':
            print(f"Table {table_name} already exists.")
        else:
            print(f"Error creating table {table_name}: {e.response['Error']['Message']}")
    except Exception as ex:
        print(f"Unexpected error: {ex}")

def main():
    """Main function to create all tables."""
    for table_name, schema in TABLE_SCHEMAS.items():
        create_table(table_name, schema)

if __name__ == "__main__":
    main()
