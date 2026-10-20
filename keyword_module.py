
import ollama


def generate_keywords(topic, blog):
    """Generate SEO-friendly keywords for a blog."""

    prompt = f"""
    Generate 10 relevant SEO-friendly keywords for the following blog.

    Topic: {topic}

    Blog content:
    {blog[:3000]}

    Requirements:
    - Include short keywords and relevant search phrases.
    - Avoid duplicate keywords.
    - Number the keywords from 1 to 10.
    - Output only the keywords.
    """

    print("\nGenerating SEO Keywords...")

    try:
        response = ollama.chat(
            model="qwen2.5:0.5b",
            messages=[
                {"role": "user", "content": prompt}
            ],
            options={"num_predict": 150}
        )

        keywords = response["message"]["content"].strip()

        print("\nSEO Keywords\n")
        print(keywords)

        return keywords

    except Exception as error:
        print(f"Error generating keywords: {error}")
        return None
