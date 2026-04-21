#!/bin/bash
# deploy.sh - Infrastructure-as-code deployment for Jacob Davis's predictive maintenance project
az deployment group create \
  --resource-group jacob-davis-robotics-rg \
  --template-file main.bicep \
  --parameters @parameters.json
