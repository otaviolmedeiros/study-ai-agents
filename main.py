from router import Router

def main():
    router = Router()
    print("AI Agent initialized. Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        response = router.process(user_input)
        print(f"Agent: {response}")

if __name__ == "__main__":
    main()