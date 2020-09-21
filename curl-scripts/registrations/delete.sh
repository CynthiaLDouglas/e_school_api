#!/bin/bash

curl "http://localhost:8000/registrations/${ID}" \
  --include \
  --request DELETE \
  --header "Authorization: Token ${TOKEN}"

echo
