import openai
import os

def generate_story(prompt):
    openai.api_key = os.environ.get('OPENAI_API_KEY')
    if not openai.api_key:
        raise ValueError("OpenAI API key not found in environment variables")
    
    try:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"Generate a short manga story based on the following prompt: {prompt}",
            max_tokens=500,
            n=1,
            stop=None,
            temperature=0.7,
        )
        return response.choices[0].text.strip()
    except openai.error.OpenAIError as e:
        raise RuntimeError(f"OpenAI API error: {str(e)}")
