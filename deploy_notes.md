# AirBnB clone - Deploy static

(Quoted)Ever since you completed project 0x0F. Load balancer of the SysAdmin track, you’ve had 2 web servers + 1 load balancer but nothing to distribute with them.

It’s time to make your work public!

In this first deployment project, you will be deploying your web_static work. You will use Fabric (for Python3). Fabric is a Python library and command-line tool for streamlining the use of SSH for application deployment or systems administration tasks. It provides a basic suite of operations for executing local or remote shell commands (normally or via sudo) and uploading/downloading files, as well as auxiliary functionality such as prompting the running user for input, or aborting execution. This concept is important: execute commands locally or remotely. Locally means in your laptop (physical laptop or inside your Vagrant), and Remotely means on your server(s). Fabric is taking care of all network connections (SSH, SCP etc.), it’s an easy tool for transferring, executing, etc. commands from locale to a remote server.

![someimage](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/288/aribnb_diagram_0.jpg?cache=off)

## What is Fabric?

Fabric is a Python library and command-line tool for streamlining the use of SSH
for application deployment or systems administration tasks. 

Typical usage involves creating a Python module containing one or more functions,
then executing them via the fab command-line tool.

Albeit being Python-based, it does not mean that it is used strictly for working with other Python applications or tools. In fact, Fabric is there for you to achieve just about anything regardless of a specific language or a system. As long as the very basic requirements are met, you can take advantage of this excellent library.

Fabric scripts are basic Python files. They are run using the fab tool that is shipped with with Fabric. All this does is include (i.e. ```import``` ..) your script (i.e. instructions to perform) and execute the provided procedure.

Say “Hello Fab!” using Fabric (fabfile.py):

```python
# def hello(who="world"):
#    print "Hello {who}!".format(who=who)
    
$ fab hello:who=Fab
Hello Fab!
```



## How to deploy code to a server easily

The [**Flask website**](https://flask.palletsprojects.com/en/2.0.x/patterns/fabric/) explains this really nicely and simply.

## What is a tgz archive

A TGZ file is a compressed archive created using GZIP, an open-source data compression program.

## How to execute Fabric command locally

ON THE SERVER, we use ```local``` (```fabric.operations.local```):

a single Fabric script (fabfile) can be used to perform actions both on the local machine and remote system(s). For this purpose, Fabric provides the ```local``` operative to run commands locally.

Unlike ```run``` or ```sudo```, however, interacting with the output of ```local``` the same way is not possible. Either output can be captured or printed – the switch can be set with ```capture``` argument.

Local helpers such as the ```lcd``` context manager (which is used for setting the local working directory) are honoured with ```local```, the same way ```run``` (or ```sudo```) honours the ```cd``` context manager.

Usage examples:

```python
# Create a source distribution tar archive (for a Python App.)
local("python setup.py sdist --formats=gztar", capture=False)

# Extract the contents of a tar archive
local("tar xzvf /tmp/trunk/app.tar.gz")

# Remove a file
local("rm /tmp/trunk/app.tar.gz")
```

## How to execute Fabric command remotely

```run``` (```fabric.operations.run```):

Fabric’s ```run``` procedure is used for executing a shell command on one or more remote hosts.

The output results of ```run``` can be captured using a variable.

If command succeeded or failed can be checked using ```.failed``` and ```.succeeded```.

Usage examples:

```python
# Create a directory (i.e. folder)
run("mkdir /tmp/trunk/")

# Uptime
run("uptime")

# Hostname
run("hostname")

# Capture the output of "ls" command
result = run("ls -l /var/www")

# Check if command failed
result.failed
```

```sudo``` (```fabric.operations.sudo```):

Along with ```run```, the most widely used Fabric command is probably ```sudo```. It allows the execution of a given set of commands and arguments with ```sudo``` (i.e. superuser) privileges on the remote host.

If ```sudo``` command is used with an explicitly specified user, the execution will happen not as root but another (i.e. UID 1010).

Usage examples:

```python
# Create a directory
sudo("mkdir /var/www")

# Create a directory as another user
sudo("mkdir /var/www/web-app-one", user="web-admin")

# Return the output
result = sudo("ls -l /var/www")
```

## How to transfer files with Fabric

**Local To Remote:**

```put``` (```fabric.operations.put```)

When you need to upload files, ```put``` command can be used. You can again access to the results of command’s execution with ```.failed``` or ```.succeeded```.

* ```local_path``` - set the local path.

* ```remote_path``` - set the remote path.

* ```use_sudo``` - upload the file to anywhere on the remote machine using a nifty trick: upload to a temporary location then move.

* ```mode``` - set the file mode (flags).

* ```mirror_local``` - set the file flags (i.e. make executable) automatically by reading the local file’s mode.

Usage examples:

```python

# Upload a tar archive of an application
put("/local/path/to/app.tar.gz", "/tmp/trunk/app.tar.gz")

# Use the context manager `cd` instead of "remote_path" arg.
# This will upload app.tar.gz to /tmp/trunk/
with cd("/tmp"):
    put("local/path/to/app.tar.gz", "trunk")

# Upload a file and set the exact mode desired
upload = put("requirements.txt", "requirements.txt", mode=664)

# Verify the upload
upload.succeeded
```

## How to manage Nginx configuration

[There's this really nice and informative tutorial](https://nginx.org/en/docs/beginners_guide.html)

## What is the difference between root and alias in a Nginx configuration

```root``` specifies the **actual document root, the directory on the filesystem to serve static files from**, which corresponds to the URL path ```/```. For instance, if you have root ```/var/www/html/public``` and ask for a URL ```/css/myapp.css``` then this will map to the file path ```/var/www/html/public/css/myapp.css```.
*More like... appending the latter to the former*

```alias``` allows you to **remap some URL path below the root to some other directory so that you can serve static files from elsewhere.** For example, for a ```location /static/``` you might define ```alias /var/www/html/files/```. In this case, instead of going to a subdirectory of the root, the alias will be substituted for the part of the URL path in the location. So ```/static/``` becomes ```/var/www/html/files/``` and a request for ```/static/myapp.css``` will try to load the file ```/var/www/html/files/myapp.css``` instead of ```/var/www/html/public/css/myapp.css```.

**It doesn't make sense to use ```alias``` with ```location /```.**
