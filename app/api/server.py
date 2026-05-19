from fastapi import FastAPI
from pydantic import BaseModel

from app.graph.teleops_graph import teleops_graph
from fastapi.middleware.cors import CORSMiddleware
import logging

logging.basicConfig(level=logging.INFO)


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class QueryRequest(BaseModel):
    query: str
    cell_id: str
    

@app.post("/query")
def query_agent(request: QueryRequest):

    result = teleops_graph.invoke({
        "query": request.query,
        "cell_id": request.cell_id
    })
    logging.info(f"Received query: {request.query}")


    return {
        "status": "success",

        "diagnosis": result["final_answer"],

        "root_causes": [
            "Interference",
            "High congestion"
        ],

        "recommendations": [
            "Check antenna tilt",
            "Load balancing"
        ],

        "observability": {
            "kpi": result["kpi_data"],
            "alarms": result["alarms"]
        },

        "knowledge_sources": result["rag_results"]
    }