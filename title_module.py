
import ollama


def generate_titles(topic, blog):
    """Generate five attractive titles for a blog."""

    prompt = f"""
    Based on the following blog topic and content, generate exactly
    five attractive, relevant blog titles.

    Topic: {topic}

    Blog content:
    {blog[:3000]}

    Requirements:
    - Generate exactly five titles.
    - Make each title engaging and relevant.
    - Number the titles from 1 to 5.
    - Output only the numbered titles.
    """

    print("\nGenerating Blog Titles...")

    try:
        response = ollama.chat(
            model="qwen2.5:0.5b",
            messages=[
                {"role": "user", "content": prompt}
            ],
            options={"num_predict": 200}
        )

        titles = response["message"]["content"].strip()
        print("\nSuggested Titles\n")
        print(titles)

        return titles

    except Exception as error:
        print(f"Error generating titles: {error}")
        return None
