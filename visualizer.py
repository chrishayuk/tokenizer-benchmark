import argparse
from transformers import AutoTokenizer
import pandas as pd
import tiktoken  # Ensure TikToken is installed and imported

def load_text_from_file(file_path):
    print(f"Loading text from {file_path}...")
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    print("Text loaded successfully.")
    return text

def extract_tokens(tokenizer, text, is_gpt4=False):
    if is_gpt4:
        # Encode the text to get a list of token IDs
        token_ids = tokenizer.encode(text)
        # Ensure that the input to 'decode' is a list, even for individual token IDs
        tokens = [tokenizer.decode([token_id]) for token_id in token_ids]
    else:
        tokens = tokenizer.tokenize(text)
    return tokens



def display_tokens_in_table(tokens):
    # Create a DataFrame for better visualization
    pd.set_option('display.max_rows', None)
    df = pd.DataFrame(tokens, columns=['Tokens'])
    # Use `print` to display the DataFrame in the console
    print(df)

def main():
    parser = argparse.ArgumentParser(description='Token Visualizer')
    parser.add_argument('--file', type=str, required=True, help='Path to the text file')
    parser.add_argument('--model', type=str, required=True, help='Tokenizer model to use')

    args = parser.parse_args()
    text = load_text_from_file(args.file)

    print("Loading tokenizer model...")
    is_gpt4 = args.model.lower() == "gpt-4"
    if is_gpt4:
        # Initialize TikToken for GPT-4
        tokenizer = tiktoken.encoding_for_model("gpt-4")
    else:
        tokenizer = AutoTokenizer.from_pretrained(args.model)
    print(f"Model loaded: {args.model}")

    tokens = extract_tokens(tokenizer, text, is_gpt4)
    print("Displaying tokens extracted from file:")
    display_tokens_in_table(tokens)

if __name__ == "__main__":
    main()
