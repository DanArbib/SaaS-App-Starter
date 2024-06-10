#!/bin/bash

flask_url="http://nginx"
signup_data='{"email": "test@example.com", "password123": "password123"}'

# Check health
response=$(curl -s -o /dev/null -w "%{http_code}" $flask_url/health)

if [ $response -eq 200 ]; then
    echo "Health check passed. Status code: $response"
    exit 0
fi

# Sign up
response=$(curl -s -o /dev/null -w "%{http_code}" -X POST -H "Content-Type: application/json" -d "$signup_data" $flask_url/api/v1/sign)

if [ $response -ne 200 ]; then
    echo "Signup test failed. Status code: $response"
    exit 1
fi

# Login
login_response=$(curl -s -H "Content-Type: application/json" -d "$signup_data" $flask_url/api/v1/login)
access_token=$(echo $login_response | tr -d '\n' | sed -e 's/.*"access_token":"\([^"]*\)".*/\1/')

if [ ! -z "$access_token" ]; then
    echo "Login test passed. Access token obtained: $access_token"
else
    echo "Login test failed. Unable to obtain access token."
    exit 1
fi

# Add to database


# Get from database


# Delete from database


exit 0