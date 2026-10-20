
import ollama


def generate_blog(topic, style, tone, word_count):
    """Generate a complete blog using the local Ollama model."""

    prompt = f"""
    Write a complete blog about: {topic}

    Requirements:
    - Writing style: {style}
    - Tone: {tone}
    - Approximate word count: {word_count} words
    - Include an engaging title
    - Include an introduction
    - Explain the main topic using clear paragraphs
    - Include relevant headings
    - Include a conclusion
    - Write original, informative content
    - Do not include unnecessary commentary

    Generate only the blog content.
    """

    print("\nGenerating Blog using Ollama...")
    print("-" * 60)

    try:
        response = ollama.chat(
            model="qwen2.5:0.5b",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        blog = response["message"]["content"].strip()

        print("\n" + blog)
        print("\n" + "-" * 60)

        return blog

    except Exception as error:
        print("\nError generating blog:", error)
        print("Check that Ollama is running and llama3.2 is installed.")
        return None
