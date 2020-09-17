#!/bin/bash

curl "http://localhost:8000/courses" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
