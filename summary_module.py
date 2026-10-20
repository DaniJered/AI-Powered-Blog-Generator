
import ollama


def generate_summary(blog):
    """Generate a concise summary of approximately 100 words."""

    prompt = f"""
Summarize this blog in approximately 100 words.

Return ONLY one short paragraph.
Do not include a title, introduction, headings, bullet points,
references, explanations, or the original blog.

BLOG:
{blog[:4000]}
"""

    print("\nGenerating Blog Summary...")

    try:
        response = ollama.chat(
            model="qwen2.5:0.5b",
            messages=[
                {"role": "user", "content": prompt}
            ],
            options={
                "num_predict": 140,
                "temperature": 0.3
            }
        )

        summary = response["message"]["content"].strip()

        print("\nBlog Summary\n")
        print(summary)

        return summary

    except Exception as error:
        print(f"Error generating summary: {error}")
        return None
