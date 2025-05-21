from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/problem')
def problem():
    return render_template('problem.html')

@app.route('/solution')
def solution():
    return render_template('solution.html')

@app.route('/market')
def market():
    return render_template('market.html')

@app.route('/business')
def business():
    return render_template('business.html')

@app.route('/competition')
def competition():
    return render_template('competition.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/closing')
def closing():
    return render_template('closing.html')

@app.route('/slides/<int:slide_number>')
def slides(slide_number):
    # Map slide numbers to corresponding routes
    slide_routes = {
        1: 'home',
        2: 'problem',
        3: 'solution',
        4: 'market',
        5: 'business',
        6: 'competition',
        7: 'team',
        8: 'closing'
    }
    
    # Default to home if invalid slide number
    route_name = slide_routes.get(slide_number, 'home')
    return redirect(url_for(route_name))

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
