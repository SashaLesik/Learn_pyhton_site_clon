from flask import Blueprint, request, render_template

from web_app.database_functions import extract_from_db

blueprint = Blueprint('adverts', __name__)


@blueprint.route('/adverts')
def adverts():
    ads_list = extract_from_db()
    page = request.args.get('page', 1, type=int)
    pagination = ads_list.paginate(page=page, per_page=5)

    return render_template('adverts.html', pagination=pagination)
