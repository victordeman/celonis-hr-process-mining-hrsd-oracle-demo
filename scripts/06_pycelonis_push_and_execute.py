import os
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

# We try to import pycelonis. If it's not installed, we'll mock it.
try:
    from pycelonis import get_celonis
    PYCELONIS_INSTALLED = True
except ImportError:
    PYCELONIS_INSTALLED = False

def push_to_celonis():
    celonis_url = os.getenv('CELONIS_URL')
    api_token = os.getenv('CELONIS_API_TOKEN')
    
    file_to_push = 'data/harmonized_eventlog.csv'
    
    if not os.path.exists(file_to_push):
        print(f"Error: {file_to_push} not found. Run script 03 first.")
        return

    # Check if we have credentials
    if not celonis_url or not api_token or 'YOUR_TEAM_ID' in celonis_url:
        print("MOCK: Celonis EMS credentials not configured in .env. Simulating push...")
        print(f"MOCK: Would push {file_to_push} to {celonis_url}")
        return

    if not PYCELONIS_INSTALLED:
        print("PyCelonis is not installed. Skipping actual push to EMS.")
        print("Please install with: pip install pycelonis")
        return

    try:
        c = get_celonis(url=celonis_url, api_token=api_token)
        print(f"Connected to Celonis team: {c.team.name}")
        
        # 1. Find or create a Data Pool
        pool_name = "HR Process Mining Demo - Mund Consulting ID02400"
        try:
            pool = c.data_integration.get_data_pools().find(pool_name)
            print(f"Found existing Data Pool: {pool.name}")
        except:
            pool = c.data_integration.create_data_pool(pool_name)
            print(f"Created new Data Pool: {pool.name}")
            
        # 2. Upload Dataframe
        df = pd.read_csv(file_to_push)
        print(f"Uploading {len(df)} records to Celonis...")
        table_name = "HRSD_ORACLE_HARMONIZED_LOG"
        
        # In PyCelonis 2.x style:
        pool.create_table(df, table_name=table_name, if_exists='replace')
        print(f"Table {table_name} uploaded successfully!")
        
        # 3. Trigger Data Model Reload (Example)
        # model = pool.get_data_models().find("HR Process Mining Model")
        # model.reload()
        # print("Data model reload triggered.")
        
    except Exception as e:
        print(f"Error connecting to Celonis EMS: {e}")

if __name__ == "__main__":
    push_to_celonis()
