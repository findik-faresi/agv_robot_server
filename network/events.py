from flask_socketio import join_room, leave_room, emit
from . import socketio

@socketio.on("message")
def handle_send_message(data):
    room = data["room"]
    order = data["order"]
    # emit("controll", {"id": id, "order": order}, room=room)

@socketio.on("join")
def on_join(data):
    room = data["room"]
    join_room(room)
    # emit("join", {"id": id, "status": 200}, room=room)

@socketio.on("leave")
def on_leave(data):
    room = data["room"]
    leave_room(room)
    # emit("leave", {"id": id, "status": 200}, room=room)
