from pathlib import Path

import pygsheets

import pandas as pd

import requests

gc = pygsheets.authorize(service_file=("/Users/silvia/Documents/python_2023spring/class7/dark-gateway-384601-9e775e0c520f.json"))

sht = gc.open_by_url("https://docs.google.com/spreadsheets/d/1qRmlfNZCPAUgVHKOCIr7TeDoov1Bw49UrzCJzlUPmTA/edit#gid=0")

ws = sht[0]

ws.update_value("A1","國家")
ws.update_value("B1","匯率(以台灣為基準)")
ws.update_value("B2","0.0327")
ws.update_value("A2","美國")
ws.update_value("B3","4.4")
ws.update_value("A3","日本")
ws.update_value("B4","0.257")
ws.update_value("A4","香港")