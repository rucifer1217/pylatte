'''
Created on 2012. 8. 4.

@author: HwanSeung Lee(rucifer1217@gmail.com)
'''
from distutils.core import setup, Extension

setup(name='Pylatte',
      author='Hwanseung Lee, Sangkeun Park',
      author_email='pylatte@pylatte.org',
      url='http://pylatte.org',
      version='1.0',
      description='Web Framework - Insert Python code in HTML(called PYL)',
      classifiers=['Development Status :: 4 - Beta',
                'Intended Audience :: Developers',
                'License :: OSI Approved :: MIT License',
                'Operating System :: OS Independent',
                'Programming Language :: Python :: 3.2',
                'Topic :: Internet :: WWW/HTTP :: WSGI'],
      license='MIT License',
      keywords='Web Framework',
      packages=['pylatte','pylatte.database','pylatte.web','pylatte.web.middleware'],
      install_requires=['ply','mysql-connector-python','pymongo3'],
      homepage='http://pylatte.org',
      download_url='https://github.com/rucifer1217/pylatte',
      long_description="""
      .. image:: http://pylatte.org/image/pylatte.png
        
        =======
        Pylatte 
        =======
        Pylatte : A Web Framework Based on Python 3 Pylatte is a web framework created specifically for Python 3. Developers can now generate websites with Pylatte in Python 3, just as they might for Python 2x-based frameworks such as Django, Flask, or Bottle.
        
        Visit to http://www.pylatte.org/
        
        mail : pylatte@pylatte.org
        
        Facebook Page : https://www.facebook.com/pylatte
        
        Sample code
        -----------
        The following code is a example pyl file.
        
        ::
        
         <p>Pylatte</p>
         {$
         pyl = "HTML" + " + " + "python"
         $}
         <p>
         {$=pyl$}
         </p>
        
        The pyl code is translated by Pylatte to HTML in the browser.
        ::
        
         <p>Pylatte</p>
         <p>
         HTML + python
         </p>
        
        Functions
        ---------
        Translation Engine Pylatte uses pyl file format. pyl consists of HTML and Python. pyl is fully translated by the Pylatte engine into HTML. It is unique feature of Pylatte.
        
        Database
        --------
        To use the database, external library must be installed: the MySQLdb(for mysql) module or pymongo3(for MonogoDB) module for Python 3.
        
        Simple and advanced SQL via specific functions that are similar to iBATIS are provided.
        
        Session
        -------
        A session is needed to distinguish each client.
        
        Filter
        ------
        If a filter is set, select pages pass through the filter.
        
        Form File
        ---------
        It is possible to upload a file to server via POST.
        
        URL Mapping
        -----------
        For security purposes, URL mapping transfers virtual URLs accessed by clients to web pages.
        """
)

