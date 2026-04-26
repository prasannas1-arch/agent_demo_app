from langchain_core.tools import tool

@tool
def to_uppercase(text: str) -> str:
    """Convert text to uppercase"""
    return text.upper()

@tool
def to_lowercase(text: str) -> str:
    """Convert text to lowercase"""
    return text.lower()

@tool
def reverse_string(text: str) -> str:
    """Reverse the input string"""
    return text[::-1]

@tool
def count_chars(text: str) -> int:
    """Count characters from the input string"""
    return len(text)

@tool
def count_words(text: str) -> int:
    """Count words from the input string"""
    return len(text.split(" "))


STRING_TOOLS = [to_uppercase, to_lowercase, reverse_string, count_chars, count_words]