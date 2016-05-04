#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, cgi, cgitb


def list_files_names(path):

    print "<h3> Liste des fichiers dans le repertoire "+ path + " : "
    print "<ul>"

    # liste tous les fichiers dans le repertoire path
    for el in  os.listdir(path):
        print "<li>" + el + "</li>"

    print "</ul>"


print "Content-Type: text/html"
print 


print """
<html>
    <head>
    
    </head>

    <body>
"""

# On récupère le formulaire rempli par l'utilisateur
form = cgi.FieldStorage()

# Dans la variable path on stock la valeur de l'input "new_path" entré par l'utilisateur 
# si c'est vide on affiche le path devient /var/www/
path = form.getvalue("new_path") or "/var/www/"

list_files_names(path)

print """
        <form action='app.py' method='POST'>
            <input type='text' name='new_path' />
            <button type='submit'>Chercher...</button>
        </form>
"""
print """
    <body>
</html>

"""
