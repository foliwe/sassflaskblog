from flask import render_template, url_for, flash, redirect, abort, request, Blueprint
from flask_login import login_required, current_user

from main_content import db
from main_content.models import  Blog
from main_content.blogs.forms import  AddForm

blogs = Blueprint('blogs', __name__,)


@blogs.route('/create_blog', methods=['GET', 'POST'])
@login_required
def create_blog():
  form = AddForm()

  if form.validate_on_submit():
    user = current_user.id
    newPost = Blog(user_id=user, title=form.title.data, description=form.description.data)
    db.session.add(newPost)
    db.session.commit()
    flash("message Created")
    return redirect(url_for('core.index'))
  return render_template('newblog.html',form=form)


@blogs.route('/<int:blog_id>')
def show_blog(blog_id):
  blog = Blog.query.get_or_404(blog_id)
  return render_template('single_blog.html',blog=blog)


@blogs.route('/<int:blog_id>/update', methods=['GET', 'POST'])
@login_required
def update_blog(blog_id):
  blog = Blog.query.get_or_404(blog_id)
  if blog.author != current_user:
    abort(403)
  form = AddForm()

  if form.validate_on_submit():

    blog.title= form.title.data
    blog.description= form.description.data
    db.session.commit()
    flash("Updates Created")
    return redirect(url_for('blogs.show_blog', blog_id=blog.id))
  elif request.method == 'GET':
    form.title.data = blog.title
    form.description.data = blog.description

  return render_template('newblog.html',form=form)


@blogs.route('/<int:blog_id>/delete', methods=['GET', 'POST'])
@login_required
def delete_blog(blog_id):
  blog = Blog.query.get_or_404(blog_id)
  if blog.author != current_user:
    abort(403)

  db.session.delete(blog)
  db.session.commit()
  flash("Deleted")
  return redirect(url_for('core.index'))