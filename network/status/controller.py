from flask_socketio import emit
from network import socketio

@socketio.on("_c3")
def _c3(payload):
    try:
        room = payload.get("room")
        data = payload.get("data")

        if not (room and data):
            emit("_sc3", {"message":"Invalid data","status":400}) 
            return

        emit("_sc3", {"data": data,"status":200}, room=room)

    except Exception as e:
        print(f"Error handling _c3 event: {str(e)}")
        emit("_sc3", {"message": "An error occurred while processing your request", "status": 500})
