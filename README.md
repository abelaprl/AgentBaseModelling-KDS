# AgentBaseModelling-KDS

# Forest Biodiversity Simulation

This project simulates a forest ecosystem using agent-based modeling with the Mesa framework. It features a grid-based environment, five randomized tree species from GBIF data, and allows for parameterization by elevation, growth rate, and reproduction rate. The simulation includes basic statistical analysis and visualization, and a Solara-based GUI frontend.

## How to Run

To run the model interactively, in this directory, run:

```
$ solara run app.py
```

## Files

* `forest_biodiversity/agents.py`: Defines the Tree agent class and species logic.
* `forest_biodiversity/model.py`: Defines the ForestBiodiversity model.
* `forest_biodiversity/server.py`: Sets up the interactive visualization server.
* `forest_biodiversity/statistics.py`: Basic statistical analysis with pandas and numpy.
* `run.py`: Launches a model visualization server.
* `GBIF_Data.csv`: Reference data for tree species.

## Data

The simulation uses `GBIF_Data.csv` to randomize five tree species and their characteristics.