# azure-predictive-maintenance-robotics
# Predictive Maintenance for Robotics Order Fulfillment

**Azure IoT + Machine Learning Solution**  
**Author:** Jacob Davis  
**Date:** April 2026  
**Course:** Unit 6 AI Enhancement Project

## Overview

Hi, I'm Jacob Davis. For my Unit 6 assignment I built a complete predictive maintenance system for autonomous robots used in manufacturing and distribution warehouses. The robots handle order picking, packaging, and shipping — basically the backbone of a modern fulfillment center.

Instead of waiting for a motor or gripper to fail and shut down the line, this solution analyzes real-time sensor data (vibration, temperature, current draw, run hours, and error logs) to predict failures 4–8 hours in advance. It then triggers proactive actions like creating maintenance tickets and rerouting orders to healthy robots.

I chose Microsoft Azure because the services integrate really cleanly, and I wanted to show how AI can be added to an existing automation workflow without taking over the whole process. The AI piece (XGBoost model) is intentionally limited to about 35% of the decision logic — the rest stays rule-based for reliability and maintainability.

## Key Features

- Real-time IoT telemetry ingestion and processing
- Feature engineering on rolling sensor windows
- XGBoost multi-class failure prediction (No Failure / <4h / 4–8h)
- Hybrid rule-based + AI decision engine
- Automated maintenance tickets, order rerouting, and alerts via Logic Apps
- Simulation mode so you can test everything without real robots
- Infrastructure-as-code deployment with Bicep
- Full monitoring dashboard in Power BI + Azure Monitor

## Architecture

The data flows from robots → Azure IoT Hub → Stream Analytics → Data Lake → Databricks (feature engineering) → Azure Machine Learning (prediction) → Functions + Logic Apps (actions).

You can see the full diagram in the report PDF (Figure 1). The AI model is clearly highlighted so you can see exactly where the intelligent decision-making happens.

## Prerequisites

- Azure subscription (free tier works for testing)
- Azure CLI installed
- Python 3.9+
- GitHub account (obviously)

## Quick Start / Deployment

1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/azure-predictive-maintenance-robotics.git
   cd azure-predictive-maintenance-robotics
## Deploy the infrastructure
./deploy.sh

## Run the IoT simulator 
pip install azure-iot-device
python iot_simulator.py




   
