from PIL import Image
from google import genai

client = genai.Client(api_key="AIzaSyCq84fCMDrHedjuDrQ6PXmsR_tiCSJ8QTU")

image = Image.open("/Users/cc/workspace/images/ggb.jpeg")
response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=[image, "Tell me about this bridge?"]
    )
print(response.text)