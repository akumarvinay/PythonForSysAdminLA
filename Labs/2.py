import math
import os
roundoff = int(os.getenv("DIGITS") or 10)
#print(round(math.pi,roundoff))
print(math.pi)
print(f"Valu of PI is {round(math.pi, roundoff)}")
#print("PI value is %.*f" % (roundoff, math.pi))
#digits = int(os.getenv("DIGITS") or 10)
#print("%.*f" % (digits, math.pi))
