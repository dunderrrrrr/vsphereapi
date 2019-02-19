# VSPHEREAPI
Connect and get vsphere vms using VMWare REST API.

Best used with virtualenv like below.
```
mkvirtualenv --python=/usr/bin/python3 vsphereapi
```

## Installation
`git clone git@github.com:dunderrrrrr/vsphereapi.git`  

Then install requirements with pip.
```
pip install -r requirements.txt
```

Edit auth details in get_all_vms.py
```
username = "" #vsphere username
password = "" #vsphere passwd
```

Run script with args
```
$ python get_all_vms.py --host server01
server01, guest-01_web, UBUNTU_64, POWERED_ON
server01, guest02_pgsql, UBUNTU_64, POWERED_ON
server01, guest03_mx, UBUNTU_64, POWERED_OFF
server01, guest04_log, UBUNTU_64, POWERED_ON
```
Export to file
```
$ python get_all_vms.py --host server01 > output.txt
```
Help
```
$ python get_all_vms.py -h
usage: get_all_vms.py [-h] [--host HOST]

optional arguments:
  -h, --help   show this help message and exit
  --host HOST  Specify vmware host, FQDN or IP.
```
