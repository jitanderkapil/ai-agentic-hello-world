#!/usr/bin/env python3
"""
AI Agentic Hello World Solution

A simple demonstration of an autonomous AI agent that can:
- Perceive its environment
- Make decisions based on goals
- Take actions autonomously
- Learn from feedback
"""

import time
import random
from typing import Dict, List


class Agent:
    """A simple autonomous AI agent."""
    
    def __init__(self, name: str, goal: str):
        self.name = name
        self.goal = goal
        self.state = "initialized"
        self.memory = []
        self.actions_taken = []
        
    def perceive(self, environment: Dict) -> Dict:
        """Perceive and understand the environment."""
        print(f"[{self.name}] Perceiving environment...")
        perception = {
            "time": time.time(),
            "environment_data": environment,
            "goal_status": self.evaluate_goal_status(environment)
        }
        self.memory.append(perception)
        return perception
    
    def evaluate_goal_status(self, environment: Dict) -> str:
        """Evaluate progress toward goal."""
        if "goal_achieved" in environment and environment["goal_achieved"]:
            return "achieved"
        return "in_progress"
    
    def decide(self, perception: Dict) -> str:
        """Make a decision based on perception."""
        print(f"[{self.name}] Making decision...")
        
        if perception["goal_status"] == "achieved":
            return "celebrate"
        
        # Simple decision logic
        possible_actions = ["greet", "introduce", "explain_purpose", "learn"]
        action = random.choice(possible_actions)
        return action
    
    def act(self, action: str) -> None:
        """Execute the chosen action."""
        print(f"[{self.name}] Taking action: {action}")
        
        actions = {
            "greet": self.greet,
            "introduce": self.introduce,
            "explain_purpose": self.explain_purpose,
            "learn": self.learn,
            "celebrate": self.celebrate
        }
        
        if action in actions:
            actions[action]()
            self.actions_taken.append(action)
        else:
            print(f"Unknown action: {action}")
    
    def greet(self):
        """Greet the world."""
        print(f"\n🤖 Hello, World! I am {self.name}, an autonomous AI agent!\n")
    
    def introduce(self):
        """Introduce self and capabilities."""
        print(f"\nI am an AI agent with the following capabilities:")
        print("  - Autonomous decision making")
        print("  - Environmental perception")
        print("  - Goal-oriented behavior")
        print("  - Learning from experience\n")
    
    def explain_purpose(self):
        """Explain the agent's purpose."""
        print(f"\nMy goal is: {self.goal}")
        print("I operate autonomously to achieve this goal.\n")
    
    def learn(self):
        """Learn from past actions."""
        print(f"\nLearning from experience...")
        print(f"Total actions taken: {len(self.actions_taken)}")
        print(f"Memory entries: {len(self.memory)}\n")
    
    def celebrate(self):
        """Celebrate goal achievement."""
        print(f"\n🎉 Goal achieved! {self.goal}\n")
    
    def run(self, environment: Dict, steps: int = 5):
        """Run the agent for a number of steps."""
        print(f"\n{'='*60}")
        print(f"Starting Agent: {self.name}")
        print(f"Goal: {self.goal}")
        print(f"{'='*60}\n")
        
        for step in range(steps):
            print(f"--- Step {step + 1} ---")
            
            # Perceive -> Decide -> Act cycle
            perception = self.perceive(environment)
            decision = self.decide(perception)
            self.act(decision)
            
            time.sleep(0.5)  # Small delay for readability
            
            # Update environment (simple simulation)
            if step == steps - 1:
                environment["goal_achieved"] = True
        
        print(f"\n{'='*60}")
        print(f"Agent {self.name} completed {steps} steps")
        print(f"{'='*60}\n")


def main():
    """
    Main function to demonstrate the AI agent.
    """
    # Create an environment
    environment = {
        "world": "Hello World Environment",
        "goal_achieved": False,
        "resources": ["knowledge", "autonomy", "learning"]
    }
    
    # Create an AI agent
    agent = Agent(
        name="AgenticHelloWorld",
        goal="Demonstrate autonomous AI agent capabilities"
    )
    
    # Run the agent
    agent.run(environment, steps=5)
    
    print("\n✨ AI Agentic Hello World demonstration complete!\n")


if __name__ == "__main__":
    main()
