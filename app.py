from flask import Flask, render_template, redirect, url_for, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)
app.app_context().push()

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_adoption_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "pets_R_K00L"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)
# db.drop_all()
# db.create_all()

@app.route('/')
def home_page():
    """Render home page with a list of pets."""

    pets = Pet.query.all()
    return render_template('list_pets.html', pets=pets)

@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """Add a pet."""
    
    form = AddPetForm()

    if form.validate_on_submit():
        new_pet = Pet(name=form.name.data, species=form.species.data, photo_url=form.photo_url.data, age=form.age.data, notes=form.notes.data)
        db.session.add(new_pet)
        db.session.commit()
        return redirect(url_for('home_page'))

    return render_template('add_form.html', form=form)


@app.route('/pet_details/<int:pet_id>', methods=["GET", "POST"])
def show_pet(pet_id):
    """Edit pet."""

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.notes = form.notes.data
        pet.available = form.available.data
        pet.photo_url = form.photo_url.data
        db.session.commit()
        return redirect('/')

    return render_template("edit_form.html", form=form, pet=pet)

@app.route("/api/pets/<int:pet_id>", methods=['GET'])
def api_get_pet(pet_id):
    """Return info about a pet in JSON"""

    pet = Pet.query.get_or_404(pet_id)
    data = {'name': pet.name, 'age': pet.age}

    return jsonify(data)