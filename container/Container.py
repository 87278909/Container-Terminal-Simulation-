import simpy
import random
import argparse

# Constants
AVG_ARRIVAL_TIME = 5 * 60  # average time between vessel arrivals (in minutes)
NUM_CONTAINERS = 150
CRANE_TIME = 3  # time to move one container (in minutes)
TRUCK_TIME = 6  # time for truck to drop off container and return (in minutes)
NUM_BERTHS = 2
NUM_CRANES = 2
NUM_TRUCKS = 3

class ContainerTerminal:
    def __init__(self, env):
        self.env = env
        self.berths = simpy.Resource(env, NUM_BERTHS)
        self.cranes = simpy.Resource(env, NUM_CRANES)
        self.trucks = simpy.Resource(env, NUM_TRUCKS)

    def berth_vessel(self, vessel_id):
        with self.berths.request() as request:
            yield request
            print(f"Vessel {vessel_id} berthed at time {self.env.now}")  # Log berthing event
            yield self.env.process(self.discharge_containers(vessel_id))
            print(f"Vessel {vessel_id} leaves at time {self.env.now}")  # Log vessel leaving event

    def discharge_containers(self, vessel_id):
        for i in range(NUM_CONTAINERS):
            with self.cranes.request() as crane_request:
                yield crane_request
                print(f"Crane starts moving container {i+1} from vessel {vessel_id} at time {self.env.now}")  # Log crane event
                yield self.env.timeout(CRANE_TIME)
                with self.trucks.request() as truck_request:
                    yield truck_request
                    print(f"Truck starts transporting container {i+1} from vessel {vessel_id} at time {self.env.now}")  # Log truck start event
                    yield self.env.timeout(TRUCK_TIME)
                    print(f"Truck delivered container {i+1} from vessel {vessel_id} at time {self.env.now}")  # Log truck delivery event

def vessel_arrival(env, terminal):
    vessel_id = 0
    while True:
        yield env.timeout(random.expovariate(1.0 / AVG_ARRIVAL_TIME))
        vessel_id += 1
        print(f"Vessel {vessel_id} arrives at time {env.now}")  # Log vessel arrival event
        env.process(terminal.berth_vessel(vessel_id))

def main(simulation_time):
    # Main simulation setup
    env = simpy.Environment()
    terminal = ContainerTerminal(env)
    env.process(vessel_arrival(env, terminal))
    env.run(until=simulation_time)  # Run the simulation for the specified time

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simulate a container terminal.")
    parser.add_argument("simulation_time", type=int, help="Simulation time in minutes")
    args = parser.parse_args()

    main(args.simulation_time)
