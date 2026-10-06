import os
from PIL import Image, ImageDraw, ImageFont

os.makedirs('assets', exist_ok=True)
os.makedirs('public/media', exist_ok=True)
os.makedirs('output', exist_ok=True)

font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
font_regular_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

def get_fonts():
    if os.path.exists(font_path):
        return {
            'huge': ImageFont.truetype(font_path, 60),
            'header': ImageFont.truetype(font_path, 44),
            'title': ImageFont.truetype(font_path, 34),
            'bold': ImageFont.truetype(font_path, 28),
            'body': ImageFont.truetype(font_regular_path, 24),
            'small': ImageFont.truetype(font_regular_path, 20),
            'badge': ImageFont.truetype(font_path, 22),
        }
    else:
        d = ImageFont.load_default()
        return {'huge': d, 'header': d, 'title': d, 'bold': d, 'body': d, 'small': d, 'badge': d}

fonts = get_fonts()

def generate_scene1_n4():
    img = Image.new('RGB', (1080, 1920), color=(10, 15, 29))
    draw = ImageDraw.Draw(img)

    draw.rounded_rectangle([60, 80, 1020, 170], radius=16, fill=(245, 158, 11))
    draw.text((540, 125), "ONTARIO RTA FORM N4 CALENDAR TRAP", fill=(0, 0, 0), font=fonts['title'], anchor="mm")

    draw.rounded_rectangle([60, 210, 1020, 1840], radius=24, fill=(255, 255, 255), outline=(203, 213, 225), width=3)
    
    draw.rectangle([60, 210, 1020, 340], fill=(15, 23, 42))
    draw.text((100, 250), "Tribunals Ontario", fill=(245, 158, 11), font=fonts['title'])
    draw.text((100, 295), "Landlord and Tenant Board", fill=(255, 255, 255), font=fonts['body'])
    draw.text((980, 275), "FORM N4", fill=(245, 158, 11), font=fonts['huge'], anchor="rm")

    draw.text((540, 380), "Notice to End your Tenancy Early for Non-payment of Rent", fill=(15, 23, 42), font=fonts['title'], anchor="mm")
    draw.line([100, 420, 980, 420], fill=(226, 232, 240), width=2)

    draw.rounded_rectangle([90, 460, 990, 780], radius=16, fill=(254, 242, 242), outline=(239, 68, 68), width=4)
    draw.rounded_rectangle([110, 480, 520, 530], radius=8, fill=(239, 68, 68))
    draw.text((315, 505), "CRITICAL FATAL DEFECT", fill=(255, 255, 255), font=fonts['badge'], anchor="mm")

    draw.text((120, 550), "Termination Date Calculation (Section B):", fill=(185, 28, 28), font=fonts['bold'])
    draw.text((120, 595), "• Day 0 Rule: The date of service does NOT count as Day 1.", fill=(15, 23, 42), font=fonts['body'])
    draw.text((120, 640), "• Hand Delivery: Minimum 14 full clear calendar days.", fill=(15, 23, 42), font=fonts['body'])
    draw.text((120, 685), "• Regular Mail (Rule 3): +5 days for postage = 19 FULL DAYS.", fill=(185, 28, 28), font=fonts['bold'])
    draw.text((120, 730), "• Consequence: 1 day short = Instant L1 Dismissal + 8-month reset.", fill=(15, 23, 42), font=fonts['small'])

    y = 820
    draw.rounded_rectangle([90, y, 990, y + 160], radius=12, fill=(248, 250, 252), outline=(226, 232, 240), width=2)
    draw.text((120, y + 25), "To (Tenant's Name):", fill=(71, 85, 105), font=fonts['small'])
    draw.text((120, y + 60), "John Doe & All Other Occupants", fill=(15, 23, 42), font=fonts['bold'])
    draw.text((120, y + 100), "Rental Unit Address: 104-755 King St W, Toronto, ON M5V 1N3", fill=(51, 65, 85), font=fonts['body'])

    y = 1010
    draw.rounded_rectangle([90, y, 990, y + 360], radius=12, fill=(248, 250, 252), outline=(226, 232, 240), width=2)
    draw.text((120, y + 25), "Termination Date Requirement (Residential Tenancies Act, 2006, s. 59)", fill=(15, 23, 42), font=fonts['bold'])
    
    draw.rounded_rectangle([110, y + 70, 970, y + 180], radius=10, fill=(254, 240, 138), outline=(234, 179, 8), width=3)
    draw.text((130, y + 90), "The termination date must be at least 14 days after notice is given.", fill=(113, 63, 18), font=fonts['bold'])
    draw.text((130, y + 130), "DATE ON FORM: October 15, 2026 (SERVED OCT 1 VIA MAIL)", fill=(185, 28, 28), font=fonts['bold'])

    draw.rounded_rectangle([550, y + 200, 960, y + 330], radius=16, fill=(254, 226, 226), outline=(220, 38, 38), width=4)
    draw.text((755, y + 245), "VOID NOTICE", fill=(220, 38, 38), font=fonts['huge'], anchor="mm")
    draw.text((755, y + 295), "DISMISSED UNDER RTA S. 59", fill=(185, 28, 28), font=fonts['badge'], anchor="mm")

    draw.rounded_rectangle([90, 1400, 990, 1800], radius=16, fill=(15, 23, 42))
    draw.text((540, 1450), "LTB DISMISSAL STATISTIC", fill=(245, 158, 11), font=fonts['title'], anchor="mm")
    draw.text((540, 1510), "Over 34% of self-filed L1 applications are thrown out", fill=(255, 255, 255), font=fonts['bold'], anchor="mm")
    draw.text((540, 1560), "due to arithmetic errors in the 14-day statutory timeline.", fill=(203, 213, 225), font=fonts['body'], anchor="mm")
    draw.text((540, 1640), "DM 'CHECKLIST' FOR FREE PRE-FILING AUDIT", fill=(16, 185, 129), font=fonts['huge'], anchor="mm")
    draw.text((540, 1720), "Ontario Landlord Strategy Overview • Nightly at 8 PM EST", fill=(148, 163, 184), font=fonts['body'], anchor="mm")

    img.save('assets/borrowed_authority_scene1_n4.png')
    img.save('public/media/borrowed_authority_scene1_n4.png')
    print("Generated scene 1 N4 asset!")

def generate_scene2_statute():
    img = Image.new('RGB', (1080, 1920), color=(10, 15, 29))
    draw = ImageDraw.Draw(img)

    draw.rounded_rectangle([60, 80, 1020, 170], radius=16, fill=(59, 130, 246))
    draw.text((540, 125), "ONTARIO e-LAWS STATUTORY AUTHORITY", fill=(255, 255, 255), font=fonts['title'], anchor="mm")

    draw.rounded_rectangle([60, 210, 1020, 1840], radius=24, fill=(255, 255, 255), outline=(203, 213, 225), width=3)

    draw.rectangle([60, 210, 1020, 330], fill=(241, 245, 249))
    draw.text((100, 245), "ONTARIO e-LAWS • OFFICIAL STATUTE", fill=(30, 41, 59), font=fonts['title'])
    draw.text((100, 285), "Residential Tenancies Act, 2006, S.O. 2006, c. 17", fill=(71, 85, 105), font=fonts['body'])

    y = 360
    draw.rounded_rectangle([90, y, 990, y + 420], radius=16, fill=(248, 250, 252), outline=(148, 163, 184), width=2)
    draw.text((120, y + 30), "Section 59(1) — Notice of Termination for Non-payment", fill=(15, 23, 42), font=fonts['title'])
    
    draw.rounded_rectangle([110, y + 80, 970, y + 210], radius=10, fill=(254, 240, 138), outline=(234, 179, 8), width=2)
    draw.text((130, y + 95), "59. (1) If a tenant fails to pay rent lawfully owing under a tenancy", fill=(15, 23, 42), font=fonts['body'])
    draw.text((130, y + 130), "agreement, the landlord may give the tenant notice of termination of the", fill=(15, 23, 42), font=fonts['body'])
    draw.text((130, y + 165), "tenancy demanding payment or vacant possession within 14 days.", fill=(15, 23, 42), font=fonts['bold'])

    draw.text((120, y + 235), "STATUTORY CALCULATION RULE:", fill=(185, 28, 28), font=fonts['bold'])
    draw.text((120, y + 275), "• Day of delivery = Day 0 (Excluded under Interpretation Act)", fill=(15, 23, 42), font=fonts['body'])
    draw.text((120, y + 315), "• Count starts NEXT morning at 12:01 AM", fill=(15, 23, 42), font=fonts['body'])
    draw.text((120, y + 355), "• If 14th day falls on a holiday/weekend: extends to next business day", fill=(15, 23, 42), font=fonts['body'])

    y = 810
    draw.rounded_rectangle([90, y, 990, y + 420], radius=16, fill=(239, 246, 255), outline=(59, 130, 246), width=3)
    draw.rounded_rectangle([110, y + 25, 450, y + 75], radius=8, fill=(59, 130, 246))
    draw.text((280, y + 50), "LTB RULE OF PROCEDURE 3", fill=(255, 255, 255), font=fonts['badge'], anchor="mm")
    
    draw.text((120, y + 95), "Rule 3.3 — Service by Regular / Registered Mail:", fill=(30, 58, 138), font=fonts['bold'])
    
    draw.rounded_rectangle([110, y + 135, 970, y + 255], radius=10, fill=(254, 240, 138), outline=(234, 179, 8), width=2)
    draw.text((130, y + 155), "\"Service by mail is deemed to be given on the FIFTH DAY", fill=(185, 28, 28), font=fonts['huge'])
    draw.text((130, y + 215), "following the date of mailing.\"", fill=(185, 28, 28), font=fonts['title'])

    draw.text((120, y + 280), "Calculation formula: [Mailing Date] + 5 Days + 14 Days = 19 Days", fill=(15, 23, 42), font=fonts['bold'])
    draw.text((120, y + 325), "Example: Mailed Oct 1 -> Deemed Oct 6 -> 14 Days -> Termination Oct 20", fill=(30, 58, 138), font=fonts['body'])
    draw.text((120, y + 365), "If you wrote Oct 15: Your case is INVALID.", fill=(220, 38, 38), font=fonts['bold'])

    y = 1260
    draw.rounded_rectangle([90, y, 990, 1800], radius=16, fill=(15, 23, 42))
    draw.text((540, y + 60), "PROTECT YOUR TIME & RENT ARREARS", fill=(245, 158, 11), font=fonts['title'], anchor="mm")
    draw.text((540, y + 130), "Do not let a $2.50 calendar oversight cost you", fill=(255, 255, 255), font=fonts['bold'], anchor="mm")
    draw.text((540, y + 180), "8 months of unpaid rent at the LTB.", fill=(203, 213, 225), font=fonts['body'], anchor="mm")
    
    draw.rounded_rectangle([140, y + 230, 940, y + 330], radius=14, fill=(16, 185, 129))
    draw.text((540, y + 280), "DM 'CHECKLIST' FOR INSTANT AUDIT", fill=(255, 255, 255), font=fonts['huge'], anchor="mm")
    
    draw.text((540, y + 390), "Free LTB Timeline Verification Sheet • Strategy Call 8 PM EST", fill=(148, 163, 184), font=fonts['body'], anchor="mm")

    img.save('assets/borrowed_authority_scene2_statute.png')
    img.save('public/media/borrowed_authority_scene2_statute.png')
    print("Generated scene 2 statute asset!")

def generate_scene3_checklist():
    img = Image.new('RGB', (1080, 1920), color=(10, 15, 29))
    draw = ImageDraw.Draw(img)

    draw.rounded_rectangle([60, 80, 1020, 170], radius=16, fill=(16, 185, 129))
    draw.text((540, 125), "ONTARIO LTB PRE-FILING VERIFICATION", fill=(255, 255, 255), font=fonts['title'], anchor="mm")

    draw.rounded_rectangle([60, 210, 1020, 1840], radius=24, fill=(255, 255, 255), outline=(203, 213, 225), width=3)

    draw.rectangle([60, 210, 1020, 330], fill=(15, 23, 42))
    draw.text((540, 250), "OFFICIAL PRE-FILING AUDIT CHECKLIST", fill=(245, 158, 11), font=fonts['title'], anchor="mm")
    draw.text((540, 290), "5 Critical Steps Before Submitting Form L1 / L2 to Tribunals Ontario", fill=(255, 255, 255), font=fonts['body'], anchor="mm")

    items = [
        ("1. Exact Service Method Verification", "Confirm Hand Delivery (14d), Mail (+5d=19d), or Approved Email Consent Form."),
        ("2. Day 0 Calendar Exclusion", "Verify service date is excluded from calculation. Count begins at 12:01 AM next day."),
        ("3. Rent Ledger Reconciliation", "Ensure only lawful monthly rent arrears are included (exclude utilities & late fees)."),
        ("4. Certificate of Service (Form COS)", "Complete Form COS simultaneously with precise timestamp and delivery details."),
        ("5. Nightly LTB Strategy Audit", "Have your notice pre-audited before paying the $186 non-refundable LTB fee.")
    ]

    y = 360
    for i, (title, desc) in enumerate(items):
        draw.rounded_rectangle([90, y, 990, y + 140], radius=14, fill=(248, 250, 252), outline=(203, 213, 225), width=2)
        draw.rounded_rectangle([115, y + 35, 185, y + 105], radius=10, fill=(16, 185, 129))
        draw.text((150, y + 70), "✓", fill=(255, 255, 255), font=fonts['huge'], anchor="mm")
        draw.text((210, y + 35), title, fill=(15, 23, 42), font=fonts['bold'])
        draw.text((210, y + 75), desc, fill=(71, 85, 105), font=fonts['small'])
        y += 160

    draw.rounded_rectangle([90, 1200, 990, 1800], radius=20, fill=(15, 23, 42), outline=(245, 158, 11), width=3)
    draw.text((540, 1260), "CLAIM YOUR FREE CHECKLIST NOW", fill=(245, 158, 11), font=fonts['huge'], anchor="mm")
    
    draw.rounded_rectangle([130, 1320, 950, 1440], radius=16, fill=(16, 185, 129))
    draw.text((540, 1380), "💬 DM 'CHECKLIST' OR TAP BIO", fill=(255, 255, 255), font=fonts['huge'], anchor="mm")

    draw.text((540, 1490), "• Instant PDF Download to your phone", fill=(255, 255, 255), font=fonts['bold'], anchor="mm")
    draw.text((540, 1540), "• Pass to Nightly Landlord Strategy Overview (8 PM EST)", fill=(203, 213, 225), font=fonts['body'], anchor="mm")
    draw.text((540, 1590), "• Avoid 8-month tribunal hearing dismissals", fill=(203, 213, 225), font=fonts['body'], anchor="mm")
    
    draw.rounded_rectangle([130, 1640, 950, 1750], radius=14, fill=(30, 41, 59))
    draw.text((540, 1695), "100% Free Educational Tool for Ontario Landlords", fill=(245, 158, 11), font=fonts['title'], anchor="mm")

    img.save('assets/borrowed_authority_scene3_checklist.png')
    img.save('public/media/borrowed_authority_scene3_checklist.png')
    print("Generated scene 3 checklist asset!")

if __name__ == '__main__':
    generate_scene1_n4()
    generate_scene2_statute()
    generate_scene3_checklist()
