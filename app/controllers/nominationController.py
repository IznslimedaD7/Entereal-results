from flask import render_template, redirect, url_for, request
from app.repositories.nominationrepository import NominationRepository
from app.blueprints.nomination.form import NominationForm
from app.models.LikeToNomination import LikeToNomination
from flask_login import current_user


class NominationController():
    def nominations():
        if current_user.is_anonymous:
            return redirect(url_for('main.main'))

        nominations = NominationRepository.get_all_nominations()
        nominations_with_likes = []
        for nomination in nominations:
            likes = LikeToNomination.query.filter_by(nomination_id=nomination.id).count()
            users = LikeToNomination.query.filter_by(nomination_id=nomination.id, user_id=current_user.id).first()
            nominations_with_likes.append((nomination, likes, users))
        return render_template('nomination/index.html.jinja', nominations = nominations_with_likes)
    
    def create():
        if current_user.is_anonymous:
            return redirect(url_for('main.main'))
        form = NominationForm('nominations')
        return render_template('nomination/create.html.jinja', form = form)
    
    def store():
        title = request.form.get('title')
        description = request.form.get('description')
        user_id = current_user.id 
        NominationRepository.create_nomination(title=title, description=description, user_id=user_id)
        return redirect(url_for('nomination.index'))
    
    def add_like(id):
        NominationRepository.add_like(id, current_user.id)
        return redirect(url_for('nomination.index'))
    
    def remove_like(id):
        print(6666666)
        NominationRepository.remove_like(id, current_user.id)
        return redirect(url_for('nomination.index'))