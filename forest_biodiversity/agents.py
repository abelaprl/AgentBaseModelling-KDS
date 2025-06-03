import pandas as pd
import numpy as np
from mesa.discrete_space import CellAgent

# Load GBIF data and select 5 random species
GBIF_CSV = "GBIF_Data.csv"
df = pd.read_csv(GBIF_CSV, sep='\t')
species_list = df['species'].dropna().unique()
selected_species = np.random.choice(species_list, 5, replace=False)
species_data = df[df['species'].isin(selected_species)]

# Assign random growth and reproduction rates for demonstration
np.random.seed(42)
species_traits = {}
for sp in selected_species:
    elevs = species_data[species_data['species'] == sp]['elevation'].dropna()
    mean_elev = elevs.mean() if not elevs.empty else np.random.uniform(0, 1000)
    species_traits[sp] = {
        'growth_rate': np.random.uniform(0.01, 0.1),
        'reproduction_rate': np.random.uniform(0.01, 0.1),
        'elevation': mean_elev
    }

class Tree(CellAgent):
    """A tree agent with species-specific traits."""
    def __init__(self, model, species, cell=None):
        super().__init__(model)
        self.species = species
        self.growth_rate = species_traits[species]['growth_rate']
        self.reproduction_rate = species_traits[species]['reproduction_rate']
        self.elevation = species_traits[species]['elevation']
        self.size = 1.0  # Initial size
        self.cell = cell

    def step(self):
        # Grow
        self.size += self.growth_rate
        # Reproduce with probability
        if self.model.random.random() < self.reproduction_rate:
            self.spawn_offspring()

    def spawn_offspring(self):
        # Place offspring in a random neighboring cell
        neighbors = self.cell.neighborhood
        target_cell = neighbors.select_random_cell()
        Tree(self.model, self.species, cell=target_cell)
