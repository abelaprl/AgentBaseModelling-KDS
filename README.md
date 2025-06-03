# Forest Biodiversity Simulation

This project simulates a forest ecosystem using agent-based modeling with the Mesa framework. It features a grid-based environment, five randomized tree species from GBIF data, and allows for parameterization by elevation, growth rate, and reproduction rate. The simulation includes basic statistical analysis and visualization, and a Solara-based GUI frontend.

## How to Run

Create python virtual environment:
```bash
python -m venv venv
```

Activate virtual environment:
```bash
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

Update pip to latest version:
```bash
python -m pip install --upgrade pip
```

Install requirements:
```bash
pip install -r requirements.txt
```

Run the interactive model:
```bash
solara run app.py
```

## Files

* `forest_biodiversity/agents.py`: Defines the Tree agent class and species logic.
* `forest_biodiversity/model.py`: Defines the ForestBiodiversity model.
* `forest_biodiversity/server.py`: Sets up the interactive visualization server.
* `forest_biodiversity/statistics.py`: Basic statistical analysis with pandas and numpy.
* `run.py`: Launches a model visualization server.
* `GBIF_Data.csv`: Reference data for tree species.

## Data

The simulation uses GBIF_Data.csv to randomize five tree species and their characteristics.

## Architecture

This project follows the architecture of the Wolf-Sheep Predation Model (see `wolf_sheep.md.txt`).
