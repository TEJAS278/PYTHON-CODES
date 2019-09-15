from chatbot import Chat,reflections,multiFunctionCall
import wikipedia

def whoIs(query,sessionID="general"):
    try:
        return wikipedia.summary(query)
    except:
        for newquery in wikipedia.search(query):
            try:
                return wikipedia.summary(newquery)
            except:
                pass
    return "I don't know about "+query

call = multiFunctionCall({"whoIs":whoIs})
firstQuestion="Hi, how are you?"
Chat("examples/Example.template", reflections,call=call).converse(firstQuestion)
##{ variable : value }
##{! variable : value }
##{ variable }
##{% if condition %}
##    do this first
##{% elif condition %}
##    do this next
##{% else %}
##    do otherwise
##{% endif %}
##{% topic TopicName %}
##{% group topicName %}
##  {% block %}
##      {% client %}client says {% endclient %}
##      {% response %}response text{% endresponse %}
##  {% endblock %}
##  ...
##{% endgroup %}
##{% learn %}
##  {% group topicName %}
##    {% block %}
##        {% client %}client says {% endclient %}
##        {% response %}response text{% endresponse %}
##    {% endblock %}
##    ...
##  {% endgroup %}
##  ...
##{% endlearn %}
##{% up string %}
##{% low string %}
##{% cap string %}
##{% block %}
##    {% client %}client's statement pattern{% endclient %}
##    {% prev %}previous bot's statement pattern{% endprev %}
##    {% response %}response string{% endresponse %}
##{% endblock %}
