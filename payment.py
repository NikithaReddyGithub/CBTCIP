from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

def create_payment_receipt(customer_name, amount_paid, payment_method, filename):
    doc = SimpleDocTemplate(filename, pagesize=letter)
    
    # Create data
    data = [
        ["Customer Name", customer_name],
        ["Amount Paid", "${:.2f}".format(amount_paid)],
        ["Payment Method", payment_method]
    ]

    # Create table
    table = Table(data, colWidths=[200, 200])
    
    # Style
    style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                        ('GRID', (0, 0), (-1, -1), 1, colors.black)])

    table.setStyle(style)

    # Create flowables
    elements = []
    elements.append(table)

    # Build PDF
    doc.build(elements)

# Example usage
customer_name = "John Doe"
amount_paid = 100.0
payment_method = "Credit Card"
filename = "payment_receipt.pdf"

create_payment_receipt(customer_name, amount_paid, payment_method, filename)
