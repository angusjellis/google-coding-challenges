import collections

# def solution(s):
#     individ_chars = [x for x in s]
    
def solution(s):
    chars = [x for x in s]
    largest_tuple = find_largest_tuple(s, chars)
    if largest_tuple != find_largest_tuple(largest_tuple, chars):
        largest_tuple = find_largest_tuple(largest_tuple, chars)
    num_slices = len(chars) / len(largest_tuple)
    return int(num_slices)

        

def find_largest_tuple(s, chars):
        storage = []
        for length in range(1,int(len(s)/2)+1):
                valid_strings = {}
                for start in range(0,len(s)-length+1):
                        valid_strings[start] = tuple(s[start:start+length])
                candidates = set(valid_strings.values())
                verified_candidates = set()
                for c in candidates:
                    pos = len(c)
                    last = tuple(chars[-pos:])
                    if c == last:
                        storage.append(c)
                # if len(candidates) != len(valid_strings):
                #         storage = valid_strings
                # else:
                #         break
        if len(storage) > 0:
            print(storage)
        else:
            print('hello')
        first_sol = storage[0]
        return first_sol


print(solution("abcabcabcabc"))