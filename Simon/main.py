
# Daten sollen von einer xml schnittstelle geholt, in eine csv datei umgeschrieben und dann in eine postgresql Datenbank geschrieben werden

import requests as req
import os
import csv
import xml.etree.ElementTree as ET
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import psycopg2 as pg


