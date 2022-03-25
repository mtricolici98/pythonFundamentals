from database import Session
from models import User, Post


def create_user(username, first_name, last_name, password):
    session = Session()
    new_user = User(
        user_name=username,
        first_name=first_name,
        last_name=last_name
    )
    new_user.set_password(password)
    print(new_user)
    session.add(new_user)
    session.commit()


def list_users():
    session = Session()
    print(session.query(User).count())
    print(session.query(User).all())
    try:
        session.query(User).filter(User.id == 10).one()
    except Exception as ex:
        print(ex)
    # my_user = session.query(User).filter(User.id == 1).one()
    # print(my_user)
    return session.query(User).all()


def login(username, password):
    session = Session()
    try:
        user = session.query(User).filter(User.user_name == username).one()
    except Exception:
        print('No such user')
        return
    if not user.hash_password_text(password) == user.password:
        print('Password is not correct')
        return
    return user


def create_post(title, message, user):
    session = Session()
    post = Post(
        title=title,
        message=message,
        created_by=user
    )
    session.add(post)
    session.commit()


def list_posts_for_user(user_id):
    with Session() as session:
        user = session.query(User).filter(User.id == user_id).one()
        print(user.posts)
        session.rollback()


def exmaple():
    session = Session(autocommit=True)
    print(session.query(Post).filter(Post.title.like('%First%')).all())
    session.query(Post).filter((Post.id.in_([1, 2, 3]) & (Post.created_by_id == 2)
                                )).delete()
    raise Exception()


def test():
    with Session() as session:
        user = session.query(User).filter(User.id == 1).one()
        user.add_post(
            'From object',
            'Created post'
        )
        print(session.dirty)
        print(session.new)
        print(session.deleted)
        session.commit()


def delete_post_by_id(post_id):
    with Session() as session:
        post = session.query(Post).filter(Post.id == post_id).one()
        session.delete(post)
        print(session.deleted)
        session.commit()


def delete_post_by_id_alt(post_id):
    with Session() as session:
        session.query(Post).filter(Post.id == post_id).delete(synchronize_session=False)
        print(session.deleted)


if __name__ == '__main__':
    # create_user('mtricolici', 'Marius', 'Tricolic', 'pass')
    # list_users()
    my_user = login('mtricolic', 'pass')
    user_session = Session.object_session(my_user)
    my_user.add_post('post', 'yep')
    user_session.commit()
    # list_posts_for_user(my_user.id)
    # test()
    # delete_post_by_id(7)
    # exmaple()
