import pandas as pd
from openai import OpenAI

client = OpenAI()

# Load your spreadsheet
df = pd.read_excel("leads.xlsx")

# Function to generate AI output
def generate_outreach(row):
    prompt = f"""
    You are a sales assistant for a boxing gym.

    Lead info:
    Name: {row.get('Name', '')}
    Notes: {row.get('Notes', '')}

    Based on this, generate:
    1. Intent level (High, Medium, Low)
    2. Short customer profile
    3. Main pain point
    4. A personalized outreach message (friendly, natural, not salesy, 2-3 sentences max, invite them to a free session)

    Format:
    Intent:
    Profile:
    Pain Point:
    Message:
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )

    return response.choices[0].message.content

# Apply to each row
outputs = []
for _, row in df.head(5).iterrows():
    result = generate_outreach(row)
    outputs.append(result)

# Save results
df["AI_Output"] = outputs
df.to_excel("enriched_leads.xlsx", index=False)

print("Done. Check enriched_leads.xlsx")