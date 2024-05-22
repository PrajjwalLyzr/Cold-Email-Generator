from lyzr import Generator
import os


def save_api_key(key):
    with open("api_key.txt", "w") as file:
        file.write(key)

def email_generator(API_KEY, prospect_name, company_information, prodcut_service_info, outcome):
    generator = Generator(api_key=API_KEY)
    email = generator.generate(text='Generate a personalized cold email', 
                               instructions=f"""Craft a compelling email body that:
                                                    - Subject Line: Generate attention-grabbing subject lines that mention the prospect's name:{prospect_name} or prospect company:{company_information} and highlight a relevant benefit.
                                                    - Salutation: Use the prospect's name:{prospect_name} and appropriate title for a personalized greeting.
                                                    - Highlights how the sender's product/service:{prodcut_service_info} can address that challenge and benefit the prospect's company.
                                                    - Includes a clear call to action (CTA) prompting the desired outcome: {outcome}.
                                                    - Tone and Style Consistency: Ensure the generated email maintains a professional and courteous tone while aligning with the user's overall communication style.
                                            """)
    
    return email


