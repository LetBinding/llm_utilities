
print ("start")

import lmstudio as lms
SERVER_API_HOST = "localhost:1234"

# This must be the *first* SDK interaction (otherwise the SDK will
# implicitly attempt to access the default server instance)
lms.get_default_client(SERVER_API_HOST)

# model = lms.llm("deepseek-r1-distill-qwen-7b") # Get any loaded LLM

# prediction = llm.respond_stream("What is a Capybara?")

# for token in prediction:
#     print(token, end="", flush=True)
# import lmstudio as lms


# model = lms.llm("llama-3.2-1b-instruct")
# result = model.respond("What is the meaning of life?")

# print(result)

print ("end")