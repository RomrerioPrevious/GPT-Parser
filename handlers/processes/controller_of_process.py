from multiprocessing import Process
from handlers.processes import ProcessOfParsers, process_of_parser
import time


class ControllerOfProcess:
    def __init__(self, links: [str]):
        self.links = links
        self.processes = {
            "prc-1": Process(), "prc-9": Process(),
            "prc-2": Process(), "prc-10": Process(),
            "prc-3": Process(), "prc-11": Process(),
            "prc-4": Process(), "prc-12": Process(),
            "prc-5": Process(), "prc-13": Process(),
            "prc-6": Process(), "prc-14": Process(),
            "prc-7": Process(), "prc-15": Process(),
            "prc-8": Process(), "prc-16": Process()
        }

    def run(self):
        for link in self.links:
            current_process = Process(target=process_of_parser, args=(link, ))
            while not self.balancing(current_process):
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
            process.start()
            return True
        return False
