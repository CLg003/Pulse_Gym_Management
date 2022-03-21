from flask import Flask, render_template
from datetime import datetime

from controllers.member_controller import members_blueprint
from controllers.fitness_class_controller import fitness_classes_blueprint
from controllers.booking_controller import bookings_blueprint
from controllers.contact_controller import contact_blueprint

import repositories.fitness_class_repository as fitness_class_repository

app = Flask(__name__)

app.register_blueprint(members_blueprint)
app.register_blueprint(fitness_classes_blueprint)
app.register_blueprint(bookings_blueprint)
app.register_blueprint(contact_blueprint)

@app.route('/')
def home():
    fitness_classes = fitness_class_repository.select_all()
    today = datetime.now().strftime("%A")
    return render_template('index.html', title="Home", fitness_classes=fitness_classes, today=today)

if __name__ == '__main__':
    app.run(debug=True)