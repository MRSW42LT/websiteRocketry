from flask import Blueprint, render_template, request, jsonify
from flask.helpers import flash
from flask_login import login_required, current_user
from sqlalchemy.sql.functions import user
from flask import session    
from .models import ComentarioHome, ComentarioPropellants, Note, Formulario, User
from . import db
import json
import sqlite3 as sql

views =  Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        comment = request.form.get('comment')
        
        new_comment = ComentarioHome(data_home=comment)
        db.session.add(new_comment)
        db.session.commit()
        
    try:
        con = sql.connect('websiteRocketry/website/database.db')
    except:
        con = sql.connect('website/database.db')
            
    con.row_factory = sql.Row
            
    cur = con.cursor()
    cur.execute('SELECT data_home FROM comentario_home')
            
    rowsHome = cur.fetchall();    
    
    return  render_template('home.html', user=current_user, rowsHome = rowsHome)

@views.route('/about')
def about():
    return  render_template('about.html', user=current_user)

@views.route('/escola', methods=['GET', 'POST'])
@login_required
def escola():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added.', category='success')

    return  render_template('escola.html', user=current_user)

@views.route('escola/formulario', methods=['GET', 'POST'])
def formulario():
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        opiniao = request.form.get('opiniao')
                
        new_opiniao = Formulario(opiniao_data=opiniao, nome=nome, email=email)
        db.session.add(new_opiniao)
        db.session.commit()
        flash('Sua opinião foi enviada com sucesso para nosso banco de dados.', category='success')
    
    try:
        con = sql.connect('websiteRocketry/website/database.db')
    except:
        con = sql.connect('website/database.db')
        
    con.row_factory = sql.Row
        
    cur = con.cursor()
    cur.execute('SELECT opiniao_data FROM formulario')
        
    rows = cur.fetchall();    
    
    return render_template('formulario.html', user=current_user, rows = rows)

@views.route('/propellants', methods=['GET', 'POST'])
def propellants():
    if request.method == 'POST':
        comment = request.form.get('comment')
        
        new_comment = ComentarioPropellants(data_propellants=comment)
        db.session.add(new_comment)
        db.session.commit()
        
    try:
        con = sql.connect('websiteRocketry/website/database.db')
    except:
        con = sql.connect('website/database.db')
            
    con.row_factory = sql.Row
            
    cur = con.cursor()
    cur.execute('SELECT data_propellants FROM comentario_propellants')
            
    rowsPropellants = cur.fetchall();    
        
    return render_template('propellants.html', user=current_user, rowsPropellants=rowsPropellants)

@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note =  Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})

@views.route('escola/pesquisa_bootstrap')
def pesquisa_bootstrap():
    return render_template('pesquisa_bootstrap.html', user=current_user)