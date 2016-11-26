from flask import Flask, render_template, jsonify, session, redirect, url_for
from flask import request

import os
import datetime

from models import Barbershop, BarbershopPhoto, HaircutType, BarbershopUser, Booking
from database import db_session

app = Flask(__name__)

from flask import send_from_directory

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/partner/')
def partner_signup():
    return render_template('partner/signup.html')

@app.route('/partner/sign-in/')
def partner_singin():
    if 'barbershop_id' in session:
        return redirect(url_for('partner_panel'))
    else:
        return render_template('partner/signin.html')

@app.route('/partner/panel/')
def partner_panel():
    if 'barbershop_id' in session:
        barbershop =get_barbershop_by_id(session['barbershop_id'])
        bookings = Booking.query.filter_by(barbershop_id=barbershop['id']).all()
        barbershop['bookings'] = bookings
        return render_template('partner/panel.html', barbershop= barbershop)
    else:
        return redirect(url_for('partner_singin'))


@app.route('/api/partner/login/', methods=['POST'])
def partner_login():
    login = request.form['login']
    password = request.form['password']
    users=BarbershopUser.query.filter_by(username=login, password=password).all()
    if users:
        user = BarbershopUser.query.filter_by(username=login, password=password).all()[0]
        session['user_id'] = user.id
        session['barbershop_id'] = user.barbershop_id
        return redirect(url_for('partner_panel'))
    else:
        return redirect(url_for('partner_singin'))


@app.route('/api/barbershops/booking/add/', methods=['POST'])
def add_booking():
    booking = Booking()
    booking.client_name = request.form['name']
    booking.client_phone = request.form['phone']
    booking.created_at = datetime.datetime.now()
    booking.time_to = datetime.datetime.now() + datetime.timedelta(hours=2)
    booking.closed = False
    booking.barbershop_id = request.form['bbShop']
    db_session.add(booking)
    db_session.commit()
    return 'ok'


@app.route('/api/barbershops/booking/close/', methods=['POST'])
def close_booking():
    id = request.form['id']
    booking = db_session.query(Booking).get(id)
    booking.closed = True
    print(booking.id, booking.closed )
    db_session.commit()
    return redirect(url_for('partner_panel'))

@app.route('/api/barbershops/all_data/')
def get_barbershop_all_data():
    barbershops = Barbershop.query.all()
    to_json = []
    for barbershop in barbershops:
        photos = BarbershopPhoto.query.filter_by(barbershop_id=barbershop.id).all()
        haircut_types = HaircutType.query.filter_by(barbershop_id=barbershop.id).all()

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
        to_json.append({
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
        })
    return jsonify(to_json)

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
    to_json = get_barbershop_by_id(id)

    return jsonify(to_json)


def get_barbershop_by_id(id):
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
    obj = {
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
    return obj


app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
