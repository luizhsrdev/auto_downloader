from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("URL_DA_PAGINA_DO_SEI")  # Substitua pela URL real

# Faça login manualmente (se necessário), depois execute:
links = driver.find_elements_by_xpath('//a[contains(@href, "action=visualizar")]')

for i, link in enumerate(links):
    link.click()
    time.sleep(3)  # Aguarda o download
    print(f"Download {i + 1}/{len(links)} concluído.")

driver.quit()