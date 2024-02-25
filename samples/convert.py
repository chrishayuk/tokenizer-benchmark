import argparse

def convert_file_to_format(file_path):
    # Read the content of the source file
    with open(file_path, 'r') as file:
        content = file.read()

    # Escape backslashes and double quotes
    escaped_content = content.replace('\\', '\\\\').replace('"', '\\"')

    # Replace newline characters with the \n escape sequence
    escaped_content = escaped_content.replace('\n', '\\n')

    # Format the escaped content into the specified format
    formatted_content = f'"prompt": "{escaped_content}"'

    return formatted_content

def main():
    parser = argparse.ArgumentParser(description='Convert a source file to a specific format.')
    parser.add_argument('source_file', type=str, help='Path to the source file to be converted.')
    parser.add_argument('-o', '--output', type=str, help='Path to the output file. If not specified, output will be printed to stdout.')

    args = parser.parse_args()

    formatted_content = convert_file_to_format(args.source_file)

    if args.output:
        with open(args.output, 'w') as output_file:
            output_file.write(formatted_content)
            print(f'Formatted content has been written to {args.output}')
    else:
        print(formatted_content)

if __name__ == '__main__':
    main()
