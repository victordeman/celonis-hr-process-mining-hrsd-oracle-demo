# celonis-hr-process-mining-hrsd-oracle-demo

![Celonis HR Dashboard Hero](https://via.placeholder.com/1200x400/0A2540/00FFAA?text=Celonis+HR+Process+Mining+Dashboard+-+EVU/EIU+Insights)
*(Replace with real exported Celonis dashboard screenshot after Phase 4)*

**End-to-End HR Process Mining Solution**  
**ServiceNow HRSD + Oracle HCM → Celonis EMS**  
**Fully simulating the Mund Consulting ID02400 project stack (EVU/EIU-style HR structures)**

---

## 🎯 One-Sentence Project Goal
This repository delivers a complete, production-ready demonstration of harmonizing ServiceNow HR Service Delivery (HRSD) cases and Oracle HCM master data into Celonis EMS for advanced process mining, real-time KPIs, Action Flows, ML-powered predictions, and Power BI visualization — exactly mirroring the technical and functional scope of the Mund Consulting ID02400 EVU/EIU HR transformation project.

---

## 🏗️ Architecture Overview

```mermaid
graph TD
    subgraph "Source Systems"
        SN[ServiceNow HRSD<br>Case & Ticket Data] 
        OH[Oracle HCM<br>Employee Master Data]
    end
    subgraph "Ingestion Layer (Python + AWS)"
        PY[Python Pipeline<br>01-06 scripts]
        S3[AWS S3 Bucket]
    end
    subgraph "Celonis EMS Core"
        DM[Data Pool + Custom Data Model]
        PQL[PQL Queries + Analyses]
        DASH[Executive & Operational Dashboards]
        AF[Action Flows & Execution Apps]
        ML[ML Workbench - SLA Breach Prediction]
    end
    subgraph "Visualization"
        PBI[Power BI via Official Celonis Connector]
    end

    SN --> PY
    OH --> PY
    PY --> S3
    S3 --> DM
    DM --> PQL & DASH & AF & ML
    DASH --> PBI
