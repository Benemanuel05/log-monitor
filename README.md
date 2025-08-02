# Log Monitor

A simple Python tool that reads a login log file, detects failed login attempts, and sends alerts if any IP has too many failures.

## 🔍 What It Does
- Reads from `sample_log.txt`
- Flags IPs with 3 or more failed login attempts
- Prints alert messages to the terminal

## 🧪 How to Run

```bash
python3 log_monitor.py
