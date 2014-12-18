
def solution(arg_group):
    n = len(arg_group)
    for u in range(n - 1):
        for v in range(u + 1, n):
            if arg_group[u]["status"] == arg_group[v]["awareness"]:
                return "celebrity is at position: {0}".format(u + 1)
                
            if arg_group[u]["awareness"] == arg_group[v]["status"]:
                return "celebrity is at position: {0}".format(v + 1)
                
    return "no celebrity"
                
                
if __name__ == "__main__":
    group_list = [{"status" : "regular", "awareness" : "nobody"},{"status" : "regular", "awareness" : "nobody"},{"status" : "regular", "awareness" : "nobody"},{"status" : "regular", "awareness" : "nobody"},{"status" : "regular", "awareness" : "nobody"},{"status" : "regular", "awareness" : "celebrity"},{"status" : "regular", "awareness" : "nobody"},{"status" : "celebrity", "awareness" : "nobody"}]
    
    print solution(group_list)
    print range(0, 10)