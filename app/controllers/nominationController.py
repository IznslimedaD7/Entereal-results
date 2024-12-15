from flask import render_template, redirect, url_for, request
from app.repositories.nominationrepository import NominationRepository
from app.blueprints.nomination.form import NominationForm, NominatForm
from app.repositories.nominantrepository import NominantsRepository
from app.models.LikeToNomination import LikeToNomination
from flask_login import current_user


class NominationController():
    def nominations():
        if current_user.is_anonymous:
            return redirect(url_for('main.main'))

        nominations = NominationRepository.get_all_nominations()
        nominations_with_likes = []
        c = 0
        for nomination in nominations:
            c += 1
            likes = LikeToNomination.query.filter_by(nomination_id=nomination.id).count()
            users = LikeToNomination.query.filter_by(nomination_id=nomination.id, user_id=current_user.id).first()
            nominations_with_likes.append((nomination, likes, users, c))
        return render_template('nomination/index.html.jinja', nominations = nominations_with_likes)
    
    def create():
        if current_user.is_anonymous:
            return redirect(url_for('main.main'))
        form = NominationForm('nominations')
        return render_template('nomination/create.html.jinja', form = form)
    
    def store():
        if current_user.is_anonymous:
            return redirect(url_for('main.main'))
        title = request.form.get('title')
        description = request.form.get('description')
        user_id = current_user.id 
        NominationRepository.create_nomination(title=title, description=description, user_id=user_id)
        return redirect(url_for('nomination.index'))
    
    def add_like(id):
        if current_user.is_anonymous:
            return redirect(url_for('main.main'))
        NominationRepository.add_like(id, current_user.id)
        return redirect(url_for('nomination.index'))
    
    def remove_like(id):
        if current_user.is_anonymous:
            return redirect(url_for('main.main'))
        NominationRepository.remove_like(id, current_user.id)
        return redirect(url_for('nomination.index'))
    
    def nominants(id):
        if current_user.is_anonymous:
            return redirect(url_for('main.main'))
        nominants = []
        nominantion = NominationRepository.nomination_by_id(id)
        c = 0
        for n in NominantsRepository.nominants_by_the_nomination(id):
            c += 1
            nominants.append((n, c))
        form = NominatForm('nominations')
        return render_template('nomination/nominat.html.jinja', nominants=nominants, nominantion=nominantion, form=form)
    
    def create_nominant(id):
        if current_user.is_anonymous:
            return redirect(url_for('main.main'))
        title = request.form.get('title')
        user_id = current_user.id 
        NominantsRepository.nominant_create(nomination_id=id, user_id=user_id, title=title)
        return redirect(url_for('nomination.nominants', id=id))
    
    def edit(id):
        if current_user.is_anonymous:
            return redirect(url_for('main.main'))
        form = NominationForm('nominations')
        return render_template('nomination/edit.html.jinja', form = form, nid = id)
    
    def store_edit(id):
        if current_user.is_anonymous:
            return redirect(url_for('main.main'))
        title = request.form.get('title')
        description = request.form.get('description')
        NominationRepository.edit(title=title, description=description, id=id)
        return redirect(url_for('nomination.index'))