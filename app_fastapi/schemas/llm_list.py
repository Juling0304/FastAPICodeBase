from enum import Enum


class SelectModel(str, Enum):
    gpt_4o = "gpt-4o"
    gpt_35_turbo = "gpt-3.5-turbo"
    claude_35_sonnet = "claude-3-5-sonnet-20241022"
    claude_3_haiku = "claude-3-haiku-20240307"
