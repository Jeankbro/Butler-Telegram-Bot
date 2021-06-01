import os
import requests
import json
import telebot


API_KEY = os.getenv("API_KEY")
bot = telebot.TeleBot(API_KEY)


def get_mensaje_inspiracional():
    respuesta = requests.get("https://zenquotes.io/api/random")
    dato_json = json.loads(respuesta.text)
    mensaje = dato_json[0]["q"] + " - " + dato_json[0]["a"]
    mensaje_final = "Aquí tengo una frase bonita, por ahora en inglés: \n\n" + mensaje
    return mensaje_final

def kelvin_centigrados(temperatura):
  return (temperatura - 273.15)

def get_clima():
  API_KEY = os.getenv("API_KEY_WEATHER")
  url_base = "http://api.openweathermap.org/data/2.5/weather?"
  id_ciudad = "3672486"
  url_completa = url_base + "id=" + id_ciudad + "&appid=" + API_KEY
  respuesta = requests.get(url_completa)
  datos_json = respuesta.json()
  if datos_json["cod"] != "404":
    y = datos_json["main"]
    temperatura = y["temp"]
    temperatura_centi = kelvin_centigrados(temperatura)
    return temperatura_centi

def get_humedad():
  API_KEY = os.getenv("API_KEY_WEATHER")
  url_base = "http://api.openweathermap.org/data/2.5/weather?"
  id_ciudad = "3672486"
  url_completa = url_base + "id=" + id_ciudad + "&appid=" + API_KEY
  respuesta = requests.get(url_completa)
  datos_json = respuesta.json()
  if datos_json["cod"] != "404":
    y = datos_json["main"]
    humedad = y["humidity"]
    return humedad
  


# Comandos del bot y sus respectivas acciones

@bot.message_handler(commands=["Comandos"])
def comandos(mensaje):
    bot.reply_to(mensaje, """Hola! Soy Butler, estos son mis comandos:
/Comandos Muestra toda la lista de comandos disponibles.
/Hola Te saludo :)
/Inspírame Te doy una frase bonita :D
/Clima Te doy el clima de hoy más la humedad!""")

@bot.message_handler(commands=["Hola"])
def saludo(mensaje):
  bot.reply_to(mensaje, "Hola! como estás?")


@bot.message_handler(commands=["Inspírame"])
def inspirar(mensaje):
  bot.reply_to(mensaje, get_mensaje_inspiracional())

@bot.message_handler(commands=["Clima"])
def clima(mensaje):
  bot.reply_to(mensaje, "Hoy en Pereira estamos a unos " + str(get_clima()) + " grados centigrados, y con una humedad del " + str(get_humedad()) + "%!")


bot.polling()