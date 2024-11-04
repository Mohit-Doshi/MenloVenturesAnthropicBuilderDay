import anthropic

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="",
)

# Use Claude to convert to a more readable prompt
def call_claude(user_inp, is_slang):

    if is_slang == True:
        message = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=1024,
            system="You are well aware of Gen-Z slang and will convert requested sentences into proper American English. Do nothing further.",
            messages=[
                {"role": "user", "content": f"Convert the following Gen-Z slang into proper English - {user_inp}"}
            ]
        )   
        print(type(message.content))
        print(message.content[0].text)
    else:
        message = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=1024,
            system="You will convert the requested sentence to Gen-Z slang. Do nothing further.",
            messages=[
                {"role": "user", "content": f"Convert the following sentence into Gen-Z slang - {user_inp}"}
            ]
        )
        print(type(message.content))
        print(message.content[0].text)
    pass



# Paste prompt in ChatGPT?

# Main program logic
def main():
    # Prompt the user for input
    user_input = input("Enter your prompt: ")
    is_genz_slang = False
    slang_input = input("Is this slang: y/n")
    if slang_input == "y":
        is_genz_slang = True
    # Print the user's input
    print("You entered:", user_input)

    # Call Claude with the user input
    call_claude(user_inp=user_input, is_slang=is_genz_slang)

# Run the program
if __name__ == "__main__":
    main()