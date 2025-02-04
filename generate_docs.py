"""
Generate documentation for AWS infrastructure code.
It script reads all Terraform (.tf) and CDK (.ts, .py) files in the given directory.
"""

import glob
import logging
import os
import re

from dotenv import load_dotenv
from github import Github
from langchain_openai import ChatOpenAI

from promtps import human_prompt, system_prompt

# from langchain_openai import ChatOpenAI


load_dotenv()


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY is not set")

github_client = Github(os.getenv("GITHUB_TOKEN"))


logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)
logger.info("Loading OpenAI")
llm = ChatOpenAI(model="gpt-4o")
# llm = ChatOllama(model="llama3:latest", base_url="http://localhost:11434")


def remove_code_blocks(text, block_code):
    """

    Args:
        text (_type_): _description_
    """
    if block_code == "python":
        return re.sub(
            r"^```python\n",
            "",
            re.sub(r"```$", "", text, flags=re.MULTILINE),
            flags=re.MULTILINE,
        )
    elif block_code == "markdown":
        return re.sub(
            r"^```markdown\n",
            "",
            re.sub(r"```$", "", text, flags=re.MULTILINE),
            flags=re.MULTILINE,
        )


def extract_infrastructure_code(directory):
    """
    Reads all Terraform (.tf) and CDK (.ts, .py) files in the given directory.
    """
    infrastructure_code = ""

    for file in (
        glob.glob(f"{directory}/**/*.tf", recursive=True)
        + glob.glob(f"{directory}/**/*.ts", recursive=True)
        + glob.glob(f"{directory}/**/*.py", recursive=True)
    ):
        with open(file, "r", encoding="utf-8") as f:
            infrastructure_code += f.read() + "\n\n"

    return infrastructure_code


def geneate_documentation(infra_folder: str, infrastructure_code: str):
    """
    Generate documentation for a given infrastructure code
    :param repo_name: Name of the repository
    :param infra_folder: Folder where the infrastructure code is located
    :param infraescture_code: Infrastructure code
    :return: Documentation for the given infrastructure code
    """

    messages = [
        system_prompt(infrastructure_code, infra_folder),
        human_prompt(infrastructure_code, infra_folder),
    ]

    response = llm.invoke(messages)
    os.makedirs(f"output/{infra_folder}/", exist_ok=True)

    readme_content, diagram_code = response.content.split("```python", 1)
    diagram_code = "```python" + diagram_code.split("```")[0] + "```"

    readme_content = remove_code_blocks(readme_content, "markdown")
    diagram_code = remove_code_blocks(diagram_code, "python")

    readme_content.replace("# generate_diagram.py", "")

    with open(f"output/{infra_folder}/README.md", "w", encoding="utf-8") as f:
        f.write(readme_content.strip())

    with open(f"output/{infra_folder}/generate_diagram.py", "w", encoding="utf-8") as f:
        f.write(diagram_code.strip())

    logger.info("Documentation for %s generated successfully", infra_folder)


def process_repository(base_directory):
    """
    Processes each infrastructure folder separately.
    :param base_directory: Base directory where the repository is located
    """

    infrastructure_folders = [
        d
        for d in os.listdir(base_directory)
        if os.path.isdir(os.path.join(base_directory, d))
    ]

    for infra_folder in infrastructure_folders:
        infra_path = os.path.join(base_directory, infra_folder)
        infrastructure_code = extract_infrastructure_code(infra_path)
        if infrastructure_code.strip():
            geneate_documentation(infra_folder, infrastructure_code)


process_repository("/Users/aparra/workspaces/occ/ra-iac")
