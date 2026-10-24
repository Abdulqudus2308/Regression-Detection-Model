import yaml

with open("Prompts/v1.yaml", encoding="utf-8") as f:
    data = yaml.safe_load(f)

print(data)
