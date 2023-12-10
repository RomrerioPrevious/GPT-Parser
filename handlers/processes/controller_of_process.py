from multiprocessing import Process
from handlers.processes import ProcessOfParsers
import time


class ControllerOfProcess:
    def __init__(self, links: [str]):
        self.links = links
        self.processes = {
            "prc-1": Process(),
            "prc-2": Process(),
            "prc-3": Process(),
            "prc-4": Process(),
            "prc-5": Process(),
            "prc-6": Process(),
            "prc-7": Process(),
            "prc-8": Process()
        }

    def run(self):
        for link in self.links:
            process = Process(target=ProcessOfParsers(link).process())
            while not self.balancing(process):
                time.sleep(0.5)
        for process in self.processes:
            if not self.processes[process].is_alive():
                continue
            self.processes[process].join()

    def balancing(self, process: Process) -> bool:
        for i in self.processes:
            if self.processes[i].is_alive():
                continue
            self.processes[i] = process
            self.processes[i].run()
            return True
        return False
