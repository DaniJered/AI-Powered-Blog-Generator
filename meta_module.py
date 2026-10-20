
import ollama


def generate_meta_description(topic, blog):
    """Generate an SEO meta description within 160 characters."""

    prompt = f"""
    Write one SEO-friendly meta description for this blog.

    Topic: {topic}
    Blog content:
    {blog[:3000]}

    Requirements:
    - Maximum 150 characters.
    - Include the main topic naturally.
    - Make it informative and attractive.
    - Return only the description.
    """

    print("\nGenerating SEO Meta Description...")

    try:
        response = ollama.chat(
            model="qwen2.5:0.5b",
            messages=[
                {"role": "user", "content": prompt}
            ],
            options={"num_predict": 80}
        )

        description = response["message"]["content"].strip()
        description = description.strip('"').strip("'")
        description = " ".join(description.split())

        # Enforce the character limit in Python.
        if len(description) > 160:
            description = description[:157].rsplit(" ", 1)[0] + "..."

        print("\nMeta Description\n")
        print(description)
        print(f"Character count: {len(description)}")

        return description

    except Exception as error:
        print(f"Error generating meta description: {error}")
        return None
