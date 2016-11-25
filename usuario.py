import requests
import json

class Usuario:
	nombre = ""

	def __init__(self):
		self.url  = "https://graph.facebook.com/v2.8/me"
		self.token = "EAACEdEose0cBAOl96KrAAXI1Cm0yhEZAp3dyRN5WjJcyfmF8xe5qRq1q3K7s3mybTNqZAfwgFnTc5JfF61oFRe2Ii9g6eUZBVcf8dibeLaKZBN98Sy9IgonOLuZBtRWGw21X8mZC45ZARbTNXurm92iQ2NCP3pZCZCgNuEj4MAQkzdAZDZD"

	def obtenerInformacion(self):
		paramentros = {"access_token": self.token}
		resultado = requests.get(self.url, params = paramentros).json()
		print(resultado)
		self.nombre = resultado ["name"]
		return resultado


	def publicarComentario(self, message):
		self.url = "https://graph.facebook.com/v2.8/feed"
		paramentros = {"message": message, "access_token": self.token}
		resultado = requests.post(self.url, params = paramentros).json()
		print(resultado)
		return resultado

	def borrarComentario(self):
