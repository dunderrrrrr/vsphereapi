import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

s=requests.Session()
s.verify=False

def get_vc_session(vcip,username,password):
         s.post('https://'+vcip+'/rest/com/vmware/cis/session',auth=(username,password))
         return s

def get_vms(vcip):
        vms=s.get('https://'+vcip+'/rest/vcenter/vm')
        return vms

def get_vm(vcip, vmid):
        vms=s.get('https://'+vcip+'/rest/vcenter/vm/'+vmid+'')
        return vms
