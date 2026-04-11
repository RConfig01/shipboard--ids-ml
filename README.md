# Detection of Cyber Threats in Shipboard Networks Using Machine Learning

## Overview

This project investigates the use of machine learning techniques for detecting cyber threats in a simulated maritime operational technology (OT) network.

A virtual environment was developed to generate both normal and attack traffic, which was processed into flow-based features for intrusion detection.

---

## Features

* Simulated shipboard network environment (VMware)
* Flow-based feature extraction
* Binary and multiclass classification
* Random Forest and Support Vector Machine (SVM) models
* SMOTE for class imbalance handling
* Explainable AI using SHAP

---

## Attack Types

* Spoofed navigation message injection
* Irregular communication timing
* Flooding attack

---

## Results

* Random Forest achieved consistent performance across classification tasks
* Support Vector Machine improved with SMOTE balancing
* Flooding and timing-based attacks were detected effectively
* Spoofing attacks were more difficult to detect

---

## Explainability

SHAP (SHapley Additive exPlanations) was applied to analyse feature contributions to model predictions. The results confirm the importance of timing-based and traffic volume features in intrusion detection.

---

## Repository Structure

* `notebooks/` – Data processing, model training, and evaluation
* `scripts/` – Traffic generation scripts for normal and attack scenarios
* `results/figures/` – Generated plots and visualisations
* `results/tables/` – Model performance results

---

## Requirements

See `requirements.txt` for required Python packages.

---

## Author

Lloyd McGinty
