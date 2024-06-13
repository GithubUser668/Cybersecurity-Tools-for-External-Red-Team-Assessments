# Cybersecurity Tools for External Red Team Assessments
This repository contains a collection of scripts designed to assist cybersecurity professionals and red team experts in conducting external assessments. Each script is accompanied by a detailed README.md file for individual usage instructions. These tools were developed with the assistance of ChatGPT, ensuring robust functionality and ease of use.

## Overview
The purpose of these scripts is to help cybersecurity experts who are conducting external red team assessments. Below are the current scripts available in this repository:

### Wayback Machine Sensitive Information Finder
- Description: This script searches for sensitive information within the Wayback Machine archives of a specified domain. It helps uncover historical data that might be useful for penetration testing and security assessments.

- Purpose: To identify and analyze any sensitive information that might have been exposed in the past, providing valuable insights into potential vulnerabilities.

### Apache Tomcat Version Identifier
- Description: This script is designed to identify the version of Apache Tomcat running on a target server. Knowing the version can help in assessing potential vulnerabilities and planning subsequent actions.

- *Purpose*: To quickly and accurately determine the Apache Tomcat version, facilitating vulnerability assessment and informed decision-making during red team operations.

### Liferay Application Version Identifier
- Description: This script identifies the version of Liferay applications running on a target server. This information is crucial for determining known vulnerabilities and potential attack vectors specific to that version.

- Purpose: To identify the Liferay application version, enabling targeted vulnerability assessment and exploitation strategies.

## Getting Started
To use these scripts, follow the instructions in each script's respective README.md file. Ensure you have the necessary dependencies installed, which are typically listed in each file.

##### Prerequisites
Python 3.x
Required Python libraries (as specified in each script's README.md)
## Installation
Clone the repository:
- git clone https://github.com/yourusername/cybersecurity-tools.git
- cd cybersecurity-tools
- Navigate to the script directory and install dependencies:
- pip install -r requirements.txt
## Scripts Details
### Wayback Machine Sensitive Information Finder
- Purpose: To help cybersecurity experts conducting external assessments by identifying previously exposed sensitive information in the Wayback Machine.

- Usage: This script fetches archived pages of a specified domain from the Wayback Machine and scans them for sensitive information such as email addresses, API keys, and other potentially exposed data.

- Languages/Technologies Used: Python, Requests, BeautifulSoup

- Example Usage:
- <sup> python wayback_sensitive_info_finder.py --domain example.com</sup>

Apache Tomcat Version Identifier
Purpose: To assist in identifying the Apache Tomcat version during external assessments, aiding in the discovery of potential vulnerabilities.

Usage: This script connects to the target server, retrieves the server response headers, and identifies the version of Apache Tomcat based on known version patterns.

Languages/Technologies Used: Python, Requests

## Example Usage:

python tomcat_version_identifier.py --url http://example.com
Liferay Application Version Identifier
Purpose: To determine the version of Liferay applications on target servers during external assessments, facilitating the identification of relevant vulnerabilities.

Usage: This script interacts with the Liferay application running on a specified server to determine its version using specific endpoints and known response patterns.

Languages/Technologies Used: Python, Requests

Example Usage:

bash
Copy code
python liferay_version_identifier.py --url http://example.com
Contributing
Contributions are welcome! Please read the CONTRIBUTING.md for details on our code of conduct and the process for submitting pull requests.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Special thanks to ChatGPT for assistance in writing these scripts.
Inspiration and resources from the cybersecurity community.
Open-source tools and libraries that made these scripts possible.

