import math
from mesa import Model
from mesa.datacollection import DataCollector
from mesa.discrete_space import OrthogonalVonNeumannGrid
from mesa.experimental.devs import ABMSimulator
from forest_biodiversity.agents import Tree, selected_species
import numpy as np

class ForestBiodiversity(Model):
    """Forest Biodiversity Model with grid-based spatial simulation."""
    description = "A model for simulating forest biodiversity with tree species."

    def __init__(
        self,
        width=20,
        height=20,
        initial_trees=200,
        seed=None,
        simulator: ABMSimulator = None,
        elevation_range=(0, 2000),
    ):
        super().__init__(seed=seed)
        self.simulator = simulator
        self.simulator.setup(self)
        self.height = height
        self.width = width
        self.elevation_range = elevation_range
        # Randomized elevation grid
        self.elevation_grid = np.random.uniform(
            elevation_range[0], elevation_range[1], size=(height, width)
        )
        self.grid = OrthogonalVonNeumannGrid(
            [self.height, self.width], torus=False, capacity=math.inf, random=self.random
        )
        self.datacollector = DataCollector({
            sp: lambda m, sp=sp: len(m.agents_by_type[Tree].select(lambda t: t.species == sp))
            for sp in selected_species
        })
        # Place initial trees
        for _ in range(initial_trees):
            sp = self.random.choice(selected_species)
            cell = self.random.choice(self.grid.all_cells.cells)
            Tree(self, sp, cell=cell)
        self.running = True
        self.datacollector.collect(self)

    def step(self):
        self.agents_by_type[Tree].shuffle_do("step")
        self.datacollector.collect(self)
