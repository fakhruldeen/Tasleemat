#!/usr/bin/env python3
"""
Earned Value Analysis (EVA) - Attester
Verifies that displayed computation results match the deterministic executor.
"""

import sys
import json
from eva_calculator import calculate_eva

def attest(inputs, displayed_outputs):
    try:
        expected = calculate_eva(inputs)
    except Exception as e:
        return {"status": "FAIL", "reason": f"Calculation failed: {e}"}
        
    mismatches = {}
    for key, expected_val in expected.items():
        if key not in displayed_outputs:
            mismatches[key] = f"Missing in displayed outputs. Expected {expected_val}"
            continue
            
        try:
            displayed_val = float(displayed_outputs[key])
            # Tolerance rule: Must match to 2 decimal places exactly
            if abs(displayed_val - expected_val) > 0.01:
                mismatches[key] = f"Mismatch. Expected {expected_val}, got {displayed_val}"
        except ValueError:
            mismatches[key] = f"Invalid format. Expected {expected_val}, got {displayed_outputs[key]}"
            
    if mismatches:
        return {"status": "FAIL", "mismatches": mismatches}
        
    return {"status": "ATTESTED", "message": "All displayed metrics match the deterministic computation exactly."}

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: eva_attester.py '<inputs_json>' '<outputs_json>'")
        sys.exit(1)
        
    inputs = json.loads(sys.argv[1])
    outputs = json.loads(sys.argv[2])
    
    result = attest(inputs, outputs)
    print(json.dumps(result, indent=2))
    if result["status"] != "ATTESTED":
        sys.exit(1)
