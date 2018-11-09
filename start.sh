# stop script on error
set -e

# Check to see if root CA file exists, download if not
if [ ! -f ./certs/root-CA.crt ]; then
  printf "\nDownloading AWS IoT Root CA certificate from AWS...\n"
  curl https://www.amazontrust.com/repository/AmazonRootCA1.pem > ./certs/root-CA.crt
fi

# install AWS Device SDK for Python if not already installed
if [ ! -d ./aws-iot-device-sdk-python ]; then
  printf "\nInstalling AWS SDK...\n"
  git clone https://github.com/aws/aws-iot-device-sdk-python.git
  # pushd aws-iot-device-sdk-python
  cd ./aws-iot-device-sdk-python
  python setup.py install
  # popd
  cd ..
fi

# run Heatermeter AWS IOT Connector app using certificates downloaded in package
printf "\nRunning Heatermeter AWS IOT Connector application...\n"
python heatermeter_IoT_Connector.py
# python heatermeter_IoT_Connector.py -e $endpoint -r ./certs/root-CA.crt -c $private_cert -k $private_key --url "http://$ip_address/luci/lm/stream/" --topic "heatermeter/$mac_address"
# python heatermeter_IoT_Connector.py -e a2b34sex7tdupr-ats.iot.ap-southeast-2.amazonaws.com -r ./certs/root-CA.crt -c ./certs/heatermeter-osx.cert.pem -k ./certs/heatermeter-osx.private.key --url "http://192.168.1.37/luci/lm/stream/" --topic "heatermeter/B40429203C26"
# python heatermeter_IoT_Connector.py -e a2b34sex7tdupr-ats.iot.ap-southeast-2.amazonaws.com -r ./certs/root-CA.crt -c ./certs/heatermeter-osx.cert.pem -k ./certs/heatermeter-osx.private.key -f "event-sample.json" --topic "heatermeter/B40429203C26"