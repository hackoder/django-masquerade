from django import template
from django.core.urlresolvers import reverse

register = template.Library()

@register.tag
def masquerade_link(parser, token):
    return MasqueradeLinkNode()

class MasqueradeLinkNode(template.Node):
    def __init__(self):
        self.request = template.Variable('request')
    
    def render(self, context):
        request = self.request.resolve(context)

        link = '<a href="%s">%s</a>'

        try:
            if request.user.is_masked:
                link = link % (reverse('masquerade.views.unmask'),
                  'Unmask!')
            else:
                link = link % (reverse('masquerade.views.mask'),
                  'Masquerade as user')

        except AttributeError:
            return ''

        return link
        
@register.tag
def masquerade_status(parser, token):
    return MasqueradeStatusNode()

class MasqueradeStatusNode(template.Node):
    def __init__(self):
        self.request = template.Variable('request')
    
    def render(self, context):
        request = self.request.resolve(context)

        status = "You are not currently masquerading as any other user."

        try:
            if request.user.is_masked:
                status = "You are masquerading as %s (%s %s)" % (
                  request.user.username,
                  request.user.first_name,
                  request.user.last_name,
                )

        except AttributeError:
            pass

        return status

