# Detection of Cyber Threats in Shipboard Networks Using Machine Learning

## Overview

This project investigates the use of machine learning techniques for detecting cyber threats in a simulated maritime operational technology (OT) network.

A virtual environment was created to generate normal and attack traffic, which was processed into flow-based features for intrusion detection.

## Features

* Simulated shipboard network environment (VMware)
* Flow-based feature extraction
* Binary and multiclass classification
* Random Forest and Support Vector Machine models
* SMOTE for class imbalance handling
* Explainable AI using SHAP

## Attack Types

* Spoofed navigation messages
* Irregular communication timing
* Flooding attacks

## Results

* Random Forest achieved the most consistent performance
* SVM improved with SMOTE
* Flooding and timing attacks were detected effectively
* Spoofing attacks remained difficult to detect

## Explainability

SHAP analysis was applied to understand feature contributions, confirming the importance of timing and traffic volume features.

## Requirements

See `requirements.txt`

## Author

Lloyd McGitny


