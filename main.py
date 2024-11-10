import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd

Casas = {"Zona" : [],
        "Precios" : [],
        "Direcciones" : [],
        "Dimensiones" : []}

def CiudadNorte(paginas,df):
    pagina = 1
    s = Service(ChromeDriverManager().install())
    opc = Options()
    opc.add_argument("--window-size=1020,1200")


    for n in range(0,paginas):
        if n > 0:
            page = f"/page-{pagina}"
        else:
            page = ""
        navegador = webdriver.Chrome(service=s, options=opc)
        navegador.get(f"https://www.vivanuncios.com.mx/s-casas-en-venta{page}/v1c1293p{pagina}?q=sonora")
        time.sleep(15)



        soup = BeautifulSoup(navegador.page_source, "html5lib")
        precio = soup.find_all('div',attrs={'class' : 'Price-sc-12dh9kl-3 geYYII'})
        for i in precio :
            df["Precios"].append(i.text)

        direccion = soup.find_all('div',attrs={'class' : "LocationAddress-sc-ge2uzh-0 iylBOA postingAddress"})
        for i in direccion:
            df["Direcciones"].append(i.text)

        dimesion = soup.find_all('h3',attrs={'class' : "PostingMainFeaturesBlock-sc-1uhtbxc-0 cHDgeO"})
        for i in dimesion:
            df["Dimensiones"].append(i.text)

        pagina += 1
        navegador.quit()

    if len(df["Precios"]) < 150:
        cant = 150 - len(df["Precios"])
        for i in range(cant):
            df["Precios"].append(None)

    elif len(df["Dimensiones"]) < 150:
        cant = 150 - len(df["Dimensiones"])
        for i in range(cant):
            df["Dimensiones"].append(None)

    elif len(df["Direcciones"]) < 150:
        cant = 150 - len(df["Direcciones"])
        for i in range(cant):
            df["Direcciones"].append(None)

    for i in range(150):
        df["Zona"].append("Norte")

def CiudadCentro(paginas,df):
    pagina = 1
    s = Service(ChromeDriverManager().install())
    opc = Options()
    opc.add_argument("--window-size=1020,1200")

    for n in range(0, paginas):
        if n > 0:
            page = f"/page-{pagina}"
        else:
            page = ""
        navegador = webdriver.Chrome(service=s, options=opc)
        navegador.get(f"https://www.vivanuncios.com.mx/s-casas-en-venta/distrito-federal{page}/v1c1293l1008p{pagina}")
        time.sleep(15)

        soup = BeautifulSoup(navegador.page_source, "html5lib")
        precio = soup.find_all('div', attrs={'class': 'Price-sc-12dh9kl-3 geYYII'})
        for i in precio:
            df["Precios"].append(i.text)

        direccion = soup.find_all('div', attrs={'class': "LocationAddress-sc-ge2uzh-0 iylBOA postingAddress"})
        for i in direccion:
            df["Direcciones"].append(i.text)

        dimesion = soup.find_all('h3', attrs={'class': "PostingMainFeaturesBlock-sc-1uhtbxc-0 cHDgeO"})
        for i in dimesion:
            df["Dimensiones"].append(i.text)

        pagina += 1
        navegador.quit()


    if len(df["Precios"]) < 300:
        cant = 300 - len(df["Precios"])
        for i in range(cant):
            df["Precios"].append(None)

    elif len(df["Dimensiones"]) < 300:
        cant = 300 - len(df["Dimensiones"])
        for i in range(cant):
            df["Dimensiones"].append(None)

    elif len(df["Direcciones"]) < 300:
        cant = 300 - len(df["Direcciones"])
        for i in range(cant):
            df["Direcciones"].append(None)

    for i in range(150):
        df["Zona"].append("Centro")

def CiduadSur(paginas,df):
    pagina = 1
    s = Service(ChromeDriverManager().install())
    opc = Options()
    opc.add_argument("--window-size=1020,1200")

    for n in range(0, paginas):
        if n > 0:
            page = f"/page-{pagina}"
        else:
            page = ""
        navegador = webdriver.Chrome(service=s, options=opc)
        navegador.get(f"https://www.vivanuncios.com.mx/s-casas-en-venta/oaxaca{page}/v1c1293l1019p{pagina}")
        time.sleep(15)

        soup = BeautifulSoup(navegador.page_source, "html5lib")
        precio = soup.find_all('div', attrs={'class': 'Price-sc-12dh9kl-3 geYYII'})
        for i in precio:
            df["Precios"].append(i.text)

        direccion = soup.find_all('div', attrs={'class': "LocationAddress-sc-ge2uzh-0 iylBOA postingAddress"})
        for i in direccion:
            df["Direcciones"].append(i.text)

        dimesion = soup.find_all('h3', attrs={'class': "PostingMainFeaturesBlock-sc-1uhtbxc-0 cHDgeO"})
        for i in dimesion:
            df["Dimensiones"].append(i.text)

        pagina += 1
        navegador.quit()

    if len(df["Precios"]) < 450:
        cant = 450 - len(df["Precios"])
        for i in range(cant):
            df["Precios"].append(None)

    elif len(df["Dimensiones"]) < 450:
        cant = 150 - len(df["Dimensiones"])
        for i in range(cant):
            df["Dimensiones"].append(None)

    elif len(df["Direcciones"]) < 450:
        cant = 450 - len(df["Direcciones"])
        for i in range(cant):
            df["Direcciones"].append(None)

    for i in range(150):
        df["Zona"].append("Sur")

if __name__ == "__main__":
    paginas = 5
    CiudadNorte(paginas,Casas)

    CiudadCentro(paginas,Casas)

    CiduadSur(paginas,Casas)

    df = pd.DataFrame(Casas)
    df.to_csv("dataframes/Casas")