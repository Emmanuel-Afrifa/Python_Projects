# A user’s IP address is defanged to prevent the user from clicking on a malicious link. 
#To convert an IP address to a defanged IP address, we need to replace “.” with “[.]”.

def ip_defang(ip_address):
    tmp = ip_address.split('.')
    defang_pi = '[.]'.join(tmp)
    return defang_pi

if __name__ == "__main__":
    ip = "1.1.2.3"
    defanged_ip = ip_defang(ip)
    print(defanged_ip)


