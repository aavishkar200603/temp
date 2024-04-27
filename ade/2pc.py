import threading
import time

class Coordinator:
    def __init__(self):
        self.participants = []
        self.decision = None
        self.decision_lock = threading.Lock()

    def add_participant(self, participant):
        self.participants.append(participant)

    def start_transaction(self):
        # Phase 1: Ask participants to prepare
        self.decision = None
        threads = []
        for participant in self.participants:
            t = threading.Thread(target=participant.prepare, args=(self,))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        # Phase 2: Commit or abort based on prepare outcome
        if all(participant.vote == 'Yes' for participant in self.participants):
            self.decision = 'Commit'
        else:
            self.decision = 'Abort'

        # Inform participants of decision
        for participant in self.participants:
            participant.decide(self.decision)

    def get_decision(self):
        with self.decision_lock:
            return self.decision

class Participant:
    def __init__(self, name):
        self.name = name
        self.vote = None

    def prepare(self, coordinator):
        # Simulate preparation
        time.sleep(1)
        # Simulate voting
        self.vote = 'Yes' if self.name != 'P2' else 'No'
        print(f"{self.name} voted: {self.vote}\n")

    def decide(self, decision):
        print(f"{self.name} received decision: {decision}")

# Create coordinator and participants
coordinator = Coordinator()
p1 = Participant('P1')
p2 = Participant('P2')
p3 = Participant('P3')

# Register participants with coordinator
coordinator.add_participant(p1)
coordinator.add_participant(p2)
coordinator.add_participant(p3)

# Start the transaction
coordinator.start_transaction()

# Get the final decision
print("Final decision:", coordinator.get_decision())
