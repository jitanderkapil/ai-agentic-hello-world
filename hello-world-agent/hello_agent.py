#!/usr/bin/env python3
"""Hello World Agent - the simplest possible AI-style agent.

No frameworks, no API keys, no dependencies - just the Python standard library.

An agent is a loop:
    OBSERVE  -> read the user's request
    DECIDE   -> pick which tool fits the request (simple keyword rules)
    ACT      -> run the tool
    RESPOND  -> report the result

Run it:
    python3 hello_agent.py                    # interactive mode
    python3 hello_agent.py "say hello to Sam" # single request

Try requests like:
    "say hello to Sam"
    "what time is it?"
    "add 3 and 4"
    "help"
"""

import re
import sys
from datetime import datetime


# ---------------------------------------------------------------- tools ----
# A tool is just a function the agent can call. Each one takes text in and
# returns text out.

def tool_greet(text: str) -> str:
    """Greet a person by name, e.g. 'say hello to Sam'."""
    match = re.search(r"(?:to|for)\s+([A-Za-z]+)", text)
    name = match.group(1) if match else "World"
    return f"Hello, {name}! I am a tiny agent, pleased to meet you."


def tool_time(text: str) -> str:
    """Tell the current time."""
    return "It is currently " + datetime.now().strftime("%A, %B %d, %Y at %I:%M %p") + "."


def tool_add(text: str) -> str:
    """Add two numbers found in the text, e.g. 'add 3 and 4'."""
    numbers = re.findall(r"-?\d+(?:\.\d+)?", text)
    if len(numbers) < 2:
        return "I need two numbers to add, e.g. 'add 3 and 4'."
    a, b = float(numbers[0]), float(numbers[1])
    result = a + b
    if result == int(result):
        result = int(result)
    return f"{numbers[0]} + {numbers[1]} = {result}"


def tool_help(text: str) -> str:
    """List what the agent can do."""
    return (
        "I can:\n"
        "  - greet someone:   'say hello to Sam'\n"
        "  - tell the time:   'what time is it?'\n"
        "  - add two numbers: 'add 3 and 4'\n"
        "  - show this help:  'help'"
    )


# The agent's toolbox: name -> function.
TOOLS = {
    "greet": tool_greet,
    "time": tool_time,
    "add": tool_add,
    "help": tool_help,
}


# --------------------------------------------------------------- decide ----
def decide(request: str) -> str:
    """Pick a tool for the request using simple keyword rules.

    This is the 'brain' of the agent. In a real AI agent an LLM makes this
    decision; here, transparent rules keep it dependency-free and obvious.
    """
    text = request.lower()
    if any(word in text for word in ("hello", "hi", "greet", "hey")):
        return "greet"
    if "time" in text or "date" in text:
        return "time"
    if "add" in text or "+" in text:
        return "add"
    return "help"


# ----------------------------------------------------------------- loop ----
def run_agent(request: str, max_steps: int = 3) -> str:
    """The agent loop: observe -> decide -> act -> respond."""
    for _step in range(max_steps):
        tool_name = decide(request)          # DECIDE
        result = TOOLS[tool_name](request)   # ACT
        return result                        # RESPOND
    return "I could not figure out what to do with that."


def main() -> None:
    if len(sys.argv) > 1:
        # Single-shot mode: everything after the script name is the request.
        print(run_agent(" ".join(sys.argv[1:])))
        return

    print("Hello World Agent (type 'quit' to exit)")
    while True:
        try:
            request = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if request.lower() in ("quit", "exit"):
            break
        if request:
            print("Agent:", run_agent(request))


if __name__ == "__main__":
    main()
