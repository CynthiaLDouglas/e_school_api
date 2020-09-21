#!/bin/bash

curl "http://localhost:8000/registrations/${ID}" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
