 IT Support Ticket Automation System (Python)
A Python-based automation tool that processes 140+ enterprise IT support tickets, categorizes them using keyword detection, assigns ITIL‑aligned priority levels, and generates structured logs for analysis.
This project simulates real service desk workflows and demonstrates practical skills in automation, Python scripting, incident management, and enterprise IT operations.

📑 Table of Contents
Overview

Features

Technologies Used

Project Structure

How It Works

Installation

Usage

Sample Output

Dataset

Future Enhancements

Skills Demonstrated

Contact

Overview
Modern IT service desks handle hundreds of tickets daily. Manual triage is slow, inconsistent, and prone to human error.
This project automates the triage process by:

Reading tickets from a CSV dataset

Categorizing incidents using keyword rules

Assigning priority levels based on ITIL practices

Features
Automated Categorization  
Detects keywords in ticket descriptions and assigns categories (Network, Hardware, Access, Application, Security, Cloud).

ITIL-Based Priority Assignment  
Maps categories to priority levels (High, Medium, Low).

Enterprise-Grade Dataset  
Includes 140+ realistic IT support tickets across multiple departments.

Structured Log Output  
Generates a clean .log file with ticket ID, category, priority, and timestamp.

Easy to Extend  
Add more keywords, categories, or integrate with APIs (ServiceNow, Jira, Freshdesk).

🛠 Technologies Used
Python 3

CSV Data Processing

ITIL Incident Management Concepts

VS Code 

📁 Project Structure:
ticket_automation_project/
│── ticket_automation.py      # Main automation script
│── tickets.csv               # 140+ enterprise IT tickets
│── processed_tickets.log     # Output log file
│── README.md                 # Documentation

How It Works
1. Keyword Detection
The script scans each ticket description for keywords:

python
CATEGORY_RULES = {
    "password": "Access Issue",
    "vpn": "Network Issue",
    "database": "Application Issue",
    "error": "Application Issue",
    "email": "Account Issue",
    "overheating": "Hardware Issue"
}
2. Priority Mapping
Each category maps to a priority:

python
PRIORITY_RULES = {
    "Hardware Issue": "High",
    "Network Issue": "High",
    "Application Issue": "Medium",
    "Access Issue": "Low",
    "Account Issue": "Low"
}
3. Processing Engine
The script:

Reads the CSV

Applies rules

Generates logs

📥 Installation
1. Clone the Repository

git clone https://github.com/YOUR-USERNAME/ticket-automation-python.git
2. Navigate to the Project Folder

cd ticket-automation-python
3. Run the Script

python ticket_automation.py
▶️ Usage
After running the script, a new file appears:

processed_tickets.log
This file contains categorized and prioritized tickets.

📊 Sample Output (processed_tickets.log)

101 | Account Issue | Low | 2026-09-15 12:30:22
102 | Hardware Issue | High | 2026-09-15 12:30:22
103 | Network Issue | High | 2026-09-15 12:30:22
104 | Access Issue | Low | 2026-09-15 12:30:22
105 | Application Issue | Medium | 2026-09-15 12:30:22

🗂 Dataset
The dataset includes 140+ enterprise IT tickets, covering:

Network failures

VPN issues

Hardware problems

Access & authentication issues

ERP/CRM errors

Cloud sync failures

Security alerts

Email issues

Mobile device problems

This makes the project realistic and suitable for automation testing.

🚀 Future Enhancements
Add severity levels (Critical, High, Medium, Low)

Add ticket status (Open, In Progress, Resolved)

Add timestamps (Created_at, Updated_at)

Add SLA timers

Add department field (HR, Finance, IT, Sales)

Integrate with ServiceNow or Jira API

Build a dashboard using Flask or Streamlit

🎓 Skills Demonstrated
Python scripting

Automation

CSV data processing

ITIL incident management

Problem classification

Logging & documentation

Real-world IT support simulation


Logging results with timestamps

The result is a lightweight automation engine that improves consistency and reduces manual workload.
