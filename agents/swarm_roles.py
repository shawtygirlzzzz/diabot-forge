from agents.base_agent import ADKBaseAgent

def create_data_wrangler():
    prompt = """
    You are the DataWrangler Agent, a senior data engineer. Your job is to process raw medical CSV data using 'pandas'.
    Assume the input file is 'data/raw_diabetes_data.csv'.
    You must dynamically find and handle missing values (e.g., fill with median or drop).
    Save the cleaned output exactly as 'data/clean_diabetes_data.csv'.
    """
    return ADKBaseAgent(name="DataWrangler", role_prompt=prompt, model_name="gemini-2.5-flash")

def create_ml_diagnostic():
    prompt = """
    You are the MLDiagnostic Agent, a senior machine learning engineer. Your job is to train predictive models using 'scikit-learn'.
    Load the data from 'data/clean_diabetes_data.csv'.
    Assume the target variable column is the last column in the dataset.
    Train a Random Forest Classifier.
    Print out the accuracy score and a brief classification report.
    """
    return ADKBaseAgent(name="MLDiagnostic", role_prompt=prompt, model_name="gemini-2.5-flash")