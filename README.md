# Container Terminal Simulation with SimPy

## Project Overview

This project provides a simulation of a container terminal using the SimPy library. It models the process of vessels arriving at a terminal, unloading containers using quay cranes, and moving those containers to yard blocks with terminal trucks.

## Simulation Features

- **Vessel Arrivals**: Vessels arrive based on an exponential distribution with an average interval of 5 hours.
- **Containers**: Each vessel carries 150 containers, which need to be unloaded at the terminal.
- **Berths**: The terminal has 2 berths. If both are occupied, arriving vessels will have to wait until a berth becomes available.
- **Quay Cranes**: There are 2 quay cranes available. Each crane can handle containers from any berth, with each container taking 3 minutes to unload.
- **Trucks**: The terminal has 3 trucks to transport containers from the cranes to yard blocks. Each truck requires 6 minutes for a round trip.

## Logging

The simulation records and displays important events with timestamps, such as vessel arrivals, berthing, crane operations, and truck movements.

## Requirements

- Python 3.x
- SimPy library

## Setup Instructions

1. Clone or download the repository containing the simulation code.
2. Install the SimPy library if it is not already installed:

    ```sh
    pip install simpy
    ```

## Running the Simulation

1. Open the script file named `container_terminal_simulation.py`.
2. Modify the simulation parameters as needed.
3. Execute the script:

    ```sh
    python container.py
    ```

## License

This project is distributed under the MIT License. For more details, refer to the [LICENSE](LICENSE) file.
