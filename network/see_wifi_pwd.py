import subprocess

# NOTE netsh is a windows tool, You can't use it on Ubuntu. But as an alternative tools the ip command from iproute2 package may be helpful for you.

# The netsh command is a built-in tool in Windows for network configuration Here in ubuntu there are few packages that help you configure the network.

# ifconfig a older network configuration tool from the net-tools package
# ip modern tool for network configuration from iproute2 package.
# nmcli command line network manager. It is quite easy in my perspective to manage network congiguration.

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profile']).decode('utf-8').split('\n')
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

for i in profiles:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]

    try:
        print("{:<30}| {:<}".format(i, results[0]))
    except IndexError:
        print("{:<30}| {:<}".format(i, ""))
