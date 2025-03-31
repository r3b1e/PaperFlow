import pdfplumber
import re
import format

def extract_pdf_sections(pdf_path, section_headers):
    target_lower = {header.strip().lower() for header in section_headers}
    sections = {header.lower(): "" for header in section_headers}
    
    with pdfplumber.open(pdf_path) as pdf:
        full_text = ""
        for page in pdf.pages:
            full_text += page.extract_text() + "\n"
        lines = [line.strip() for line in full_text.split('\n')]
    
    headers = []
    for line_num, line in enumerate(lines):
        stripped_line = line.strip()
        header_title = None
        
        # Check for numbered headers (e.g., "1. Introduction")
        numbered_match = re.match(r'^\s*(\d+\.)\s*(.+)$', stripped_line, re.IGNORECASE)
        if numbered_match:
            title_part = numbered_match.group(2).strip()
            header_title = title_part.lower()
        else:
            # Check if the line is a target header (case-insensitive)
            lower_line = stripped_line.lower()
            if lower_line in target_lower:
                header_title = lower_line
            else:
                # Check for all-caps headers (heuristic)
                if re.fullmatch(r'^[A-Z\s]+$', stripped_line):
                    header_title = stripped_line.lower()
        
        if header_title is not None:
            headers.append((line_num, header_title))
    
    # Process each detected header to capture content for target sections
    for i in range(len(headers)):
        current_line, current_title = headers[i]
        
        if current_title in target_lower:
            start_line = current_line + 1
            end_line = len(lines) - 1  # Default to end of document
            
            # Find the next header's line
            if i + 1 < len(headers):
                end_line = headers[i + 1][0] - 1
            
            # Extract content between start_line and end_line inclusive
            content_lines = []
            for j in range(start_line, end_line + 1):
                if j < len(lines):
                    content_lines.append(lines[j])
            
            content = '\n'.join(content_lines).strip()
            
            # Update the section content (append if already exists)
            if sections[current_title]:
                sections[current_title] += '\n\n' + content
            else:
                sections[current_title] = content
    
    return sections

# Example Usage
def pdf_send(path):
    pdf_path = path
    target_sections = ["Abstract", "Introduction", "Methodogy", "Result", "Conclusion", "reference"]

    # Extract sections
    section_content = extract_pdf_sections(pdf_path, target_sections)

    # Save to variables
    abstract = section_content.get("abstract", "")
    introduction = section_content.get("introduction", "")
    methodogy = section_content.get("methodogy", "")
    result = section_content.get("result", "")
    conclusion = section_content.get("conclusion", "")
    reference = section_content.get("reference", "")
    
    format.papers(title = '', author = '', abstract=abstract[:1000], introduction=introduction[:1000], methodology=methodogy[:1000], results=result[:1000], conclusion=conclusion[:1000], reference=reference[:1000])

    # Print results
    # print("Abstract:\n", abstract)
    # print("\nIntroduction:\n", introduction)
    # print("\nMethodogy:\n", methodogy)
    # print("\nResult:\n", result)
    # print("\nConclusion:\n", conclusion)
    # print("\nReference:\n", reference)