from prompts_loader import load_prompts
from llm import generate

# Load version v1
prompts = load_prompts("v1")

# Generate a response
answer = generate(
    system_prompt=prompts.system_prompt,
    user_text="I was charged twice for my subscription this month.",
)

print(answer)
