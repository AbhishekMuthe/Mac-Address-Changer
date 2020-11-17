import subprocess

interface_name = input('Enter Interface')
new_mac = input('Enter your new_mac)

#ifconfig eth0 down
subprocess.call(['ifconfig', interface_name, 'down'])

#ifconfig eth0 hw ether <MAC address>
subprocess.call(['ifconfig', interface_name, 'hw', 'ether', new_mac])

#ifconfig eth0 up
subprocess.call('ifconfig, interface_name, 'up')

#output
output = str(subprocess.check_output(['ifconfig', interface_name])
changed_mac = re.search(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w', output)

#check
if new_mac == changed_mac.group(0):
	print('succesfully changed mac')