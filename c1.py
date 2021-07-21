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
        storage = {}
        for length in range(1,int(len(s)/2)+1):
                valid_strings = {}
                for start in range(0,len(s)-length+1):
                        valid_strings[start] = tuple(s[start:start+length])
                candidates = set(valid_strings.values())
                print(candidates)
                verified_candidates = []
                valid_no_leftovers = {}
                for c in candidates:
                    print(c)
                    pos = len(c)
                    last = tuple(chars[-pos:])
                    if c == last:
                        verified_candidates.append(c)
                for start in range(0,len(verified_candidates)-length+1):
                        valid_no_leftovers[start] = tuple(verified_candidates[start:start+length])
                set_no_leftovers = set(valid_no_leftovers.values())
                if len(set_no_leftovers) != len(valid_no_leftovers):
                        storage = valid_no_leftovers
                else:
                        break
        # if len(storage) > 0:
        #     print(storage)
        # else:
        #     print('hello')
        print(storage)
        first_sol = storage[0]
        return first_sol


print(solution("abcabcabcabc"))