import heapq
import random
import argparse
import math

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Discrete Time Event Simulator"
    )
    parser.add_argument("--num1", required=True, type=int)
    args = parser.parse_args()

    num1 = args.num1

class Simulator:
    def __init__(self, num1):
        self.clock = 0
        self.cpu_busy = 0
        self.completed_processes = 0
        self.total_turnaround_time = 0
        self.lamda_ = num1    # Average arrival rate (processes per second)
        self.sTime = 25    # Average service rate (processes per second)
        self.cpu_busy_start_time = 0  # Time when CPU last became busy
        self.total_cpu_busy_time = 0  # Cumulative CPU busy time
    def generate_interarrival_time(self):
        randNumY = random.uniform(0.0, 1.0)
        return (-1 / self.lamda_) * math.log(1 - randNumY)
    
    def generate_service_time(self):
        randNumZ = random.uniform(0.0, 1.0)
        return -1 / self.sTime * math.log(1 - randNumZ)
    
    def handle_arrival(self, event):
        arrival_time = self.clock
#        print( "Process", event.process_id, "arrived at", arrival_time)
        if (self.cpu_busy == 0):
            self.cpu_busy = 1
            self.cpu_busy_start_time = self.clock
            service_time = self.generate_service_time()
            start_time = self.clock
#            print( "Process", event.process_id, "started at", start_time)

            departure_time = self.clock + service_time
            

            event_queue.schedule_event(Event(departure_time, 'DEP', event.process_id))
#            print("Departure scheduled")
        else:
            ready_queue.add_event(event)
        event_queue.schedule_event(Event(self.clock + self.generate_interarrival_time(), 'ARR', event.process_id + 1))


    def handle_departure(self, event):
        if len(ready_queue.ready_queue) > 0:
            next_event = ready_queue.get_event()
            departure_time = self.clock + self.generate_service_time()
            event_queue.schedule_event(Event(departure_time, 'DEP', next_event.process_id))
        else:
            self.cpu_busy = 0
            busy_period = self.clock - self.cpu_busy_start_time  
            self.total_cpu_busy_time += busy_period 
#        print( "Process", event.process_id, "completed at", event.time)


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
            self.arrival_time = 0
        def __lt__(self, other):
            return self.time < other.time

ready_queue = ReadyQueue()
event_queue = EventQueue()
s = Simulator(num1)

arrival_times = {}
event_changes = 0
processes_in_rq = 0

event_queue.schedule_event(Event(0, 'ARR', 1))
while s.completed_processes < 10000:
#    print("CPU busy:", s.cpu_busy)
    current_event = event_queue.get_event() 
    s.clock = current_event.time
    if current_event.type == 'ARR':
        s.handle_arrival(current_event)
        arrival_times[current_event.process_id] = s.clock
    elif current_event.type == 'DEP':
        if current_event.process_id in arrival_times:
            original_arrival_time = arrival_times[current_event.process_id]
            completion_time = s.clock
            turnaround_time = completion_time - original_arrival_time
            s.total_turnaround_time += turnaround_time
        else:
            print("Error: Arrival time not found for process", current_event.process_id)
        s.handle_departure(current_event)
        s.completed_processes += 1
    else:
        print('Invalid event type')
    processes_in_rq += len(ready_queue.ready_queue)
    event_changes += 1
if s.cpu_busy == 1:
    busy_period = s.clock - s.cpu_busy_start_time
    s.total_cpu_busy_time += busy_period
final_time = s.clock
avg_processes_in_rq = processes_in_rq / event_changes

print("CPU Utilization: ", s.total_cpu_busy_time / final_time * 100, "%")
print("Average Throughput:", s.completed_processes / final_time, "processes per second")
print("Average Turnaround time:", s.total_turnaround_time / s.completed_processes, " seconds")
print("Average number of processes in ready queue:", avg_processes_in_rq)