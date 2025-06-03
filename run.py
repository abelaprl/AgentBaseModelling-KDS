from mesa.experimental.devs import ABMSimulator
from forest_biodiversity.model import ForestBiodiversity

def main():
    simulator = ABMSimulator()
    model = ForestBiodiversity(simulator=simulator)
    simulator.run(model)

if __name__ == "__main__":
    main()
