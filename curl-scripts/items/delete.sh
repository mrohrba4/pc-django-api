#!/bin/bash

curl "http://localhost:8000/items/${ID}/" \
  --include \
  --request DELETE \
  --header "Authorization: Token ${TOKEN}"

echo
