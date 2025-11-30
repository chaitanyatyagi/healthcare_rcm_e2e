# Healthcare RCM Data Lake (healthcare_rcm_e2e)

## 📄 Overview
This repository implements a complete end-to-end **Healthcare Revenue Cycle Management (RCM) Data Lake** on Google Cloud Platform (GCP).  
It integrates EMR, Claims, CPT/ICD, and NPI data, builds multi-layer data pipelines (Landing → Bronze → Silver → Gold), and creates analytics-ready data marts for RCM dashboards.

---

## 📁 Repository Structure

| Directory / File | Description |
|------------------|-------------|
| `data/` | Sample raw files / schema formats |
| `ingestion/` | Scripts for ingesting raw data into GCS landing zone |
| `layers/` | ETL logic for Bronze → Silver → Gold layers |
| `orchestration/` | Airflow DAGs / scheduler scripts |
| `python/` | PySpark jobs (transformations, SCD2, CDM mapping) |
| `shell/` | Shell utilities for automation |
| `requirements.txt` | Python dependencies |
| `.gitignore` | Ignore rules |

---

# 🔄 **End-to-End Data Flow**

### **High-Level Architecture Flow**

```text
External Data Sources
│
├── EMR Data (patients, visits, encounters)
├── Claims Data (837/835, payer info)
├── CPT/ICD Medical Coding Data
└── NPI Registry Data
        │
        ▼
──────────────────────────────────────────────
           1. Landing Zone (GCS)
 - Raw ingestion (no modification)
 - Daily loads + archive folder
──────────────────────────────────────────────
        │
        ▼
──────────────────────────────────────────────
           2. Bronze Layer (Raw Standardized)
 - Basic cleaning
 - Data type alignment
 - Schema normalization
──────────────────────────────────────────────
        │
        ▼
──────────────────────────────────────────────
           3. Silver Layer (Business-Ready)
 - CDM (Common Data Model) mapping
 - SCD Type-2 implementation
 - Joins & referential integrity checks
 - Deduplication, enrichment
──────────────────────────────────────────────
        │
        ▼
──────────────────────────────────────────────
           4. Gold Layer (Analytics Marts)
 - Aggregated RCM metrics
 - KPI tables:
    • Denial Rates
    • AR Aging Buckets
    • Revenue by CPT/Rendering Provider
    • Payer Mix
 - Final BigQuery tables for dashboards
──────────────────────────────────────────────
        │
        ▼
Analytics & Consumption
 - Looker / Power BI / Tableau / BigQuery SQL
 - Automated reporting dashboards
