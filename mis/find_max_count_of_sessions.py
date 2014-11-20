import datetime
def solution(arg_log_list):
    sessions_list = [] # sessions list
    sessions_count = {} # store the amount of sessions of certain user
    
    for elem in arg_log_list:
        if elem['user'] not in sessions_count:
            sessions_count[elem['user']] = 1
            temp_session = {'user' : elem['user'], 'last_time' : elem['time'],'count' : 1, 'session_index' : sessions_count[elem['user']] }
            sessions_list.append(temp_session)
        else:
            for session in sessions_list:
                if session['user'] is elem['user'] and session['session_index'] is sessions_count[elem['user']]:
                    time_diff = (elem['time'] - session['last_time']).total_seconds()
                    # if the difference of time is bigger than one hour, then create a session log
                    if time_diff > 3600:
                        sessions_count[elem['user']] += 1
                        temp_session = {'user' : elem['user'], 'last_time' : elem['time'],'count' : 1, 'session_index' : sessions_count[elem['user']] }
                        sessions_list.append(temp_session)
                    # increment the count of the existing session
                    else:
                        session['count'] += 1
                        session['last_time'] = elem['time']
                    break
                        
    return sessions_list
    
def find_max(arg_sessions):
    max_sessions = {}
    for session in arg_sessions:
        if session['user'] not in max_sessions:
            max_sessions[session['user']] = session
        else:
            if session['count'] > max_sessions[session['user']]['count']:
                max_sessions[session['user']] = session
                
    return max_sessions

if __name__ == "__main__":
    log_list = [{'user' : 'user_2', 'time' : datetime.datetime(2010, 1, 21, 2, 31)},
    {'user' : 'user_3', 'time' : datetime.datetime(2010, 1, 21, 2, 33)},
    {'user' : 'user_5', 'time' : datetime.datetime(2010, 1, 21, 2, 34)},
    {'user' : 'user_1', 'time' : datetime.datetime(2010, 1, 21, 2, 46)},
    {'user' : 'user_2', 'time' : datetime.datetime(2010, 1, 21, 2, 48)},
    {'user' : 'user_1', 'time' : datetime.datetime(2010, 1, 21, 2, 51)},
    {'user' : 'user_1', 'time' : datetime.datetime(2010, 1, 21, 2, 52)},
    {'user' : 'user_2', 'time' : datetime.datetime(2010, 1, 21, 2, 54)},
    {'user' : 'user_1', 'time' : datetime.datetime(2010, 1, 21, 2, 58)},
    {'user' : 'user_3', 'time' : datetime.datetime(2010, 1, 21, 3, 1)},
    {'user' : 'user_5', 'time' : datetime.datetime(2010, 1, 21, 3, 11)},
    {'user' : 'user_1', 'time' : datetime.datetime(2010, 1, 21, 3, 21)},
    {'user' : 'user_5', 'time' : datetime.datetime(2010, 1, 21, 3, 31)},
    {'user' : 'user_3', 'time' : datetime.datetime(2010, 1, 21, 3, 33)},
    {'user' : 'user_1', 'time' : datetime.datetime(2010, 1, 21, 3, 37)},
    {'user' : 'user_2', 'time' : datetime.datetime(2010, 1, 21, 3, 42)},
    {'user' : 'user_2', 'time' : datetime.datetime(2010, 1, 21, 4, 11)},
    {'user' : 'user_1', 'time' : datetime.datetime(2010, 1, 21, 4, 21)},
    {'user' : 'user_2', 'time' : datetime.datetime(2010, 1, 21, 4, 51)},
    {'user' : 'user_5', 'time' : datetime.datetime(2010, 1, 21, 5, 21)},
    {'user' : 'user_2', 'time' : datetime.datetime(2010, 1, 21, 5, 31)},
    {'user' : 'user_3', 'time' : datetime.datetime(2010, 1, 21, 6, 33)},
    {'user' : 'user_4', 'time' : datetime.datetime(2010, 1, 21, 6, 37)},
    {'user' : 'user_2', 'time' : datetime.datetime(2010, 1, 21, 8, 42)},
    {'user' : 'user_4', 'time' : datetime.datetime(2010, 1, 21, 8, 47)},
    {'user' : 'user_1', 'time' : datetime.datetime(2010, 1, 21, 8, 49)},
    {'user' : 'user_2', 'time' : datetime.datetime(2010, 1, 21, 9, 5)},
    {'user' : 'user_3', 'time' : datetime.datetime(2010, 1, 21, 9, 10)},
    {'user' : 'user_1', 'time' : datetime.datetime(2010, 1, 21, 9, 35)},
    {'user' : 'user_3', 'time' : datetime.datetime(2010, 1, 21, 11, 1)}]
    
    sessions = solution(log_list)
    max_sessions = find_max(sessions)
    print max_sessions