from database import Base, db_session

import models
from models import Barbershop, BarbershopPhoto, HaircutType
Base.metadata.create_all(bind=engine)

barbershop = Barbershop('Ляйсан')
db_session.add(barbershop)
barbershop.query.all()
db_session.commit()
barbershop.phone_number = '2-237-654'
barbershop.description = '''Давно выяснено, что при оценке дизайна и композиции читаемый текст мешает сосредоточиться. Lorem Ipsum используют потому, что тот обеспечивает более или менее стандартное заполнение шаблона, а также реальное распределение '''
barbershop.latitude
barbershop.longitude
barbershop.stars = 4.5
barbershop.address = 'Кувыкино, 16'
barbershop.saloon_type = 'Мужской салон'
db_session.commit()

barbershop_photo = BarbershopPhoto(1, 'media/barbershop_photos/1/1.jpg')
db_session.add(barbershop_photo)
barbershop_photo = BarbershopPhoto(1, 'media/barbershop_photos/1/2.jpg')
db_session.add(barbershop_photo)
barbershop_photo = BarbershopPhoto(1, 'media/barbershop_photos/1/3.jpg')
db_session.add(barbershop_photo)

haircut_type = HaircutType(1, 'классический', 200)
db_session.add(haircut_type)
haircut_type = HaircutType(1, 'спортивный', 300)
db_session.add(haircut_type)
haircut_type = HaircutType(1, 'романтический', 400)
db_session.add(haircut_type)
haircut_type = HaircutType(1, 'шапочка', 500)
db_session.add(haircut_type)


barbershop = Barbershop('Костя и Максим')
db_session.add(barbershop)
barbershop.query.all()
db_session.commit()
barbershop.phone_number = '2-75127'
barbershop.description = '''Давно выяснено, что при оценке дизайна и композиции читаемый текст мешает сосредоточиться. Lorem Ipsum используют потому, что тот обеспечивает более или менее стандартное заполнение шаблона, а также реальное распределение '''
barbershop.latitude
barbershop.longitude
barbershop.stars = 4
barbershop.address = 'Ростовская, 205'
barbershop.saloon_type = 'Салон красоты'
db_session.commit()

barbershop_photo = BarbershopPhoto(2, 'media/barbershop_photos/2/1.jpg')
db_session.add(barbershop_photo)
barbershop_photo = BarbershopPhoto(2, 'media/barbershop_photos/2/2.jpg')
db_session.add(barbershop_photo)

haircut_type = HaircutType(2, 'классический', 200)
db_session.add(haircut_type)
haircut_type = HaircutType(2, 'спортивный', 300)
db_session.add(haircut_type)
haircut_type = HaircutType(2, 'романтический', 400)
db_session.add(haircut_type)
haircut_type = HaircutType(2, 'шапочка', 500)
db_session.add(haircut_type)

barbershop = Barbershop('Ватрюскин')
db_session.add(barbershop)
barbershop.query.all()
db_session.commit()
barbershop.phone_number = '2-75127'
barbershop.description = '''Давно выяснено, что при оценке дизайна и композиции читаемый текст мешает сосредоточиться. Lorem Ipsum используют потому, что тот обеспечивает более или менее стандартное заполнение шаблона, а также реальное распределение '''
barbershop.latitude
barbershop.longitude
barbershop.stars = 4
barbershop.address = 'Николаева, 2'
barbershop.saloon_type = 'Мужской салон'
db_session.commit()

barbershop_photo = BarbershopPhoto(3, 'media/barbershop_photos/3/1.jpg')
db_session.add(barbershop_photo)
barbershop_photo = BarbershopPhoto(3, 'media/barbershop_photos/3/2.jpg')
db_session.add(barbershop_photo)

haircut_type = HaircutType(3, 'классический', 200)
db_session.add(haircut_type)
haircut_type = HaircutType(3, 'спортивный', 300)
db_session.add(haircut_type)
haircut_type = HaircutType(3, 'романтический', 400)
db_session.add(haircut_type)
haircut_type = HaircutType(3, 'шапочка', 500)
db_session.add(haircut_type)

barbershop = Barbershop('Ватрюскин')
db_session.add(barbershop)
barbershop.query.all()
db_session.commit()
barbershop.phone_number = '2-75127'
barbershop.description = '''Давно выяснено, что при оценке дизайна и композиции читаемый текст мешает сосредоточиться. Lorem Ipsum используют потому, что тот обеспечивает более или менее стандартное заполнение шаблона, а также реальное распределение '''
barbershop.latitude
barbershop.longitude
barbershop.stars = 5
barbershop.address = 'Николаева, 2'
barbershop.saloon_type = 'Мужской салон'
db_session.commit()

barbershop_photo = BarbershopPhoto(4, 'media/barbershop_photos/4/1.jpg')
db_session.add(barbershop_photo)

haircut_type = HaircutType(4, 'классический', 200)
db_session.add(haircut_type)
haircut_type = HaircutType(4, 'спортивный', 300)
db_session.add(haircut_type)
haircut_type = HaircutType(4, 'романтический', 400)
db_session.add(haircut_type)
haircut_type = HaircutType(4, 'шапочка', 500)
db_session.add(haircut_type)

db_session.commit()
