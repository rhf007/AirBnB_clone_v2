# AirBnB clone - Web framework

Alright, things are getting very interesting here B) Okay, seriously. So this is where we start using a framework, Flask, and get into templating.

![diagram](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/cb778ec8a13acecb53ef.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20231227%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231227T140715Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=47ccdd4019e0ceb8ca1a0974aae0402021537c0260cbb08cdeceea6faf33186c)

## What is a Web Framework?

GeeksforGeeks describes ‘web application frameworks’ or ‘web frameworks’ as “a software framework that is designed to support the development of web applications including web services, web resources and web APIs”. In simple words, web frameworks are a piece of software that offers a way to create and run web applications. Thus, you don’t need to code on your own and look for probable miscalculations and faults.

In earlier days of web app development, web frameworks were introduced as a means to end hand-coding of applications where just the developer of a particular app could change it. That was long ago, now we have web-specific languages and the trouble with changing an app’s structure is resolved because of the arrival of a general performance. Now, depending upon your task you may choose one web framework that fulfills all your requirements or converges multiple frameworks.

## How to build a web framework/application with Flask?

A minimal Flask application looks something like this:

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
```

So what did that code do?

First we imported the ```Flask``` class. An instance of this class will be our WSGI(Web Service Gateway Interface) application.

Next we create an instance of this class. The first argument is the name of the application’s module or package. ```__name__``` is a convenient shortcut for this that is appropriate for most cases. This is needed so that Flask knows where to look for resources such as templates and static files.

We then use the ```route()``` decorator to tell Flask *what URL should trigger our function.*

The function returns the message we want to display in the user’s browser. The **default content type is HTML**, so HTML in the string will be rendered by the browser.

Save it as ```hello.py``` or something similar. And please don't be a know-it-all and call your application ```flask.py``` because this would conflict with Flask itself.

To run the application, use the ```flask``` command or ```python -m flask```. You need to tell the Flask where your application is with the ```--app``` option.

```bash
$ flask --app hello run
 * Serving Flask app 'hello'
 * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
```
**Application Discovery Behavior**

As a shortcut, if the file is named ```app.py``` or ```wsgi.py```, you don’t have to use ```--app```.

This launches a very simple *builtin server*, which is good enough for testing but probably not what you want to use in production.

Now head over to ```http://127.0.0.1:5000/```, and you should see your hello world greeting.

If another program is already using port 5000, you’ll see ```OSError: [Errno 98]``` or ```OSError: [WinError 10013]``` when the server tries to start.

**Externally Visible Server**

If you run the server you will notice that the server is **only accessible from your own computer**, not from any other in the network. This is the default because in debugging mode a user of the application can execute arbitrary Python code on your computer.

If you have the debugger disabled or trust the users on your network, you can make the server publicly available simply by adding ```--host=0.0.0.0``` to the command line:

```bash
$ flask run --host=0.0.0.0
```

This tells your operating system to listen on all public IPs.

## What is a route and how to define routes in Flask?

In very simple terms, a route is a path to a destination. Modern web applications use meaningful URLs to help users. Users are more likely to like a page and come back if the page uses a meaningful URL they can remember and use to directly visit a page.

Use the ```route()``` decorator to **bind a function to a URL.**

```python
@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'
```

You can do more! You can make parts of the URL dynamic and attach multiple rules to a function.

## How to handle variables in a route?

You can add variable sections to a URL by marking sections with ```<variable_name>```. Your function then receives the ```<variable_name>``` as a **keyword argument.** *Optionally*, you can use a converter to specify the type of the argument like ```<converter:variable_name>```.

```python
from markupsafe import escape

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'
```

*Converter types:*

<table class="docutils align-default">
<tbody>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">string</span></code></p></td>
<td><p>(default) accepts any text without a slash</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">int</span></code></p></td>
<td><p>accepts positive integers</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">float</span></code></p></td>
<td><p>accepts positive floating point values</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">path</span></code></p></td>
<td><p>like <code class="docutils literal notranslate"><span class="pre">string</span></code> but also accepts slashes</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">uuid</span></code></p></td>
<td><p>accepts UUID strings</p></td>
</tr>
</tbody>
</table>

## What is a template?

Templates can be used to generate any type of text file. For web applications, you’ll primarily be generating HTML pages, but you can also generate markdown, plain text for emails, and anything else.

Templates are especially useful if inheritance is used. Basically template inheritance makes it possible to keep certain elements on each page (like header, navigation and footer).

Generating HTML from within Python is not fun, and actually pretty cumbersome because you have to do the HTML escaping on your own to keep the application secure. Because of that Flask configures the Jinja2 template engine for you automatically.

To render a template you can use the ```render_template()``` method. All you have to do is provide the name of the template and the variables you want to pass to the template engine as **keyword arguments**. Here’s a simple example of how to render a template:

```python
from flask import render_template

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
```

Flask will look for templates in the ```templates``` folder. So if your **application** is a **module**, this **folder is next to that module**, if **it’s a package** it’s actually **inside your package**:

**Case 1: a module:**

```
/application.py
/templates
    /hello.html
```

**Case 2: a package:**

```
/application
    /__init__.py
    /templates
        /hello.html
```

For templates you can use the full power of Jinja2 templates.

Here is an example template:

```
<!doctype html>
<title>Hello from Flask</title>
{% if name %}
  <h1>Hello {{ name }}!</h1>
{% else %}
  <h1>Hello, World!</h1>
{% endif %}
```

Inside templates you also have access to the ```config```, ```request```, ```session``` and ```g``` objects as well as the ```url_for()``` and ```get_flashed_messages()``` functions.

Automatic escaping is enabled, so if ```name``` contains HTML it will be escaped automatically. If you can trust a variable and you know that it will be safe HTML (for example because it came from a module that converts wiki markup to HTML) you can mark it as safe by using the ```Markup``` class or by using the ```|safe``` filter in the template.

Here is a basic introduction to how the ```Markup``` class works:

```python
from markupsafe import Markup

>>> Markup('<strong>Hello %s!</strong>') % '<blink>hacker</blink>'
Markup('<strong>Hello &lt;blink&gt;hacker&lt;/blink&gt;!</strong>')
>>> Markup.escape('<blink>hacker</blink>')
Markup('&lt;blink&gt;hacker&lt;/blink&gt;')
>>> Markup('<em>Marked up</em> &raquo; HTML').striptags()
'Marked up » HTML'
```

But trust me, you are going to love Jinja.

## How to create a HTML response in Flask by using a template?

The return value from a view function is automatically converted into a response object for you. If the return value is a string it’s converted into a response object with the string as response body, a ```200 OK``` status code and a *text/html* mimetype. If the return value is a dict or list, ```jsonify()``` is called to produce a response. The logic that Flask applies to converting return values into response objects is as follows:

**1.** If a response object of the correct type is returned it’s directly returned from the view.

**2.** If it’s a string, a response object is created with that data and the default parameters.

**3.** If it’s an iterator or generator returning strings or bytes, it is treated as a streaming response.

**4.** If it’s a dict or list, a response object is created using ```jsonify()```.

**5.** If a tuple is returned the items in the tuple can provide extra information. Such tuples have to be in the form ```(response, status)```, ```(response, headers)```, or ```(response, status, headers)```. **The status value will override the status code and headers can be a list or dictionary of additional header values.**

**6.** If none of that works, Flask will assume the return value is a valid WSGI application and convert that into a response object.

If you want to get hold of the resulting response object inside the view you can use the ```make_response()``` function.

Imagine you have a view like this:

```python
from flask import render_template

@app.errorhandler(404)
def not_found(error):
    return render_template('error.html'), 404
```

You just need to wrap the return expression with ```make_response()``` and get the response object to modify it, then return it:

```python
from flask import make_response

@app.errorhandler(404)
def not_found(error):
    resp = make_response(render_template('error.html'), 404)
    resp.headers['X-Something'] = 'A value'
    return resp
```

**APIs with JSON**

A common response format when writing an API is JSON. It’s easy to get started writing such an API with Flask. If you return a ```dict``` or ```list``` from a view, it will be converted to a JSON response.

```python
@app.route("/me")
def me_api():
    user = get_current_user()
    return {
        "username": user.username,
        "theme": user.theme,
        "image": url_for("user_image", filename=user.image),
    }

@app.route("/users")
def users_api():
    users = get_all_users()
    return [user.to_json() for user in users]
```

This is a shortcut to passing the data to the ```jsonify()``` function, which will serialize any supported JSON data type. **That means that all the data in the dict or list must be JSON serializable.**

**BUT** for complex types such as database models, you’ll want to use a serialization library to convert the data to valid JSON types first. There are many serialization libraries and Flask API extensions maintained by the community that support more complex applications.

## How to create a dynamic template (loops, conditions…)?

That's exactly where Jinja makes all the difference!

A Jinja template is simply a text file. Jinja can generate any text-based format (HTML, XML, CSV, LaTeX, etc.). A Jinja template doesn’t need to have a specific extension: ```.html```, ```.xml```, or any other extension is just fine.

A template contains **variables** and/or **expressions**, which get replaced with values when a template is *rendered*; and **tags**, which control the logic of the template. The template syntax is heavily inspired by Django and Python.

Below is a minimal template that illustrates a few basics using the default Jinja configuration. We will cover the details later in this document:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>My Webpage</title>
</head>
<body>
    <ul id="navigation">
    {% for item in navigation %}
        <li><a href="{{ item.href }}">{{ item.caption }}</a></li>
    {% endfor %}
    </ul>

    <h1>My Webpage</h1>
    {{ a_variable }}

    {# a comment #}
</body>
</html>
```

The following example shows the default configuration settings. An application developer can change the syntax configuration from ```{% foo %}``` to ```<% foo %>```, or something similar.

There are a few kinds of delimiters. The default Jinja delimiters are configured as follows:

* ```{% ... %}``` for **Statements**

* ```{{ ... }}``` for Expressions to **print** to the template output

* ```{# ... #}``` for **Comments** not included in the template output

* ```#  ... ##``` for Line Statements

**Variables**

Template variables are defined by the context dictionary passed to the template.

You can mess around with the variables in templates provided they are passed in by the application. Variables may have attributes or elements on them you can access too. What attributes a variable has depends heavily on the application providing that variable.

You can use a dot (```.```) to access attributes of a variable in addition to the standard Python ```__getitem__``` “subscript” syntax (```[]```).

The following lines do the same thing:

```
{{ foo.bar }}
{{ foo['bar'] }}
```

It’s important to know that the outer double-curly braces are not part of the variable, but the print statement. If you access variables inside tags don’t put the braces around them.

If a variable or attribute **does not exist**, you will get back an **undefined value.** What you can do with that kind of value depends on the application configuration: the default behavior is to evaluate to an empty string if printed or iterated over, and to fail for every other operation.


***Implementation Note:***


For the sake of convenience, ```foo.bar``` in Jinja2 does the following things on the Python layer:

* check for an **attribute** called bar on foo (```getattr(foo, 'bar')```)

* if there is not, check for an **item** 'bar' in foo (```foo.__getitem__('bar')```)

* if there is not, return an **undefined** object.

```foo['bar']``` works mostly the same with a small difference in sequence:

* check for an **item** 'bar' in foo. (```foo.__getitem__('bar')```)

* if there is not, check for an **attribute** called bar on foo. (```getattr(foo, 'bar')```)

* if there is not, return an **undefined** object.

This is important if an object has an item and attribute with the same name. 

**Comments** and *you better be writing them*

To comment-out part of a line in a template, use the comment syntax which is by default set to ```{# ... #}```. This is useful to comment out parts of the template for debugging or to add information for other template designers or yourself:

```
{# note: commented-out template because we no longer use this
    {% for user in users %}
        ...
    {% endfor %}
#}
```

**Whitespace Control**

In the default configuration:

* a single trailing newline is stripped if present

* other whitespace (spaces, tabs, newlines etc.) is returned unchanged

If an application configures Jinja to *trim_blocks*, the first newline after a template tag is removed automatically (like in PHP). The *lstrip_blocks* option can also be set to strip tabs and spaces from the beginning of a line to the start of a block. (Nothing will be stripped if there are other characters before the start of the block.)

With both *trim_blocks* and *lstrip_blocks* enabled, you can put block tags on their own lines, and the entire block line will be removed when rendered, preserving the whitespace of the contents. For example, **without** the *trim_blocks* and *lstrip_blocks* options, this template:

```html
<div>
    {% if True %}
        yay
    {% endif %}
</div>
```

gets rendered with blank lines inside the div:

```html
<div>

        yay

</div>
```

But **with** both *trim_blocks* and *lstrip_blocks* enabled, the template block lines are removed and other whitespace is preserved:

```html
<div>
        yay
</div>
```

You can manually disable the *lstrip_blocks* behavior by putting a plus sign (```+```) at the start of a block:

```html
<div>
        {%+ if something %}yay{% endif %}
</div>
```

You can also strip whitespace in templates by hand. If you add a minus sign (```-```) to the start or end of a block (e.g. a For tag), a comment, or a variable expression, the whitespaces before or after that block will be removed:

```
{% for item in seq -%}
    {{ item }}
{%- endfor %}
```

This will yield all elements without whitespace between them. If seq was a list of numbers from ```1``` to ```9```, the output would be ```123456789```.

If Line Statements are enabled, they strip leading whitespace automatically up to the beginning of the line.

By default, Jinja2 also removes trailing newlines. To keep single trailing newlines, configure Jinja to *keep_trailing_newline*.

***Note***
You must not add whitespace between the tag and the minus sign.

valid:

```
{%- if foo -%}...{% endif %}
```

invalid:

```
{% - if foo - %}...{% endif %}
```

### Control Structures

*Because they're the real deal*

**For**

Loop over each item in a sequence. For example, to display a list of users provided in a variable called users:

```html
<h1>Members</h1>
<ul>
{% for user in users %}
  <li>{{ user.username|e }}</li>
{% endfor %}
</ul>
```

As variables in templates retain their object properties, it is possible to iterate over containers like ```dict```:

```
<dl>
{% for key, value in my_dict.iteritems() %}
    <dt>{{ key|e }}</dt>
    <dd>{{ value|e }}</dd>
{% endfor %}
</dl>
```
Note, however, that Python dicts are not ordered; so you might want to either pass a sorted ```list``` of ```tuple```s – or a ```collections.OrderedDict``` – to the template, or use the *dictsort* filter.

Inside of a for-loop block, you can access some special variables:

<table class="docutils align-default">
<colgroup>
<col style="width: 31%">
<col style="width: 69%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Variable</p></th>
<th class="head"><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p><cite>loop.index</cite></p></td>
<td><p>The current iteration of the loop. (1 indexed)</p></td>
</tr>
<tr class="row-odd"><td><p><cite>loop.index0</cite></p></td>
<td><p>The current iteration of the loop. (0 indexed)</p></td>
</tr>
<tr class="row-even"><td><p><cite>loop.revindex</cite></p></td>
<td><p>The number of iterations from the end of the loop
(1 indexed)</p></td>
</tr>
<tr class="row-odd"><td><p><cite>loop.revindex0</cite></p></td>
<td><p>The number of iterations from the end of the loop
(0 indexed)</p></td>
</tr>
<tr class="row-even"><td><p><cite>loop.first</cite></p></td>
<td><p>True if first iteration.</p></td>
</tr>
<tr class="row-odd"><td><p><cite>loop.last</cite></p></td>
<td><p>True if last iteration.</p></td>
</tr>
<tr class="row-even"><td><p><cite>loop.length</cite></p></td>
<td><p>The number of items in the sequence.</p></td>
</tr>
<tr class="row-odd"><td><p><cite>loop.cycle</cite></p></td>
<td><p>A helper function to cycle between a list of
sequences.  See the explanation below.</p></td>
</tr>
<tr class="row-even"><td><p><cite>loop.depth</cite></p></td>
<td><p>Indicates how deep in a recursive loop
the rendering currently is.  Starts at level 1</p></td>
</tr>
<tr class="row-odd"><td><p><cite>loop.depth0</cite></p></td>
<td><p>Indicates how deep in a recursive loop
the rendering currently is.  Starts at level 0</p></td>
</tr>
</tbody>
</table>

Within a for-loop, it’s possible to cycle among a list of strings/variables each time through the loop by using the special ```loop.cycle``` helper:

```html
{% for row in rows %}
    <li class="{{ loop.cycle('odd', 'even') }}">{{ row }}</li>
{% endfor %}
```

Unlike in Python, it’s not possible to **break** or **continue** in a loop. You can, however, filter the sequence during iteration, which allows you to skip items. The following example skips all the users which are hidden:

```
{% for user in users if not user.hidden %}
    <li>{{ user.username|e }}</li>
{% endfor %}
```

The advantage is that the special loop variable will count correctly; thus not counting the users not iterated over.

If no iteration took place because the sequence was empty or the filtering removed all the items from the sequence, you can render a default block by using else:

```html
<ul>
{% for user in users %}
    <li>{{ user.username|e }}</li>
{% else %}
    <li><em>no users found</em></li>
{% endfor %}
</ul>
```

Note that, in Python, else blocks are executed whenever the corresponding loop did not break. Since Jinja loops cannot break anyway, a slightly different behavior of the else keyword was chosen.

It is also possible to use loops recursively. This is useful if you are dealing with recursive data such as sitemaps or RDFa. To use loops recursively, you basically have to add the recursive modifier to the loop definition and call the loop variable with the new iterable where you want to recurse.

The following example implements a sitemap with recursive loops:

```html
<ul class="sitemap">
{%- for item in sitemap recursive %}
    <li><a href="{{ item.href|e }}">{{ item.title }}</a>
    {%- if item.children -%}
        <ul class="submenu">{{ loop(item.children) }}</ul>
    {%- endif %}</li>
{%- endfor %}
</ul>
```

The loop variable always refers to the closest (innermost) loop. If we have more than one level of loops, we can rebind the variable loop by writing ```{% set outer_loop = loop %}``` after the loop that we want to use recursively. Then, we can call it using ```{{ outer_loop(…) }}```

**If**

The if statement in Jinja is comparable with the Python if statement. In the simplest form, you can use it to test if a variable is defined, not empty and not false:

```html
{% if users %}
<ul>
{% for user in users %}
    <li>{{ user.username|e }}</li>
{% endfor %}
</ul>
{% endif %}
```

For multiple branches, elif and else can be used like in Python. You can use more complex Expressions there, too:

```
{% if kenny.sick %}
    Kenny is sick.
{% elif kenny.dead %}
    You killed Kenny!  You bastard!!!
{% else %}
    Kenny looks okay --- so far
{% endif %}
```

If can also be used as an inline expression and for loop filtering.

**Macros**

Macros are comparable with **functions** in regular programming languages. They are useful to put often used idioms into reusable functions to not repeat yourself (“DRY”).

Here’s a small example of a macro that renders a form element:

```
{% macro input(name, value='', type='text', size=20) -%}
    <input type="{{ type }}" name="{{ name }}" value="{{
        value|e }}" size="{{ size }}">
{%- endmacro %}
```

The macro can then be called like a function in the namespace:

```html
<p>{{ input('username') }}</p>
<p>{{ input('password', type='password') }}</p>
```

***If the macro was defined in a different template, you have to import it first.***

Inside macros, you have access to three special variables:

* ***varargs***

    If more positional arguments are passed to the macro than accepted by the macro, they end up in the special varargs variable as a list of values.

* ***kwargs***

    Like varargs but for keyword arguments. All unconsumed keyword arguments are stored in this special variable.

* ***caller***

    If the macro was called from a call tag, the caller is stored in this variable as a callable macro.

Macros also expose some of their internal details. The following attributes are available on a macro object:

* ***name***

    The name of the macro. {{ input.name }} will print input.

* ***arguments***

    A tuple of the names of arguments the macro accepts.

* ***defaults***

    A tuple of default values.

* ***catch_kwargs***

    This is true if the macro accepts extra keyword arguments (i.e.: accesses the special kwargs variable).

* ***catch_varargs***

    This is true if the macro accepts extra positional arguments (i.e.: accesses the special varargs variable).

* ***caller***

    This is true if the macro accesses the special caller variable and may be called from a call tag.

***If a macro name starts with an underscore, it’s not exported and can’t be imported.***

## How to display in HTML data from a MySQL database?

**(retrieve with flask)**

**(display with jinja)**
