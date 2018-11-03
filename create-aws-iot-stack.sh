aws cloudformation create-stack \
  --stack-name heatermeter-`echo $(date +%s)` \
  --template-body file://./templates/iot-gateway.yaml \
  --disable-rollback \
    --parameters \
    "[{ \"ParameterKey\": \"HeatermeterThingID\", \"ParameterValue\": \"b827eb0114ac\" },
    { \"ParameterKey\": \"S3BucketARNRawEvents\", \"ParameterValue\": \"arn:aws:s3:::tommcm-heatermeter\" },
    { \"ParameterKey\": \"CertificateARN\", \"ParameterValue\": \"arn:aws:iot:ap-southeast-2:447119549480:cert/3168a6b6108792fb263d4c6ea06b2b1536426f0a749d0ab289f347d88ae4e08a\" } ]" \
        --capabilities CAPABILITY_NAMED_IAM