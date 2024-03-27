import heapq
import numpy as np
import random

class Simulator:
    def __init__(self):
        self.clock = 0
        self.cpu_busy = 0
        self.completed_processes = 0
        self.lamda_ = 2
        self.sTime = 0.04
        
    def handle_arrival(self, event):
        if (self.cpu_busy == 0):
            self.cpu_busy = 1
            randNumX = random.uniform(0.0, 1.0)
            service_time = -1 / 0.04 * np.log(1 - randNumX)
            departure_time = self.clock + service_time
            heapq.heappush(event_queue, event(departure_time, 'DEP', event.process_id))
        else:
            ready_queue.append(event)

    def handle_departure(self, event):
        if len(ready_queue) > 0:
            next_event = ready_queue.pop(0)
            randNumZ = random.uniform(0.0, 1.0)
            service_time = -1 / 2 * np.log(1 - randNumZ)
            departure_time = self.clock + service_time
            heapq.heappush(self.event_queue, event(departure_time, 'DEP', next_event.process_id))
        else:
            Simulator.cpu_busy = 0

class ReadyQueue:
        def __init__(self):
            self.ready_queue = []
        def add_event(self, event):
            self.ready_queue.append(event)
        def get_event(self):
            return self.ready_queue.pop(0)

class EventQueue:
        def __init__(self):
            self.event_queue = []
        def add_event(self, event):
            heapq.heappush(self.event_queue, event)
        def get_event(self):
            return heapq.heappop(self.event_queue)
        
class Event:
        def __init__(self, time, type, process_id):
            self.time = time
            self.type = type
            self.process_id = process_id

ready_queue = ReadyQueue()
event_queue = EventQueue()
s = Simulator()

while s.completed_processes < 3:
    current_event = event_queue.get_event() 
    s.clock = current_event.time
    match (current_event.type):
        case 'ARR':
            s.handle_arrival(current_event)
        case 'DEP':
            s.handle_departure(current_event)
        case _:
            print('Invalid event type')
