
Templates preceeded with two underscores are intended to be baseline templates.
Example: __layout.html
    These will be imported into typical pages by use of:
        {% extends "__layout.html" %}


Templates preceeded with one underscore are intended to be common components.
Example: _table.html
    These will be included into typical pages by use of:
        {% include '_table.html' %}


Templates preceeded with a single dash are intended to be macro templates.
Example: -bootstrap_wtf.html
    These are imported as the top of the file similarly to:
        {% import '-bootstrap_wtf.html' as wtf %}
