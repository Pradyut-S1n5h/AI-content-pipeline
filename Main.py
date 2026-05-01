import sys

def generate_script(user_input):
    """Step 1: Convert user idea into a script."""
    print(f"[PROCESS] Analyzing input: '{user_input}'")
    # This is a placeholder for a real AI call
    generated_script = f"SCRIPT: A story centered around {user_input}."
    return generated_script

def generate_character_design(script):
    """Step 2: Extract character details from the script."""
    print("[PROCESS] Extracting character descriptions...")
    # This is where an LLM would describe the visuals
    design_prompt = "DESIGN: A character wearing futuristic gear based on the story."
    return design_prompt

def generate_storyboard(script, design):
    """Step 3: Combine script and design into a shot list."""
    print("[PROCESS] Finalizing storyboard layout...")
    # This would eventually trigger an image generator
    frames = [
        "Frame 1: Establishing shot of the setting.",
        "Frame 2: Character is introduced.",
        f"Frame 3: Action sequence following the {script}."
    ]
    return "\n".join(frames)

def run_pipeline():
    """The main engine that runs the steps in order."""
    print("--- AI Content Pipeline Activated ---")
    
    # Get user input
    user_prompt = input("Enter your video idea: ")
    
    if not user_prompt:
        print("Error: You didn't enter an idea!")
        return

    # Execute the stages
    script_output = generate_script(user_prompt)
    design_output = generate_character_design(script_output)
    storyboard_output = generate_storyboard(script_output, design_output)
    
    # Show the results
    print("\n" + "="*30)
    print("PIPELINE RESULTS:")
    print(f"1. {script_output}")
    print(f"2. {design_output}")
    print(f"3. STORYBOARD:\n{storyboard_output}")
    print("="*30)

if __name__ == "__main__":
    try:
        run_pipeline()
    except KeyboardInterrupt:
        print("\nPipeline stopped by user.")
        sys.exit()
