#!/usr/bin/env python3
"""
a function that returns the log message obfuscated.
"""
from typing import List
import re


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    returns the log message obfuscated.
    """
    pattern = f"({'|'.join(fields)})=([^ {separator}]+)"
    for field in fields:
        return re.sub(pattern, f"\\1={redaction}", message)
