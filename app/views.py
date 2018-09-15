from flask import render_template, make_response, request
from flask_restful import Resource
from app.forms import UnbabelForm


class Index(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        form = UnbabelForm()
        return make_response(render_template('index.html', title='Unbabel Coding Challenge', form=form), 200, headers)

    def post(self):
        input_text = request.form.get('input_field')

        from app.tasks import send_request
        send_request.delay(input_text)
