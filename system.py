import random

from future_events_queue import FutureEventsQueue
from clock import Clock
from stats import Stats

class System(object):
    def reset(self, seed=None):
        self.feq = FutureEventsQueue()
        self.clock = Clock()
        self.stats = Stats()
        if seed is not None:
            random.seed(seed)
        self.initialize()
        
    def run(self, seed=None):
        self.reset(seed)
        event = self.generate_initial_event()
        self.feq.schedule_event(event)
        while self.feq.has_events():
            event = self.feq.next_event()
            self.clock.update(event.time)
            self.simulate(event)
        return self.stats
        
    def initialize(self):
        """ System-specific variables are initialized here """
        pass
        
    def generate_initial_event(self):
        """ Returns the initial event in the simulation """
        pass
        
    def simulate(self, event):
        """ Updating of system state and stats, and scheduling of next event
            should go here """
        pass
