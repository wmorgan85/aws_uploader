#!/usr/bin/env bash

# from https://stackoverflow.com/questions/37267916/how-to-run-aws-configure-in-a-travis-deploy-script

mkdir -p ~/.aws

cat > ~/.aws/credentials << EOL
[default]
aws_access_key_id = ${AWS_ACCESS_KEY_ID}
aws_secret_access_key = ${AWS_SECRET_ACCESS_KEY}
EOL