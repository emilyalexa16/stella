from flask import Blueprint, current_app, flash, request, redirect, url_for, render_template, session
from werkzeug.utils import secure_filename

bp = Blueprint("main", __name__)

@bp.route("/", methods=["GET", "POST"])
def index():
        if request.method == 'POST':
            # if form did not include a file input named 'file', browser may submit an empty part without filename
            if 'file' not in request.files:
                flash('No selected file')
                return redirect(request.url)
            
            file = request.files['file']

            # if user opened the finder but did not select a file
            if file.filename == '':
                flash('No selected file')
                return redirect(request.url)
            
            if file:
                secure_filename(file.filename)
                path = current_app.config['UPLOAD_DEST']
                file.save(path)
                session['uploaded_file'] = path
                return redirect(url_for('categories.verify_session'))
            
        return render_template('index.html')