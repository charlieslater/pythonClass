def ls(name,cnt=18):
    """print the last cnt attributes of an object"""
    from pprint import pprint
    from inspect import getmembers
    pprint([x[0] for x in getmembers({})[-cnt:]])
