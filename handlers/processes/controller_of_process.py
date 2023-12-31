from multiprocessing import Process, RLock
from handlers.processes import process_of_parser
import time


class ControllerOfProcess:
    def __init__(self, links: [str], path: str = "/resources/data/result.xlsx"):
        self.links = links
        self.path = path
        self.lock = RLock()
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
        ic("the program has been launched")
        for completed_processes, link in enumerate(self.links):
            current_process = Process(target=process_of_parser, args=(link, self.path, self.lock))
            while not self.balancing(current_process):
                time.sleep(0.5)
            if completed_processes % 20 == 0:
                ic(completed_processes)
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
