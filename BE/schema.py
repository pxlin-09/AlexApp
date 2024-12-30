# schema.py

# Table schemas
TABLE_SCHEMAS = {
    "Users": {
        "key_schema": [
            {"AttributeName": "UserId", "KeyType": "HASH"}  # Partition key: unique user ID
        ],
        "attribute_definitions": [
            {"AttributeName": "UserId", "AttributeType": "S"}
        ],
        "provisioned_throughput": {
            "ReadCapacityUnits": 5,
            "WriteCapacityUnits": 5
        },
    },
    "Connections": {
        "key_schema": [
            {"AttributeName": "UserId", "KeyType": "HASH"},  # Partition key: user initiating connection
            {"AttributeName": "ConnectionId", "KeyType": "RANGE"}  # Sort key: ID of the connected user
        ],
        "attribute_definitions": [
            {"AttributeName": "UserId", "AttributeType": "S"},
            {"AttributeName": "ConnectionId", "AttributeType": "S"}
        ],
        "provisioned_throughput": {
            "ReadCapacityUnits": 5,
            "WriteCapacityUnits": 5
        },
    },
    "Portfolios": {
        "key_schema": [
            {"AttributeName": "PortfolioId", "KeyType": "HASH"}  # Partition key: unique portfolio ID
        ],
        "attribute_definitions": [
            {"AttributeName": "PortfolioId", "AttributeType": "S"}
        ],
        "provisioned_throughput": {
            "ReadCapacityUnits": 5,
            "WriteCapacityUnits": 5
        },
    },
    "Interests": {
        "key_schema": [
            {"AttributeName": "UserId", "KeyType": "HASH"},  # Partition key: user ID
            {"AttributeName": "Interest", "KeyType": "RANGE"}  # Sort key: interest category/tag
        ],
        "attribute_definitions": [
            {"AttributeName": "UserId", "AttributeType": "S"},
            {"AttributeName": "Interest", "AttributeType": "S"}
        ],
        "provisioned_throughput": {
            "ReadCapacityUnits": 5,
            "WriteCapacityUnits": 5
        },
    },
    "Messages": {
        "key_schema": [
            {"AttributeName": "ConversationId", "KeyType": "HASH"},  # Partition key: conversation ID
            {"AttributeName": "MessageTimestamp", "KeyType": "RANGE"}  # Sort key: message timestamp
        ],
        "attribute_definitions": [
            {"AttributeName": "ConversationId", "AttributeType": "S"},
            {"AttributeName": "MessageTimestamp", "AttributeType": "N"}
        ],
        "provisioned_throughput": {
            "ReadCapacityUnits": 5,
            "WriteCapacityUnits": 5
        },
    }
}
