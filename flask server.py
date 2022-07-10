from flask import Flask, request, Response
import random

app = Flask(__name__)

random.seed("this a seed")
"""
65
9
32
49
27
"""

data = {}

# __name__ is passed as the paremater
@app.route('/data')
# when the home page is open
# e.g https://yourwebsite/
def data():
    return {'stages': [{'name': 'Rebirth', 'substages': ['Movement', 'Pummel', 'Gunner', 'Cascade', 'Elevate', 'Bounce', 'Purify', 'Climb', 'Fasttrack', 'Glass Port'], 'users': [{'name': 'Adam', 'user_id': 1, 'wins': 10, 'times': [(19.21, 1), (8.46, 1), (11.23, 1), (12.317, 1), (17.4, 1), (20.75, 1), (11.85, 1), (22.384, 1), (28.3, 1), (27.934, 1)]}, {'name': 'Austin', 'user_id': 2, 'wins': 0, 'times': [(19.71, -1), (9.28, -1), (12.53, -1), (13.74, -1), (17.44, -1), (21.2, -1), (19.71, -1), (22.85, -1), (28.34, -1), (29.74, -1)]}]}, {'name': 'Killer Inside', 'substages': ['Take Flight', 'Godspeed', 'Dasher', 'Thrasher', 'Outstretched', 'Smackdown', 'Catwalk', 'Fastlane', 'Distinguish', 'Dancer'], 'users': [{'name': 'Adam', 'user_id': 1, 'wins': 10, 'times': [(18.25, 1), (9.066, 1), (12.75, 1), (14.3, 1), (12.2, 1), (12.71, 1), (15.81, 1), (25.86, 1), (17.68, 1), (18.183, 1)]}, {'name': 'Austin', 'user_id': 2, 'wins': 0, 'times': [(19.74, -1), (9.984, -1), (12.98, -1), (15.66, -1), (15.21, -1), (17.39, -1), (17.96, -1), (28.18, -1), (23.61, -1), (24.16, -1)]}]}, {'name': 'Only Shallow', 'substages': ['Guardian', 'Stomp', 'Jumper', 'Dash Tower', 'Descent', 'Driller', 'Canals', 'Sprint', 'Mountain', 'Superkinetic'], 'users': [{'name': 'Adam', 'user_id': 1, 'wins': 6, 'times': [(26.73, 1), (18.75, 1), (23.717, -1), (17.65, 1), (13.386, 1), (16.5, -1), (37.168, -1), (24.968, -1), (23.65, 1), (23.867, 1)]}, {'name': 'Austin', 'user_id': 2, 'wins': 4, 'times': [(29.4, -1), (19.56, -1), (22.68, 1), (18.09, -1), (15.73, -1), (14.88, 1), (35.48, 1), (21.64, 1), (24.85, -1), (30.21, -1)]}]}, {'name': 'The Old City', 'substages': ['Arrival', 'Forgotten City', 'Clocktower', '', '', '', '', '', '', ''], 'users': [{'name': 'Adam', 'user_id': 1, 'wins': 3, 'times': [(23.617, 1), (35.667, 1), (91.503, 1), '', '', '', '', '', '', '']}, {'name': 'Austin', 'user_id': 2, 'wins': 0, 'times': [(23.94, -1), (36.78, -1), (94.63, -1), '', '', '', '', '', '', '']}]}, {'name': 'The Burn That Cures', 'substages': ['Fireball', 'Ringer', 'Cleaner', 'Warehouse', 'Boom', 'Streets', 'Steps', 'Demolition', 'Arcs', 'Apartment'], 'users': [{'name': 'Adam', 'user_id': 1, 'wins': 9, 'times': [(23.101, 1), (19.95, 1), (25.117, 1), (14.367, 1), (24.15, -1), (14.65, 1), (17.934, 1), (13.05, 1), (25.084, 1), (34.167, 1)]}, {'name': 'Austin', 'user_id': 2, 'wins': 1, 'times': [(23.91, -1), (22.52, -1), (27.39, -1), (15.04, -1), (23.26, 1), ('', 0), ('', 0), ('', 0), ('', 0), ('', 0)]}]}, {'name': 'Convenant', 'substages': ['Hanging Gardens', 'Tangled', 'Waterworks', 'Killswitch', 'Falling', 'Shocker', 'Bouquet', 'Prepare', 'Triptrack', 'Race'], 'users': [{'name': 'Adam', 'user_id': 1, 'wins': 10, 'times': [(37.23, 1), (20.884, 1), (23.567, 1), (30.33, 1), (27.617, 1), (33.867, 1), (31.117, 1), (33.051, 1), (42.301, 1), (30.067, 1)]}, {'name': 'Austin', 'user_id': 2, 'wins': 0, 'times': [('', 0), ('', 0), ('', 0), ('', 0), ('', 0), ('', 0), ('', 0), ('', 0), ('', 0), ('', 0)]}]}, {'name': 'Reckoning', 'substages': ['Bubble', 'Shield', 'Overlook', 'Pop', 'Minefield', 'Mimic', 'Trigger', 'Greenhouse', 'Sweep', 'Fuse'], 'users': [{'name': 'Adam', 'user_id': 1, 'wins': 10, 'times': [(22.534, 1), (26.3, 1), (19.067, 1), (39.734, 1), (21.234, 1), (14.317, 1), (27.667, 1), (16.583, 1), (23.8, 1), (40.71, 1)]}, {'name': 'Austin', 'user_id': 2, 'wins': 0, 'times': [('', 0), ('', 0), ('', 0), ('', 0), ('', 0), ('', 0), ('', 0), ('', 0), ('', 0), ('', 0)]}]}, {'name': 'Benediction', 'substages': ['Heavens Edge', 'Zipline', 'Swing', 'Chute', 'Crash', 'Ascent', 'Straightaway', 'Firecracker', 'Streak', 'Mirror'], 'users': [{'name': 'Adam', 'user_id': 1, 'wins': 10, 'times': [(21.75, 1), (19.05, 1), (24.317, 1), (50.868, 1), (38.768, 1), (37.784, 1), (46.068, 1), (45.934, 1), (44.051, 1), (54.135, 1)]}, {'name': 'Austin', 'user_id': 2, 'wins': 0, 'times': [('', 0), ('', 0), ('', 0), ('', 0), ('', 0), ('', 0), ('', 0), ('', 0), ('', 0), ('', 0)]}]}, {'name': 'Apocrypha', 'substages': ['Escalation', 'Bolt', 'Godstreak', 'Plunge', 'Mayhem', 'Barrage', 'Estate', 'Trapwire', 'Ricochet', 'Fortress'], 'users': [{'name': 'Adam', 'user_id': 1, 'wins': 0, 'times': [('', 0), ('', 0), ('', 0), ('', 0), ('', 0), ('', 0), ('', 0), ('', 0), ('', 0), ('', 0)]}, {'name': 'Austin', 'user_id': 2, 'wins': 0, 'times': [('', 0), ('', 0), ('', 0), ('', 0), ('', 0), ('', 0), ('', 0), ('', 0), ('', 0), ('', 0)]}]}, {'name': 'The Third Temple', 'substages': ['Holy Ground', 'The Third Temple', '', '', '', '', '', '', '', ''], 'users': [{'name': 'Adam', 'user_id': 1, 'wins': 0, 'times': [('', 0), ('', 0), '', '', '', '', '', '', '', '']}, {'name': 'Austin', 'user_id': 2, 'wins': 0, 'times': [('', 0), ('', 0), '', '', '', '', '', '', '', '']}]}, {'name': 'Thousand Pound Butterfly', 'substages': ['Spree', 'Breakthrough', 'Glide', 'Closer', 'Hike', 'Switch', 'Access', 'Congregation', 'Sequence', 'Marathon'], 'users': [{'name': 'Adam', 'user_id': 1, 'wins': 0, 'times': [('', 0), ('', 0), ('', 0), ('', 0), ('', 0), ('', 0), ('', 0), ('', 0), ('', 0), ('', 0)]}, {'name': 'Austin', 'user_id': 2, 'wins': 0, 'times': [('', 0), ('', 0), ('', 0), ('', 0), ('', 0), ('', 0), ('', 0), ('', 0), ('', 0), ('', 0)]}]}, {'name': 'Hand Of God', 'substages': ['Sacrifice', 'Absolution', '', '', '', '', '', '', '', ''], 'users': [{'name': 'Adam', 'user_id': 1, 'wins': 0, 'times': [('', 0), ('', 0), '', '', '', '', '', '', '', '']}, {'name': 'Austin', 'user_id': 2, 'wins': 0, 'times': [('', 0), ('', 0), '', '', '', '', '', '', '', '']}]}], 'stats_users': [{'name': 'Adam', 'wins': 68}, {'name': 'Austin', 'wins': 5}]}



@app.route('/about/')
# when the about page is open
# https://yourwebsite/about/
def about():
    return "About Text"


@app.route('/login', methods=["POST"])
# when the about page is open
# https://yourwebsite/about/
def login():
    if random.randint(0, 100) == 65:
        return Response(status=403)
    return Response(status=200)


# when running your file the file name is __main__
# whatever you name it
# but when importing the file the name will be the name you named it
# so to run this file without importing we passed in the paremater __name__
# which is equal to __main__
# so we have to make sure it runs only from this file
if __name__ == "__main__":
    app.run()
