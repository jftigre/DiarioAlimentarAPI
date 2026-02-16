from flask import Flask, jsonify, request
from database import db
from models.meal import Meal


app = Flask(__name__)
app.config["SECRET_KEY"] = "your_secret_key"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://admin:admin123@127.0.0.1:3306/daily_diet"

db.init_app(app)

@app.route("/meals", methods=['POST'])
def create_meal():
    data = request.get_json()
    
    name = data.get('name')
    description = data.get('description')
    datetime_value = data.get('datetime')
    is_diet = data.get('is_diet')

    if name and description and datetime_value and is_diet is not None:
        new_meal = Meal(
            name=name,
            description=description,
            datetime=datetime_value,
            is_diet=is_diet
        )
        db.session.add(new_meal)
        db.session.commit()
        return jsonify({"message": "Alimentação cadastrada com sucesso"}), 201

    return jsonify({"message": "Dados inválidos"}), 400

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)