#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, cgi, cgitb


def list_files_names(path):

    print "<h3> Liste des fichiers dans le repertoire <strong>"+ path + "</strong> : </h3>"
    print "<ul class='list-group'>"

    # liste tous les fichiers dans le repertoire path
    for el in  os.listdir(path):
        print "<li class='list-group-item'>" + el + "</li>"
    
    if not bool(os.listdir(path)):
        print "<li class='list-group-item danger'><strong>Vous n'avez pas les autoriations</strong></li>"

    print "</ul>"


print "Content-Type: text/html"
print 

# On récupère le formulaire rempli par l'utilisateur
form = cgi.FieldStorage()

# Dans la variable path on stock la valeur de l'input "new_path" entré par l'utilisateur 
# si c'est vide on affiche le path devient /var/www/
path = form.getvalue("new_path") or "/var/www/"

# On appelle les fichiers qui listent le dossier
list_files_names(path)
