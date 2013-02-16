# install pip
curl -O https://raw.github.com/pypa/pip/master/contrib/get-pip.py
sudo python get-pip.py

# install Django
pip install django==1.4.3

# install boto
wget http://boto.googlecode.com/files/boto-2.6.0.tar.gz
tar xzvf boto-2.6.0.tar.gz 
cd boto-2.6.0
sudo python setup.py install
cd ..

# install git
yum install git

# install MySQL-python
yum install -y MySQL-python

# install PIL
yum install -y zlib zlib-devel
yum install -y libjpeg libjpeg-level
yum install -y freetype freetype-devel
yum install -y python-imaging
