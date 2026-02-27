import pandas as pd
import numpy as np
from faker import Faker
import os
import random

fake = Faker('de_DE')
random.seed(42)

def generate_oracle_master():
    event_log_path = 'data/synthetic_servicenow_hrsd_events.csv'
    if not os.path.exists(event_log_path):
        print(f"Error: {event_log_path} not found. Run script 01 first.")
        return

    df_events = pd.read_csv(event_log_path)
    unique_employees = df_events['Employee_ID'].unique()
    
    job_roles = ["Specialist", "Senior Specialist", "Manager", "Senior Manager", "Director", "Lead"]
    locations = ["Berlin", "Munich", "Hamburg", "Essen", "Stuttgart", "Cologne"]
    nationalities = ["German", "Austrian", "Swiss", "French", "Polish", "Spanish"]
    genders = ["Male", "Female", "Non-binary"]
    
    master_data = []
    for emp_id in unique_employees:
        name = fake.name()
        role = random.choice(job_roles)
        loc = random.choice(locations)
        hire_date = fake.date_between(start_date='-10y', end_date='-1y')
        gender = random.choice(genders)
        nat = random.choice(nationalities)
        
        # Determine entity based on existing data if possible, or just random
        # For simplicity, we'll just pick one that matches the EVU/EIU style
        entity = random.choice(["EVU_Nord", "EVU_Sued", "EIU_West", "EIU_East"])
        
        master_data.append([
            emp_id, name, role, loc, hire_date, gender, nat, entity
        ])
        
    df_master = pd.DataFrame(master_data, columns=[
        "Employee_ID", "Employee_Name", "Job_Role", "Location", "Hire_Date", "Gender", "Nationality", "Home_Entity"
    ])
    
    output_path = 'data/synthetic_oracle_hcm_master.csv'
    df_master.to_csv(output_path, index=False)
    print(f"Generated {len(df_master)} employee master records at {output_path}")

if __name__ == "__main__":
    generate_oracle_master()
