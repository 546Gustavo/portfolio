from flask import Flask, render_template

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'fus-ro-dah'

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/projetos')
    def projetos():
        return render_template('projetos.html')

    @app.route('/contato')
    def contato():
        return render_template('contato.html')

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
