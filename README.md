# DiaBot Analytics Forge 

**Track B: Quantitative Forge - Autonomous Data Swarm**

## The Mission
DiaBot Analytics Forge is an autonomous, self-healing data analytics swarm built with the **Agent Development Kit (ADK)** and powered by **Gemini 2.5 Flash**. 

Designed to tackle the messy reality of healthcare data, this system deploys a multi-agent swarm to handle the entire machine learning pipeline autonomously:
* **Agentic Agency & Recovery:** Agents write their own Python code, execute it in a secure environment, read their own traceback errors, and dynamically rewrite their code to recover from unexpected missing data.
* **DataWrangler Agent:** Ingests raw CSV files. Im using Pima Indian Diabetes dataset got it from kaggle and autonomously imputes or drops missing values using `pandas`.
* **MLDiagnostic Agent:** Takes the sanitized data and trains a Random Forest Classifier using `scikit-learn`, outputting real-time accuracy and classification reports.
* **Web Frontend:** A clean, interactive Streamlit UI that allows users to trigger the swarm and monitor the mission.

**Live Demo : https://diabot-forge-mh7qracs9vcgswyzes9aca.streamlit.app/ **

## System Architecture Diagram (A2A Flow)

```mermaid
flowchart TD
    %% Colors and Styles
    classDef agent fill:#2C3E50,stroke:#3498DB,stroke-width:3px,color:#fff
    classDef data fill:#27AE60,stroke:#fff,stroke-width:2px,color:#fff
    classDef action fill:#34495E,stroke:#fff,stroke-width:1px,color:#fff
    classDef error fill:#E74C3C,stroke:#fff,stroke-width:2px,color:#fff

    %% Phase 1: DataWrangler
    Raw[(Raw Diabetes CSV)]:::data --> Wrangler{DataWrangler Agent}:::agent
    Wrangler -->|Writes & Executes Pandas Script| Check1{Error Detected?}:::error
    Check1 -- Yes --> Fix1[Reads Traceback & Rewrites Code]:::action
    Fix1 --> Wrangler
    Check1 -- No --> Clean[(Cleaned Data CSV)]:::data

    %% Phase 2: MLDiagnostic
    Clean --> MLAgent{MLDiagnostic Agent}:::agent
    MLAgent -->|Writes & Executes scikit-learn Script| Check2{Error Detected?}:::error
    Check2 -- Yes --> Fix2[Reads Traceback & Rewrites Code]:::action
    Fix2 --> MLAgent
    Check2 -- No --> Output[/Model Metrics & Classification Report/]:::data
```


