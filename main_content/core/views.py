from flask import render_template,request,Blueprint
from main_content.models import Blog
core = Blueprint('core', __name__,)


@core.route('/')
def index():
  page = request.args.get('page', 1, type=int)
  blog_posts = Blog.query.order_by(Blog.created_at.desc()).paginate(page=page, per_page=2)
  return render_template('index.html',blog_posts=blog_posts)


@core.route('/info')
def info():
  return render_template('info.html')