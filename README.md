# Vult - Automated Vulnerability Scanner

## Overview

**Vult** is an automated vulnerability scanner built in Python. It allows users to scan target systems for common vulnerabilities using network scanning (via Nmap) and packet crafting (via Scapy). The tool is designed to provide both detailed and structured reports of potential vulnerabilities in the scanned systems.

## Features

- **Network Scanning:** Uses Nmap to scan for open ports, services, and hosts.
- **Packet Crafting:** Utilizes Scapy to send custom packets and analyze system responses.
- **Vulnerability Detection:** Identifies possible vulnerabilities based on open ports and system responses.
- **Report Generation:** Provides reports in JSON format (extendable to HTML or XML) summarizing detected vulnerabilities.
- **Logging:** Records scan activities and results for auditing and troubleshooting.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Reporting](#reporting)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/vult.git
   cd vult

2. **Set up a virtual environment (Python 3.12):**
   ```bash
    python3.12 -m venv vult_env
    source vult_env/bin/activate

3. **Install dependencies:**
   ```bash
    pip install -r requirements.txt

## Usage

1. **Basic scan:** Run a basic scan against a target system:
   ```bash
    python3.12 vult/cli.py -t <target-ip> -p <ports> -o <output-file>

- Exemple:
   ```bash
    python3 vult/cli.py -t 192.168.1.1 -p 1-1024 -o report.json

2. **Parameters:**
    ```bash
    -t, --target: Target system (IP address or range).
    -p, --ports: Ports to scan (default: 1-1024).
    -o, --output: Output file for the report (default: report.json).


## Configuration

Vult allows customization via command-line arguments. You can also extend it to support configuration files (e.g., JSON or YAML) to load more complex scan options.

## Reporting
Vult generates scan reports in JSON format by default. These reports contain detailed information about:

- Open ports.
- Services running on detected hosts.
- Identified vulnerabilities (if any).

You can extend the reporting functionality by modifying the reporter.py module to generate HTML or XML reports.

## Testing
**Unit Tests**
    Vult includes unit tests for key modules. You can run the tests using **pytest**:


```
pytest
```
**Functional Testing**
- To manually test the scanner, run it against local or controlled targets (e.g., localhost or a vulnerable VM like Metasploitable):

    ```
    python3 vult/cli.py -t 127.0.0.1 -p 1-1024 -o report.json
    ```
    Check the log file vult.log and the generated report to ensure the scanner behaves as expected.


## Contributing
We welcome contributions to Vult. Please follow these steps to contribute:

- Fork the repository.
- Create a new branch with a descriptive name (e.g., feature-new-scan-mode).
- Make your changes and write tests for them.
- Submit a pull request describing your changes.

