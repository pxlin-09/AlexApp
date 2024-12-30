## Enter Repo

`cd AlexApp`

## Run Docker

`docker-compose up --build`

## Create DB tables after docker finishes

`python create_table.py`

## Visualize table from localhost:8001

`DYNAMO_ENDPOINT=http://localhost:4566 dynamodb-admin`

## Run SwiftApp

signup

email: test@example.com

username: test

password: password123

# NOTE!
even if db fails to add a user, firebase will create it, so you will need to create new emails to reproduce error

每一个user即使db出错，firebase也会成功注册。想要抱错的话每个email只能用一次！！！


