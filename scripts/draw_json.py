import json
import sys
from graphviz import Digraph


def draw_json(filename):
    # Load the JSON data
    with open(filename) as f:
        data = json.load(f)

    # Create a new directed graph
    dot = Digraph()

    # Add the states to the graph
    for state in data["states"]:
        dot.node(str(state["id"]), color="black")

    # Add the transitions to the graph
    for transition in data["transitions"]:
        label = "Pos: " + ", ".join(transition["conditions"]["pos"])
        if transition["conditions"]["neg"]:
            label += "\nNeg: " + ", ".join(transition["conditions"]["neg"])
        dot.edge(
            str(transition["from"]), str(transition["to"]), label=label, color="red"
        )

    # Save the graph to a dot file
    dot.save("buchi.dot")


def main():
    # Check if a file name was provided
    if len(sys.argv) < 2:
        print("Usage: python script.py <filename>")
        sys.exit(1)


if __name__ == "__main__":
    main()
