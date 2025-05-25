
import pandas as pd
from fpdf import FPDF

# Step 1: Create sample data and save to CSV
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [24, 30, 22, 35, 28],
    'Score': [85, 90, 78, 88, 92]
}
df = pd.DataFrame(data)
df.to_csv('sample_data.csv', index=False)

# Step 2: Read data from CSV
df = pd.read_csv('sample_data.csv')

# Step 3: Analyze data - basic statistics
mean_age = df['Age'].mean()
mean_score = df['Score'].mean()

# Step 4: Create PDF report
class PDFReport(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, 'Sample Data Report', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

pdf = PDFReport()
pdf.add_page()
pdf.set_font('Arial', '', 12)

# Add analysis results
pdf.cell(0, 10, f'Mean Age: {mean_age:.2f}', ln=True)
pdf.cell(0, 10, f'Mean Score: {mean_score:.2f}', ln=True)

# Add table header
pdf.ln(10)
pdf.set_font('Arial', 'B', 12)
pdf.cell(40, 10, 'Name', 1)
pdf.cell(30, 10, 'Age', 1)
pdf.cell(30, 10, 'Score', 1)
pdf.ln()

# Add table data
pdf.set_font('Arial', '', 12)
for index, row in df.iterrows():
    pdf.cell(40, 10, row['Name'], 1)
    pdf.cell(30, 10, str(row['Age']), 1)
    pdf.cell(30, 10, str(row['Score']), 1)
    pdf.ln()

# Save PDF
pdf.output('sample_report.pdf')

print("PDF report generated: sample_report.pdf")
