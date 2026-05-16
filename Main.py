def generate_script(user_input):
    """Step 1: Convert user idea into a script."""
    print(f"[PROCESS] Analyzing input: '{user_input}'")

    generated_script = f"""
Scene 1: Introduction of the world based on {user_input}.
Scene 2: Conflict begins and tension rises.
Scene 3: Final resolution and conclusion.
"""

    return generated_script


# NEW FUNCTION (ADD THIS HERE)
def split_into_scenes(script):
    """Step 2: Convert script into structured scene list."""
    print("[PROCESS] Splitting script into scenes...")

    scenes = []

    lines = script.strip().split("\n")

    for line in lines:
        line = line.strip()
        if line:
            # basic parsing (later replace with LLM)
            if ":" in line:
                scene_id, description = line.split(":", 1)
                scenes.append({
                    "scene": scene_id.strip(),
                    "description": description.strip(),
                    "visual_prompt": f"Visual of: {description.strip()}"
                })

    return scenes


def generate_character_design(script):
    """Step 3: Extract character details from the script."""
    print("[PROCESS] Extracting character descriptions...")

    design_prompt = "Character in futuristic cyberpunk armor with neon lighting."

    return design_prompt


def generate_storyboard(scenes, design):
    """Step 4: Combine scenes and design into storyboard."""
    print("[PROCESS] Building storyboard...")

    frames = []

    for scene in scenes:
        frames.append(
            f"{scene['scene']}: {scene['description']} | STYLE: {design}"
        )

    return "\n".join(frames)


def run_pipeline():
    print("--- AI Content Pipeline Activated ---")

    user_prompt = input("Enter your video idea: ")

    if not user_prompt:
        print("Error: You didn't enter an idea!")
        return

    script_output = generate_script(user_prompt)

    # NEW STEP INSERTED HERE
    scenes_output = split_into_scenes(script_output)

    design_output = generate_character_design(script_output)

    storyboard_output = generate_storyboard(
        scenes_output,
        design_output
    )

    print("\n" + "=" * 30)
    print("PIPELINE RESULTS:")
    print("=" * 30)

    print("\n1. SCRIPT")
    print(script_output)

    print("\n2. SCENES")
    for s in scenes_output:
        print(s)

    print("\n3. STORYBOARD")
    print(storyboard_output)

    print("=" * 30)


if __name__ == "__main__":
    run_pipeline()
