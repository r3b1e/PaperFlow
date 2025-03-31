from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.lib.units import cm


def create_report(title, author, abstract, introduction, methodology, results, conclusion, reference):
    # Create a PDF file
    file_name = "combined_project_report.pdf"
    pdf = SimpleDocTemplate(
        file_name,
        pagesize=A4,
        leftMargin=1.56 * cm,
        rightMargin=1.56 * cm,
        topMargin=2 * cm,
        bottomMargin=2 * cm,
    )

    # Define styles
    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        "TitleStyle",
        parent=styles["Heading1"],
        fontSize=14,
        leading=18,
        alignment=TA_CENTER,
        spaceAfter=12,
        fontName="Times-Bold"
    )

    subtitle_style = ParagraphStyle(
        "SubtitleStyle",
        parent=styles["Normal"],
        fontSize=12,
        alignment=TA_CENTER,
        spaceAfter=10,
        fontName="Times-Roman"
    )

    clg_style = ParagraphStyle(
        "ClgStyle",
        parent=styles["Normal"],
        fontSize=16,
        alignment=TA_CENTER,
        spaceAfter=5,
        spaceBefore=5,
        fontName="Times-Bold"
    )

    justified_style = ParagraphStyle(
        "Justified",
        parent=styles["Normal"],
        fontName="Times-Roman",
        fontSize=12,
        leading=21,
        alignment=TA_JUSTIFY,
    )

    heading_style = ParagraphStyle(
        "Heading",
        parent=styles["Normal"],
        fontName="Times-Bold",
        fontSize=16,
        leading=24,
        alignment=TA_JUSTIFY,
    )

    # Add spacing function
    def add_spacing(line_height=18, num_lines=1):
        return Spacer(1, line_height * num_lines)

    # Content for the cover page
    content = []
    
    content.append(add_spacing(18, 1))
    content.append(Paragraph(f"<b>{title}</b>", title_style))
    content.append(add_spacing(18, 1))
    content.append(Paragraph(f"<b>{author}</b>", subtitle_style))
    content.append(add_spacing(46, 1))

    # Add abstract if not empty
    if abstract.strip():
        content.append(Paragraph("<b>Abstract</b>", clg_style))
        content.append(add_spacing(18, 1))
        content.append(Paragraph(abstract, justified_style))
        content.append(add_spacing(35, 1))
        content.append(PageBreak())

    # Add introduction if not empty
    if introduction.strip():
        content.append(Paragraph("1. Introduction", heading_style))
        content.append(add_spacing(12, 1))
        content.append(Paragraph(introduction, justified_style))
        content.append(add_spacing(40, 1))

    # Add methodology if not empty
    if methodology.strip():
        content.append(Paragraph("2. Methodology", heading_style))
        content.append(add_spacing(12, 1))
        content.append(Paragraph(methodology, justified_style))
        content.append(add_spacing(40, 1))

    # Add results if not empty
    if results.strip():
        content.append(Paragraph("3. Results", heading_style))
        content.append(add_spacing(12, 1))
        content.append(Paragraph(results, justified_style))
        content.append(add_spacing(40, 1))

    # Add conclusion if not empty
    if conclusion.strip():
        content.append(Paragraph("4. Conclusion", heading_style))
        content.append(add_spacing(12, 1))
        content.append(Paragraph(conclusion, justified_style))
        content.append(add_spacing(40, 1))
    
    # Add references if not empty
    if reference.strip():
        content.append(Paragraph("Reference", heading_style))
        content.append(add_spacing(12, 1))
        content.append(Paragraph(reference, justified_style))
        content.append(add_spacing(40, 1))

    # Build the PDF only if content exists
    if len(content) > 4:  # Ensuring it's more than just the title and author
        pdf.build(content)
        print(f"✅ Combined project report generated and saved as '{file_name}' successfully!")
    else:
        print("⚠️ No valid content found. PDF not generated.")