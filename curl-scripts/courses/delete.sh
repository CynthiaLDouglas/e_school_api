#!/bin/bash

curl "http://localhost:8000/courses/${ID}" \
  --include \
  --request DELETE \
  --header "Authorization: Token ${TOKEN}"

echo
