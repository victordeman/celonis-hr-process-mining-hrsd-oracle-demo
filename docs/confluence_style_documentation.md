# HR Process Mining Solution (Mund Consulting ID02400) - Documentation

**Status:** Draft / Production-Ready Demo  
**Owner:** Victor de Man  
**Tech Stack:** ServiceNow HRSD, Oracle HCM, AWS S3, Celonis EMS, Power BI  

---

## 1. Executive Summary
This project simulates the harmonization of two disparate HR systems into a unified Celonis EMS environment. The goal is to identify process inefficiencies, reduce manual rework, and predict SLA breaches in an EVU/EIU-structured utility company.

### Business Goals
1.  **Transparency**: Visibility across all HR entities (Nord, Sued, West, East).
2.  **Efficiency**: Identify bottlenecks in the "Manager Approval" and "HR Review" stages.
3.  **Predictability**: Predict SLA breaches using machine learning before they happen.
4.  **Automation**: Trigger notifications via Celonis Action Flows when rework is detected.

---

## 2. Technical Architecture

### 2.1. Source Systems
- **ServiceNow HRSD**: Captures the event log (activities, timestamps, actors) for HR cases.
- **Oracle HCM Cloud**: Provides employee master data (Job Role, Location, Hire Date, Entity).

### 2.2. Data Pipeline (Python/AWS)
- **ETL Scripts**: Python-based pipeline for data generation (Synthetic), cleaning, and harmonization.
- **Storage**: AWS S3 acts as the landing zone for raw and harmonized data.
- **Ingestion**: PyCelonis connects the S3 bucket (or local data) to Celonis Data Integration.

### 2.3. Celonis EMS Core
- **Data Model**: A consolidated Snowflake schema with `HRSD_ORACLE_HARMONIZED_LOG` as the central event log and case attribute table.
- **PQL Layer**: Custom PQL queries for SLA compliance, idle time, and rework rates.
- **ML Workbench**: Jupyter notebooks for training SLA breach prediction models.

---

## 3. Key Process Insights (Simulated)

### 3.1. The "Rework Loop" Bottleneck
Analysis showed that **15% of cases** undergo a "Rework Loop". This activity increases the average cycle time by **3.5 days**. Cases in the "Benefits" department are 2x more likely to require rework than "Payroll".

### 3.2. Manager Approval Latency
The longest idle time occurs between "Assign to Team" and "Manager Approval". This is particularly high in the **EVU_Nord** entity, suggesting a need for automated reminders or delegation rules.

---

## 4. Automation & Actions
We have implemented **Action Flows** to address detected inefficiencies:
- **Auto-Escalation**: If a 'Critical' priority case hasn't been resolved within 24 hours of creation, an email is sent to the Department Head.
- **Resource Re-assignment**: If an agent has more than 20 active cases, a Slack alert is triggered to the team lead.

---

## 5. Maintenance and Support
- **Pipeline Monitoring**: Check `scripts/04_upload_to_aws_s3.log` for ingestion failures.
- **Data Refresh**: Data is currently refreshed every 24 hours via a scheduled Action Flow trigger.
- **Model Retraining**: The SLA prediction model should be retrained monthly using the provided ML Workbench notebook.
