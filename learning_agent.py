import sys
import os

class CoreyLearningAgent:
    def __init__(self):
        self.summary_file = "SUMMARY.md"
        self.problems_file = "PROBLEMS.md"
        self.summary_content = self._load_file(self.summary_file)
        self.problems_content = self._load_file(self.problems_file)

    def _load_file(self, filepath):
        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                return f.read()
        return "File not found."

    def display_welcome(self):
        print("="*60)
        print("🚀 Welcome to the Corey Schafer Python Learning Agent! 🚀")
        print("Your structured guide to mastering Python, from Zero to Hero.")
        print("="*60)

    def show_menu(self):
        print("\nWhat would you like to explore?")
        print("1. View Playlist Summary")
        print("2. Browse 50 Practice Problems")
        print("3. Search for a Topic")
        print("4. Exit")

    def show_summary(self):
        print("\n--- Corey Schafer Python Tutorial Summary ---")
        print(self.summary_content)
        input("\nPress Enter to return to menu...")

    def show_problems(self):
        print("\n--- 50 Problem-Solving Challenges ---")
        print(self.problems_content)
        input("\nPress Enter to return to menu...")

    def search_topic(self):
        query = input("\nEnter a keyword to search for (e.g., 'OOP', 'Decorator', 'List'): ").lower()
        print(f"\n--- Search results for '{query}' ---")

        found = False
        combined_content = self.summary_content + self.problems_content
        lines = combined_content.split('\n')

        for i, line in enumerate(lines):
            if query in line.lower():
                # Print a bit of context
                start = max(0, i - 1)
                end = min(len(lines), i + 2)
                for j in range(start, end):
                    print(lines[j])
                print("-" * 20)
                found = True

        if not found:
            print("No matching topics found.")

        input("\nPress Enter to return to menu...")

    def run(self):
        self.display_welcome()
        while True:
            self.show_menu()
            choice = input("\nEnter choice (1-4): ")

            if choice == '1':
                self.show_summary()
            elif choice == '2':
                self.show_problems()
            elif choice == '3':
                self.search_topic()
            elif choice == '4':
                print("Happy Coding! Goodbye!")
                break
            else:
                print("Invalid choice, please try again.")

if __name__ == "__main__":
    agent = CoreyLearningAgent()
    if len(sys.argv) > 1:
        # Simple CLI argument support
        arg = sys.argv[1].lower()
        if arg == "--summary":
            print(agent.summary_content)
        elif arg == "--problems":
            print(agent.problems_content)
        else:
            print("Unknown argument. Use --summary or --problems, or run without arguments for interactive mode.")
    else:
        agent.run()
