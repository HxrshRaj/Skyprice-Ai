# ✈️ SkyPrice AI

## Airline Revenue Management & Pricing Optimization Platform

SkyPrice AI is an airline-focused revenue management and pricing optimization platform designed to simulate core capabilities used by modern airlines and travel technology companies.

The platform combines demand forecasting, airline revenue optimization, fare-class analysis, and decision intelligence to help maximize revenue while efficiently managing seat inventory.

---

## Live Demo

https://skyprice-ai-a5tcnmpbvschscmrbjpgkh.streamlit.app/

---

## Project Overview

Airlines sell a perishable asset: seats.

Once a flight departs, unsold seats generate zero revenue. Revenue management systems are therefore used to determine:

* How many seats should be protected for higher-paying customers
* How much inventory should be allocated to each fare class
* Expected future demand
* Revenue-maximizing pricing and allocation strategies

SkyPrice AI demonstrates these concepts through an interactive analytics platform.

---

## Key Features

### Demand Forecasting

Predict future passenger demand using historical airline booking trends.

Capabilities:

* Historical demand analysis
* Demand trend visualization
* Forecast demand estimation
* Route-level analytics

---

### Revenue Optimization

Implements the EMSRb (Expected Marginal Seat Revenue) algorithm used in airline revenue management.

Capabilities:

* Seat protection level calculation
* Fare-class optimization
* Inventory allocation support
* Revenue maximization strategies

---

### Revenue Analytics Dashboard

Executive-level airline revenue insights.

Metrics include:

* Forecast Demand
* Total Revenue
* Average Ticket Price
* Revenue Distribution by Fare Class

---

### AI Revenue Recommendations

Generates business-focused recommendations based on demand and revenue behavior.

Examples:

* Increase premium seat protection
* Prioritize high-yield inventory
* Improve fare mix allocation
* Optimize seat availability

---

## Business Problem

Airlines face three major challenges:

1. Demand uncertainty
2. Limited seat inventory
3. Multiple fare classes

Traditional first-come-first-served selling often leaves revenue on the table.

SkyPrice AI addresses this problem by combining forecasting and optimization techniques to improve revenue outcomes.

---

## Architecture

```text
Historical Airline Data
            │
            ▼
     Data Processing
            │
            ▼
    Demand Forecasting
            │
            ▼
      EMSRb Engine
            │
            ▼
 Revenue Optimization
            │
            ▼
 Executive Dashboard
            │
            ▼
 Business Recommendations
```

---

## Technology Stack

### Frontend

* Streamlit

### Data Processing

* Pandas
* NumPy

### Analytics & Forecasting

* Scikit-Learn

### Optimization

* RevPy
* EMSRb Revenue Management Algorithms
* Operations Research Concepts

### Visualization

* Plotly

---

## Project Structure

```text
SkyPrice-AI/
│
├── backend/
│   ├── demand_forecasting.py
│   └── revenue_optimizer.py
│
├── datasets/
│   ├── booking.csv
│   └── demand.csv
│
├── frontend/
│   └── app.py
│
├── notebooks/
│
├── revpy_core/
│
├── requirements.txt
└── README.md
```

---

## Revenue Management Methodology

The platform uses EMSRb (Expected Marginal Seat Revenue - version b), a widely recognized airline revenue management approach.

The algorithm determines:

* Seat protection levels
* Inventory controls
* Revenue-maximizing allocations

This enables airlines to reserve capacity for potentially higher-paying future passengers.

---

## Sample Business Insights

* Forecast demand for a selected route
* Identify high-performing fare classes
* Analyze revenue contribution by cabin category
* Optimize seat inventory allocation
* Improve expected flight revenue

---

## Potential Future Enhancements

* Dynamic Pricing Engine
* Fare Class Recommendation System
* Route Profitability Analysis
* Competitor Fare Monitoring
* Network Revenue Optimization
* XGBoost Demand Forecasting
* OR-Tools Optimization Models
* FastAPI Backend Services
* PostgreSQL Data Warehouse
* React Enterprise Dashboard

---

## Skills Demonstrated

* Business Analytics
* Airline Revenue Management
* Demand Forecasting
* Revenue Optimization
* Data Visualization
* Operations Research
* Decision Intelligence
* Python Development
* Data Science
* Travel Technology

---

## Author

Harsh Raj

B.Tech – SRM University AP

Interests:

* Business Analytics
* Airline Technology
* Revenue Management
* Data Science
* Optimization Systems

---

## License

This project is developed for educational, research, and portfolio purposes.
