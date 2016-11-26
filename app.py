from flask import Flask
from flask import render_template
from flask import jsonify

import os

from models import Barbershop, BarbershopPhoto, HaircutType
from database import db_session

app = Flask(__name__)

from flask import send_from_directory

@app.route('/api/barbershops/map_list/')
def get_barbershop_map_list():
    barbershops = Barbershop.query.all()
    to_json = []
    for barbershop in barbershops:
        to_json.append({
            'id': barbershop.id,
            'name': barbershop.name
        })
    return jsonify(to_json)


@app.route('/api/barbershops/<int:id>/')
def get_barbershop_info(id):
    barbershop = db_session.query(Barbershop).get(id)
    photos = BarbershopPhoto.query.filter_by(barbershop_id=id).all()
    haircut_types = HaircutType.query.filter_by(barbershop_id=id).all()

    photos_to_json = []
    for photo in photos:
        photos_to_json.append({
            'url': photo.file_path
        })
    haircut_type_to_json = []
    for haircut_type in haircut_types:
        haircut_type_to_json.append({
            'name': haircut_type.name,
            'price': haircut_type.price
        })
    to_json = {
        'id': barbershop.id,
        'name': barbershop.name,
        'phone_number': barbershop.phone_number,
        'description': barbershop.description,
        'working_time': barbershop.working_time,
        'latitude': barbershop.latitude,
        'longitude': barbershop.longitude,
        'stars': barbershop.stars,
        'address': barbershop.address,
        'saloon_type': barbershop.saloon_type,
        'photos': photos_to_json,
        'haircut_types': haircut_type_to_json,
    }

    return jsonify(to_json)



app.run(host='0.0.0.0', debug=True)
