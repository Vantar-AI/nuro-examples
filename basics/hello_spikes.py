"""
Hello Spikes — Your first spiking network in Nuro.

This example creates two populations of spiking neurons,
connects them with STDP plasticity, and runs a short
simulation on the GPU backend.
"""

import nuro

# Create two populations
input_pop = nuro.Population(size=100, dynamics="lif", params={"tau": 20e-3})
output_pop = nuro.Population(size=10, dynamics="lif", params={"tau": 10e-3})

# Connect them with STDP plasticity
conn = nuro.Connection(
    source=input_pop,
    target=output_pop,
    pattern="dense",
    plasticity="stdp",
)

# Build and compile
graph = nuro.Graph([input_pop, output_pop], [conn])
runtime = nuro.compile(graph, target="gpu")

# Run for 1 second
runtime.run(duration=1.0)

# Print results
print(f"Nuro v{nuro.__version__} — Hello Spikes!")
print(f"Duration: {runtime.metrics['duration']}s ({runtime.metrics['num_steps']} steps)")
print(f"Total spikes: {runtime.metrics['total_spikes']}")
for pop_id, count in runtime.metrics["spike_counts"].items():
    label = "input " if pop_id == input_pop.id else "output"
    print(f"  {label} ({pop_id}): {count} spikes")
