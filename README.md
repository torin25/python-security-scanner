# 🛡️ Basic Python Security Scanner

A lightweight, beginner-friendly security tool built in Python that performs basic reconnaissance and port scanning on a target host.  
This project focuses on **security automation**, aligning with real-world security engineering tasks such as service enumeration, banner grabbing, and report generation.

---

## 🚀 Features
- 🔍 Scans commonly used ports  
- 🧪 Performs service banner grabbing  
- 📝 Saves results into a timestamped report  
- ⚡ Fast and simple — ideal for learning security scripting  
- 🛠️ Built using only Python’s standard library  

---

## 📂 Project Structure
```
python-security-scanner/
│── scanner.py
│── README.md
└── reports/ (optional: generated scan reports)
```

---

## 🧠 How It Works
1. Prompts the user for a target host (default: `scanme.nmap.org` — a legal test server).  
2. Attempts TCP connections to selected ports.  
3. Performs banner grabbing when available.  
4. Logs open ports + banner data into a timestamped `.txt` report.

---

## 📦 Requirements
- Python 3.x  
- No external dependencies

---

## ▶️ Usage

### **1. Clone the repository**
```bash
git clone https://github.com/<your-username>/python-security-scanner
cd python-security-scanner

### **2. Run the Scanner**
```bash
python3 scanner.py

### **3. Enter a target**
```bash
python3 scanner.py

 - Report files are automatically created in the project directory