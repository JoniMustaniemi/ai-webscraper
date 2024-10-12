from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

# Define the template for Ollama.
OLLAMA_TEMPLATE = (
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string ('')."
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
)

# Initialize the LLM model using Ollama.
model = OllamaLLM(model="llama3.1")



def parse_with_ollama(dom_chunks, parse_description):
    """
    Parse the DOM content chunks using the Ollama language model to extract specific information.

    Args:
        dom_chunks (list of str): A list of DOM content chunks to parse.
        parse_description (str): The user-specified description of what to extract.

    Returns:
        str: The concatenated results of parsed information from all chunks.
    """
    # Create a prompt template from the extraction instructions.
    prompt_template = ChatPromptTemplate.from_template(OLLAMA_TEMPLATE)
    chain = prompt_template | model

    parsed_results = []

    # Process each chunk of DOM content.
    for i, chunk in enumerate(dom_chunks, start=1):
        # Invoke the model to extract information based on the current chunk and description.
        response = chain.invoke(
            {"dom_content": chunk, "parse_description": parse_description}
        )
        print(f"Parsed batch {i} of {len(dom_chunks)}")
        parsed_results.append(response)

    # Join and return all parsed results as a single string.
    return "\n".join(parsed_results)
