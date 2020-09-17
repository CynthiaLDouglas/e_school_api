#!/bin/bash

curl "http://localhost:8000/courses/" \
  --include \
  --request POST \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "course": {
      "name": "'"${NAME}"'",
      "subject": "'"${SUBJECT}"'",
      "course_description": "'"${COURSE_DESCRIPTION}"'"
    }
  }'

echo
