#!/usr/bin/python
# -*- coding: latin-1 -*-

#model usado como exemplo, suas consultas devem ser construidas conforme sua necessidade

from donaclotilde.donaclotilde import *

from datetime import date
import sqlite3



class Model(Donaclotilde):
	"""ATRIBUTOS DO Model HERDADOS DE Donaclotilde"""
	""" /entrada_select /entrada_count /entrada_from_table /entrada_where /entrada_insert /query """
	def __init__(self):
		super().__init__()
		self.map={}
		self.map['user'] = [
			["id", "inter key "],
			["name", "string"],
			["name", "string"],
			["name", "string"],
		]
		
		"""
		talves proximo passso, declarar os valores do banco de dados em um dicionario no model
		dessa forma controlar e mapear db automaticamente no codigo
		desenvolver exemplo acima para melhor aprimorar o conceito gradativamente

		self.map[''] = "user"
		self.map['TABLE'] = "user"
		tabela dados

			0"sge_loc_id"	INTEGER,
			1"unidade"	TEXT,
			2"grupo_pavilhao"	TEXT,
			3"pavilhao"	TEXT,
			"area_banca"	TEXT,
			"m2_area"	TEXT,
			"ilha_coluna"	TEXT,
			"banca_numero"	INTEGER,
			"valor_contrato"	TEXT,
			"metragem_area_contrato"	TEXT,
			"valor_m2"	TEXT,
			"status"	TEXT,
			"tipo_contrato"	TEXT,
			"nr_contrato"	INTEGER,
			"nome_permissionario"	TEXT,
			"matricula"	INTEGER,
			"ini_vigencia"	TEXT,
			"fim_vigencia"	TEXT,
			"dt_encerrado"	TEXT,
			"area_funcao"	TEXT,
			"uso_administrativo"	TEXT,
			"area_ativa"	TEXT,
			"crdii_financeiro"	REAL,
			"mezanino_m2"	TEXT,
			"ponderacao_tempo_uso"	TEXT,
			"data_base"	TEXT

		"""
	"""	
	def connect_db(self):
		self.conn = sqlite3.connect('database.db')
		self.cursor = self.conn.cursor()

	"""
	def save(self,kwargs):
		#original
		values=[x for x in kwargs.values()]
		columns=[x for x in kwargs.keys()]
		
		sql = self.set("user",values,columns)
		#print(sql)
		self.insert(sql)

	def update(self,kwargs):
		#original
		values=[x for x in kwargs.values()]
		columns=[x for x in kwargs.keys()]
		
		self.where( 5 ,"id","=")
		
		sql = self.setup("user",values,columns)
		#print(sql)
		self.insert(sql)


	def update_consulta(self,dado,condicao):
		#modificado
		kwargs={}
		kwargs['nome_permissionario'] = dado

		values=[x for x in kwargs.values()]
		columns=[x for x in kwargs.keys()]
		
		
		self.where( condicao[0] ,"ilha_coluna","=")
		
		self.where_combining("AND")
		
		self.where( condicao[1] ,"banca_numero","=")

		self.where_combining("AND")
		
		self.where( condicao[2] ,"nome_permissionario","=")
		
		sql = self.setup("dados",values,columns)
		#print(sql)
		self.insert(sql)

	def list_all(self):
		#modificado
		self.select('*')
		
		self.from_table("dados")
		
		sql = self.get()
		data = self.result_list(sql)
		return data
		
	def lista_limite(self, limite):

		self.select('*')
		
		self.from_table("dados")
		self.limit(limite,10)
		sql = self.get()
		data = self.result_list(sql)
		return data
	def lista_empresas_filt(self, busca=None):

		self.select('nome_permissionario')
		self.select('ilha_coluna')
		self.select('banca_numero')

		
		self.from_table("dados")

		if busca:
			self.where(busca,"nome_permissionario")

		sql = self.get()
		data = self.result_list(sql)
		return data
	def consulta(self,ilha,banca):
		#terminar

		self.select('nome_permissionario')
		self.from_table("dados")
		self.where(ilha,"ilha_coluna","=")
		self.where_combining("AND")
		self.where(banca,"banca_numero","=")
		#self.where_combining("AND")
		#self.where(banca,"area_banca","=")

		sql = self.get()
		data = self.result_list(sql)
		return data
	
	def listar_cordenadas(self):

		self.select('nome_permissionario')
		self.select('cordenada_x')
		self.select('cordenada_y')
		
		self.from_table("dados")
		
		sql = self.get()
		data = self.result_list(sql)
		return data


	def list_filter(self,search=None, coluna=None):
		
		#self.select('id')
		self.select('name')

		if coluna:
			self.select('adress')
		#self.select('number')
		self.select('password')
		#self.select('last')
		
		self.from_table("user")

		if search:
			self.where(search,"name")
			self.where_combining("AND")
			self.where("Josef Stalin","name","=")

		sql = self.get()
		data = self.result_list(sql)
		return data		
		pass

	def list_filter_where(self,search=None, id=1):
		
		#self.select('id')
		self.select('name')
		self.select('adress')
		#self.select('number')
		self.select('password')
		#self.select('last')
		
		self.from_table("user")

		if search:
			self.where(search,"name","LIKE","start")
			self.where_combining("AND")
			self.where_combining("(")

			self.where( id ,"id","=")
			self.where_combining("OR")
			self.where( "321" ,"password","=")

			self.where_combining(")")


		sql = self.get()
		data = self.result_list(sql)
		return data		
		pass

	def list_count(self, search):
		
		self.count('*')
		
		self.from_table("user")

		if search:
			self.where(search,"name")
			
			self.where_combining("OR")
			self.where("sta","name")
			
		sql = self.get()
		data = self.result_list(sql)
		return data		
		pass
		


	def list_limite(self):

		self.select('*')
		
		self.from_table("user")
		self.limit(3,2)
		sql = self.get()
		data = self.result_list(sql)
		return data

	def list_order(self):

		self.select('*')
		
		self.from_table("user")
		
		#self.order("name")
		#self.order_desc("name")
		
		self.order_desc("number")
		self.order_asc('name')
		
		sql = self.get()
		data = self.result_list(sql)
		return data




