# activemq_client
ActiveMQを用いてメッセージングを行うプログラム

# Install
```
git clone https://github.com/social-robotics-lab/activemq_client.git
cd activemq_client
docker build -t activemq_client .
```

# Run
1. ActiveMQを起動
```
docker network create -d bridge amqnet
docker run -it -p 8161:8161 --name activemq --network activemq --rm activemq ./activemq console
```

2. Dockerコンテナを起動
```
docker run -it --name activemq_client --network activemq --mount type=bind,source="$(pwd)"/src,target=/tmp --rm activemq_client /bin/bash
python sample.py --amq_host activemq --sub_topic test --pub_topic test --pub_message "Hello world"
```
