from db.vector import chroma

vectorstore = chroma()

def retrieve_context(state):
    docs = vectorstore.similarity_search(state["question"], k=3)

    context = "\n\n".join([d.page_content for d in docs])
    return {"docs": context}