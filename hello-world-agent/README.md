# Hello World Agent

The simplest possible agent — no frameworks, no API keys, no dependencies.
Just Python 3 and the standard library.

An agent is a loop:

```
OBSERVE  -> read the user's request
DECIDE   -> pick which tool fits the request (simple keyword rules)
ACT      -> run the tool
RESPOND  -> report the result
```

In a production AI agent an LLM makes the DECIDE step; here transparent rules
keep the example dependency-free and easy to follow. The loop, the toolbox,
and the tool-calling shape are the real thing.

## Run it

Interactive mode:

```bash
python3 hello_agent.py
```

Single request:

```bash
python3 hello_agent.py "say hello to Sam"
python3 hello_agent.py "what time is it?"
python3 hello_agent.py "add 3 and 4"
```

## Tools

| Tool  | Example request      | What it does              |
|-------|----------------------|---------------------------|
| greet | "say hello to Sam"   | Greets a person by name   |
| time  | "what time is it?"   | Tells the current time    |
| add   | "add 3 and 4"        | Adds two numbers          |
| help  | "help"               | Lists what the agent does |

## Next steps

- Add a tool: write a function, register it in `TOOLS`, add a rule in `decide()`.
- Swap `decide()` for an LLM call (e.g. Amazon Bedrock) to turn the rule-based
  brain into a model-driven one — the loop stays exactly the same.
