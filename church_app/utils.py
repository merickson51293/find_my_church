def isloggedinuser(session):
    if session.user_id is None:
        return False
    return True


def isloggedinchurch(session):
    if session.church_id is None:
        return False
    return True
