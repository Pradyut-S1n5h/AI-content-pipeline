from huggingface_hub import InferenceClient
import getpass

# ===================================
# ASK FOR TOKEN
# ===================================

HF_TOKEN = getpass.getpass(
    "Enter your Hugging Face API token: "
)

# ===================================
# CONNECT TO HUGGING FACE
# ===================================

client = InferenceClient(
    api_key=HF_TOKEN
)

# ===================================
# USER IDEA
# ===================================

idea = input("Enter your video idea: ")

print("\nGenerating script...\n")

# ===================================
# SCRIPT GENERATION
# ===================================

response = client.chat.completions.create(
    model="Qwen/Qwen3-32B",
    messages=[
        {
            "role": "user",
            "content": f"""
Create a short cinematic story based on:

{idea}

Format:

Scene 1: ...
Scene 2: ...
Scene 3: ...
"""
        }
    ]
)

script = response.choices[0].message.content

print("=" * 50)
print("GENERATED SCRIPT")
print("=" * 50)
print(script)
print("=" * 50)
