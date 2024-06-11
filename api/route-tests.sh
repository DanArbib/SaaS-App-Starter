#!/bin/bash

# Set the host variable
HOST="127.0.0.1:5000"

# The email to test
EMAIL="test@example.com"

# Make the POST request and store the response
response=$(curl -s -X POST \
  -H "Content-Type: application/json" \
  -d '{"email": "'"${EMAIL}"'"}' \
  "http://${HOST}/api/v1/email")

# Output the response
echo "Response from server: $response"