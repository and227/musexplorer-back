from django.db import connection
from .models import Group, Album, Track

def get_groups(**params):
    group_uuids = params.get('group_uuids', None)
    genre_uuids = params.get('genre_uuids', None)

    sql_query = "select g.* from groups as g"
    if group_uuids and genre_uuids:
        group_uuids = map(lambda s: "'{}'".format(s), group_uuids)
        genre_uuids = map(lambda s: "'{}'".format(s), genre_uuids)
        sql_query += ' where g.group_uuid in ({}) and g.genre in ({})'. \
        format(','.join(group_uuids), ','.join(genre_uuids))
    elif group_uuids:
        group_uuids = map(lambda s: "'{}'".format(s), group_uuids)
        sql_query += ' where g.group_uuid in ({})'. \
        format(','.join(group_uuids))
    elif genre_uuids:
        genre_uuids = map(lambda s: "'{}'".format(s), genre_uuids)
        sql_query += ' where g.genre in ({})'. \
        format(','.join(genre_uuids))
    sql_query += ';'
    group_list = Group.objects.raw(sql_query)

    return group_list

def get_albums(**params):
    album_uuids = params.get('album_uuids', None)
    genre_uuids = params.get('genre_uuids', None)
    group_uuids = params.get('group_uuids', None)

    sql_query = "select a.* from albums as a"
    if album_uuids and genre_uuids:
        album_uuids = map(lambda s: "'{}'".format(s), album_uuids)
        genre_uuids = map(lambda s: "'{}'".format(s), genre_uuids)
        sql_query += ' where a.album_uuid in ({}) and a.genre in ({})'. \
        format(','.join(album_uuids), ','.join(genre_uuids))
    elif album_uuids:
        album_uuids = map(lambda s: "'{}'".format(s), album_uuids)
        sql_query += ' where a.album_uuid in ({})'. \
        format(','.join(album_uuids))
    elif genre_uuids:
        genre_uuids = map(lambda s: "'{}'".format(s), genre_uuids)
        sql_query += ' where a.genre in ({})'. \
        format(','.join(genre_uuids))
    elif group_uuids:
        group_uuids = map(lambda s: "'{}'".format(s), group_uuids)
        sql_query += ' where a.album_group in ({})'. \
        format(','.join(group_uuids))
    sql_query += ';'
    album_list = Album.objects.raw(sql_query)

    return album_list

def get_tracks(**params):
    tracks_uuids = params.get('tracks_uuids', None)
    albums_uuids = params.get('albums_uuids', None)
    sql_query = "select t.* from tracks as t"
    if tracks_uuids and albums_uuids:
        tracks_uuids = map(lambda s: "'{}'".format(s), tracks_uuids)
        albums_uuids = map(lambda s: "'{}'".format(s), albums_uuids)
        sql_query += ' where t.track_uuid in ({}) and t.album in ({})'. \
        format(','.join(album_uuids), ','.join(tracks_uuids))
    elif tracks_uuids:
        tracks_uuids = map(lambda s: "'{}'".format(s), tracks_uuids)
        sql_query += ' where t.track_uuid in ({})'. \
        format(','.join(tracks_uuids))
    elif albums_uuids:
        albums_uuids = map(lambda s: "'{}'".format(s), albums_uuids)
        sql_query += ' where t.album in ({})'. \
        format(','.join(albums_uuids))
    sql_query += ';'
    track_list = Track.objects.raw(sql_query)

    return track_list