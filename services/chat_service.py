from db.vector import chroma
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
import re

vectorstore = chroma() 

def conversation(q: str):
    # retrieve top 3 similar docs
    docs = vectorstore.similarity_search(q, k=3)

    TEMPLATE = """
        You are a Stargallery assistant.

        Answer the question using ONLY the context below.

        Rules:
        - Return clean plain text
        - No markdown (**, bullets, etc.)
        - Keep answer concise and readable

        Question:
        {q}

        Context:
        {context}
    """

    # Create the prompt
    prompt_template = PromptTemplate.from_template(TEMPLATE)
    
    cleaned_docs = "\n\n".join([doc.page_content for doc in docs])

    # Format the prompt with actual values
    final_prompt = prompt_template.format(q=q, context=cleaned_docs)

    # Initialize the LLM
    chat = ChatOpenAI(
        model='gpt-4o-mini',
        seed=365,
        max_tokens=250,
        temperature=0  # reduces randomness = cleaner output
    )

    # Call the LLM directly with the formatted prompt
    answer = chat.invoke(final_prompt)

    # Parse output as string
    return clean_output(StrOutputParser().invoke(answer))

def clean_output(text: str) -> str:
    # remove markdown bold/italic
    text = re.sub(r"\*\*(.*?)\*\*", r"\1", text)
    text = re.sub(r"\*(.*?)\*", r"\1", text)

    # normalize spaces
    text = " ".join(text.split())

    return text