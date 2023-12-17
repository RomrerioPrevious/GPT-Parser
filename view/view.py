import time

from rich.console import Console
from rich.progress import Progress, track
from rich.layout import Layout
from rich.panel import Panel


class View:
    def __init__(self):
        self.console = Console()

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
