"""
Hello Spikes — Your first spiking network in Nuro.

This example creates two populations of spiking neurons,
connects them, and runs a short simulation on the GPU backend.
"""

# import nuro
#
# # Create two populations
# input_pop = nuro.Population(size=100, dynamics="lif", params={"tau": 20e-3})
# output_pop = nuro.Population(size=10, dynamics="lif", params={"tau": 10e-3})
#
# # Connect them
# conn = nuro.Connection(
#     source=input_pop,
#     target=output_pop,
#     pattern="dense",
#     plasticity="stdp",
# )
#
# # Build and compile
# graph = nuro.Graph([input_pop, output_pop], [conn])
# runtime = nuro.compile(graph, target="gpu")
#
# # Run for 1 second
# runtime.run(duration=1.0)
# print("Spikes recorded:", runtime.metrics["total_spikes"])

print("🚧 Nuro SDK is under development. This example will work once v0.1.0 ships.")
