from flask import render_template

def render(component, props={}):
    template = 'index.html'
    data = {
        'component' : component,
        'props' : props
    }

    return render_template(template, data=data)

class React:
    def __init__(self, app):
        self.app = app

    def render(component, props={}):
        template = 'index.html'

        data = {
            'component' : component,
            'props' : props
        }

        return render_template(template, data=data)

