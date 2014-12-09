from django.forms.forms import pretty_name
from django.template.loader import render_to_string


class Group(list):
    template_name = 'django_backend/_group.html'

    def __init__(self, id, name=None, position=0, template_name=None):
        self.id = id
        if name is None:
            name = pretty_name(id)
        self.template_name = template_name or self.template_name
        self.name = name
        self.position = position
        super(Group, self).__init__()

    @property
    def backends(self):
        return list(self)

    def get_context_data(self, context, **kwargs):
        data = {
            'group': self,
        }
        data.update(kwargs)
        return data

    def get_template_name(self):
        return self.template_name

    def render(self, context):
        return render_to_string(
            self.get_template_name(),
            self.get_context_data(context),
            context)
