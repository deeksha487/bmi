# Simple BMI Calculator using arguments

import sys

# Take weight and height from command line arguments
weight = float(sys.argv[1])
height = float(sys.argv[2])

if height > 0:
    bmi = weight / (height * height)
    print("Your BMI is:", bmi)
else:
    print("Height must be greater than 0")
