#!/usr/bin/env python3
"""
PyATS Network Test Suite for Cisco DevNet Sandbox
"""

import os
import datetime
from pyats.topology import loader

def main():
    print("🚀 Starting PyATS Network Test Suite for Cisco DevNet...")
    
    # Load testbed
    testbed = loader.load('testbed.yaml')
    device = testbed.devices['devnet-sandbox']
    
    try:
        device.connect(log_stdout=True)
        print(f"✅ Successfully connected to {device.name}")
        
        # Import and run tests
        from tests.interface_test import test_interfaces
        from tests.bgp_test import test_bgp
        from tests.ospf_test import test_ospf
        
        results = {}
        results['interfaces'] = test_interfaces(device)
        results['bgp'] = test_bgp(device)
        results['ospf'] = test_ospf(device)
        
        # Generate HTML report
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        report_dir = "reports"
        os.makedirs(report_dir, exist_ok=True)
        report_file = f"{report_dir}/network_report_{timestamp}.html"
        
        with open(report_file, "w", encoding="utf-8") as f:
            f.write(generate_html_report(results, device))
        
        print(f"✅ Tests completed successfully!")
        print(f"📊 Report generated: {report_file}")
        
    except Exception as e:
        print(f"❌ Error during execution: {str(e)}")
    finally:
        if device.is_connected():
            device.disconnect()
            print("Disconnected from device.")

def generate_html_report(results, device):
    html = f"""
<!DOCTYPE html>
<html>
<head>
    <title>PyATS Test Report - {device.name}</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 40px; background: #f8f9fa; }}
        h1, h2 {{ color: #007bff; }}
        pre {{ background: #f4f4f4; padding: 15px; border-radius: 5px; }}
        .success {{ color: green; }}
        .fail {{ color: red; }}
    </style>
</head>
<body>
    <h1>PyATS Network Test Report</h1>
    <p><strong>Device:</strong> {device.name} | <strong>Time:</strong> {datetime.datetime.now()}</p>
    <hr>
    <h2>Interface Status</h2>
    <pre>{results['interfaces']}</pre>
    <h2>BGP Neighbors</h2>
    <pre>{results['bgp']}</pre>
    <h2>OSPF Adjacency</h2>
    <pre>{results['ospf']}</pre>
</body>
</html>
    """
    return html

if __name__ == "__main__":
    main()
