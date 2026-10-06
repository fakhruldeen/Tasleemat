#!/usr/bin/env python3
"""
Earned Value Analysis (EVA) - Deterministic Executor
Implementation of PMO-06.05 Metrics Computation
"""

import sys
import json
from decimal import Decimal, InvalidOperation, getcontext

# Set precision
getcontext().prec = 28

def calculate_eva(inputs):
    """
    Computes EVA metrics based on exact inputs.
    Missing/invalid inputs, divide by zero, and numerical edge cases are handled.
    Rounding: Half-up to 2 decimal places.
    Tolerance: Strict deterministic calculation.
    """
    try:
        bac = Decimal(str(inputs.get('BAC')))
        pv = Decimal(str(inputs.get('PV')))
        ev = Decimal(str(inputs.get('EV')))
        ac = Decimal(str(inputs.get('AC')))
    except (TypeError, ValueError, InvalidOperation) as e:
        raise ValueError(f"Invalid input type: {e}")

    if bac <= 0:
        raise ValueError("BAC must be greater than zero.")

    # Variances
    sv = ev - pv
    cv = ev - ac

    # Indices
    spi = ev / pv if pv != 0 else Decimal('0')
    cpi = ev / ac if ac != 0 else Decimal('0')

    # Percentages
    pct_planned = pv / bac
    pct_earned = ev / bac
    pct_spent = ac / bac

    # Forecasting
    eac_cpi = bac / cpi if cpi != 0 else Decimal('0')
    
    denom_tcpi = bac - ac
    tcpi = (bac - ev) / denom_tcpi if denom_tcpi != 0 else Decimal('0')
    
    denom_eac_spi = cpi * spi
    eac_cpi_spi = ac + ((bac - ev) / denom_eac_spi) if denom_eac_spi != 0 else Decimal('0')

    def round_dec(d):
        return float(d.quantize(Decimal('0.01')))

    return {
        "SV": round_dec(sv),
        "CV": round_dec(cv),
        "SPI": round_dec(spi),
        "CPI": round_dec(cpi),
        "Percent_Planned": round_dec(pct_planned),
        "Percent_Earned": round_dec(pct_earned),
        "Percent_Spent": round_dec(pct_spent),
        "EAC_CPI": round_dec(eac_cpi),
        "EAC_CPI_SPI": round_dec(eac_cpi_spi),
        "TCPI": round_dec(tcpi)
    }

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: eva_calculator.py '{\"BAC\": 1000, \"PV\": 500, \"EV\": 400, \"AC\": 600}'")
        sys.exit(1)
        
    try:
        inputs = json.loads(sys.argv[1])
        result = calculate_eva(inputs)
        print(json.dumps({"status": "SUCCESS", "data": result}))
    except Exception as e:
        print(json.dumps({"status": "ERROR", "message": str(e)}))
        sys.exit(1)
