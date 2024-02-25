# Introduction


## Running the benchmark
The following command line will allow you to run the tokenizer benchmark against multiple different models

```bash
python benchmark.py --file dataset.json --models mistralai/Mistral-7B-v0.1 gpt-4 google/gemma-7b
```

## visualizer

```bash
python visualizer.py --file ./samples/Programming/BASIC/guess.bas --model google/gemma-7b
```

or

```bash
python visualizer2.py --file ./samples/Programming/BASIC/guess.bas --models mistralai/Mistral-7B-v0.1 gpt-4 google/gemma-7b
```

```bash
python visualizer2.py --file ./samples/Text/cities.txt --models mistralai/Mistral-7B-v0.1 gpt-4 google/gemma-7b --ignore-numbers
```