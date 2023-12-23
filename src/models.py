from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

FavoritePeople = db.Table("FavoritePeople", 
db.Column("userId", db.Integer, db.ForeignKey("user.id"), primary_key=True),
db.Column("peopleId", db.Integer, db.ForeignKey("people.id"), primary_key=True)
)
FavoritePlanets = db.Table("FavoritePlanets", 
db.Column("userId", db.Integer, db.ForeignKey("user.id"), primary_key=True),
db.Column("planetsId", db.Integer, db.ForeignKey("planets.id"), primary_key=True)
)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    favoritePeople = db.relationship("People", secondary = "FavoritePeople")
    favoritePlanets = db.relationship("Planets", secondary = "FavoritePlanets")

    def __repr__(self):
        return '<User %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "favoritePeople": list(map(lambda x: x.serialize(), self.favoritePeople)),
            "favoritePlanets": list(map(lambda x: x.serialize(), self.favoritePlanets))
            # do not serialize the password, its a security breach

        }

class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=False, nullable=False)
    eye_color = db.Column(db.String(80), unique=False, nullable=True)
    gender = db.Column(db.String(80), unique=False, nullable=True)
    birth_year = db.Column(db.String(120), unique=False, nullable=False)
    # favorites = db.relationship("Favorites",backref = "People")

    def __repr__(self):
        return '<People %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "eye_color": self.eye_color,
            "gender": self.gender,
            "birth_year": self.birth_year
            
            # do not serialize the password, its a security breach
        }

class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    climate = db.Column(db.String(120), unique=False, nullable=True)
    population = db.Column(db.Integer, unique=False, nullable=True)
    orbital_period = db.Column(db.Float, unique=False, nullable=False)
    gravity = db.Column(db.String(120), unique=False, nullable=False)
    # favorites = db.relationship("Favorites",backref = "Planets")

    def __repr__(self):
        return '<Planets %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "climate": self.climate,
            "population": self.population,
            "orbital_period": self.orbital_period,
            "gravity": self.gravity
            # do not serialize the password, its a security breach
        }

# class Favorites(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     userId = db.Column(db.Integer, db.ForeignKey("user.id"))
#     characterId = db.Column(db.Integer, db.ForeignKey("character.id"))
#     planetId = db.Column(db.Integer, db.ForeignKey("planet.id"))

#     def __repr__(self):
#         return '<Favorites %r>' % self.name

#     def serialize(self):
#         return {
#             "id": self.id,
#             "userId": self.userId,
#             "charactesId": self.characterId,
#             "planetId": self.planetId
#             # do not serialize the password, its a security breach

#         }
