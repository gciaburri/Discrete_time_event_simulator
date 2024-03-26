import random
import numpy as np

def randomIntA():
   numberA = [0] * 100
   for x in range(100):
    numberA[x] = random.randint(0, 99)
   print(*numberA, end =" ")
   return

def randomFloatB():
  numberB = [0] * 100
  for y in range(100):
    numberB[y] = random.uniform(0.25, 0.5)
  print(*numberB, end =" ")
  return


def randomNumC():
  numberC = [0] * 100
  for z in range(100):
    temp = random.uniform(0.0,1.0)
    if (temp <= 0.5):
      numberC[z] = 1
    elif (temp <= 0.7):
      numberC[z] = 2
    else:
      numberC[z] = random.uniform(3.0, 4.0)
  print(*numberC)
  return

def workloadGenerator(average_arrival_rate, t):
  processes = []
  cumulative_arrival_time = 0

  for process_id in range(50):
    randNumY = random.uniform(0.0, 1.0)
    interarrival_time = (-1 / average_arrival_rate) * np.log(1 - randNumY)
    cumulative_arrival_time += interarrival_time

    randNumZ = random.uniform(0.0, 1.0)
    service_time = -1 / t * np.log(1 - randNumZ)
    process = {"process_id": process_id, "arrival_time": cumulative_arrival_time, "service_time": service_time}
    processes.append(process)
  return processes

print(workloadGenerator(2, 0.04))