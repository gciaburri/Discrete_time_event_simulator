import heapq
import random
import argparse
import math

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Discrete Time Event Simulator"
    )
    parser.add_argument("--num1", required=True, type=int)
    parser.add_argument("--num2", required=True, type=int)
    args = parser.parse_args()

    num1 = args.num1
    num2 = args.num2

class Simulator:
    def __init__(self, num1, num2):
        self.clock = 0
        self.cpu_busy = 0
        self.completed_processes = 0
        self.lamda_ = num1    # Average arrival rate (processes per second)
        self.sTime = num2   # Average service time (processes per second)
    def generate_interarrival_time(self):
        randNumY = random.uniform(0.0, 1.0)
        return (-1 / self.lamda_) * math.log(1 - randNumY)
    
    def generate_service_time(self):
        randNumZ = random.uniform(0.0, 1.0)
        return -1 / self.sTime * math.log(1 - randNumZ)
    
    def handle_arrival(self, event):
        if (self.cpu_busy == 0):
            self.cpu_busy = 1

            departure_time = self.clock + self.generate_service_time()

            event_queue.schedule_event(Event(departure_time, 'DEP', event.process_id))
            print("Departure scheduled")
        else:
            ready_queue.add_event(event)
        event_queue.schedule_event(Event(self.clock + self.generate_interarrival_time(), 'ARR', event.process_id + 1))
        print("Arrival scheduled at", self.clock)


    def handle_departure(self, event):
        if len(ready_queue.ready_queue) > 0:
            next_event = ready_queue.get_event()
            departure_time = self.clock + self.generate_service_time()

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
s = Simulator(num1, num2)


event_queue.schedule_event(Event(0, 'ARR', 0))
while s.completed_processes < 1000:
    print("CPU busy:", s.cpu_busy)
    current_event = event_queue.get_event() 
    s.clock = current_event.time
    if current_event.type == 'ARR':
        s.handle_arrival(current_event)
    elif current_event.type == 'DEP':
        s.handle_departure(current_event)
        s.completed_processes += 1
        print('Process', current_event.process_id, 'completed at', s.clock)
    else:
        print('Invalid event type')
