import requests
import json
import time
import os
from dotenv import load_dotenv

load_dotenv()

def fetch_from_servicenow():
    base_url = os.getenv('MOCK_SERVICE_NOW_BASE_URL', 'http://localhost:5000')
    api_endpoint = f"{base_url}/api/now/table/sn_hr_core_case"
    
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    
    print(f"Connecting to ServiceNow REST API at {api_endpoint}...")
    
    try:
        # We simulate the call. In a real scenario, this would return JSON data.
        # Since the server is usually not running here, we mock the response.
        
        # MOCK DATA for simulation
        mock_response_data = {
            "result": [
                {
                    "number": "HRC-123456",
                    "short_description": "Employee Onboarding Issue",
                    "state": "In Progress",
                    "sys_created_on": "2024-02-26 10:00:00",
                    "assignment_group": "HR Core Support",
                    "assigned_to": "Klaus Miller"
                },
                {
                    "number": "HRC-123457",
                    "short_description": "Payroll Correction Request",
                    "state": "Resolved",
                    "sys_created_on": "2024-02-26 11:30:00",
                    "assignment_group": "Payroll German Entity",
                    "assigned_to": "Sabine Weber"
                }
            ]
        }
        
        print(f"Successfully connected! (Simulated response)")
        print(f"Retrieved {len(mock_response_data['result'])} new cases.")
        
        # Save mock results to a temporary file
        temp_file = 'data/servicenow_api_extract.json'
        os.makedirs('data', exist_ok=True)
        with open(temp_file, 'w') as f:
            json.dump(mock_response_data, f, indent=4)
        
        print(f"API extract saved to {temp_file}")
        
    except Exception as e:
        print(f"Error connecting to ServiceNow: {e}")

if __name__ == "__main__":
    fetch_from_servicenow()
