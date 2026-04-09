from db.vector import chroma
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

vectorstore = chroma() 

def conversation(q: str):
    # retrieve top 3 similar docs
    docs = vectorstore.similarity_search(q, k=3)

    TEMPLATE = '''
        System:
        You are a Stargallery bot.

        Question:
        {q}

        Answer using only the following context:
        {context}
    '''

    # Create the prompt
    prompt_template = PromptTemplate.from_template(TEMPLATE)

    # Format the prompt with actual values
    final_prompt = prompt_template.format(q=q, context=docs)

    # Initialize the LLM
    chat = ChatOpenAI(
        model='gpt-4',
        seed=365,
        max_tokens=250
    )

    # Call the LLM directly with the formatted prompt
    answer = chat.invoke(final_prompt)

    # Parse output as string
    return StrOutputParser().invoke(answer)