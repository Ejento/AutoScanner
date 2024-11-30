# HTB Enumeration Automation Tool

## Overview
A Python3-based automation tool designed to streamline the enumeration phase for HackTheBox challenges and boxes. This tool is currently in experimental status and is being actively developed.

## ⚠️ Disclaimer
This tool is experimental and may contain bugs. Use at your own risk and always verify the results manually.

## Features
* Automated port scanning
* Service enumeration
* Basic vulnerability checks
* Report generation
* Custom target specification

## Prerequisites
* Python 3.x
* Required Python packages (install via pip):
```bash
pip install -r requirements.txt
```

## Installation
```bash
git clone <repository-url>
cd htb-enum-tool
chmod +x setup.sh
./setup.sh
```

## Usage
Basic usage:
```bash
python3 htb-enum.py -t <target_ip>
```

Advanced options:
```bash
python3 htb-enum.py -t <target_ip> --thorough --output report.txt
```

## Configuration
The tool can be configured by editing the `config.yml` file:
```yaml
scan_timeout: 300
threads: 4
verbose: true
```

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## To-Do
- [ ] Add more service fingerprinting
- [ ] Implement automated report generation
- [ ] Add custom script support
- [ ] Improve error handling
- [ ] Add configuration validation

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
* HackTheBox for providing the platform
* The security community for feedback and support

## Contact
Project Link: [https://github.com/yourusername/htb-enum-tool](https://github.com/yourusername/htb-enum-tool)

---
**Note**: This tool is intended for use only on machines and challenges that you have explicit permission to test. Do not use this tool against systems you do not have permission to test.
