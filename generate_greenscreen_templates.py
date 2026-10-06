import os
from PIL import Image, ImageDraw, ImageFont

os.makedirs('assets', exist_ok=True)
os.makedirs('public/media', exist_ok=True)
os.makedirs('output', exist_ok=True)

WIDTH = 1080
HEIGHT = 1920

font_bold = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
font_reg = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

def get_fonts():
    return {
        'super_hook': ImageFont.truetype(font_bold, 64),
        'hook_sub': ImageFont.truetype(font_bold, 54),
        'doc_gov': ImageFont.truetype(font_bold, 36),
        'doc_sub': ImageFont.truetype(font_bold, 28),
        'doc_title': ImageFont.truetype(font_bold, 42),
        'bullet_title': ImageFont.truetype(font_bold, 32),
        'bullet_body': ImageFont.truetype(font_reg, 28),
        'badge': ImageFont.truetype(font_bold, 24),
    }

fonts = get_fonts()

def create_unannounced_entry_template():
    # 1080x1920 Canvas
    img = Image.new('RGB', (WIDTH, HEIGHT), color=(10, 15, 29))
    draw = ImageDraw.Draw(img)

    # Top Hook Section (Matching Reference Style Exactly)
    draw.text((WIDTH // 2, 90), "Your landlord walked", fill=(255, 255, 255), font=fonts['super_hook'], anchor="mm")
    draw.text((WIDTH // 2, 175), "in unannounced?", fill=(255, 255, 255), font=fonts['super_hook'], anchor="mm")
    draw.text((WIDTH // 2, 265), "Here's what the RTA", fill=(245, 158, 11), font=fonts['hook_sub'], anchor="mm")
    draw.text((WIDTH // 2, 335), "actually says.", fill=(255, 255, 255), font=fonts['hook_sub'], anchor="mm")

    # Document Container Card (White government document feel)
    doc_top = 400
    doc_bottom = 1450
    draw.rounded_rectangle([40, doc_top, WIDTH - 40, doc_bottom], radius=24, fill=(255, 255, 255), outline=(203, 213, 225), width=3)

    # ontario.ca Official Header Bar
    draw.rectangle([40, doc_top, WIDTH - 40, doc_top + 130], fill=(248, 250, 252))
    draw.text((70, doc_top + 35), "ontario.ca", fill=(15, 23, 42), font=fonts['doc_gov'])
    draw.text((70, doc_top + 80), "Residential Tenancies Act (RTA)", fill=(2, 132, 199), font=fonts['doc_sub'])
    draw.line([70, doc_top + 115, 520, doc_top + 115], fill=(2, 132, 199), width=3)

    # Document Title
    y = doc_top + 160
    draw.text((70, y), "ENTRY TO RENTAL UNIT", fill=(15, 23, 42), font=fonts['doc_title'])
    draw.line([70, y + 55, WIDTH - 70, y + 55], fill=(226, 232, 240), width=2)

    # Bullet Point 1: 24 Hour Written Notice
    y += 85
    draw.ellipse([70, y + 10, 90, y + 30], fill=(15, 23, 42))
    draw.text((110, y), "24 HOUR WRITTEN NOTICE REQUIRED", fill=(185, 28, 28), font=fonts['bullet_title'])
    draw.text((110, y + 42), "for landlord entry into the rental unit", fill=(71, 85, 105), font=fonts['bullet_body'])

    # Bullet Point 2: Notice Must Include
    y += 115
    draw.ellipse([70, y + 10, 90, y + 30], fill=(15, 23, 42))
    draw.text((110, y), "NOTICE MUST INCLUDE:", fill=(15, 23, 42), font=fonts['bullet_title'])
    draw.text((110, y + 42), "• Specific reason for entry (repairs / inspection)", fill=(51, 65, 85), font=fonts['bullet_body'])
    draw.text((110, y + 80), "• Exact entry window (between 8:00 AM – 8:00 PM)", fill=(51, 65, 85), font=fonts['bullet_body'])

    # Bullet Point 3: Exceptions (Emergency Only)
    y += 150
    # Highlight Box around Exception
    draw.rounded_rectangle([70, y - 10, WIDTH - 70, y + 150], radius=12, fill=(254, 242, 242), outline=(239, 68, 68), width=2)
    draw.text((95, y + 10), "EXCEPTION: NO NOTICE REQUIRED ONLY IF:", fill=(185, 28, 28), font=fonts['bullet_title'])
    draw.text((95, y + 55), "1. Immediate emergency (fire, flooding, gas leak)", fill=(15, 23, 42), font=fonts['bullet_body'])
    draw.text((95, y + 95), "2. Tenant consents to entry at that exact moment", fill=(15, 23, 42), font=fonts['bullet_body'])

    # Statutory fine note
    y += 185
    draw.text((70, y), "Penalty for Illegal Entry (RTA s. 234):", fill=(71, 85, 105), font=fonts['bullet_title'])
    draw.text((70, y + 42), "Up to $50,000 fine for individual landlord / T2 LTB remedy.", fill=(15, 23, 42), font=fonts['bullet_body'])

    # Lower Third Green Screen Anchor Silhouette Placeholder
    draw.rounded_rectangle([WIDTH - 480, HEIGHT - 550, WIDTH - 40, HEIGHT - 40], radius=24, fill=(15, 23, 42), outline=(245, 158, 11), width=3)
    draw.text((WIDTH - 260, HEIGHT - 310), "👤 ALVIN CUFFY", fill=(245, 158, 11), font=fonts['doc_title'], anchor="mm")
    draw.text((WIDTH - 260, HEIGHT - 250), "Green Screen Subject Zone", fill=(203, 213, 225), font=fonts['badge'], anchor="mm")
    draw.text((WIDTH - 260, HEIGHT - 210), "Pointing up at 24-hr clause 👆", fill=(148, 163, 184), font=fonts['badge'], anchor="mm")

    # Bottom CTA Pill (Left of Subject)
    draw.rounded_rectangle([40, HEIGHT - 260, WIDTH - 510, HEIGHT - 60], radius=20, fill=(16, 185, 129))
    draw.text((280, HEIGHT - 185), "💬 DM 'ENTRY'", fill=(255, 255, 255), font=fonts['doc_title'], anchor="mm")
    draw.text((280, HEIGHT - 120), "For Free Tenant Illegal Entry Guide", fill=(255, 255, 255), font=fonts['badge'], anchor="mm")

    img.save('assets/greenscreen_template_unannounced_entry.png')
    img.save('public/media/greenscreen_template_unannounced_entry.png')
    print("Generated Unannounced Entry Green Screen Template!")

def create_why_still_landlord_template():
    img = Image.new('RGB', (WIDTH, HEIGHT), color=(10, 15, 29))
    draw = ImageDraw.Draw(img)

    # Top Hook Section
    draw.text((WIDTH // 2, 90), "Ontario Landlords...", fill=(245, 158, 11), font=fonts['super_hook'], anchor="mm")
    draw.text((WIDTH // 2, 175), "Why are you still", fill=(255, 255, 255), font=fonts['super_hook'], anchor="mm")
    draw.text((WIDTH // 2, 260), "doing this?", fill=(239, 68, 68), font=fonts['super_hook'], anchor="mm")

    # Document Container Card
    doc_top = 340
    doc_bottom = 1380
    draw.rounded_rectangle([40, doc_top, WIDTH - 40, doc_bottom], radius=24, fill=(255, 255, 255), outline=(203, 213, 225), width=3)

    # Header
    draw.rectangle([40, doc_top, WIDTH - 40, doc_top + 130], fill=(15, 23, 42))
    draw.text((70, doc_top + 35), "Tribunals Ontario", fill=(245, 158, 11), font=fonts['doc_gov'])
    draw.text((70, doc_top + 80), "Landlord and Tenant Board Arrears Realities", fill=(255, 255, 255), font=fonts['doc_sub'])

    # Shock Realities
    y = doc_top + 160
    draw.text((70, y), "THE ONTARIO RENTAL MATH (2026)", fill=(185, 28, 28), font=fonts['doc_title'])
    draw.line([70, y + 50, WIDTH - 70, y + 50], fill=(226, 232, 240), width=2)

    y += 80
    items = [
        ("Average LTB Hearing Delay", "8 to 10 Months before first adjudicator review."),
        ("Tribunal Compensation Cap", "Maximum order capped at $35,000 (even if arrears exceed $60K)."),
        ("The 'Fatal Defect' Rule", "1 single calculation error on Form N4 resets the entire 8-month wait."),
        ("Small Claims Limit", "Excess arrears require separate civil court enforcement.")
    ]

    for title, desc in items:
        draw.rounded_rectangle([70, y, WIDTH - 70, y + 105], radius=12, fill=(248, 250, 252), outline=(226, 232, 240), width=2)
        draw.text((95, y + 18), f"⚠️ {title}:", fill=(185, 28, 28), font=fonts['bullet_title'])
        draw.text((95, y + 58), desc, fill=(51, 65, 85), font=fonts['bullet_body'])
        y += 125

    # Bottom Area for Alvin's Hands-on-Head Shocked Pose
    draw.rounded_rectangle([WIDTH // 2 - 240, HEIGHT - 520, WIDTH // 2 + 240, HEIGHT - 40], radius=24, fill=(15, 23, 42), outline=(239, 68, 68), width=3)
    draw.text((WIDTH // 2, HEIGHT - 300), "👤 ALVIN CUFFY", fill=(255, 255, 255), font=fonts['doc_title'], anchor="mm")
    draw.text((WIDTH // 2, HEIGHT - 240), "Shocked Reaction Zone (Hands to Head)", fill=(245, 158, 11), font=fonts['badge'], anchor="mm")
    draw.text((WIDTH // 2, HEIGHT - 190), "Looking into camera: 'Drop your thoughts below'", fill=(148, 163, 184), font=fonts['badge'], anchor="mm")

    img.save('assets/greenscreen_template_why_still_landlord.png')
    img.save('public/media/greenscreen_template_why_still_landlord.png')
    print("Generated Why Are You Still A Landlord Green Screen Template!")

if __name__ == '__main__':
    create_unannounced_entry_template()
    create_why_still_landlord_template()
