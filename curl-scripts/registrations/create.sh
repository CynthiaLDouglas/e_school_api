#!/bin/bash

curl "http://localhost:8000/registrations/" \
  --include \
  --request POST \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "registrations": {
      "course_name": "'"${NAME}"'",
      "student_enrolled": "'"${STUDENT_ENROLLED}"'",
    }
  }'

echo
