# DOS TOOL: UNKNOWN

## Overview

This script is a demonstration of a Denial-of-Service (DoS) attack tool. It attempts to send multiple requests to a target URL using multiple threads, potentially overwhelming the server and causing it to become unresponsive.

**Disclaimer:** This script was created for educational purposes only. It is intended to demonstrate how such attacks can be carried out and to highlight the importance of securing your web applications against them. **Do not use this script for any malicious activity.**

## Important Note

I wrote this script when I was young (around 14 or 15 years old). It is very inefficient and most likely won't work correctly with modern web security measures. It is not recommended to use this script for any practical purposes.

## Features

- Supports both normal HTTP requests and Cloudflare-bypassing requests.
- Uses multiple threads to send a large number of requests to the target URL.
- Randomizes user agents and referrer headers to simulate different clients.

## Usage

1. **Install Dependencies:**
   Make sure you have the required Python packages installed:
   ```bash
   pip install cfscrape requests
   ```

2. **Run the Script:**
   ```bash
   python dos-tool.py
   ```

4. **Follow the Prompts:**
   - Enter the target URL.
   - Choose whether to use Cloudflare Bypass or Normal Attack.
   - Specify the number of threads to use (default is 800).

## Example

```
##############################
DOS TOOL:UNKNOWN
##############################
Enter Url to DoS> http://example.com
[y]Cloudflare Bypass | [Enter]Normal Attack> 
Enter the amount of threads[800]> 100
::::::::::::::::::::::::::::::
Target: http://example.com
CloudFlare Bypass: False
Threads: 100
Starting in 5 seconds
::::::::::::::::::::::::::::::
```

## Important

- This script is for educational purposes only. 
- Using this tool to attack a website without permission is illegal and unethical. 
- Use this script responsibly.

---

**Disclaimer:** This is a poorly written script that was created when I was quite young. It is not efficient and probably won't run successfully with modern web technologies. Use it at your own risk, and only for learning and educational purposes.