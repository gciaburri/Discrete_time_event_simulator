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
            service_time = 1 #-1 / 0.04 * np.log(1 - randNumX)
            departure_time = self.clock + service_time

            event_queue.schedule_event(Event(departure_time, 'DEP', event.process_id))
            print("Departure scheduled")
        else:
            ready_queue.add_event(event)
        event_queue.schedule_event(Event(self.clock + 1, 'ARR', event.process_id + 1))
        print("Arrival scheduled")


    def handle_departure(self, event):
        if len(ready_queue.ready_queue) > 0:
            next_event = ready_queue.get_event()

            randNumZ = random.uniform(0.0, 1.0)
            service_time = 1 #-1 / 2 * np.log(1 - randNumZ)
            departure_time = self.clock + service_time

            event_queue.schedule_event(Event(departure_time, 'DEP', next_event.process_id))
        else:
            self.cpu_busy = 0

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
        def get_event(self):
            if self.event_queue:  # Ensure the queue is not empty
                return heapq.heappop(self.event_queue)
            else:
                return None  # Or handle the empty queue case appropriately
        def schedule_event(self, event):
            heapq.heappush(self.event_queue, event)
        
class Event:
        def __init__(self, time, type, process_id):
            self.time = time
            self.type = type
            self.process_id = process_id
        def __lt__(self, other):
            return self.time < other.time

ready_queue = ReadyQueue()
event_queue = EventQueue()
s = Simulator()


while s.completed_processes < 3:
    print("CPU busy:", s.cpu_busy)
    current_event = event_queue.get_event() 
    s.clock = current_event.time
    match (current_event.type):
        case 'ARR':
            s.handle_arrival(current_event)
        case 'DEP':
            s.handle_departure(current_event)
            s.completed_processes += 1
            print('Process', current_event.process_id, 'completed at', s.clock)
        case _:
            print('Invalid event type')
