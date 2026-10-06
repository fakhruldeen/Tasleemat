#!/usr/bin/env python3
import unittest
import sys
import os

# Add tools to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'tools', 'attested_computations')))

from eva_calculator import calculate_eva
from eva_attester import attest

class TestEVA(unittest.TestCase):
    def setUp(self):
        self.valid_inputs = {"BAC": 1000, "PV": 500, "EV": 400, "AC": 600}
        self.expected_outputs = {
            "SV": -100.0,
            "CV": -200.0,
            "SPI": 0.8,
            "CPI": 0.67,
            "Percent_Planned": 0.5,
            "Percent_Earned": 0.4,
            "Percent_Spent": 0.6,
            "EAC_CPI": 1500.0,
            "EAC_CPI_SPI": 1725.0, # 600 + ((1000 - 400) / (0.67 * 0.8)) -> 600 + 600 / 0.536 -> ~ 1719. Wait, precise math: 0.8 * 0.6666... = 0.5333... 600 / 0.5333... = 1125. 1125 + 600 = 1725. Exactly!
            "TCPI": 1.5
        }

    def test_positive_calculation(self):
        res = calculate_eva(self.valid_inputs)
        self.assertEqual(res["SV"], -100.0)
        self.assertEqual(res["EAC_CPI_SPI"], 1725.0)

    def test_positive_attestation(self):
        # The attester should pass
        res = attest(self.valid_inputs, self.expected_outputs)
        self.assertEqual(res["status"], "ATTESTED")

    def test_negative_mismatched_output(self):
        tampered_outputs = self.expected_outputs.copy()
        tampered_outputs["SPI"] = 0.9 # Hallucinated or manipulated
        res = attest(self.valid_inputs, tampered_outputs)
        self.assertEqual(res["status"], "FAIL")
        self.assertIn("SPI", res["mismatches"])

    def test_negative_divide_by_zero(self):
        # If PV and AC are 0
        inputs = {"BAC": 1000, "PV": 0, "EV": 0, "AC": 0}
        res = calculate_eva(inputs)
        # Should gracefully return 0.0 for indices
        self.assertEqual(res["SPI"], 0.0)
        self.assertEqual(res["CPI"], 0.0)

    def test_negative_invalid_input(self):
        inputs = {"BAC": "invalid", "PV": 500, "EV": 400, "AC": 600}
        with self.assertRaises(ValueError):
            calculate_eva(inputs)

if __name__ == '__main__':
    unittest.main()
