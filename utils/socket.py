
from flask_socketio import SocketIO
socketio = SocketIO()


def register_socket(app):
    socketio.init_app(app)
