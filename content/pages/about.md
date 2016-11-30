Title: About
Date: 2016/11/30 15:30
<dl>
    {% for name, link in SOCIAL %}
        <dd><a href="{{ link }}">{{ name }}</a></dd>
    {% endfor %}
</dl>
