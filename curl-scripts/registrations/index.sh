#!/bin/bash

curl "http://localhost:8000/registrations" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
