def test_ospf(device):
    """Test OSPF neighbors"""
    try:
        output = device.parse("show ip ospf neighbor")
        return str(output)
    except Exception as e:
        return f"Error getting OSPF info: {str(e)}"