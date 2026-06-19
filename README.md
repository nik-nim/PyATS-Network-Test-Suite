# PyATS Network Test Suite

A professional PyATS + Genie test suite for Cisco devices, focused on DevNet sandboxes.

## Features
- Interface status checks
- BGP neighbor validation
- OSPF adjacency checks
- Beautiful HTML reports
- Easy to extend

## Quick Start

1. Create virtual environment:
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

2. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```

3. Run tests:
   ```powershell
   python main.py
   ```

## Note
- Update `testbed.yaml` with correct credentials if needed.
- DevNet sandbox IP and credentials may change over time.

Made with ❤️ for Network Automation.