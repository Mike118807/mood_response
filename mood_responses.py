# Task 1: Your Mood Today

def mood_response(mood):
    responses = {
        "happy": "I'm glad to hear you're happy! Keep smiling!",
        "sad": "I'm sorry you're feeling sad. I hope things get better soon.",
        "excited": "That's awesome! Excitement is contagious!",
        "angry": "It's okay to feel angry sometimes. Take a deep breath and try to relax.",
        "tired": "Make sure to get some rest. You deserve it!"
    }
    return responses.get(mood.lower(), "I see. I'm here to chat if you need anything.")










