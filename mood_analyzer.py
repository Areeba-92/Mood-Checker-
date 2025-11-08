# mood_analyzer.py (FIXED VERSION)

import re

def analyze_mood(text):
    """
    Analyzes the user's text to determine their mood and returns a
    motivational message.
    """
    text = text.lower()

    positive_keywords = [
    "happy", "joy", "good", "wonderful", "awesome", "great", "fantastic",
    "amazing", "love", "like", "beautiful", "charming", "cheerful",
    "delightful", "excellent", "perfect", "superb", "thrilled", "excited",
    "content", "satisfied", "peaceful", "grateful", "thankful", "blessed",
    "optimistic", "hopeful", "positive", "motivated", "inspired", "proud",
    "energetic", "enthusiastic", "joyful", "ecstatic", "glad", "pleased",
    "smiling", "radiant", "vibrant", "marvelous", "brilliant", "outstanding",
    "spectacular", "terrific", "fun", "enjoy", "sweet", "nice", "kind",
    "friendly", "supportive", "helpful", "amused", "laughing", "elated",
    "heavenly", "fabulous", "overjoyed", "refreshing", "breezy", "sunny",
    "lively", "awesome", "strong", "confident", "balanced", "relaxed",
    "peaceful", "safe", "comfortable", "glorious", "magnificent"
    ]


    negative_keywords = [
    "sad", "bad", "terrible", "horrible", "awful", "cry", "depressed",
    "angry", "hate", "dislike", "ugly", "boring", "dull", "miserable",
    "poor", "stressed", "unhappy", "anxious", "lonely", "frustrated",
    "upset", "disappointed", "hurt", "regret", "gloomy", "fearful",
    "overwhelmed", "tired", "exhausted", "hopeless", "annoyed"
    ]

    motivational_keywords = [
    "motivated", "inspired", "determined", "ready", "focused", "ambitious",
    "driven", "enthusiastic", "powerful", "unstoppable", "confident",
    "strong", "resilient", "courageous", "brave", "persistent", "optimistic",
    "energetic", "accomplished", "capable"
    ]

    negations = [
    "not", "no", "never", "don't", "doesn't", "isn't", "aren't", "wasn't",
    "weren't", "haven't", "hasn't", "hadn't", "can't", "couldn't", "won't",
    "wouldn't", "shouldn't", "mightn't", "mustn't"
     ]

    score = 0
    mood = "neutral"
    message = "Thanks for sharing. Every feeling is valid."

    # Function to check for whole word matches
    def word_in_text(word, text):
        return bool(re.search(r'\b' + word + r'\b', text))

    # Check for negations
    has_negation = any(word_in_text(neg, text) for neg in negations)

    # Calculate score
    positive_count = sum(1 for word in positive_keywords if word_in_text(word, text))
    negative_count = sum(1 for word in negative_keywords if word_in_text(word, text))
    
    score = positive_count - negative_count

    # Adjust score for negations (flip it)
    if has_negation and score > 0:
        score = -score

    # Determine mood based on score
    if score > 0:
        mood = "positive"
        message = "That's great to hear! Keep shining."
    elif score < 0:
        mood = "negative"
        message = "I'm sorry to hear that. Better days are coming."
    else:  # score == 0
        # Check for motivational keywords only if mood is neutral
        is_motivational = any(word_in_text(word, text) for word in motivational_keywords)
        if is_motivational:
            mood = "motivational"
            message = "You've got this! Go and conquer your goals."

    return mood, message