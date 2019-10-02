#!/usr/bin/env python3.6
import os
#stage = os.environ["STAGE"].upper()
stage = os.getenv("STAGE", default="TEST").upper()
output = f"We are in {stage} right now"

if stage.startswith("PROD"):
    output = "DANGER...!" + output

print(output)
