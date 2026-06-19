def test_interfaces(device):
    """Test interface status"""
    try:
        output = device.parse("show ip interface brief")
        return str(output)
    except Exception as e:
        return f"Error getting interfaces: {str(e)}"