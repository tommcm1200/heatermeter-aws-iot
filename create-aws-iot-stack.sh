aws cloudformation create-stack \
  --stack-name heatermeter-`echo $(date +%s)` \
  --template-body file://./templates/iot-gateway.yaml \
  --disable-rollback \
    --parameters \
    "[{ \"ParameterKey\": \"HeatermeterThingID\", \"ParameterValue\": \"B40429203C26\" },
    { \"ParameterKey\": \"S3BucketARNRawEvents\", \"ParameterValue\": \"arn:aws:s3:::tommcm-heatermeter\" },
    { \"ParameterKey\": \"CertificateARN\", \"ParameterValue\": \"arn:aws:iot:ap-southeast-2:447119549480:cert/f9f6aa49c3a43098161bfda845084adc32f3c0013e81d162c3d04f8881bdcd0e\" } ]" \
        --capabilities CAPABILITY_NAMED_IAM