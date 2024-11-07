from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return render_template('index.html')  # Serve the HTML page

# Handle Offer
@socketio.on('offer')
def handle_offer(offer):
    emit('offer', offer, broadcast=True, include_self=False)

# Handle Answer
@socketio.on('answer')
def handle_answer(answer):
    emit('answer', answer, broadcast=True, include_self=False)

# Handle ICE Candidate
@socketio.on('candidate')
def handle_candidate(candidate):
    emit('candidate', candidate, broadcast=True, include_self=False)


if __name__ == '__main__':
    # Use your .crt and .key files here
    ssl_context = ('server.crt', 'server.key')
    socketio.run(app, debug=True, host='0.0.0.0', port=5000, ssl_context=ssl_context)
