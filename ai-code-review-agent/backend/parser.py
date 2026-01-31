import re


def parse_review_response(text: str):
    priorities = {"Critical": [], "High": [], "Medium": [], "Low": []}


    for level in priorities.keys():
        pattern = rf"{level}.*?:([\s\S]*?)(?=Critical|High|Medium|Low|$)"
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            priorities[level] = match.group(1).strip().split("\n")


    return priorities
