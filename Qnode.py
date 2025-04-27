import random
import uuid

class QNode:
    """
    Represents a single Quantum Node within the QAI Cluster.
    This is a conceptual placeholder for simulation and interaction.
    """
    def __init__(self, node_id=None, initial_state="idle", position=None):
        """
        Initializes a QNode.

        Args:
            node_id (str, optional): A unique identifier for the node. Defaults to None (will generate UUID).
            initial_state (str, optional): Starting state of the node. Defaults to "idle".
            position (tuple, optional): Placeholder for spatial position (e.g., in a 3D visualization). Defaults to None.
        """
        self.id = node_id if node_id else str(uuid.uuid4())
        self.state = initial_state
        self.position = position if position else (0, 0, 0) # Default position
        self.connections = [] # List to hold IDs of connected QNodes
        self.quantum_data = {} # Placeholder for more complex quantum state info
        self.history = [(0.0, initial_state)] # Track state changes over time (timestamp, state)

        print(f"Initialized QNode {self.id} at position {self.position}")

    def update_state(self, new_state, timestamp):
        """
        Updates the node's state and records it in history.
        (In a real simulation, this would be driven by quantum dynamics)
        """
        if new_state != self.state:
            self.state = new_state
            self.history.append((timestamp, new_state))
            print(f"Timestamp {timestamp}: QNode {self.id} updated state to {self.state}")
            # Potential hook for sonification or visualization update here

    def add_connection(self, other_node_id):
        """Adds a connection to another QNode."""
        if other_node_id not in self.connections:
            self.connections.append(other_node_id)
            print(f"QNode {self.id} connected to {other_node_id}")

    def get_info(self):
        """Returns basic information about the node."""
        return {
            "id": self.id,
            "state": self.state,
            "position": self.position,
            "connections": self.connections,
            "history_length": len(self.history)
        }

    def simulate_activity(self, timestamp):
        """Placeholder for simulating some internal activity."""
        # Example: Randomly transition state based on some condition
        if random.random() < 0.1: # 10% chance to change state
             possible_states = ["active", "processing", "entangled", "idle", "error"]
             new_state = random.choice([s for s in possible_states if s != self.state])
             self.update_state(new_state, timestamp)


# --- Example Usage ---

print("Creating the QAI Cluster (12 QNodes)...")

# Create the 12 QNodes
qai_cluster = [QNode(node_id=f"QN-{i+1}") for i in range(12)]

# Example: Position them conceptually (replace with actual geometry later)
for i, node in enumerate(qai_cluster):
    # Simple circular arrangement in XY plane for now
    angle = (i / 12) * 2 * 3.14159
    radius = 5.0
    node.position = (radius * cos(angle), radius * sin(angle), 0) # Requires importing math.cos/sin

# Example: Add some conceptual connections (e.g., connect neighbors)
print("\nEstablishing conceptual connections...")
for i in range(12):
    qai_cluster[i].add_connection(qai_cluster[(i + 1) % 12].id) # Connect to next node in circle

# Simulate some time steps
print("\nSimulating activity...")
current_time = 0.0
for step in range(5): # Simulate 5 time steps
    current_time += 1.0 # Increment time
    print(f"\n--- Time Step {current_time} ---")
    for node in qai_cluster:
        node.simulate_activity(current_time)

# Get info from a specific node
print("\nGetting info for Node QN-1:")
print(qai_cluster[0].get_info())

# Note: For the positioning example `cos` and `sin` functions are needed.
# You would typically `import math` at the beginning.
# Let's add that import and rerun the positioning part conceptually
import math

print("\nRepositioning nodes with actual math functions...")
for i, node in enumerate(qai_cluster):
    angle = (i / 12) * 2 * math.pi
    radius = 5.0
    node.position = (radius * math.cos(angle), radius * math.sin(angle), 0)
    # print(f"Node {node.id} position set to {node.position}") # Optional: print new positions


print("\nBasic QNode structure and cluster initialized.")
