import argparse
from transformers import AutoTokenizer, AutoModelForCausalLM

def generate_text(model_name, prompt):
    # Get the tokenizer and model
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto")

    # Tokenize the input text
    input_ids = tokenizer(prompt, return_tensors="pt").to("mps")

    # Generate output from the model
    outputs = model.generate(**input_ids, max_length=200)

    # Decode and print the output
    print(tokenizer.decode(outputs[0]))

def main():
    # Initialize argument parser
    parser = argparse.ArgumentParser(description="Generate text using a specified model and prompt")
    parser.add_argument("--model", type=str, default="google/gemma-7b-it", help="Name of the model to use (default: google/gemma-7b-it)")
    parser.add_argument("--prompt", type=str, default="Who is Ada Lovelace?", help="Prompt to feed to the model (default: 'Who is Ada Lovelace?')")

    # Parse arguments
    args = parser.parse_args()

    # Generate text
    generate_text(args.model, args.prompt)

if __name__ == "__main__":
    main()
