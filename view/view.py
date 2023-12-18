from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
import json


class View:
    def __init__(self):
        self.console = Console()

    def config(self):
        while True:
            command = self.console.input("Write [red]command[/]: ")
            command = command.split()
            match command[0]:
                case "start":
                    break
                case "edit":
                    with open("settings.json") as file:
                        parameters = json.load(file)
                    if command[1] in parameters.keys():
                        parameters[command[1]] = command[2]
                        with open("settings.json", "w") as file:
                            json.dump(parameters, file)
                case "back":
                    raise KeyboardInterrupt()

    def print_description(self):
        layout = Layout()
        commands = ["1. start", "2. edit", "3. back"]
        parameters = ["1. api", "2. site_list_path"]
        height = max(len(commands) + 2, len(parameters) + 2)
        layout.split_row(
            Layout(Panel("\n".join(commands), title="commands", height=height), name="commands"),
            Layout(Panel("\n".join(parameters), title="parameters", height=height), name="parameters"),
        )
        self.console.print(layout, height=height)
