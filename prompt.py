'''prompt module'''


class Prompt:
    '''Prompt'''
    @staticmethod
    def get_prompt(memories):
        '''Returns the prompt for the given topic'''
        prompt = f"""You are an expert at crafting captivating captions for pictures, tailored for sharing across various social media platforms.

        Input Details:

        The user will provide a picture along with some memories or context related to the image.
        Based on these inputs, generate 2-3 unique and engaging captions that resonate with the emotions and story behind the picture.
        Memory-Based Captions:

        If memories or context are provided, ensure the captions reflect these sentiments, making the post meaningful and personal.
        Image-Driven Captions:

        If no memories are provided, analyze the picture carefully. Then, create captions that capture its essence, mood, or any notable elements.
        Memories Provided: {memories}

        Your Captions:
        """
        return prompt
