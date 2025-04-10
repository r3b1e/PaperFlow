from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, ListFlowable, ListItem
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.units import cm
from reportlab.platypus import PageBreak
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
import json


def apsit_formater(content_data):
    
# Create a PDF file
    file_name = "apsit_project_report.pdf"
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

    def custom():
        subtitle_style = ParagraphStyle(
            "SubtitleStyle",
            parent=styles["Normal"],
            fontSize=12,
            alignment=TA_CENTER,
            spaceAfter=10,
            fontName="Times-Roman"
        )
        return subtitle_style

    bold_style = ParagraphStyle(
        "BoldStyle",
        parent=styles["Normal"],
        fontSize=12,
        alignment=TA_CENTER,
        spaceAfter=5,
        spaceBefore=5,
        fontName="Times-Bold"
    )

    clg_style = ParagraphStyle(
        "BoldStyle",
        parent=styles["Normal"],
        fontSize=16,
        alignment=TA_CENTER,
        spaceAfter=5,
        spaceBefore=5,
        fontName="Times-Bold"
    )

    guide_style = ParagraphStyle(
        "GuideStyle",
        parent=styles["Normal"],
        fontSize=10,
        alignment=TA_CENTER,
        spaceAfter=5,
        fontName="Times-Bold"
    )

    academic_style = ParagraphStyle(
        "AcademicStyle",
        parent=styles["Normal"],
        fontSize=10,
        alignment=TA_CENTER,
        spaceAfter=20,
        fontName="Times-Bold"
    )

    justified_style = ParagraphStyle(
        "Justified",
        parent=styles["Normal"],
        fontName="Times-Roman",
        fontSize=12,
        leading=21,
        alignment=4,  # Justified text
    )

    heading_style = ParagraphStyle(
        "Heading",
        parent=styles["Normal"],
        fontName="Times-Bold",
        fontSize=16,
        leading=24,
        alignment=4,  # Justified heading
    )

    chapter_style = ParagraphStyle(
        "Chapter",
        parent=styles["Normal"],
        fontName="Times-Bold",
        fontSize=18,
        leading=24,
        alignment=4,
    )

    # Add spacing function
    def add_spacing(line_height=18, num_lines=1):
        return Spacer(1, line_height * num_lines)


    # Content for the cover page
    content = []

    # Add headings and details for the cover page
    content.append(Paragraph("<b>A</b>", title_style))
    content.append(Paragraph("<b>Mini Project Report</b>", title_style))
    content.append(Paragraph("<b>on</b>", title_style))
    content.append(Paragraph(f"<b>{content_data['title']}</b>", title_style))

    content.append(add_spacing(12, 1))
    content.append(Paragraph("Submitted in partial fulfillment of the requirements for the degree", custom()))
    content.append(Paragraph("of", subtitle_style))
    content.append(Paragraph("<b>Second Year Engineering – Information Technology</b>", subtitle_style))
    content.append(Paragraph("by", subtitle_style))
    content.append(add_spacing(12, 1))

    # Student names and roll numbers

    students = [
        ("Abhishekh Jamdade", "23104076"),
        ("Sunny Gupta", "23104136"),
        ("Pranav Ghodke", "23104115"),
        ("Radhika Kulkarni", "23104023"),
    ]



    for student in students:
        content.append(Paragraph(f"<b>{student[0]}</b> &nbsp;&nbsp;&nbsp;&nbsp; {student[1]}", bold_style))

    content.append(add_spacing(20, 1))

    # Under guidance section
    content.append(Paragraph("<b>Under the guidance of</b>", guide_style))
    content.append(Paragraph("<b>Mr. Sachin Kasara</b>", bold_style))
    content.append(add_spacing(20, 1))

    # Add image/logo
    image_path = "apsit_logo.png"  # Path to the image (update if needed)
    content.append(Image(image_path, width=100, height=100))
    content.append(add_spacing(20, 1))

    # Institute and university information
    content.append(Paragraph("<b>DEPARTMENT OF INFORMATION TECHNOLOGY</b>", bold_style))
    content.append(Paragraph("A.P. SHAH INSTITUTE OF TECHNOLOGY", subtitle_style))
    content.append(Paragraph("G.B. Road, Kasarvadavali, Thane (W)-400615", subtitle_style))
    content.append(Paragraph("UNIVERSITY OF MUMBAI", subtitle_style))
    content.append(add_spacing(20, 1))

    # Academic year
    content.append(Paragraph("Academic Year: 2023-24", academic_style))
    content.append(add_spacing(40, 1))

    content.append(PageBreak())  # Add a page break after certain content

    # Certificate

    content.append(add_spacing(36, 1))
    content.append(Paragraph("<b>CERTIFICATE</b>", clg_style))
    # content.append(add_spacing(18, 1))
    content.append(add_spacing(36, 1))
    certificate_Text = """This to certify that the Mini Project report on   Paper Flow has been submitted by <b>Abhishek Jamdade</b> (23104076), <b>Sunny Gupta</b> (23104136), <b>Pranav Ghodke</b> (23104115)  and <b>Radhika Kulkarni</b> (23104023) who are bonafide students of  A. P. Shah Institute of Technology, Thane as a  partial fulfillment of the requirement for the degree in Information Technology, during the academic year 2023-2024 in the satisfactory manner as per the curriculum laid down by University of Mumbai."""
    content.append(Paragraph(certificate_Text, justified_style))
    content.append(add_spacing(35, 1))

    # ============================
    # 1. Add Guide Section
    # ============================
    guide_data = [
        ["Mr. Sachin Kasare", ""],  # First row: Name with empty column
        ["Guide", ""]  # Second row: Designation
    ]

    # Create a table for the guide section
    guide_table = Table(guide_data, colWidths=[250, 250])
    guide_table.setStyle(TableStyle([
        ("ALIGN", (0, 0), (-1, -1), "LEFT"),  # Align text to the left
        ("FONTNAME", (0, 0), (0, 0), "Times-Bold"),  # Bold for name
        ("FONTNAME", (0, 1), (0, 1), "Times-Roman"),  # Normal for designation
        ("FONTSIZE", (0, 0), (-1, -1), 12),  # Font size 14
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),  # Add space below cells
        ("LEFTPADDING", (0, 0), (-1, -1), 0),  # Removes left padding

    ]))
    content.append(guide_table)
    content.append(Spacer(1, 40))


    # ============================
    # 2. Add HOD and Principal Section
    # ============================
    hod_principal_data = [
        ["Dr. Kiran Deshpande", "Dr. Uttam D. Kolekar"],  # Names
        ["HOD, Information Technology", "Principal"]  # Designations
    ]

    # Create a table for HOD and Principal section
    hod_principal_table = Table(hod_principal_data, colWidths=[360, 330])
    hod_principal_table.setStyle(TableStyle([
        ("FONTNAME", (0, 0), (0, 0), "Times-Bold"),  # Bold for HOD name
        ("FONTNAME", (1, 0), (1, 0), "Times-Bold"),  # Bold for Principal name
        ("FONTNAME", (0, 1), (0, 1), "Times-Roman"),  # Normal for HOD designation
        ("FONTNAME", (1, 1), (1, 1), "Times-Roman"),  # Normal for Principal designation
        ("FONTSIZE", (0, 0), (-1, -1), 12),  # Font size 14
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),  # Center align text
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),  # Add space below cells
    ]))
    content.append(hod_principal_table)
    content.append(Spacer(1, 40))  # Add space between sections


    # ============================
    # 3. Add External and Internal Examiner
    # ============================
    examiner_data = [
        ["External Examiner:", "Internal Examiner:"],  # Headings
        ["1.", "1."]  # Examiner placeholders
    ]

    # Create a table for examiners
    examiner_table = Table(examiner_data, colWidths=[280, 210])
    examiner_table.setStyle(TableStyle([
        ("FONTNAME", (0, 0), (-1, 0), "Times-Bold"),  # Bold for headings
        ("FONTNAME", (0, 1), (-1, 1), "Times-Roman"),  # Normal for numbers
        ("FONTSIZE", (0, 0), (-1, -1), 12),  # Font size 14
        ("ALIGN", (0, 0), (-1, -1), "LEFT"),  # Align text to the left
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),  # Add space below cells
    ]))
    content.append(examiner_table)
    content.append(Spacer(1, 50))  # Add space between sections

    # ============================
    # 4. Add Place and Date Section
    # ============================

    place_date_data = [
        ["Place:", "A. P. Shah Institute of Technology, Thane"],  # Place and institute name
        ["Date:", ""]  # Empty date field for manual entry
    ]

    # Create a table for place and date
    place_date_table = Table(place_date_data, colWidths=[50, 450])
    place_date_table.setStyle(TableStyle([
        ("FONTNAME", (0, 0), (0, -1), "Times-Bold"),  # Bold for labels
        ("FONTNAME", (1, 0), (1, -1), "Times-Roman"),  # Normal for values
        ("FONTSIZE", (0, 0), (-1, -1), 12),  # Font size 14
        ("ALIGN", (0, 0), (-1, -1), "LEFT"),  # Align text to the left
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),  # Add space below cells
    ]))
    content.append(place_date_table)

    content.append(PageBreak())  # Add a page break after certain content

    content.append(Paragraph("<b>ACKNOWLEDGEMENT</b>", clg_style))
    # content.append(add_spacing(18, 1))
    content.append(add_spacing(46, 1))
    acknowledgement_Text = """This project would not have come to fruition without the invaluable help of our guide <b>Mr. Sachin Kasare</b> Expressing gratitude towards our HoD, <b>Dr. Kiran Deshpande</b>, and the Department of Information Technology for providing us with the opportunity as well as the support required to pursue this project. We would also like to thank our project coordinator <b>Mr. Mandar Ganjapurkar</b> who gave us his valuable suggestions and ideas when we were in need of them. We would also like to thank our peers for their helpful suggestions."""
    content.append(Paragraph(acknowledgement_Text, justified_style))
    content.append(add_spacing(35, 1))

    content.append(PageBreak())
    # table of content

    sub_index_style = ParagraphStyle(
        "Justified",
        parent=styles["Normal"],
        fontName="Times-Roman",
        fontSize=12,
        leading=18,
        alignment=4,  # Justified text
        leftIndent=20,  # Add 20 points of left padding
    )

    # Define a justified style with extra spacing
    index_style = ParagraphStyle(
        "Justified",
        parent=styles["Normal"],
        fontName="Times-Roman",
        fontSize=12,
        leading=21,  # Line spacing
        alignment=4,  # Justified text
        wordSpace=5,  # Add extra space between words
    )


    content.append(Paragraph("<b>TABLE OF CONTENTS</b>", clg_style))
    content.append(add_spacing(36, 1))
    content.append(Paragraph("Abstract", sub_index_style))
    content.append(add_spacing(21, 1))
    content.append(Paragraph("1. Introduction.............................................................................................................................................", index_style))
    content.append(add_spacing(10, 1))
    content.append(Paragraph("1.1 Purpose..........................................................................................................................................", sub_index_style))
    content.append(add_spacing(10, 1))
    content.append(Paragraph("1.2.	Problem Statement........................................................................................................................", sub_index_style))
    content.append(add_spacing(10, 1))
    content.append(Paragraph("1.3.	Objectives.....................................................................................................................................", sub_index_style))
    content.append(add_spacing(10, 1))
    content.append(Paragraph("1.4.	Scope............................................................................................................................................", sub_index_style))
    content.append(add_spacing(10, 1))
    content.append(Paragraph("2.	Literature Review...................................................................................................................................", index_style))
    content.append(add_spacing(10, 1))
    content.append(Paragraph("3.	Proposed System...............................................................................................................................", index_style))
    content.append(add_spacing(10, 1))
    content.append(Paragraph("3.1 Features and Functionality........................................................................................................", sub_index_style))
    content.append(add_spacing(10, 1))
    content.append(Paragraph("4.	Technical Specification..........................................................................................................", index_style))
    content.append(add_spacing(10, 1))
    content.append(Paragraph("5.	Project Design..................................................................................................................", index_style))
    content.append(add_spacing(10, 1))
    content.append(Paragraph("5.1.	Use Case diagram........................................................................................................................", sub_index_style))
    content.append(add_spacing(10, 1))
    content.append(Paragraph("5.2.	DFD (Data Flow Diagram) ................................................................................................", sub_index_style))
    content.append(add_spacing(10, 1))
    content.append(Paragraph("5.3.	System Architecture...........................................................................................", sub_index_style))
    content.append(add_spacing(10, 1))
    content.append(Paragraph("5.4.	Implementation......................................................................................................", sub_index_style))
    content.append(add_spacing(10, 1))
    content.append(Paragraph("6.	Project Scheduling........................................................................................................", index_style))
    content.append(add_spacing(10, 1))
    content.append(Paragraph("7.	Results................................................................................................................................", index_style))
    content.append(add_spacing(10, 1))
    content.append(Paragraph("8.	Conclusion.............................................................................................................", index_style))
    content.append(add_spacing(10, 1))
    content.append(Paragraph("9. Future Scope................................................................................................................", index_style))
    content.append(add_spacing(10, 1))
    content.append(Paragraph("References", index_style))
    content.append(add_spacing(10, 1))

    content.append(PageBreak())

    #abstract
    content.append(Paragraph("<b>ABSTRACT</b>", clg_style))
    content.append(add_spacing(26, 1))
    # content.append(add_spacing(18, 1))
    content.append(add_spacing(46, 1))
    abstract_Text = """Formatting research papers according to industry standards such as IEEE, ACM, and APA is a challenging and time-consuming task for students and researchers. The complexity of citation styles, layout requirements, and structural guidelines often leads to errors, which can result in paper rejection. To address this issue, we propose PaperFlow, an AI-powered Research Paper Formatter and Analyzer that streamlines the paper formatting process.
    PaperFlow automates key formatting aspects, including font selection, margin adjustments, and citation corrections. Additionally, it evaluates the quality of research papers by analysing clarity, structure, and citation accuracy, providing users with a quality score and actionable improvement suggestions. The system supports PDF and DOCX uploads, offering an automatically formatted, ready-to-submit version, reducing manual effort and increasing acceptance rates.
    """
    content.append(Paragraph(abstract_Text, justified_style))
    content.append(add_spacing(35, 1))

    content.append(PageBreak())

    # Chapter 1 - Introduction
    content.append(Paragraph("Chapter 1", chapter_style))
    content.append(add_spacing(28, 1))
    content.append(Paragraph("Introduction", heading_style))
    content.append(add_spacing(12, 1))

    intro_Text = """
    Major Depressive Disorder (MDD) is a prevalent and debilitating mental health condition, characterized by persistent sadness, loss of interest, and cognitive and physical symptoms that significantly impair daily functioning [1]. Affecting approximately 280 million individuals globally, MDD represents a major public health challenge, necessitating improved diagnostic and therapeutic strategies [2]. Traditional diagnostic methods often rely on subjective assessments, which can lead to misdiagnosis or delayed interventions, highlighting the need for objective and efficient diagnostic tools [3].
    """
    content.append(Paragraph(intro_Text, justified_style))
    content.append(add_spacing(18, 1))

    # Proposal section
    content.append(Paragraph("1.1   Proposal", heading_style))
    content.append(add_spacing(12, 1))
    propose_Text = """
    The main purpose of PaperFlow is to assist researchers, students, and professionals in writing well-structured research papers with accurate formatting and citations. The system ensures that papers follow standard guidelines without manual effort, reducing errors and saving time. Additionally, it enhances the overall readability and coherence of the document, increasing the chances of acceptance in reputed journals and conferences.
    """
    content.append(Paragraph(propose_Text, justified_style))
    content.append(add_spacing(18, 1))

    # Methodology section
    content.append(Paragraph("1.2   Methodology", heading_style))
    content.append(add_spacing(12, 1))
    metho_Text = """
    Forty-five MDD patients and seventy-six healthy controls have participated in the current study. The EEG database
    is publicly available at http://bit.ly/2rzY6ZY and was used in a recent previous study. The study was approved by the ethical committee
    of Arizona University and experiments were in accordance with relevant ethical guidelines. Prior to acquisition, all participants
    provided written informed consent. Participants were recruited from introductory psychology classes based on mass survey scores of
    the Beck Depression Inventory (BDI). Recruitment criteria included: (1) age 18–25, (2) no history of head trauma or seizures, and
    (3) no current psychoactive medication use.
    """
    content.append(Paragraph(metho_Text, justified_style))
    content.append(add_spacing(18, 1))

    # Objectives - Bullet Points
    content.append(Paragraph("1.3   Objectives", heading_style))
    content.append(add_spacing(12, 1))
    bullet_points = [
        "To develop an AI-driven tool that automates research paper formatting.",
        "To ensure compliance with academic standards (IEEE, ACM, APA).",
        "To provide automated paper quality assessment.",
        "To suggest improvements for better readability and structure.",
        "To support multiple file formats (PDF, DOCX) for easy document processing.",
    ]
    bullet_list = ListFlowable(
        [ListItem(Paragraph(point, justified_style)) for point in bullet_points],
        bulletType="bullet",
        start="•"
    )
    content.append(bullet_list)

    content.append(add_spacing(18, 1))

    # Objectives - Bullet Points
    content.append(Paragraph("1.4   Scope", heading_style))
    content.append(add_spacing(12, 1))
    bullet_points = [
        "Target Users: Researchers, students, academicians, and journal publishers.",
        "Supported Formats: PDF & DOCX.",
        "Output: A fully formatted, ready-to-submit research paper",
        "Technologies Used: Python for backend processing, Tailwind CSS for frontend styling.",
        "Potential Future Enhancements: Support for LaTeX documents, integration with reference management tools (Zotero, EndNote).",
    ]
    bullet_list = ListFlowable(
        [ListItem(Paragraph(point, justified_style)) for point in bullet_points],
        bulletType="bullet",
        start="•"
    )
    content.append(bullet_list)

    content.append(PageBreak())

    #table creation

    content.append(Paragraph("Chapter 2", chapter_style))
    content.append(add_spacing(28, 1))
    content.append(Paragraph("Literature Review", heading_style))
    content.append(add_spacing(12, 1))

    # Define styles
    styles = getSampleStyleSheet()
    normal_style = ParagraphStyle(
        "Normal",
        parent=styles["Normal"],
        fontName="Times-Roman",
        fontSize=12,
        leading=14,
        spaceAfter=5,
    )

    bold_style_of_the_table = ParagraphStyle(
        "Bold",
        parent=styles["Normal"],
        fontName="Times-Bold",
        fontSize=12,
        leading=14,
    )

    # Data for the first three rows
    data = [
        [
            Paragraph("<b>Sr.<br/>No</b>", bold_style_of_the_table),
            Paragraph("<b>Title of Research paper</b>", bold_style_of_the_table),
            Paragraph("<b>Key Findings</b>", bold_style_of_the_table),
            Paragraph("<b>Author</b>", bold_style_of_the_table),
            Paragraph("<b>Year</b>", bold_style_of_the_table),
        ],
        [
            "1.",
            Paragraph(
                "<b>Automated Research Paper Forxplores how AI c6urt6uan detect and fixxplores how AI c6urt6uan detect and fixmatting: A Rule-Based Approach</b>",
                normal_style,
            ),
            Paragraph(
                "The study presents an automated system thn automated system that corrects resean automated system that corrects resean automated system that corrects resean automated system that corrects reseaat corrects research paper formatting errors, including fonts, margins, and spacing. The system applies predefined academic formatting rules and significantly reduces manual errors.",
                normal_style,
            ),
            Paragraph(
                "A. Smith, B. Johnson, Croigtjerogjeor iioerjgtpe4u t. Rogers, D. Miller, E. Thompson, F. Brown",
                normal_style,
            ),
            "2021",
        ],
        [
            "2.",
            Paragraph(
                "<b>Improving Citation Accurajty6jrt6hrtcy Using AI-Powered Reference Management</b>",
                normal_style,
            ),
            Paragraph(
                "This research explores howxplores how AI c6urt6uan detect and fixxplores how AI c6urt6uan detect and fixxplores how AI c6urt6uan detect and fixxplores how AI c6urt6uan detect and fix AI c6urt6uan detect and fix incorrect citations in research papers. It introduces a machine learning model trained on different citation styles (IEEE, ACM, APA) to enhance citation accuracy.",
                normal_style,
            ),
            Paragraph(
                "C. Patel, D. Wang, seoleh selirjoweij M. Lee, S. Kumar",
                normal_style,
            ),
            "2020",
        ],
        [
            "3.",
            Paragraph(
                "<b>Text Analysis for Research Paper Quality Assessment</b>",
                normal_style,
            ),
            Paragraph(
                "The paper discusses how NLP-based text analysis can evaluate research paper quality based on clarity, structure, and argument flow. It proposes a rating system for assessing readability and coherence.",
                normal_style,
            ),
            Paragraph(
                "E. Thomas, F. Brown",
                normal_style,
            ),
            "2022",
        ],
    ]

    # Define Table Style
    style = TableStyle(
        [
            ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.black),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("FONTNAME", (0, 0), (-1, 0), "Times-Bold"),
            ("BOTTOMPADDING", (0, 0), (-1, 0), 8),
            ("TOPPADDING", (0, 0), (-1, -1), 6),
            ("LEFTPADDING", (0, 0), (-1, -1), 6),
            ("RIGHTPADDING", (0, 0), (-1, -1), 6),
            ("BACKGROUND", (0, 1), (-1, -1), colors.white),
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ]
    )

    # Calculate table width to fit within margins
    page_width, page_height = A4
    usable_width = page_width - (pdf.leftMargin + pdf.rightMargin)

    # Set table column widths based on available space
    table = Table(
        data,
        colWidths=[
            0.08 * usable_width,  # Sr. No
            0.3 * usable_width,   # Title
            0.35 * usable_width,  # Key Findings
            0.2 * usable_width,   # Author (with wrapping)
            0.07 * usable_width,  # Year
        ],
        repeatRows=1,  # Repeat header on every page
    )

    # Apply style to table
    table.setStyle(style)

    # Build PDF

    content.append(table)
    content.append(PageBreak())

    # Chapter 3 - Proposed System
    content.append(Paragraph("Chapter 3", chapter_style))
    content.append(add_spacing(28, 1))
    content.append(Paragraph("Proposed System", heading_style))
    content.append(add_spacing(12, 1))

    Proposed_Text = """
    Many researchers struggle with formatting their papers correctly, citing sources properly, and avoiding plagiarism. Manual formatting is time-consuming, and missing citations can lead to academic penalties. Additionally, verifying AI-generated or plagiarized content requires additional tools, making the entire process complex.
    """
    content.append(Paragraph(propose_Text, justified_style))
    content.append(add_spacing(18, 1))

    # Proposal section
    content.append(Paragraph("3.1   Features and Functionality", heading_style))
    content.append(add_spacing(12, 1))
    bullet_points = [
        "Target Users: Researchers, students, academicians, and journal publishers.",
        "Supported Formats: PDF & DOCX.",
        "Output: A fully formatted, ready-to-submit research paper",
        "Technologies Used: Python for backend processing, Tailwind CSS for frontend styling.",
        "Potential Future Enhancements: Support for LaTeX documents, integration with reference management tools (Zotero, EndNote).",
    ]
    bullet_list = ListFlowable(
        [ListItem(Paragraph(point, justified_style)) for point in bullet_points],
        bulletType="bullet",
        start="•"
    )
    content.append(bullet_list)
    content.append(add_spacing(18, 1))
    content.append(PageBreak())

    # Chapter 4 - Proposed System
    content.append(Paragraph("Chapter 4", chapter_style))
    content.append(add_spacing(28, 1))
    content.append(Paragraph("Technical Specification", heading_style))
    content.append(add_spacing(12, 1))

    content.append(PageBreak())

    # Chapter 5 - Project Design
    content.append(Paragraph("Chapter 5", chapter_style))
    content.append(add_spacing(28, 1))
    content.append(Paragraph("Project Design", heading_style))

    content.append(add_spacing(18, 1))

    # Proposal section
    content.append(Paragraph("5.1   Use Case diagram", heading_style))
    content.append(add_spacing(28, 1))

    # Add the image
    image_path = "use_case_img.png"
    img = Image(image_path, width=500, height=300)  # Adjust width/height as needed
    content.append(img)

    # Add a spacer
    content.append(Spacer(1, 12))

    # Add the caption below the image
    caption = Paragraph("Figure 5.1.1: New Feature Code", academic_style)
    content.append(caption)
    content.append(add_spacing(18, 1))
    #---------------------------------------

    content.append(add_spacing(18, 1))

    # Proposal section
    content.append(Paragraph("5.2   DFD (Data Flow Diagram)", heading_style))
    content.append(add_spacing(28, 1))

    # Add the image
    image_path = "dfd_img.png"
    img = Image(image_path, width=500, height=300)  # Adjust width/height as needed
    content.append(img)

    # Add a spacer
    content.append(Spacer(1, 12))

    # Add the caption below the image
    caption = Paragraph("Figure 5.1.1: New Feature Code", academic_style)
    content.append(caption)
    content.append(add_spacing(18, 1))
    #-------------------------------------------
    content.append(add_spacing(18, 1))

    # Proposal section
    content.append(Paragraph("5.2   DFD (Data Flow Diagram)", heading_style))
    content.append(add_spacing(28, 1))

    # Add the image
    image_path = "dfd_img.png"
    img = Image(image_path, width=500, height=300)  # Adjust width/height as needed
    content.append(img)

    # Add a spacer
    content.append(Spacer(1, 12))

    # Add the caption below the image
    caption = Paragraph("Figure 5.1.1: New Feature Code", academic_style)
    content.append(caption)
    content.append(add_spacing(18, 1))



    # Build the combined PDF
    pdf.build(content)

    print(f"Combined project report generated and saved as '{file_name}' successfully!")




data = {
        "title": " PG Accomodation ",
        "guide_name": "Mr. Sachin Kasara",
        "members": json.dumps([
            {"name": "member1", "id": "id_1"},
            {"name": "member2", "id": "id_2"},
            {"name": "member3", "id": "id_3"},
            {"name": "leader_name", "id": "id_leader"}
        ]),
        "abstract": """Formatting research papers according to industry standards such as IEEE, ACM, and APA is a
 challenging and time-consuming task for students and researchers. The complexity of citation styles,
 layout requirements, and structural guidelines often leads to errors, which can result in paper rejection.
 To address this issue, we propose PaperFlow, an AI-powered Research Paper Formatter and Analyzer
 that streamlines the paper formatting process. PaperFlow automates key formatting aspects, including
 font selection, margin adjustments, and citation corrections. Additionally, it evaluates the quality of
 research papers by analysing clarity, structure, and citation accuracy, providing users with a quality
 score and actionable improvement suggestions. The system supports PDF and DOCX uploads, offering
 an automatically formatted, ready-to-submit version, reducing manual effort and increasing acceptance
 rates.""",
        "introduction": """Writing research papers is a challenging task for students, researchers, and
professionals, requiring meticulous attention to formatting, citation management, and
adherence to specific styles such as IEEE, APA, or MLA. Ensuring consistency in
references, maintaining accurate in-text citations, and eliminating plagiarism can be
time-consuming and error-prone. Many individuals struggle with structuring their
work according to publication standards, leading to multiple revisions and potential
rejections. PaperFlow is designed to streamline this process by automating research
paper formatting, citation generation, and reference management. By integrating
advanced algorithms, it enhances efficiency, minimizes errors, and allows users to
focus on the quality of their research rather than technical complexities.""",
        "purpose": """The main purpose of PaperFlow is to assist researchers, students, and professionals in
writing well-structured research papers with accurate formatting and citations. The
system ensures that papers follow standard guidelines without manual effort, reducing
errors and saving time. Additionally, it enhances the overall readability and coherence
of the document, increasing the chances of acceptance in reputed journals and
conferences.""",
        "problem_statement": """Many researchers struggle with formatting their papers correctly, citing sources
properly, and avoiding plagiarism. Manual formatting is time-consuming, and missing
citations can lead to academic penalties. Additionally, verifying AI-generated or
plagiarized content requires additional tools, making the entire process complex.
""",
        "objectives": """• To develop an AI-driven tool that automates research paper formatting.
• To ensure compliance with academic standards (IEEE, ACM, APA).
• To provide automated paper quality assessment.
• To suggest improvements for better readability and structure.
• To support multiple file formats (PDF, DOCX) for easy document processing.""",
        "scope": """• Target Users: Researchers, students, academicians, and journal publishers.
• Supported Formats: PDF & DOCX.
• Output: A fully formatted, ready-to-submit research paper.
• Technologies Used: Python for backend processing, Tailwind CSS for frontend
styling.
• Potential Future Enhancements: Support for LaTeX documents, integration
with reference management tools (Zotero, EndNote).""",
        # "literature_review": json.dumps(st.session_state.literature_data),
        # "proposed_system": proposed_system,
        # "features": features,
        # "technical_spec": technical_spec,
        # "project_design": json.dumps({
        #     "Overall Design": project_design,
        #     "Use Case Diagram": use_case_heading,
        #     "DFD": dfd_heading,
        #     "Architecture": architecture_heading,
        #     "Implementation": implementation
        # }),
        # "scheduling": scheduling,
        # "results": results,
        # "conclusion": conclusion,
        # "future_scope": future_scope,
        # "references": reference
    }
apsit_formater(data)