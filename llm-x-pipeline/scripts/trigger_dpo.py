import yaml
import subprocess

def run_dpo_flywheel(config_path: str = "configs/dpo_training_config.yaml"):
    with open(config_path, "r") as f:
        config = yaml.safe_load(f)
        
    print(f"Triggering Direct Preference Optimization with batch size: {config.get('batch_size', 32)}")
    # Trigger training backend subprocess
    subprocess.run(["echo", "Executing automated model weight adjustment via self-correction flywheel..."])

if __name__ == "__main__":
    run_dpo_flywheel()
