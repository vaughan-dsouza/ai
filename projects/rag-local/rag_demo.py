from llama_cpp import Llama

# Load the model
llm = Llama(
    model_path="models/mistral-7b.Q4_K_M.gguf",
    n_ctx=2048,
    n_threads=4  # Adjust based on your CPU
)

# Ask something
response = llm("Q: What is Retrieval-Augmented Generation (RAG)? A:", max_tokens=200)
print(response["choices"][0]["text"].strip())
