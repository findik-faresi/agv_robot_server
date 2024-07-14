from flask_socketio import emit
from network import socketio
from termcolor import colored

@socketio.on("_c3")
def _c3(payload):
    try:
        data = payload.get("message")
        room_name = payload.get("room_name")

        if not (data and room_name):
            print(colored(f"[!] : Invalid data {data}", "yellow",attrs=["bold"]))
            emit("_sc3", {"message":"Invalid data","status":400}) 
            return

        emit("_sc3", {"message": data,"status":200}, room=room_name)

    except Exception as e:
        print(colored(f"[-] Error handling status event: {str(e)}" "red",attrs=["bold"]))
        emit("_sc3", {"message": "An error occurred while processing your request", "status": 500}, room=room_name)
