from transformers import pipeline
import torch
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.preprocessing import MinMaxScaler
import numpy as np

# Download required NLTK data
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

class TextAnalyzer:
    def __init__(self):
        # Initialize sentiment analysis pipeline
        self.sentiment_analyzer = pipeline("sentiment-analysis")
        self.stop_words = set(stopwords.words('english'))
        self.scaler = MinMaxScaler()
        
    def analyze_text_density(self, text: str) -> float:
        """Analyze text density based on word count and length."""
        # Simple word tokenization
        words = text.split()
        words = [w for w in words if w.lower() not in self.stop_words]
        return len(words) / max(len(text.split()), 1)
    
    def optimize_text_position(self, text: str, template_positions):
        """Optimize text position based on content analysis."""
        # Analyze text characteristics
        density = self.analyze_text_density(text)
        sentiment = self.sentiment_analyzer(text)[0]
        sentiment_score = sentiment['score'] if sentiment['label'] == 'POSITIVE' else -sentiment['score']
        
        # Create feature vector
        features = np.array([[density, sentiment_score]])
        scaled_features = self.scaler.fit_transform(features)
        
        # Select best position based on features
        if scaled_features[0][0] > 0.7:  # High density text
            # Prefer positions with more space
            return max(template_positions, key=lambda p: p.max_width_ratio)
        elif scaled_features[0][1] > 0.5:  # Positive sentiment
            # Prefer lower positions for positive sentiment
            return min(template_positions, key=lambda p: p.y_ratio)
        else:  # Negative sentiment or neutral
            # Prefer upper positions
            return max(template_positions, key=lambda p: p.y_ratio)
    
    def calculate_optimal_font_size(self, text: str, image_height: int) -> float:
        """Calculate optimal font size ratio based on text analysis."""
        # Analyze text characteristics
        words = text.split()
        word_count = len(words)
        max_word_length = max(len(word) for word in words) if words else 0
        
        # Calculate base size based on text length and word characteristics
        if word_count <= 2 and max_word_length <= 6:
            base_size = 0.15  # Larger text for short, punchy phrases
        elif word_count <= 4:
            base_size = 0.12  # Medium text for typical meme phrases
        else:
            base_size = 0.1   # Smaller text for longer phrases
            
        # Adjust for ALL CAPS (typical in memes)
        if text.isupper():
            base_size *= 0.9  # Slightly reduce size for all caps
            
        # Adjust for long words
        if max_word_length > 10:
            base_size *= 0.85  # Reduce size for very long words
            
        return base_size
    
    def suggest_template(self, text: str, available_templates: dict) -> str:
        """Suggest best template based on text content."""
        sentiment = self.sentiment_analyzer(text)[0]
        
        # Initialize template scores with base values
        template_scores = {tid: 0.1 for tid in available_templates}
        
        # Analyze text patterns
        has_comparison = any(x in text.lower() for x in [' vs ', ' versus ', ' or ', ' but ', 'instead of', 'better than'])
        is_achievement = any(x in text.lower() for x in ['finally', 'when', 'succeeded', 'managed to', 'did it'])
        has_exclamation = '!' in text
        word_count = len(text.split())
        has_questions = any(x in text.lower() for x in ['is this', 'what if', 'why is', 'how come'])
        has_progression = len(text.split('\n')) >= 3  # Text has multiple lines for progression
        has_disaster = any(x in text.lower() for x in ['disaster', 'chaos', 'burn', 'destroy', 'mess'])
        has_irony = any(x in text.lower() for x in ['actually', 'supposedly', 'apparently', 'meanwhile'])
        
        for template_id in available_templates:
            if 'success' in template_id.lower():
                # Success Kid works well for achievements and positive sentiment
                if is_achievement:
                    template_scores[template_id] += 0.4
                if sentiment['label'] == 'POSITIVE':
                    template_scores[template_id] += sentiment['score']
                if has_exclamation:
                    template_scores[template_id] += 0.2
                    
            elif 'drake' in template_id.lower():
                # Drake template works well for comparisons and choices
                if has_comparison:
                    template_scores[template_id] += 0.6
                if word_count >= 8:  # Drake works well with more text
                    template_scores[template_id] += 0.2
                    
            elif 'doge' in template_id.lower():
                # Doge works well for quirky or internet-speak content
                if any(x in text.lower() for x in ['wow', 'such', 'very', 'much', 'many']):
                    template_scores[template_id] += 0.7
                if len(text.split('\n')) > 1:  # Doge works well with multiple lines
                    template_scores[template_id] += 0.3
                    
            elif 'expanding_brain' in template_id.lower():
                # Expanding Brain works well for progressions and ironically "smart" ideas
                if has_progression:
                    template_scores[template_id] += 0.8
                if has_irony:
                    template_scores[template_id] += 0.3
                    
            elif 'disaster_girl' in template_id.lower():
                # Disaster Girl works well for chaotic or destructive scenarios
                if has_disaster:
                    template_scores[template_id] += 0.8
                if sentiment['label'] == 'NEGATIVE':
                    template_scores[template_id] += 0.3
                    
            elif 'distracted' in template_id.lower():
                # Distracted Boyfriend works well for three-way comparisons
                if text.count(',') >= 2 or text.count('\n') >= 2:
                    template_scores[template_id] += 0.7
                if has_irony:
                    template_scores[template_id] += 0.3
                    
            elif 'hide_pain' in template_id.lower():
                # Hide the Pain Harold works well for ironic or painful situations
                if sentiment['label'] == 'POSITIVE' and has_irony:
                    template_scores[template_id] += 0.8
                if 'inside' in text.lower() or 'pain' in text.lower():
                    template_scores[template_id] += 0.3
                    
            elif 'is_this' in template_id.lower():
                # Is This a Pigeon works well for misidentifications and rhetorical questions
                if has_questions:
                    template_scores[template_id] += 0.7
                if has_irony:
                    template_scores[template_id] += 0.3
        
        # Return template with highest score
        return max(template_scores.items(), key=lambda x: x[1])[0]
