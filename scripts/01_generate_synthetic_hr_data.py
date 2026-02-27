import pandas as pd
import numpy as np
from faker import Faker
import datetime
import random
import os

# Initialize Faker and seed for reproducibility
fake = Faker('de_DE')
random.seed(42)
np.random.seed(42)

def generate_hr_data(num_cases=10000):
    activities = [
        "Create HR Case",
        "Assign to Team",
        "Manager Approval",
        "HR Review",
        "Rework Loop",
        "Resolve",
        "Close"
    ]
    
    departments = ["HR Core", "Payroll", "Talent Acquisition", "Benefits", "Employee Relations"]
    entities = ["EVU_Nord", "EVU_Sued", "EIU_West", "EIU_East"]
    priorities = ["Low", "Medium", "High", "Critical"]
    resources = [fake.name() for _ in range(20)]
    
    data = []
    
    start_date = datetime.datetime(2020, 1, 1)
    
    for i in range(num_cases):
        case_id = f"HRC-{1000000 + i}"
        # Associate case with a specific employee ID
        emp_id = f"EMP-{random.randint(200000, 299999)}"
        dept = random.choice(departments)
        entity = random.choice(entities)
        priority = random.choices(priorities, weights=[40, 40, 15, 5])[0]
        entity_type = "EVU" if "EVU" in entity else "EIU"
        
        # Start time for the case
        current_time = start_date + datetime.timedelta(
            days=random.randint(0, 1800),
            hours=random.randint(0, 23),
            minutes=random.randint(0, 59)
        )
        
        # 1. Create HR Case
        data.append([case_id, emp_id, "Create HR Case", current_time, random.choice(resources), dept, entity, entity_type, priority, "In Progress"])
        
        # 2. Assign to Team (usually shortly after)
        current_time += datetime.timedelta(minutes=random.randint(5, 120))
        data.append([case_id, emp_id, "Assign to Team", current_time, random.choice(resources), dept, entity, entity_type, priority, "In Progress"])
        
        # 3. Manager Approval (random delay)
        if random.random() > 0.1: # 90% need approval
            current_time += datetime.timedelta(hours=random.randint(1, 72))
            data.append([case_id, emp_id, "Manager Approval", current_time, "System / Manager", dept, entity, entity_type, priority, "In Progress"])
        
        # 4. HR Review
        current_time += datetime.timedelta(hours=random.randint(2, 48))
        data.append([case_id, emp_id, "HR Review", current_time, random.choice(resources), dept, entity, entity_type, priority, "In Progress"])
        
        # 5. Rework Loop (Simulation of Mund Consulting project insight: rework often happens)
        rework_count = 0
        while random.random() < 0.15 and rework_count < 3: # 15% chance of rework
            current_time += datetime.timedelta(hours=random.randint(4, 24))
            data.append([case_id, emp_id, "Rework Loop", current_time, random.choice(resources), dept, entity, entity_type, priority, "In Progress"])
            rework_count += 1
            # After rework, usually another HR Review
            current_time += datetime.timedelta(hours=random.randint(2, 12))
            data.append([case_id, emp_id, "HR Review", current_time, random.choice(resources), dept, entity, entity_type, priority, "In Progress"])

        # 6. Resolve
        current_time += datetime.timedelta(hours=random.randint(1, 24))
        sla_status = "SLA Breached" if random.random() < 0.12 else "SLA Compliant"
        data.append([case_id, emp_id, "Resolve", current_time, random.choice(resources), dept, entity, entity_type, priority, sla_status])
        
        # 7. Close
        current_time += datetime.timedelta(days=random.randint(1, 5))
        data.append([case_id, emp_id, "Close", current_time, "System", dept, entity, entity_type, priority, sla_status])

    df = pd.DataFrame(data, columns=[
        "Case ID", "Employee_ID", "Activity", "Timestamp", "Resource", "Department", "Entity", "Entity_Type", "Priority", "SLA_Status"
    ])
    
    # Sort by Case ID and Timestamp to ensure logical process flow
    df = df.sort_values(by=["Case ID", "Timestamp"])
    
    os.makedirs('data', exist_ok=True)
    output_path = 'data/synthetic_servicenow_hrsd_events.csv'
    df.to_csv(output_path, index=False)
    print(f"Generated {len(df)} events for {num_cases} cases at {output_path}")

if __name__ == "__main__":
    generate_hr_data(10000)
