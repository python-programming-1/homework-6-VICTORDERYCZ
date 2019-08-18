import csv
import pprint


def get_video_data():
    """this function reads from a .csv file and converts the data into a list of dictionaries.
     each item in the list is a dictionary of a specific videos and their attributes."""

    vid_data = []
    with open('USvideos.csv', newline='', encoding='utf-8') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in spamreader:
            if len(row) == 16:
                vid_dict = {'video_id': row[0],
                            'trending_date': row[1],
                            'title': row[2],
                            'channel_title': row[3],
                            'category_id': row[4],
                            'publish_times': row[5],
                            'tags': row[6],
                            'views': row[7],
                            'likes': row[8],
                            'dislikes': row[9],
                            'comment_count': row[10],
                            'thumbnail_link': row[11],
                            'comments_disabled': row[12],
                            'ratings_disabled': row[13],
                            'video_error': row[14],
                            'description': row[15]
                            }
                vid_data.append(vid_dict)
    return vid_data[1:]


def print_data(data):
    for entry in data:
        pprint.pprint(entry)

def get_channel_list(vid_data):

    channel_list = []
    for element in vid_data:
        if element['channel_title'] not in channel_list:
            channel_list.append(element['channel_title'])
    return channel_list

def get_channel_info(channel_list):

    n = 0
    channel_info = []
    empty_dict = {'channel_title': None, 'views': 0, 'likes': 0, 'dislikes': 0}
    while n < len(channel_list):
        channel_info.append(empty_dict.copy())
        channel_info[n]['channel_title'] = channel_list[n]
        n += 1
    return channel_info

def fill_in_channel_info(vid_data, channel_info):

    for element in vid_data:
        index = 0
        while index < len(channel_info):
            if channel_list[index] == element['channel_title']:
                channel_info[index]['views'] += int(element['views'])
                channel_info[index]['likes'] += int(element['likes'])
                channel_info[index]['dislikes'] += int(element['dislikes'])
            index += 1
    return channel_info

def get_most_popular_and_least_popular_channel(info):

    most_popular_and_least_popular_channel = {'most_popular_channel': None, 'least_popular_channel': None, 'most_pop_num_views': None,
                                              'least_pop_num_views': None}
    
    index = 1
    most_popular_and_least_popular_channel['most_popular_channel'] = info[0]['channel_title']
    most_popular_and_least_popular_channel['most_pop_num_views'] = int(info[0]['views'])
    while index < len(info):
        if int(info[index]['views']) > most_popular_and_least_popular_channel['most_pop_num_views']:
            most_popular_and_least_popular_channel['most_popular_channel'] = info[index]['channel_title']
            most_popular_and_least_popular_channel['most_pop_num_views'] = int(info[index]['views'])
        index += 1

    index = 1
    most_popular_and_least_popular_channel['least_popular_channel'] = info[0]['channel_title']
    most_popular_and_least_popular_channel['least_pop_num_views'] = int(info[0]['views'])
    while index < len(info):
        if int(info[index]['views']) < most_popular_and_least_popular_channel['least_pop_num_views']:
            most_popular_and_least_popular_channel['least_popular_channel'] = info[index]['channel_title']
            most_popular_and_least_popular_channel['least_pop_num_views'] = int(info[index]['views'])
        index += 1  
    return most_popular_and_least_popular_channel

def get_most_liked_and_disliked_channel(info):

    most_liked_and_disliked_channel = {'most_liked_channel': None, 'num_likes': None, 'most_disliked_channel': None, 'num_dislikes': None}

    index = 1
    most_liked_and_disliked_channel['most_liked_channel'] = info[0]['channel_title']
    most_liked_and_disliked_channel['num_likes'] = int(info[0]['likes'])
    while index < len(info):
        if int(info[index]['likes']) > most_liked_and_disliked_channel['num_likes']:
            most_liked_and_disliked_channel['most_liked_channel'] = info[index]['channel_title']
            most_liked_and_disliked_channel['num_likes'] = int(info[index]['likes'])
        index += 1
    index = 1
    most_liked_and_disliked_channel['most_disliked_channel'] = info[0]['channel_title']
    most_liked_and_disliked_channel['num_dislikes'] = int(info[0]['dislikes'])
    while index < len(info):
        if int(info[index]['dislikes']) > most_liked_and_disliked_channel['num_dislikes']:
            most_liked_and_disliked_channel['most_disliked_channel'] = info[index]['channel_title']
            most_liked_and_disliked_channel['num_dislikes'] = int(info[index]['dislikes'])
        index += 1
    return most_liked_and_disliked_channel


if __name__ == '__main__':
    vid_data = get_video_data()
    
    # uncomment the line below to see what the data looks like
    #print_data(vid_data)
    channel_list = get_channel_list(vid_data)
    channel_info = get_channel_info(channel_list)
    channel_info = fill_in_channel_info(vid_data, channel_info)
    popularity_metrics = get_most_popular_and_least_popular_channel(channel_info)
    like_dislike_metrics = get_most_liked_and_disliked_channel(channel_info)

    print('Popularity Metrics: {}'.format(popularity_metrics))
    print('Like Dislike Metrics: {}'.format(like_dislike_metrics))
