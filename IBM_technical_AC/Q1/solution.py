N = int(input())
available_item = input().split()
M = int(input())
request_item = input().split()
classical_size = ['S', 'M', 'L']
fulfilled_flag = True

def check_fulfilled(request, available) -> bool:
    if request == available:
        return True
    
    r_list = list(request)
    a_list = list(available)
    if 'S' in r_list:
        if 'S' in a_list:
            if len(r_list) > len(a_list):
                return True
            else:
                return False
        else:
            return True
    
    if request == 'M':
        if 'L' in a_list or available == 'M':
            return True
        else:
            return False
    
    if 'L' in r_list:
        if 'L' in a_list:
            if len(r_list) < len(a_list):
                return True
            else:
                return False
        else:
            return False


for r_i in request_item:
    for a_i in available_item:
        # if fulfilled
        if check_fulfilled(r_i, a_i):
            break
        else:
            fulfilled_flag = False
    if fulfilled_flag is False:
        print('No')
        break

if fulfilled_flag:
    print('Yes')
