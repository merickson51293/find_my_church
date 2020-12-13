def isloggedinuser(session):
    user_id=session.get("user_id", "invalid")
    if user_id=="invalid":
        return False
    return True


def isloggedinchurch(session):
    church_id=session.get("church_id", "invalid")
    if church_id=="invalid":
        return False
    return True
