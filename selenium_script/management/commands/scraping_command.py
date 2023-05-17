from django.core.management.base import BaseCommand
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import json
from selenium_script.models import Datos


class Command(BaseCommand):
    help = 'Runs the scraping script'

    def handle(self, *args, **options):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)

        url = "https://snifa.sma.gob.cl/Sancionatorio/Resultado"
        driver.get(url)

        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "#myTable")))

        header_texts = []
        data = []

        for i in range(44):
            wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, "#myTable")))

            table = driver.find_element(By.CSS_SELECTOR, "#myTable")

            headers = table.find_elements(By.TAG_NAME, "th")
            rows = table.find_elements(By.TAG_NAME, "tr")

            if i == 0:  # We only need to capture headers once
                for header in headers:
                    header_texts.append(header.text.strip())

            for row in rows:
                row_data = []  # Start a new list for each row
                cells = row.find_elements(By.TAG_NAME, "td")

                for cell in cells:
                    row_data.append(cell.text.strip())

                data.append(row_data)

            # Click the next button after going through each row on the page
            next_button = driver.find_element(
                By.CSS_SELECTOR, "#myTable_next")
            next_button.click()

        # Store data as a dictionary
        data_dict = {
            "headers": header_texts,
            "rows": data
        }



        # Save data to a JSON file
        with open("data.json", "w") as json_file:
            json.dump(data_dict, json_file, indent=4, ensure_ascii=False)

        driver.quit()

        column_to_field_mapping = {
            '': 'numero',
            'Expediente': 'expediente',
            'Unidad Fiscalizable': 'unidad_fiscalizable',
            'Nombre razón social': 'nombre_razon_social',
            'Categoría': 'categoria',
            'Región': 'region',
            'Estado': 'estado',
            'Detalle': 'detalle'  # Asegúrate de tener este campo en tu modelo si existe en tus datos
        }


        for row in data:
            row_dict = dict(zip(header_texts, row))
            row_dict = {column_to_field_mapping[key]: value for key, value in row_dict.items() if key in column_to_field_mapping}
            Datos.objects.create(**row_dict)


        print(header_texts)
        for row in data_dict["rows"]:
            print(row) 

        self.stdout.write(self.style.SUCCESS(
            'Scraping completed successfully'))
