#!/bin/bash

curl "http://localhost:8000/items/" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
