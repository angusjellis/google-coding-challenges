import collections

# def solution(s):
#     individ_chars = [x for x in s]
    
def solution(s):
    print(s[-3:])
    chars = [x for x in s]
    largest_tuple = find_largest_tuple(s)
    if largest_tuple != find_largest_tuple(largest_tuple):
        largest_tuple = find_largest_tuple(largest_tuple)
    num_slices = len(chars) / len(largest_tuple)
    return int(num_slices)

        

def find_largest_tuple(s):
        storage = {}
        for length in range(1,int(len(s)/2)+1):
                valid_strings = {}
                for start in range(0,len(s)-length+1):
                        valid_strings[start] = tuple(s[start:start+length])
                candidates = set(valid_strings.values())
                # print(candidates)
                test_cans = [x for x in candidates]
                for c in test_cans:
                    pos = len(c)
                    
                    end = s[-pos:]
                    if c != end:
                        print("uh oh")
                        print(c)
                        print(end)
                    else:
                        print("good")
                        print(c)
                        print(end)
                if len(candidates) != len(valid_strings):
                        storage = valid_strings
                else:
                        break
        first_sol = storage[0]
        return first_sol


print(solution("abcabcabcabcabc"))