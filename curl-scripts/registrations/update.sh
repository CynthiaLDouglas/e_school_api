#!/bin/bash

curl "http://localhost:8000/registrations/${ID}" \
  --include \
  --request PATCH \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "registration": {
      "semester": "'"${SEMESTER}"'",
      "course_name": "'"${COURSE_NAME}"'",
      "student_enrolled": "'"${STUDENT_ENROLLED}"'"
    }
  }'

echo
