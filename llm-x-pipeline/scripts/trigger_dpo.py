import yaml

def trigger_fine_tuning():
    with open("configs/dpo_training_config.yaml", "r") as f:
        config = yaml.safe_load(f)
    print(f"[DPO Pipeline] Triggering fine-tuning flywheel with model: {config.get('model_name', 'base')}")

if __name__ == "__main__":
    trigger_fine_tuning()
