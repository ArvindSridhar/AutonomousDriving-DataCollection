# Backend image processor and deep learning model

import pymongo
from pymongo import MongoClient
import numpy as np
import tensorflow as tf

class BackendProcessor:
	def __init__(self):
		client = MongoClient("mongodb://arvindsridhar:addeepl3arning92@ds225028.mlab.com:25028/autonomousdriving")
		db = client.autonomousdriving
		timestamps = db.timestamps
		all_stamps = timestamps.find()
		self.data_dict = {}
		for stamp in all_stamps:
			try:
				self.data_dict[str(stamp['_id'])] = {"video_name": stamp["name"],
									   "clicks": stamp["clickLogs"]}
			except:
				self.data_dict[str(stamp['_id'])] = {"video_name": stamp["vidURL"],
									   "clicks": stamp["clickLogs"]}
		print(timestamps.find_one())
		print(self.data_dict["5a9890107f83c74e289cc500"])

	def get_images(self):
		return None
		