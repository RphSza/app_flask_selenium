from flask import Flask
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/automation")
def automation():
    navegador = webdriver.Chrome()
    navegador.get("https://www.google.com")
    texto = navegador.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/img').get_attribute('alt')
    time.sleep(5)
    navegador.quit()
    return f'<p>Esse é o texto: {texto}</p>'

if __name__ == "__main__":
    app.run(debug=True)