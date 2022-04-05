from lessons.lesson_21.example_project.db.database import Session
from lessons.lesson_21.example_project.models.models import Post, User, Comment


def list_other_posts(user):
    with Session() as session:
        posts = session.query(Post).filter(Post.created_by_id != user.id)
        for post in posts:
            print(post)


def list_my_posts(user):
    with Session() as session:
        user = session.query(User).filter(User.id == user.id).one()
        for post in user.posts:
            print(post)


def add_post(user):
    with Session() as session:
        title = input('Post title')
        message = input('Post message')
        post = Post(
            title=title,
            message=message,
            created_by=user
        )
        session.add(post)
        session.commit()


def add_comment(user):
    list_my_posts(user)
    list_my_posts(user)
    with Session() as session:
        post_id = input('Post ID')
        message = input('Comment message')
        comment = Comment(
            post_id=post_id,
            message=message,
            user_id=user.id
        )
        session.add(comment)
        session.commit()


def list_my_comments(user):
    with Session() as session:
        user = session.query(User).filter(User.id == user.id).one()
        for comment in user.comments:
            print(comment)


def list_post_comments(user):
    list_my_posts(user)
    list_my_posts(user)
    post_id = input('Select Post ID:')
    with Session() as session:
        user = session.query(Comment).filter(Comment.post_id == post_id)
        for comment in user.comments:
            print(comment)


def delete_post(user):
    list_my_posts(user)
    with Session() as session:
        post_id = input('Select post ID to delete')
        try:
            post = session.query(Post).filter((Post.id == post_id) & (User.id == user.id)).one()
            session.delete(post)
            session.commit()
        except Exception as ex:
            print(ex)
