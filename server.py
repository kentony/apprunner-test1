from wsgiref.simple_server import make_server
from pyramid.config import Congigurator
from pyramid.response import Response
import os

def hello_world(request):
  name = os.environ.get('NAME')
  if name == None or len(name) == 0:
    name = "world"
  message = "Hello, " + name + "!\n"
