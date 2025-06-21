import pandas as pd
import textwrap
from fastapi.responses import JSONResponse

CSV_FILE_PATH = "KPI_Data/Influence_Attribution.csv"

def generate_mentions_by_platform_json():
    df = pd.read_csv(CSV_FILE_PATH)

    if 'Mentioned Platform' not in df.columns or 'Influence Source Type' not in df.columns:
        raise ValueError("Required columns 'Mentioned Platform' or 'Influence Source Type' not found in CSV")

    # Group and wrap
    grouped = df.groupby('Mentioned Platform')['Influence Source Type'].apply(list).to_dict()
    wrapped_mentions = {}
    wrap_width = 30

    for platform, mentions in grouped.items():
        wrapped_text_lines = []
        for mention in mentions:
            wrapped_lines = textwrap.wrap(mention, width=wrap_width)
            wrapped_text_lines.extend(wrapped_lines)
        wrapped_mentions[platform] = wrapped_text_lines

    return JSONResponse(content=wrapped_mentions)
