# Advanced E-Waste Data Sanitization System

## Overview

The Advanced E-Waste Data Sanitization System is a cybersecurity-focused application developed using Python to securely erase digital data and prevent unauthorized recovery of deleted files. The system implements multi-pass secure deletion techniques, file integrity verification using SHA-256 hashing, audit logging, analytics, and storage recovery monitoring.

## Problem Statement

Deleted files can often be recovered using forensic tools, creating security and privacy risks when disposing of digital data. This project provides a secure and efficient solution for sanitizing files and folders before disposal, reducing the risk of data leakage.

## Objectives

* Securely delete files using multi-pass overwriting.
* Prevent data recovery after deletion.
* Generate audit logs for verification.
* Analyze file types and storage utilization.
* Detect duplicate files.
* Monitor storage recovery after sanitization.

## Features

### Secure Data Sanitization

* Multi-Pass Secure File Deletion (1, 3, and 7 passes)
* Secure Folder Sanitization
* Batch File Deletion

### Security Features

* SHA-256 File Integrity Verification
* Secure Random Data Overwriting
* Audit Logging of Deleted Files

### Analytics Features

* File Type Analytics
* Duplicate File Detection
* Large File Scanner
* Storage Recovery Statistics

### Reporting Features

* CSV Audit Logs
* Audit Report Generation
* Deletion History Tracking

## Technologies Used

* Python
* Object-Oriented Programming (OOP)
* File Handling
* CSV Processing
* SHA-256 Hashing
* Cybersecurity Concepts
* Data Analytics

## Project Structure

```text
Advanced-EWaste-Data-Sanitization-System/
│
├── securee.py
├── README.md
├── requirements.txt
├── deletion_report.csv
└── screenshots/
```

## System Workflow

1. User selects a file or folder.
2. SHA-256 hash is generated.
3. File content is overwritten using secure random data.
4. Multiple overwrite passes are executed.
5. File is renamed and permanently deleted.
6. Deletion details are logged.
7. Statistics and reports are generated.

## How to Run

### Clone Repository

```bash
git clone https://github.com/yourusername/Advanced-EWaste-Data-Sanitization-System.git
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Project

```bash
python securee.py
```

## Sample Functionalities

* Secure Delete File
* Secure Delete Folder
* Batch Delete Files
* Scan Large Files
* File Type Analytics
* Duplicate File Detection
* View Statistics
* Generate Audit Report

## Results

* Secure removal of sensitive files.
* Prevention of data recovery.
* Improved storage management.
* Automated audit logging and reporting.

## Future Scope

* Graphical User Interface (GUI)
* Cloud Storage Sanitization
* PDF Audit Reports
* Data Visualization Dashboard
* AI-Based File Classification
* Enterprise-Level User Authentication

## Applications

* Corporate Data Disposal
* Educational Institutions
* Government Organizations
* Personal Data Protection
* IT Asset Disposal Management

## Author

**Thanmai Siri Sandu**

B.Tech Advanced Computer Science and Engineering

Vignan University

## License

This project is developed for educational and academic purposes.
