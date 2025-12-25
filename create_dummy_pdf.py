# create_dummy_pdf.py
# pip install reportlab
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

pdf_path = "rag_vector/data/report.pdf" # set path where want to crate pdf file
c = canvas.Canvas(pdf_path, pagesize=letter)
width, height = letter

c.setFont("Helvetica-Bold", 16)
c.drawString(50, height - 50, "RAG Report - Retrieval Augmented Generation")

c.setFont("Helvetica", 12)
c.drawString(50, height - 100, "Introduction:")
c.drawString(50, height - 120, "Retrieval-Augmented Generation (RAG) improves AI responses")
c.drawString(50, height - 140, "by retrieving relevant documents from an external knowledge base.")

c.drawString(50, height - 180, "Use Cases:")
c.drawString(50, height - 200, "1. Customer Support")
c.drawString(50, height - 220, "2. Research Assistants")
c.drawString(50, height - 240, "3. Knowledge Management Systems")

c.save()
print(f"PDF saved at {pdf_path}")
