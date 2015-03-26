# url_ofbuscate
This is a Django application that provides methods to obfuscate/deobfuscate URLs.

## Quick start
Install using pip or easy_install

    $ pip install url-obfuscate

    $ easy_install url-obfuscate

Add "url_obfuscate" to your INSTALLED_APPS setting like this:

    INSTALLED_APPS = (
        ...
        'url_obfuscate',
    )

## Usage
To obfuscate Django's URLs, modify the URL declaration in the urls.py file by replacing the regex definition with the funcion generate_url_pattern, as follows:

    from url_obfuscate.helpers import generate_url_pattern
    ...

    urlpatterns = patterns('views',
        url(generate_url_pattern('/'), 'home', name='home'),
        url(generate_url_pattern('obfuscated_link', params=['(?P<name>[^/]+)']), 'obfuscated_link', name='obfuscated_link'),
    )

For the home URL, use / path. To include params in the URL, declare them in the desired order inside the params attribute. When obfuscating a URL with parameters, it is necessary to use the deobfuscate decorator to recover the original value of the parameter.

    from url_obfuscate.decorators import deobfuscate
    ...

    @deobfuscate
    def obfuscated_link(request, name):
        return render(request, 'obfuscate_result.html', { 'name': name })

When declaring URLs with parameters inside templates, use the obfuscate template tag, as follows:

    {% load obfuscate %}
    ...
    <p><a href="{% url 'obfuscated_link' 'Laura Manzur'|obfuscate %}">Obfuscated link: {% url 'obfuscated_link' 'Laura'|obfuscate %}</a></p>
    ...

If you need to obfuscate any value from inside a view, use the obfuscate function, as follows:

    from url_obfuscate.helpers import obfuscate
    ...

    def home(request):
        links = list()
        for i in range(10):
            links.append(obfuscate('Name %d' % (i+1)))
        return render(request, 'index.html', { 'links': links })
