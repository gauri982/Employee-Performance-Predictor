from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_report(employee_data, prediction):

    file_name = "outputs/hr_report.pdf"

    c = canvas.Canvas(file_name, pagesize=letter)

    c.drawString(100, 750, "HR Performance Report")
    c.drawString(100, 700, f"Age: {employee_data[0]}")
    c.drawString(100, 680, f"Experience: {employee_data[1]}")
    c.drawString(100, 660, f"Salary: {employee_data[2]}")
    c.drawString(100, 640, f"Training Hours: {employee_data[3]}")
    c.drawString(100, 620, f"Attendance: {employee_data[4]}")

    c.drawString(100, 580, f"Predicted Performance: {prediction}")

    c.save()

    print("PDF Report Generated!")