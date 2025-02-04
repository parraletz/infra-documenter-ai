# Infra-genDocs-AI

## 📄 Overview

`ai-infra-documenter` is a tool designed to automatically generate documentation for AWS infrastructure code. By leveraging large language models (LLMs) via OpenAI's API, it parses Terraform and AWS Cloud Development Kit (CDK) files and produces comprehensive documentation and architectural diagrams. 

## 🚀 Features

- **Automatic Documentation**: Extracts infrastructure code and generates README files and diagrams.
- **AI-powered Analysis**: Utilizes advanced LLMs to understand and describe complex infrastructure setups.
- **Multi-format Support**: Reads Terraform (.tf) and CDK (.ts, .py) files for flexible integration into various workflows. 

## 📂 Directory Structure

- `generate_docs.py`: Main script to process infrastructure code and generate documentation.
- `prompts.py`: Contains functions for generating prompts used by the LLM.
- `.env.template`: Template for defining API keys and configuration settings.
- `pyproject.toml`: Defines the project setup and dependencies.
- `README.md`: Project overview and instructions.

## 🛠 Prerequisites

- Python 3.11 or above
- AWS CLI (>=2.0)
- OpenAI API key
- Access to GitHub API for repository processing
- Terraform/CDK files to be documented

## 🔧 Installation

1. Clone the repository:
```bash
git clone https://github.com/parraletz/infra-documenter-ai.git
cd infra-documenter-ai
```

2. Install dependencies using Poetry:
```bash
poetry install
```

3. Configure environment variables by copying `.env.template` to `.env` and filling in necessary values:
```env
OPENAI_API_KEY="your-openai-api-key"
LANGCHAIN_API_KEY="your-langchain-api-key"
```

## 🚚 Usage

Run the script to process a repository and generate documentation:
```bash
python generate_docs.py
```

This command will generate documentation for the specified directory of infrastructure as code files, outputting results in an `output` directory organized by folder.

## 🔍 Github Actions

### WIP

## 📜 License

This project is licensed under the MIT License.

## 🤝 Contributions

Contributions are welcome! Please feel free to submit a Pull Request or issue for any improvements or bug fixes.
