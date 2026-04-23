import json
import datetime

with open("tree.json", "r") as f:
    tree = json.load(f)

nodes = tree["nodes"]
start_node = tree["start"]

class ReflectionAgent:
    def __init__(self, auto_mode=False, predefined_answers=None):
        self.current = start_node
        self.answers = {}
        self.path = []
        self.auto_mode = auto_mode
        self.predefined_answers = predefined_answers or []
        self.auto_index = 0

    def get_input(self, options):
        if self.auto_mode:
            choice = self.predefined_answers[self.auto_index]
            self.auto_index += 1
            print(f"[AUTO] Selected: {choice}")
            return choice
        else:
            keys = list(options.keys())
            for i, k in enumerate(keys, 1):
                print(f"{i}. {k}")
            while True:
                choice = input("Choose option: ")
                if choice.isdigit() and 1 <= int(choice) <= len(keys):
                    return keys[int(choice)-1]
                print("Invalid input")

    def run(self):
        while True:
            node = nodes[self.current]
            self.path.append(self.current)

            if node["type"] == "question":
                print("\n[QUESTION]:", node["text"])
                choice = self.get_input(node["options"])
                self.answers[node["text"]] = choice
                self.current = node["options"][choice]

            elif node["type"] == "decision":
                print("\n[DECISION]:", node["text"])
                choice = self.get_input(node["branches"])
                self.answers[node["text"]] = choice
                self.current = node["branches"][choice]

            elif node["type"] == "action":
                print("\n[ACTION]:", node["text"])
                self.current = node["next"]

            elif node["type"] == "bridge":
                print("\n--- Transition to Reflection ---")
                self.current = node["next"]

            elif node["type"] == "reflection":
                print("\n[REFLECTION]:", node["text"])
                if "next" in node:
                    self.current = node["next"]
                else:
                    break

            elif node["type"] == "summary":
                print("\n=== SUMMARY ===")
                print(node["text"])
                self.save_session()
                break

    def save_session(self):
        session = {
            "timestamp": str(datetime.datetime.now()),
            "answers": self.answers,
            "path": self.path
        }

        filename = f"session_{int(datetime.datetime.now().timestamp())}.json"
        with open(filename, "w") as f:
            json.dump(session, f, indent=2)

        print(f"\nSession saved as {filename}")


# -------- RUN MODES -------- #

if __name__ == "__main__":
    print("Select mode:")
    print("1. Interactive")
    print("2. Auto (test persona)")

    mode = input("Choice: ")

    if mode == "2":
        # Persona 1 (focused)
        answers = ["focused", "study", "yes", "yes", "productive"]
        agent = ReflectionAgent(auto_mode=True, predefined_answers=answers)
    else:
        agent = ReflectionAgent()

    agent.run()
