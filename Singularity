Bootstrap: docker
From: tensorflow/tensorflow:0.9.0

%runscript

    cd /code/boneage
    exec /usr/bin/python /code/boneage/cli.py "$@"


%post

    /bin/bash post.sh
