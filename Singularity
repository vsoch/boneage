Bootstrap: docker
From: tensorflow/tensorflow:0.9.0

%runscript

    cd /code/boneage
    exec /usr/bin/python /code/boneage/cli.py "$@"


%post

    apt-get update && apt-get install -y git
    mkdir /code
    mkdir /data
    cd /tmp
    git clone https://www.github.com/vsoch/boneage
    mv boneage /code
    /bin/bash /code/post.sh
