from bs4 import BeautifulSoup
from pprint import pprint
import re

with open("salaries.csv", "w", encoding="utf8") as o:
	o.write("")

with open("salaries.html", "r", encoding="utf8") as s:
    html = s.read()

soup = BeautifulSoup(html, "html.parser")

chart_tables = soup.find_all("tr")

with open("salaries.csv", "w", encoding="utf8") as o:
	for chart in chart_tables:

		company_elem = chart.find("td", "text-start")
		salary_elem = chart.find("td", "text-right")
		entries_elem = None

		salary_amount = None
		entries_amount = None

		if salary_elem:
			
			entries_elem = salary_elem.next.next

			if entries_elem:
				entries_amount = entries_elem.text

			salary_text = re.search(r"\d+\.\d+", str(salary_elem.text))
			
			if salary_text:
				salary_amount = float(salary_text[0]) * 1_000_000


		if company_elem and salary_amount and entries_amount:
			new_row = ",".join([company_elem.text, f"{salary_amount:.0f}", entries_amount])
			o.write(new_row + "\n")