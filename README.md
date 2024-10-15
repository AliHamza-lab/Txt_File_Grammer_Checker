# Text Grammar Correction Tool

This repository contains a Python-based tool that processes text files in chunks and automatically corrects grammatical errors using the `GingerIt` library. It reads text from a specified file, processes it in chunks to improve performance on large files, corrects any grammatical issues, and saves the corrected text to a new file.

## Features

- Processes text files in chunks for efficient memory usage.
- Automatically corrects grammar, spelling, and punctuation errors using the `GingerIt` library.
- Saves the corrected output to a new file.
- Supports large text files by reading and processing in customizable chunk sizes.

## Requirements

To run this tool, ensure you have Python installed and the necessary dependencies.

### Dependencies

Install the required dependencies using pip:

```bash
pip install gingerit
