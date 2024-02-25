import argparse
import pandas as pd
from transformers import AutoTokenizer
import tiktoken  # Assuming this is how you import TikToken

# Initialize TikToken for GPT-4, assuming this is the correct way to do so
gpt4_tokenizer = tiktoken.encoding_for_model("gpt-4")

def load_text_from_file(file_path):
    print(f"Loading text from {file_path}...")
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    print("Text loaded successfully.")
    return text

def extract_tokens(tokenizer, text, ignore_numbers=False):
    tokens = []
    if tokenizer is gpt4_tokenizer:
        # Using TikToken's method to tokenize text for GPT-4
        token_ids = gpt4_tokenizer.encode(text)
        for token_id in token_ids:
            token = gpt4_tokenizer.decode([token_id])
            if ignore_numbers and token.isdigit():
                continue  # Skip numeric tokens
            tokens.append(token)
    else:
        # Using Hugging Face's tokenizer for other models
        temp_tokens = tokenizer.tokenize(text)
        if ignore_numbers:
            tokens = [token for token in temp_tokens if not token.isdigit()]
        else:
            tokens = temp_tokens
    return tokens

def display_tokens_in_table(token_lists, model_names):
    # Determine the maximum length of the token lists
    max_len = max(len(tokens) for tokens in token_lists)
    # Pad shorter lists with empty strings so all lists have the same length
    padded_token_lists = [tokens + [''] * (max_len - len(tokens)) for tokens in token_lists]
    # Transpose the list of lists to match DataFrame's expected input format
    # Now each inner list represents a row, and each item in the inner list represents a column value
    transposed_token_lists = list(zip(*padded_token_lists))
    # Create a DataFrame with a column for each model
    pd.set_option('display.max_rows', None)
    df = pd.DataFrame(transposed_token_lists, columns=model_names)
    print(df)


def main():
    parser = argparse.ArgumentParser(description='Token Visualizer')
    parser.add_argument('--file', type=str, required=True, help='Path to the text file')
    parser.add_argument('--models', nargs='+', required=True, help='Tokenizer models to use')
    parser.add_argument('--ignore-numbers', action='store_true', help='Ignore numeric tokens')

    args = parser.parse_args()
    text = load_text_from_file(args.file)

    token_lists = []
    model_names = []
    for model_name in args.models:
        print(f"Loading tokenizer for model {model_name}...")
        if model_name.lower() == "gpt-4":
            tokenizer = gpt4_tokenizer
        else:
            tokenizer = AutoTokenizer.from_pretrained(model_name)
        print(f"Tokenizer loaded for model: {model_name}")

        tokens = extract_tokens(tokenizer, text, ignore_numbers=args.ignore_numbers)
        token_lists.append(tokens)
        model_names.append(model_name)

    print("Displaying tokens extracted from file:")
    display_tokens_in_table(token_lists, model_names)

if __name__ == "__main__":
    main()
