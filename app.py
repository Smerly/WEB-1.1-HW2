from flask import Flask, request, render_template
import random

app = Flask(__name__)


def sort_letters(message):
    """A helper method to sort the characters of a string in alphabetical order
    and return the new string."""
    return ''.join(sorted(list(message)))


@app.route('/')
def homepage():
    """A homepage with handy links for your convenience."""
    return render_template('home.html')


@app.route('/froyo')
def choose_froyo():
    """Shows a form to collect the user's Fro-Yo order."""
    return render_template('froyo_form.html')


@app.route('/froyo_results', methods=['GET'])
def show_froyo_results():

    context = {
        'users_froyo_flavor': request.args.get('flavor'),
        'users_froyo_toppings': request.args.get('topping')
    }

    return render_template('froyo_results.html', **context)


@app.route('/favorites')
def favorites():
    """Shows the user a form to choose their favorite color, animal, and city."""
    return """
    <form action='/favorites_results' method='GET'>
        <label> What is your favorite color? </label>
        <input type='text' name='color'>

        <label> What is your favorite animal? </label>
        <input type='text' name='animal'>

        <label> What is your favorite city?</label>
        <input type='text' name='city'>
        
        <input type='submit' value='Submit'>
    </form>
    """


@app.route('/favorites_results')
def favorites_results():
    """Shows the user a nice message using their form results."""
    users_favorites_color = request.args.get('color')
    users_favorites_animal = request.args.get('animal')
    users_favorites_city = request.args.get('city')
    return f'Wow! I didn\'t know {users_favorites_color} {users_favorites_animal}s live in {users_favorites_city}'


@app.route('/secret_message')
def secret_message():
    """Shows the user a form to collect a secret message. Sends the result via
    the POST method to keep it a secret!"""
    return """
    <form action='/message_results' method='POST'>
        <label> Enter your secret message </label>
        <input type='text' name='message'> 
        <input type='submit' value='Submit'>
    </form>
    """


@app.route('/message_results', methods=['POST'])
def message_results():
    """Shows the user their message, with the letters in sorted order."""
    users_secret_message = request.form.get('message')
    return f'{sort_letters(users_secret_message)}'


@app.route('/calculator')
def calculator():
    """Shows the user a form to enter 2 numbers and an operation."""
    return render_template('calculator_form.html')


@app.route('/calculator_results', methods=['GET'])
def calculator_results():
    """Shows the user the result of their calculation."""
    context = {
        'users_calc_num1': request.args.get('operand1'),
        'users_calc_num2': request.args.get('operand2'),
        'users_calc_operation': request.args.get('operation')
    }

    return render_template('calculator_results.html', **context)


HOROSCOPE_PERSONALITIES = {
    'aries': 'Adventurous and energetic',
    'taurus': 'Patient and reliable',
    'gemini': 'Adaptable and versatile',
    'cancer': 'Emotional and loving',
    'leo': 'Generous and warmhearted',
    'virgo': 'Modest and shy',
    'libra': 'Easygoing and sociable',
    'scorpio': 'Determined and forceful',
    'sagittarius': 'Intellectual and philosophical',
    'capricorn': 'Practical and prudent',
    'aquarius': 'Friendly and humanitarian',
    'pisces': 'Imaginative and sensitive'
}


@app.route('/horoscope')
def horoscope_form():
    """Shows the user a form to fill out to select their horoscope."""
    return render_template('horoscope_form.html')


@app.route('/horoscope_results', methods=['GET'])
def horoscope_results():
    """Shows the user the result for their chosen horoscope."""

    horoscope_sign = request.args.get('horoscope_sign')
    users_personality = HOROSCOPE_PERSONALITIES.get(horoscope_sign, None)
    # TODO: Get the sign the user entered in the form, based on their birthday
    # if horoscope_sign == 'aries':
    #     horoscope_sign = 'aries'
    # elif horoscope_sign == 'taurus':
    #     horoscope_sign = 'taurus'
    # elif horoscope_sign == 'gemini':
    #     horoscope_sign = 'gemini'
    # elif horoscope_sign == 'cancer':
    #     horoscope_sign = 'cancer'
    # elif horoscope_sign == 'leo':
    #     horoscope_sign = 'leo'
    # elif horoscope_sign == 'virgo':
    #     horoscope_sign = 'virgo'
    # elif horoscope_sign == 'libra':
    #     horoscope_sign = 'libra'
    # elif horoscope_sign == 'scorpio':
    #     horoscope_sign = 'scorpio'
    # elif horoscope_sign == 'sagittarius':
    #     horoscope_sign = 'sagittarius'
    # elif horoscope_sign == 'capricorn':
    #     horoscope_sign = 'capricorn'
    # elif horoscope_sign == 'aquarius':
    #     horoscope_sign = 'aquarius'
    # elif horoscope_sign == 'pisces':
    #     horoscope_sign = 'pisces'

    # TODO: Look up the user's personality in the HOROSCOPE_PERSONALITIES
    # dictionary based on what the user entered

    # TODO: Generate a random number from 1 to 99
    lucky_number = random.randint(0, 100)

    context = {
        'users_name': request.args.get('users_name'),
        'horoscope_sign': horoscope_sign,
        'personality': users_personality,
        'lucky_number': lucky_number
    }

    return render_template('horoscope_results.html', **context)


if __name__ == '__main__':
    app.config['ENV'] = 'development'
    app.run(debug=True)
