from flask import render_template, make_response
from flask_restful import Resource
from app.forms import UnbabelForm


class Index(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        form = UnbabelForm()
        return make_response(render_template('index.html', title='Unbabel Coding Challenge', form=form), 200, headers)

    def post(self):
        from app.tasks import add
        add.delay(4, 15)
