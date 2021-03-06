import asyncio
import re
from inspect import signature
import logging
import asyncio
import discord
from discord.ext import commands
from typing import Union

__all__ = ["Bot"]

__version__ = "0.0.6-pre1"

class Bot(commands.Bot):
	"""
	A pre-made bot with extensions like Jishaku, etc..
	"""
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.cog_list = ['jishaku']
	
	def run(self, token):
		for ext in self.cog_list:
			self.load_extension(ext)
		self.run(token)			
