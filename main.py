
from input_module import get_user_input
from blog_module import generate_blog
from title_module import generate_titles
from keyword_module import generate_keywords
from summary_module import generate_summary
from meta_module import generate_meta_description
from intent_module import detect_intent
from utils import save_blog


def create_blog():
    topic, style, tone, word_count = get_user_input()

    blog = generate_blog(topic, style, tone, word_count)

    if not blog:
        print("Blog generation failed.")
        return

    save_blog(blog)

    print("\n===== ADDITIONAL BLOG CONTENT =====")
    generate_titles(topic, blog)
    generate_keywords(topic, blog)
    generate_summary(blog)
    generate_meta_description(topic, blog)


def process_request():
    request = input("\nDescribe what you want: ").strip()

    if not request:
        print("Please enter a request.")
        return

    intent = detect_intent(request)

    if intent == "BLOG_GENERATION":
        create_blog()

    elif intent == "SUMMARY":
        blog = input(
            "\nPaste the blog you want to summarize:\n"
        ).strip()

        if blog:
            generate_summary(blog)
        else:
            print("No blog content provided.")

    elif intent == "KEYWORD_GENERATION":
        topic = input("Enter the blog topic: ").strip()
        blog = input("Paste the blog content:\n").strip()

        if topic and blog:
            generate_keywords(topic, blog)
        else:
            print("Topic and blog content are required.")

    elif intent == "META_DESCRIPTION":
        topic = input("Enter the blog topic: ").strip()
        blog = input("Paste the blog content:\n").strip()

        if topic and blog:
            generate_meta_description(topic, blog)
        else:
            print("Topic and blog content are required.")

    else:
        print("Unable to process this request.")


def main():
    print("========================================")
    print(" AI-POWERED BLOG CONTENT GENERATOR")
    print(" Powered by Ollama and Qwen")
    print("========================================")

    while True:
        print("\n============== MAIN MENU ==============")
        print("1. Generate a complete blog")
        print("2. Generate content from a request")
        print("3. Exit")
        print("=======================================")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            create_blog()

        elif choice == "2":
            process_request()

        elif choice == "3":
            print("\nThank you for using BlogGenerator!")
            break

        else:
            print("Invalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()
