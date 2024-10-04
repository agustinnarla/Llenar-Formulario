import pandas as pd 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Leemos el archivo excel
df = pd.read_excel("./excel/Datos.xlsx") 
print(df.columns)

opciones_chrome = Options()
opciones_chrome.add_argument("--no-sandbox")
opciones_chrome.add_argument("--disable-dev-shm-usage")

# Instalamos el ChromeDriver 
servicio = Service(ChromeDriverManager().install())

# Inicia el WebDriver con Chrome
driver = webdriver.Chrome(service=servicio, options=opciones_chrome)

# Abre el archivo  en el navegador
driver.get("http://127.0.0.1:5500/index.html")

# Itera sobre cada fila del archivo Excel
for index, row in df.iterrows():
    # Limpiamos el nombre
    driver.find_element(By.NAME, 'nombre').clear() 
    #Enviamos el nombre
    driver.find_element(By.NAME, "nombre").send_keys(row["Nombre"])  
     # Limpiamos el campo apellido
    driver.find_element(By.NAME, 'apellido').clear() 
     # Envía el apellido
    driver.find_element(By.NAME, "apellido").send_keys(row["Apellido"]) 
    # Limpiamos el campo mail
    driver.find_element(By.NAME, "mail").clear()
    # Enviamos el mail
    driver.find_element(By.NAME, "mail").send_keys(row["Mail"])
    # Limpiamos el campo pais
    driver.find_element(By.NAME, "pais").clear()
    # Enviamos el pais
    driver.find_element(By.NAME, "pais").send_keys(row["Pais"])
    # Limpiamos el campo sueldo
    driver.find_element(By.NAME, "sueldo").clear()
    # Enviamos el sueldo
    driver.find_element(By.NAME, "sueldo").send_keys(row["Sueldo"])
    # Limpiamos el campo telefono
    driver.find_element(By.NAME, "telefono").clear()
    # Enviamos el telefono
    driver.find_element(By.NAME, "telefono").send_keys(row["Telefono"])
    # Limpiamos el campo caracter
    driver.find_element(By.NAME, "caracter").clear()
    # Enviamos el caracter
    driver.find_element(By.NAME, "caracter").send_keys(row["Caracter del pais"])
    # Limpiamos el campo cv
    driver.find_element(By.NAME, "cv").clear()
    # Enviamos el cv
    driver.find_element(By.NAME, "cv").send_keys(row["Cv"])
    # Limpiamos el campo disponibilidad
    driver.find_element(By.NAME, "disponibilidad").clear()
    # Enviamos el disponibilidad
    driver.find_element(By.NAME, "disponibilidad").send_keys(row["Disponibilidad"])
    # Limpiamos el campo añosExperiencia
    driver.find_element(By.NAME, "añosExperiencia").clear()
    # Enviamos el añosExperiencia
    driver.find_element(By.NAME, "añosExperiencia").send_keys(row["Años de experiencia"])
    # Limpiamos el campo anotacion
    driver.find_element(By.NAME, "anotacion").clear()
    # Enviamos el anotacion
    driver.find_element(By.NAME, "anotacion").send_keys(row["Anotaciones"])
    # Enviamos el formulario
    driver.find_element(By.NAME, "enviar").click() 

    print(f"Datos enviados: {row['Nombre']} {row['Apellido']} {row['Mail']} {row['Pais']} {row['Sueldo']} {row['Telefono']} {row['Caracter del pais']} {row['Cv']} {row['Disponibilidad']} {row['Años de experiencia']} {row['Anotaciones']}")
# Cerramos el navegador al finalizar
driver.quit()
