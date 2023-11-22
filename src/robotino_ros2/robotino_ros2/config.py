def ip_address(node):
    node.declare_parameter("robotino_ip", "")
    ip = node.get_parameter("robotino_ip").value
    if(ip == ""):
        node.get_logger.warning("No robotino ip set")
    return ip