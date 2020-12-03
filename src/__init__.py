import os
from flask import Flask

app = Flask(__name__)

app.debug = True

from .views import *
from .home.views import *
from .projects.views import *
from .contact.views import *
from .data.views import *
from .socialmedia.views import *



