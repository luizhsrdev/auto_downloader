from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configuração automática do ChromeDriver
service = Service(ChromeDriverManager().install())

chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)")

driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    driver.get("https://sei.cidadania.gov.br/sei/processo_acesso_externo_consulta.php?id_acesso_externo=282888")
    print("Aguardando login manual (30 segundos)...")
    time.sleep(30)
    
    links = driver.find_elements(By.XPATH, '//a[contains(@href, "action=visualizar")]')
    print(f"Encontrados {len(links)} documentos.")
    
    for i, link in enumerate(links, 1):
        print(f"Baixando documento {i}/{len(links)}")
        link.click()
        time.sleep(5)
        
except Exception as e:
    print(f"ERRO: {str(e)}")
finally:
    driver.quit()