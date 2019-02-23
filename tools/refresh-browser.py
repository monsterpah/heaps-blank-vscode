# reference
# https://pypi.org/project/websocket-client/
from websocket import create_connection
import sys
try:
	ws = create_connection("ws://localhost:9001")
	ws.send("reload_req")
	print("Sent")
	ws.close()
except ConnectionRefusedError:
	print("Failed to connect to websocket server.")
	print("forgot to run export/ws-server.py ?")	
	sys.exit()