from mesa.experimental.devs import ABMSimulator
from mesa.visualization import (
    CommandConsole,
    Slider,
    SolaraViz,
    make_plot_component,
    make_space_component,
)
from forest_biodiversity.model import ForestBiodiversity
from forest_biodiversity.agents import Tree, selected_species
import solara
import time
from forest_biodiversity.data_analysis import compute_shannon_index

def tree_portrayal(agent):
    if agent is None:
        return
    color_map = ["tab:green", "tab:olive", "tab:orange", "tab:brown", "tab:blue"]
    idx = list(selected_species).index(agent.species)
    return {
        "size": 20 + agent.size * 2,
        "color": color_map[idx],
        "marker": "o",
        "zorder": 2,
    }


model_params = {
    "seed": {
        "type": "InputText",
        "value": 42,
        "label": "Random Seed",
    },
    "initial_trees": Slider("Initial Tree Population", 200, 10, 500),
    "width": Slider("Grid Width", 20, 5, 50),
    "height": Slider("Grid Height", 20, 5, 50),
}


def post_process_space(ax):
    ax.set_aspect("equal")
    ax.set_xticks([])
    ax.set_yticks([])


def post_process_lines(ax):
    ax.legend(loc="center left", bbox_to_anchor=(1, 0.9))


space_component = make_space_component(
    tree_portrayal, draw_grid=False, post_process=post_process_space
)
lineplot_component = make_plot_component(
    {sp: color for sp, color in zip(selected_species, ["tab:green", "tab:olive", "tab:orange", "tab:brown", "tab:blue"])},
    post_process=post_process_lines,
)


simulator = ABMSimulator()
model = ForestBiodiversity(simulator=simulator)

@solara.component
def ShannonIndexIndicator(model):
    import solara
    shannon, set_shannon = solara.use_state(compute_shannon_index(model))

    def recalc():
        set_shannon(compute_shannon_index(model))

    solara.Text(f"Shannon Diversity Index: {shannon:.3f}", style={"fontWeight": "bold", "fontSize": "1.2em", "color": "black"})
    solara.Button(label="Recalculate Shannon Index", on_click=recalc, style={"marginTop": "0.5em"})


page = SolaraViz(
    model,
    components=[space_component, lineplot_component, CommandConsole, ShannonIndexIndicator],
    model_params=model_params,
    name="Forest Biodiversity",
    simulator=simulator,
)
page  # noqa
