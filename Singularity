Bootstrap: docker
From: tensorflow/tensorflow:0.9.0

%setup

    cp . $SINGULARITY_ROOTFS


%runscript

    cd /code/boneage
    exec /usr/bin/python /code/boneage/cli.py "$@"


%post

     apt-get update 
     apt-get -y install libtiff5-dev
     apt-get -y install libtiff5-dev
     apt-get -y install build-essential
     apt-get -y install cmake
     apt-get -y install libgtk2.0-dev
     apt-get -y install libjpeg8-dev
     apt-get -y install zlib1g-dev
     apt-get -y install libfreetype6-dev 
     apt-get -y install liblcms2-dev
     apt-get -y install libwebp-dev 
     apt-get -y install tcl8.6-dev
     apt-get -y install tk8.6-dev
     apt-get -y install wget
     apt-get -y install unzip
     apt-get -y install python-tk
     apt-get -y install python-dev 
     apt-get -y install pkg-config
     apt-get -y install libffi-dev 
     apt-get -y install libssl-dev
     apt-get -y install qt-sdk
     apt-get -y install libavcodec-dev 
     apt-get -y install libavformat-dev
     apt-get -y install libswscale-dev
     apt-get -y install libjpeg-dev
     apt-get -y install libpng-dev
     apt-get -y install libtiff-dev
     apt-get -y install libjasper-dev

     # Software dependencies. 
     # This is equivalent of requirements.txt,      on image build
     pip install --upgrade pip
     pip install cycler==0.10.0
     pip install h5py==2.6.0
     pip install matplotlib==1.5.3
     pip install nose==1.3.7
     pip install numpy==1.11.0
     pip install pandas==0.18.1
     pip install Pillow==3.2.0
     pip install pydicom==0.9.9
     pip install pyparsing==2.1.10
     pip install python-dateutil==2.5.3
     pip install pytz==2016.4
     pip install runcython==0.2.5
     pip install scipy==0.18.1
     pip install six==1.10.0
     pip install simplejson

     # Build and install OpenCV
     wget https://github.com/Itseez/opencv/archive/3.1.0.zip
     unzip 3.1.0.zip
     rm 3.1.0.zip
     wget https://github.com/Itseez/opencv_contrib/archive/3.1.0.zip
     unzip 3.1.0.zip
     mkdir -p opencv-3.1.0/build
WORKDIR opencv-3.1.0/build
     cmake -D CMAKE_BUILD_TYPE=RELEASE \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D INSTALL_PYTHON_EXAMPLES=ON \
    -D INSTALL_C_EXAMPLES=OFF \
    -D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib-3.1.0/modules \
    -D PYTHON_EXECUTABLE=/usr/bin/python \
    -D BUILD_EXAMPLES=ON ..
     make -j4
     make install
     ldconfig

     # Make directories for code and data
     mkdir /code
     mkdir /data

     wget https://stanford.box.com/shared/static/t8hvcgy4m5kh5m76pt9kg9s71kjmik6c.meta -O /code/boneage/data/bone-age-checkpoint.ckpt-19999.meta
     wget https://stanford.box.com/shared/static/5936ydxx4qjk9rjkm1aun5fa9g5h27tt.ckpt-19999 -O /code/boneage/data/bone-age-checkpoint.ckpt-19999

     # Clean up
     apt-get autoremove -y
     apt-get clean
     rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
     chmod u+x /code/boneage/cli.py
     chmod -R 777 /data
