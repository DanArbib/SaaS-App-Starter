#!/bin/bash

if [ -z "$1" ]; then
    echo "Usage: $0 <host>"
    exit 1
fi

host_url="http://$1"
signup_data='{"email": "test2@example.com", "password": "password", "name": "test"}'

# Check health
response=$(curl -s -o /dev/null -w "%{http_code}" $host_url/health)
if [ $response -ne 200 ]; then
    echo "Health check faild. Status code: $response"
    exit 1
fi

# Sign up
response=$(curl -s -o /dev/null -w "%{http_code}" -X POST -H "Content-Type: application/json" -d "$signup_data" $host_url/api/v1/sign)
    echo "$response"
if [ $response -ne 200 ]; then
    echo "Signup test failed. Status code: $response"
    exit 1
fi

# Login
login_response=$(curl -s -H "Content-Type: application/json" -d "$signup_data" $host_url/api/v1/login)
access_token=$(echo $login_response | tr -d '\n' | sed -e 's/.*"access_token":"\([^"]*\)".*/\1/')

if [ ! -z "$access_token" ]; then
    echo "Login test passed. Access token obtained: $access_token"
else
    echo "Login test failed. Unable to obtain access token."
    exit 1
fi