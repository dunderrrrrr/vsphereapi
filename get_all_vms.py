import sys
import vcrest
import json
import argparse

username = "" #vsphere username
password = "" #vsphere passwd

def list_vms(vcip): #all vms in list with moID
    try:
        vcsession = vcrest.get_vc_session(vcip, username, password)
        vms = vcrest.get_vms(vcip)
        vm_response=json.loads(vms.text)
        json_data=vm_response["value"]
        vmlist = []
        for vm in json_data:
            vmlist.append(vm)
        return(vmlist)
    except Exception as E:
        print("Error fetching vms: {}".format(E))
        sys.exit(0)

def list_vm(vcip, vmid): # detailed vm data
    vm = vcrest.get_vm(vcip, vmid)
    vm_response=json.loads(vm.text)
    json_data=vm_response["value"]
    return(json_data)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', action='store', help="Specify vmware host, FQDN or IP.")
    args = parser.parse_args()
    if len(sys.argv)==1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    vms = list_vms(args.host)
    for vm in vms:
        vmdata = list_vm(args.host, vm['vm']) #vm detals
        print("{}, {}, {}, {}".format(args.host, vmdata['name'], vmdata['guest_OS'], vmdata['power_state']))
