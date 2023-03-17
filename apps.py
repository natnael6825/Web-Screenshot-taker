import requests
import io
from PIL import Image
from fpdf import FPDF

# Replace ACCESS_KEY with your actual access key for the screenshotone API
ACCESS_KEY = '3q4hAdr5QmG8Bw'

urls = ['https://gogoanime.gr', 'https://copyassignment.com/run-python-code-install-libraries-create-virtual-environment-vs-code']

pdf = FPDF()
pdf.set_auto_page_break(0)

# Initialize counter variable
counter = 1

for url in urls:
    # Build the request URL with the screenshotone API parameters
    request_url = f'https://api.screenshotone.com/take?url={url}&access_key={ACCESS_KEY}'
    
    # Send the request and get the response
    response = requests.get(request_url)
    
    # Save the image to a file
    with open(f"{counter}.jpg", "wb") as f:
        f.write(response.content)
    
    # Open the image as a PIL image and add it to the PDF
    image = Image.open(io.BytesIO(response.content))
    image_width, image_height = image.size
    pdf.add_page()
    
    # Add image to PDF using the counter variable as the filename
    pdf.image(f"{counter}.jpg", x=0, y=0, w=pdf.w+1, h=pdf.h+1, type='', link='')
    
    # Increment counter variable
    counter += 1

# Save the PDF file
pdf.output('screenshots.pdf', 'F')
