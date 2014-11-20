import datetime
def solution(arg_log_list):
    counted_list = []
    sessions_count = {}
    
    for elem in arg_log_list:
        if elem['user'] not in sessions_count:
            sessions_count[elem['user']] = 1
            temp_session = {'user' : elem['user'], 'last_time' : elem['time'],'count' : 1, 'session_index' : sessions_count[elem['user']] }
            counted_list.append(temp_session)
        else:
            for session in counted_list:
                if session['user'] is elem['user'] and session['session_index'] is sessions_count[elem['user']]:
                    time_diff = (elem['time'] - session['last_time']).total_seconds()
                    if time_diff > 3600:
                        sessions_count[elem['user']] += 1
                        temp_session = {'user' : elem['user'], 'last_time' : elem['time'],'count' : 1, 'session_index' : sessions_count[elem['user']] }
                        counted_list.append(temp_session)
                    else:
                        session['count'] += 1
                        session['last_time'] = elem['time']
                        
    return counted_list
    
def find_max(arg_sessions):
    max_session = {}
    for session in arg_sessions:
        if session['user'] not in max_session:
            max_session[session['user']] = session
        else:
            if session['count'] > max_session[session['user']]['count']:
                max_session[session['user']] = session
                
    return max_session

if __name__ == "__main__":
    log_list = [{'user' : 'user_2', 'time' : datetime.datetime(2010, 1, 21, 2, 31)},
    {'user' : 'user_3', 'time' : datetime.datetime(2010, 1, 21, 2, 33)},
    {'user' : 'user_1', 'time' : datetime.datetime(2010, 1, 21, 2, 34)},
    {'user' : 'user_1', 'time' : datetime.datetime(2010, 1, 21, 2, 46)},
    {'user' : 'user_2', 'time' : datetime.datetime(2010, 1, 21, 2, 48)},
    {'user' : 'user_1', 'time' : datetime.datetime(2010, 1, 21, 2, 51)},
    {'user' : 'user_1', 'time' : datetime.datetime(2010, 1, 21, 2, 52)},
    {'user' : 'user_2', 'time' : datetime.datetime(2010, 1, 21, 2, 54)},
    {'user' : 'user_1', 'time' : datetime.datetime(2010, 1, 21, 2, 58)},
    {'user' : 'user_3', 'time' : datetime.datetime(2010, 1, 21, 3, 1)},
    {'user' : 'user_3', 'time' : datetime.datetime(2010, 1, 21, 3, 11)},
    {'user' : 'user_1', 'time' : datetime.datetime(2010, 1, 21, 3, 21)},
    {'user' : 'user_2', 'time' : datetime.datetime(2010, 1, 21, 3, 31)},
    {'user' : 'user_3', 'time' : datetime.datetime(2010, 1, 21, 3, 33)},
    {'user' : 'user_1', 'time' : datetime.datetime(2010, 1, 21, 3, 37)},
    {'user' : 'user_2', 'time' : datetime.datetime(2010, 1, 21, 3, 42)},
    {'user' : 'user_2', 'time' : datetime.datetime(2010, 1, 21, 4, 11)},
    {'user' : 'user_1', 'time' : datetime.datetime(2010, 1, 21, 4, 21)},
    {'user' : 'user_2', 'time' : datetime.datetime(2010, 1, 21, 4, 51)},
    {'user' : 'user_1', 'time' : datetime.datetime(2010, 1, 21, 5, 21)},
    {'user' : 'user_2', 'time' : datetime.datetime(2010, 1, 21, 5, 31)},
    {'user' : 'user_3', 'time' : datetime.datetime(2010, 1, 21, 6, 33)},
    {'user' : 'user_1', 'time' : datetime.datetime(2010, 1, 21, 6, 37)},
    {'user' : 'user_2', 'time' : datetime.datetime(2010, 1, 21, 8, 42)},
    {'user' : 'user_2', 'time' : datetime.datetime(2010, 1, 21, 8, 47)},
    {'user' : 'user_1', 'time' : datetime.datetime(2010, 1, 21, 8, 49)},
    {'user' : 'user_2', 'time' : datetime.datetime(2010, 1, 21, 9, 5)},
    {'user' : 'user_3', 'time' : datetime.datetime(2010, 1, 21, 9, 10)},
    {'user' : 'user_1', 'time' : datetime.datetime(2010, 1, 21, 9, 35)},
    {'user' : 'user_3', 'time' : datetime.datetime(2010, 1, 21, 11, 1)}]
    
    sessions = solution(log_list)
    max_sessions = find_max(sessions)
    print max_sessions