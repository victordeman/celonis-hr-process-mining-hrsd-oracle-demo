# Celonis Power BI Connector Setup Guide

This guide explains how to connect Celonis EMS to Power BI for the HR Process Mining project (Mund Consulting ID02400).

---

## 🔧 1. Prerequisites
- Celonis EMS API Token (Personal or Service Account)
- Power BI Desktop (May 2022 release or later)
- Celonis Power BI Connector (Standard)

---

## 🔌 2. Connection Steps
1. Open Power BI Desktop and select **Get Data** > **More...**
2. Search for **Celonis** and select the connector.
3. Enter your **Celonis URL** (e.g., `https://your-team.celonis.cloud`).
4. Select the **Data Pool** and **Data Model** named: `HR Process Mining (ServiceNow HRSD + Oracle HCM)`.
5. Authenticate using your **API Token**.

---

## 📊 3. Key DAX Measures
Once the data is loaded, create the following measures to enhance your Power BI dashboard:

### 📈 Total Cases
```dax
Total Cases = DISTINCTCOUNT('HRSD_ORACLE_HARMONIZED_LOG'[Case ID])
```

### ⏱️ Avg Cycle Time (Days)
```dax
Avg Cycle Time = 
AVERAGEX(
    'HRSD_ORACLE_HARMONIZED_LOG',
    DATEDIFF(
        CALCULATE(MIN('HRSD_ORACLE_HARMONIZED_LOG'[Timestamp]), ALLEXCEPT('HRSD_ORACLE_HARMONIZED_LOG', 'HRSD_ORACLE_HARMONIZED_LOG'[Case ID])),
        CALCULATE(MAX('HRSD_ORACLE_HARMONIZED_LOG'[Timestamp]), ALLEXCEPT('HRSD_ORACLE_HARMONIZED_LOG', 'HRSD_ORACLE_HARMONIZED_LOG'[Case ID])),
        DAY
    )
)
```

### ⚠️ SLA Breach Rate (%)
```dax
SLA Breach Rate = 
DIVIDE(
    CALCULATE(DISTINCTCOUNT('HRSD_ORACLE_HARMONIZED_LOG'[Case ID]), 'HRSD_ORACLE_HARMONIZED_LOG'[SLA_Status] = "SLA Breached"),
    [Total Cases],
    0
)
```

### 🔄 Rework Rate (%)
```dax
Rework Rate = 
DIVIDE(
    CALCULATE(DISTINCTCOUNT('HRSD_ORACLE_HARMONIZED_LOG'[Case ID]), 'HRSD_ORACLE_HARMONIZED_LOG'[Activity] = "Rework Loop"),
    [Total Cases],
    0
)
```

---

## 🎨 4. Dashboard Structure
- **Executive Overview Page**: KPIs (Total Cases, Cycle Time, SLA Rate) + Trendline (Cases over time).
- **Process Variant Page**: Top 10 Variants bar chart + Slicer for `Entity_Type` (EVU/EIU).
- **Bottle-neck Analysis Page**: Average time between activities matrix (using DATEDIFF).
- **Employee Insight Page**: Scatter plot (Cycle Time vs. Job Role) + Slicer for `Department`.
