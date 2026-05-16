import google.generativeai as genai
from dotenv import load_dotenv
import logging
import os

load_dotenv()

logger = logging.getLogger(__name__)

API_KEY = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-pro")


async def ask_gemini(prompt: str) -> str:
    try:
            response = model.generate_content(prompt)
                    return response.text
                        except Exception as e:
                                logger.error(f"Gemini error: {e}")
                                        return f"Error: {str(e)}"