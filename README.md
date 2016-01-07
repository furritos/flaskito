# Flaskito

Flaskito is a simple Python web application that was built using Flask Microframework and structured to run with Jython 2.7.1b2 on any Java web container thru the Modjy WSGI adapter.  This was built as an example to demonstrate and showcase that Flask can be "templated" and "WAR'd" without the usage of Pylons or Django (or django-jython or snakefight). 

Included:

* Jython 2.7.1b2 compiled with Oracle support (OracleDataHandler)
* Flask with supporting libraries in `WEB-INF/lib-python`
* SQLAlchemy with supporting libraries in `WEB-INF/lib/python`

To configure:

* Open up `flaskito.py` and edit the `SQLALCHEMY_DATABASE_URI` to suit your Oracle environment.
* (Optionally) Set `SQLALCHEMY_ECHO` to `True` for SQL statement debugging

To build the WAR file:

    $ ./bin/pack
    
To deploy the WAR file:

* **NOTE:** The assumption is that Tomcat is locally installed
* Oracle `ojdbc6.jar` is required, version `11.2.0.4.0`, but not included
* Copy `dist/flaskito.war` into `$TOMCAT/webapps`
* Open up a web browser and browse to `http://localhost:8080/`

WARNING: There is a good chance you need to adjust the deploy and undeploy scripts to fit your environment.  This has been confirmed to work in Tomcat 7.0.57.
