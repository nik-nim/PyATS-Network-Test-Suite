def test_bgp(device):
    """Test BGP neighbors"""
    try:
        output = device.parse("show bgp summary")
        return str(output)
    except Exception as e:
        return f"Error getting BGP info: {str(e)}"