from app.graph.teleops_graph import teleops_graph

response = teleops_graph.invoke({
    "query": "Cell NR-4402 has poor SINR and low throughput",
    "cell_id": "NR-4402"
})

print("\n FINAL RESPONSE:\n")

print(response["final_answer"])