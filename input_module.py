
def get_user_input():
    """Collect the blog requirements from the user."""

    print("\n===== AI-POWERED BLOG CONTENT GENERATOR =====")

    topic = input("\nEnter Blog Topic: ").strip()
    while not topic:
        print("Topic cannot be empty.")
        topic = input("Enter Blog Topic: ").strip()

    print("\nWriting Styles:")
    print("1. Professional")
    print("2. Casual")
    print("3. Technical")
    print("4. Creative")

    styles = {
        "1": "Professional",
        "2": "Casual",
        "3": "Technical",
        "4": "Creative"
    }

    style_choice = input("Choose writing style (1-4): ").strip()
    while style_choice not in styles:
        style_choice = input("Enter a valid choice (1-4): ").strip()

    style = styles[style_choice]

    print("\nTones:")
    print("1. Formal")
    print("2. Friendly")
    print("3. Informative")
    print("4. Persuasive")

    tones = {
        "1": "Formal",
        "2": "Friendly",
        "3": "Informative",
        "4": "Persuasive"
    }

    tone_choice = input("Choose tone (1-4): ").strip()
    while tone_choice not in tones:
        tone_choice = input("Enter a valid choice (1-4): ").strip()

    tone = tones[tone_choice]

    while True:
        try:
            word_count = int(input("\nApproximate Word Count: "))
            if word_count > 0:
                break
            print("Word count must be greater than zero.")
        except ValueError:
            print("Please enter a valid whole number.")

    print("\n========== YOUR INPUTS ==========")
    print(f"Blog Topic : {topic}")
    print(f"Style      : {style}")
    print(f"Tone       : {tone}")
    print(f"Words      : {word_count}")
    print("=================================")

    return topic, style, tone, word_count
