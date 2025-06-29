from flask import Flask, request, jsonify
import json
import os
from datetime import datetime

app = Flask(__name__)

EVENTS_FILE = 'events.json'

def load_events():
    if not os.path.exists(EVENTS_FILE):
        return []
    with open(EVENTS_FILE, 'r') as f:
        return json.load(f)

def save_events(events):
    with open(EVENTS_FILE, 'w') as f:
        json.dump(events, f, indent=4)

@app.route('/events', methods=['POST'])
def create_event():
    data = request.get_json()
    required = ['title', 'description', 'start_time', 'end_time']
    if not all(k in data for k in required):
        return jsonify({'error': 'Missing fields'}), 400
    
    try:
        datetime.fromisoformat(data['start_time'])
        datetime.fromisoformat(data['end_time'])
    except ValueError:
        return jsonify({'error': 'Invalid datetime format. Use ISO format.'}), 400

    events = load_events()
    data['id'] = len(events) + 1
    events.append(data)
    save_events(events)
    return jsonify(data), 201

@app.route('/events', methods=['GET'])
def list_events():
    events = load_events()
    events.sort(key=lambda x: x['start_time'])
    return jsonify(events)

@app.route('/events/<int:event_id>', methods=['PUT'])
def update_event(event_id):
    events = load_events()
    event = next((e for e in events if e['id'] == event_id), None)
    if not event:
        return jsonify({'error': 'Event not found'}), 404
    
    data = request.get_json()
    for key in ['title', 'description', 'start_time', 'end_time']:
        if key in data:
            event[key] = data[key]

    save_events(events)
    return jsonify(event)

@app.route('/events/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
    events = load_events()
    new_events = [e for e in events if e['id'] != event_id]
    if len(events) == len(new_events):
        return jsonify({'error': 'Event not found'}), 404

    save_events(new_events)
    return jsonify({'message': 'Event deleted'})

if __name__ == '__main__':
    app.run(debug=True)
