import time
import app
import os
import testagenst

average = 0

for x in range(30):
    start = time.time()
    for fileName in os.listdir():
        if ".out.csv" in fileName and ".json" not in fileName:
            app.manualRun(fileName, 1)
    average += (time.time() - start)
print(average/30)


average = 0
for x in range(30):
    start = time.time()
    for fileName in os.listdir():
        if ".out.csv" in fileName and ".json" not in fileName:
            app.manualRun(fileName, 1)
    average += (time.time() - start)
print(average/30)
