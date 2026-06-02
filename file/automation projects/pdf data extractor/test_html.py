from urllib.request import urlopen
from bs4 import BeautifulSoup
import fitz

doc = fitz.open('Page 3 Figma.pdf')
page = doc.load_page(0)
text = page.get_text()
pdf_text = ''.join(text)
pdf_text_list = text.split('\n')
pdf_final_list = [l.replace('\n','').strip() for l in pdf_text_list if l.replace('\n','').strip()]
pdf_text_final = ' '.join(pdf_final_list)

url = "file:///C:/Users/Kunal.Keni/Desktop/assignment/assignment%205/Page%203%20HTML.html"
html = urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')


text_content = soup.get_text(separator="\n")

# Split text into lines
lines = text_content.splitlines()

# Remove empty lines and strip whitespace
html_lines = [line.strip() for line in lines if line.strip()]

html_para = ' '.join(html_lines)
html_para = html_para.replace(' ,',',')
html_para = html_para.replace('\xa0',' ')

missing_in_html = []
for element_of_pdf in pdf_final_list:
    if element_of_pdf.lower() not in html_para.lower():
        missing_in_html.append(element_of_pdf)

for element in missing_in_html:
    text_instances = page.search_for(element)
    for inst in text_instances:
        highlight = page.add_highlight_annot(inst)
        highlight.update()



doc.save("output4.pdf", garbage=4, deflate=True, clean=True)