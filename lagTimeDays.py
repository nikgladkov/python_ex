#lagTimeDays
# https://www.notion.so/Learning-Python-a2584d6b8f164d8e85e7c8fd5b32e27e
# lagTimeDays <= 5 - Quick Shipping Usually ships in 1 business day*
# lagTimeDays >5, <10 - Special Order Usually ships in 1-2 weeks*
# lagTimeDays null - Special Order Usually ships in 1-2 weeks*
# lagTimeDays > 10 Special Order Usually ships in 2-3 weeks*
# lagTimeDays > 20 Special Order Usually ships in 4-5 weeks*...
import math

def generateLabelText(lagTimeDays):

    oneDayLimit = 5
    workWeeksCount = math.floor(lagTimeDays/5)

    if lagTimeDays <= oneDayLimit:
        labeltxt = "Quick Shipping Usually ships in 1 business day*"
    else:
        labeltxt = "Special Order Usually ships in " + str(workWeeksCount) + "-" + str(workWeeksCount+1) + " weeks*"
    
    return labeltxt

print(generateLabelText(21))