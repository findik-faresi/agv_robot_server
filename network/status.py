from flask_socketio import emit
from termcolor import colored

from . import socketio

@socketio.on("status")
def status(payload):
    try:
        data = payload.get("message")
        room_name = payload.get("room_name")

        if not (data and room_name):
            print(colored(f"[!] : Invalid data {data}", "yellow", attrs=["bold"]))
            emit("status", {"message":"Invalid data","status":400}, room=room_name) 
            return

        emit("status", {"message": data,"status":200}, room=room_name)

    except Exception as e:
        print(colored(f"[-] Error handling status event: {str(e)}", "red", attrs=["bold"]))
        emit("status", {"message": "An error occurred while processing your request", "status": 500}, room=room_name)
