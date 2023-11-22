
def ip_address(node):
    ip = node.get_parameter("/robotino_ip")
    if(not ip):
        print("no robotino ip set")
    return ip