from flask import Flask, render_template, request, session, make_response

app = Flask(__name__)  # '__main__'
app.secret_key = "cristina"


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/developers')
def developers():
    return render_template('developers.html')


@app.route('/clients')
def clients():
    return render_template('clients.html')


@app.route('/developer/project/view')
def developer_project_view():
    return render_template('developer_project_view.html')

@app.route('/client/project/view')
def client_project_view():
    return render_template('client_project_view.html')


@app.route('/contact')
def contact():
    return render_template("contact.html")


#
# @app.before_first_request
# def initialize_database():
#     Database.initialize()
#
#
# @app.route('/auth/login', methods=['POST'])
# def login_user():
#     email = request.form['email']
#     password = request.form['password']
#
#     if User.login_valid(email, password):
#         User.login(email)
#     else:
#         session['email'] = None
#
#     return render_template('profile.html', email=session['email'])
#
#
# @app.route('/auth/register', methods=['POST'])
# def register_user():
#     email = request.form['email']
#     password = request.form['password']
#
#     User.register(email, password)
#     session['email'] = request.form['email']
#     user = User.get_by_email(session['email'])
#
#     blogs = user.get_blogs()
#     return render_template('profile.html', blogs=blogs, email=session['email'])
#
#

#
#
# @app.route('/blogs/<string:user_id>')
# def user_blogs(user_id=None):
#     if user_id is not None:
#         user = User.get_by_id(user_id)
#     else:
#         user = User.get_by_email(session['email'])
#
#     blogs = user.get_blogs()
#
#     return render_template("user_blogs.html", blogs=blogs, email=user.email)
#
#
# @app.route('/posts')
# def all_posts():
#     posts = Post.get_posts()
#
#     return render_template('posts.html', posts=posts)
#
#
# @app.route('/post/<string:post_id>')
# def get_post(post_id):
#     post = Post.get_post(post_id)
#
#     return render_template('developers.html', post=post)
#
#
# @app.route('/posts/<string:blog_id>')
# def blog_posts(blog_id):
#     blog = Blog.from_mongo(blog_id)
#     posts = blog.get_posts()
#
#     return render_template('posts.html', posts=posts, blog_title=blog.title, blog_id=blog._id)
#
#
# @app.route('/blogs/new', methods=['POST', 'GET'])
# def create_new_blog():
#     if request.method == 'GET':
#         return render_template('new_blog.html')
#     else:
#         title = request.form['title']
#         description = request.form['description']
#         user = User.get_by_email(session['email'])
#
#         new_blog = Blog(user.email, title, description, user._id)
#         new_blog.save_to_mongo()
#
#         return make_response(user_blogs(user._id))
#
#
# @app.route('/posts/new/<string:blog_id>', methods=['POST', 'GET'])
# def create_new_post(blog_id):
#     if request.method == 'GET':
#         return render_template('new_post.html', blog_id=blog_id)
#     else:
#         title = request.form['title']
#         content = request.form['content']
#         user = User.get_by_email(session['email'])
#
#         new_post = Post(blog_id, title, content, user.email)
#         new_post.save_to_mongo()
#         blog = Blog.from_mongo(blog_id)
#         send_mail_to_subscribers(blog.title)
#         return blog_posts(blog_id)


if __name__ == '__main__':
    app.run(port=4988, debug=True)