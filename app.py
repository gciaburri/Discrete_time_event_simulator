import heapq
import numpy as np
import random

event_queue = []
ready_queue = []
t = 0.04
lambda_ = 10

class event:
    def __init__(self, time, type, process_id):
        self.time = time
        self.type = type
        self.process_id = process_id

class state:
    def __init__(self):
        self.cpu_busy = 0
        self.clock = 0
    def get_event():
        return heapq.heappop(event_queue)

def handle_arrival(event):
    if (state.cpu_busy == 0):
        state.cpu_busy = 1
        service_time = random.expovariate(0.04)
        departure_time = clock + service_time
        heapq.heappush(event_queue, event(departure_time, 'DEP', event.process_id))
    else:
        ready_queue.append(event)

def handle_departure(event):
    if len(ready_queue) > 0:
        next_event = ready_queue.pop(0)
        randNumZ = random.uniform(0.0, 1.0)
        service_time = -1 / t * np.log(1 - randNumZ)
        departure_time = clock + service_time
        heapq.heappush(event_queue, event(departure_time, 'DEP', next_event.process_id))
    else:
        state.cpu_busy = 0

while len(event_queue) < 100:
    event = state.get_event()
    clock = event.time
    match (event.type):
        case 'ARR':
            handle_arrival(event)
        case 'DEP':
            handle_departure(event)
        case _:
            print('Invalid event type')
