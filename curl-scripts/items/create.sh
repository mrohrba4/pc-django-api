#!/bin/bash

curl "http://localhost:8000/items/" \
  --include \
  --request POST \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "item": {
      "name": "'"${NAME}"'",
      "type": "'"${TYPE}"'",
      "quantity": "'"${QUANT}"'",
      "description": "'"${DESC}"'"
    }
  }'

echo
