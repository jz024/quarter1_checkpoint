import sys
import json
import time
from dotenv import load_dotenv
from code import load_dataset, get_category_list, direct_prompting_testing

load_dotenv()

def main(targets, model_name=None):
    with open('config.json') as config_file:
        config = json.load(config_file)

    if 'data' in targets:
        dataset_path = "20news-bydate/test"
        test_data = load_dataset(dataset_path, num_samples=10)
        categories_test = get_category_list(dataset_path)
        print("Dataset loaded successfully.")
    else:
        test_data = None
        categories_test = None

    if 'test' in targets:
        if test_data is None or categories_test is None:
            print("Error: 'data' target must be run before 'test' to load the dataset.")
            return

        model_config = next((m for m in config["models"] if m["name"] == model_name), None)
        
        if model_config:
            test_accuracy, test_cost = direct_prompting_testing(
                test_data, 
                categories_test, 
                model=model_config["name"], 
                token_budget=model_config["token_budget"], 
                delay=config["delay"]
            )
            print(f"Accuracy: {test_accuracy:.2%}")
            print(f"Total Estimated Cost: ${test_cost:.2f}")
        else:
            available_models = [m["name"] for m in config["models"]]
            print("Available models:", ", ".join(available_models))
    else:
        print("No testing performed.")

if __name__ == '__main__':
    targets = sys.argv[1:-1] 
    model_name = sys.argv[-1] if len(sys.argv) > 2 else None 

    if not targets:
        print("No targets specified. Available targets: 'data', 'test'")
    elif model_name is None:
        print("No model specified. Please specify a model to run.")
    else:
        main(targets, model_name)
