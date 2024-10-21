import openai
import os

def generate_story(prompt, characters, scene):
    openai.api_key = os.environ.get('OPENAI_API_KEY')
    if not openai.api_key:
        raise ValueError("OpenAI API key not found in environment variables")
    
    try:
        full_prompt = f"""
        Generate a short manga story based on the following:
        Prompt: {prompt}
        Characters: {', '.join(characters)}
        Scene: {scene}

        The story should be engaging, incorporate the given characters, and take place in the described scene.
        """

        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=full_prompt,
            max_tokens=1000,
            n=1,
            stop=None,
            temperature=0.8,
        )
        return response.choices[0].text.strip()
    except openai.error.OpenAIError as e:
        raise RuntimeError(f"OpenAI API error: {str(e)}")
