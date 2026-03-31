import logging

logger = logging.getLogger(__name__)

def suggest_priority(description: str) -> str:
    """
    Simulates calling an AI to suggest a priority based on the task description.
    In a real scenario, this would call OpenAI or Gemini via HTTP.
    
    Rules for fallback:
    - Return 'LOW', 'MEDIUM', or 'HIGH'
    - Handle any exceptions internally so it never breaks the core system
    """
    if not description:
        return 'LOW'
        
    try:
        desc_lower = description.lower()
        if 'urgent' in desc_lower or 'asap' in desc_lower or 'immediate' in desc_lower:
            return 'HIGH'
        elif 'soon' in desc_lower or 'important' in desc_lower:
            return 'MEDIUM'
        
        # Simulated AI API call that could fail
        # This code simulates a successful AI text generation fallback
        return 'LOW'
    except Exception as e:
        logger.error(f"AI priority suggestion failed: {e}")
        return 'LOW' # Safe fallback
