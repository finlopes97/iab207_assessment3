from flask import Blueprint, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from .models import Event
from .forms import EventCreationForm
from . import db
import uuid, os

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    events = db.session.scalars(db.select(Event)).all()
    return render_template('index.html', events=events)

@bp.route('/user')
def user():
    return render_template('user.html')

@bp.route('/event/<id>')
def event(id):
    event = db.session.scalar(db.select(Event).where(Event.id==id))
    return render_template('event.html', event=event)

@bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        create_form = EventCreationForm()
        
        if create_form.validate_on_submit():
            print('User has submitted the event creation form for validation...')
            # Build a filename for the image path
            filename = str(uuid.uuid4())
            uploaded_file = create_form.image.data
            secure_filename(uploaded_file.filename)
            # Set the image path to the static folder
            save_path = os.path.join('website/static/img/events', filename)
            uploaded_file.save(save_path)
        
            event = Event(
                title=create_form.title.data,
                description=create_form.description.data,
                image=filename,
                dateTime=create_form.date.data,
                price=create_form.price.data,
                ticketsAvailable=create_form.tickets.data,
                locationName=create_form.location.data
            )
            
            db.session.add(event)
            db.session.commit()

            return redirect(url_for('views.index'))    
    return render_template('create.html', create_form=create_form)
    
@bp.route('/bookings')
def bookings():
    return render_template('bookings.html')