from typing import TypedDict

from langgraph.graph import StateGraph, END

from app.tools.kpi_tool import get_kpi
from app.tools.alarm_tool import get_alarms
from app.rag.rag_engine import search, build_vector_store, load_documents, chunk_text

from langchain_ollama import ChatOllama


llm = ChatOllama(model="llama3")

class AgentState(TypedDict):
    query: str
    cell_id: str
    kpi_data: dict
    alarms: list
    rag_results: list
    final_answer: str
    

docs = load_documents("data/docs")

chunks = []

for doc in docs:
    chunks.extend(chunk_text(doc))

index, stored_chunks = build_vector_store(chunks)


def kpi_node(state: AgentState):

    kpi = get_kpi(state["cell_id"])

    return {
        "kpi_data": kpi
    }
    

def alarm_node(state: AgentState):

    alarms = get_alarms(state["cell_id"])

    return {
        "alarms": alarms
    }
    
def rag_node(state: AgentState):

    results = search(
        state["query"],
        index,
        stored_chunks
    )

    return {
        "rag_results": results
    }
    
    
def final_node(state: AgentState):

    prompt = f"""
    You are a telecom RAN operations assistant.

    User Query:
    {state['query']}

    KPI Data:
    {state['kpi_data']}

    Alarm Data:
    {state['alarms']}

    Telecom Knowledge:
    {state['rag_results']}

    Give:
    - diagnosis
    - likely causes
    - recommended actions
    """

    response = llm.invoke(prompt)

    return {
        "final_answer": response.content
    }
    
graph = StateGraph(AgentState)
graph.add_node("kpi_agent", kpi_node)
graph.add_node("alarm_agent", alarm_node)
graph.add_node("rag_agent", rag_node)
graph.add_node("final_agent", final_node)

graph.set_entry_point("kpi_agent")

graph.add_edge("kpi_agent", "alarm_agent")
graph.add_edge("alarm_agent", "rag_agent")
graph.add_edge("rag_agent", "final_agent")
graph.add_edge("final_agent", END)

teleops_graph = graph.compile()