import pandas as pd
import os

def harmonize_and_clean():
    events_path = 'data/synthetic_servicenow_hrsd_events.csv'
    master_path = 'data/synthetic_oracle_hcm_master.csv'
    
    if not os.path.exists(events_path) or not os.path.exists(master_path):
        print("Error: Required data files missing. Run script 01 and 02 first.")
        return
        
    df_events = pd.read_csv(events_path)
    df_master = pd.read_csv(master_path)
    
    # 1. Join Events and Master Data on Employee_ID
    # We use a left join to keep all events even if master data is missing (though it shouldn't be in this case)
    df_harmonized = pd.merge(df_events, df_master, on="Employee_ID", how="left")
    
    # 2. Date/Time Cleaning
    df_harmonized['Timestamp'] = pd.to_datetime(df_harmonized['Timestamp'])
    df_harmonized['Hire_Date'] = pd.to_datetime(df_harmonized['Hire_Date'])
    
    # 3. Handle Nulls
    # Fill any potential nulls with "Unknown" or relevant defaults
    df_harmonized['Job_Role'] = df_harmonized['Job_Role'].fillna('Unknown')
    df_harmonized['Employee_Name'] = df_harmonized['Employee_Name'].fillna('Unknown')
    
    # 4. Final Sorting
    df_harmonized = df_harmonized.sort_values(by=["Case ID", "Timestamp"])
    
    # 5. Output
    output_path = 'data/harmonized_eventlog.csv'
    df_harmonized.to_csv(output_path, index=False)
    print(f"Harmonized event log created at {output_path} with {len(df_harmonized)} events.")

if __name__ == "__main__":
    harmonize_and_clean()
