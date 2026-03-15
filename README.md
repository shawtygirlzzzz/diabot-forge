# DiaBot Analytics Forge 

**Track B: Quantitative Forge - Autonomous Data Swarm**

## The Mission
DiaBot Analytics Forge is an autonomous agent swarm designed to ingest, clean, and model messy medical datasets (specifically diabetes health indicators). By leveraging Python code execution, the swarm autonomously handles missing values, trains predictive models, and self-corrects if its generated scripts encounter errors.

## System Architecture Diagram (A2A Flow)
```text
[Raw Diabetes CSV] ---> (DataWrangler Agent)
                              |
                              |--> Writes Pandas cleanup script
                              |--> Executes script 
                              |--> [Error Detected?] -> Reads Traceback -> Rewrites Script
                              |
[Cleaned Data CSV] <----------|
                              |
                              V
                       (MLDiagnostic Agent)
                              |
                              |--> Writes Scikit-Learn training script (Random Forest)
                              |--> Executes script
                              |--> [Error Detected?] -> Reads Traceback -> Rewrites Script
                              |
[Model Metrics & Summary] <---|