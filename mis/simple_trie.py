def make_trie(*args):
    
    trie = {}
    for word in args:
        if type(word) != str:
            raise TypeError("Trie only words on str!")
        temp_trie = trie
            
        for letter in word:
            temp_trie = temp_trie.setdefault(letter, {})
        temp_trie = temp_trie.setdefault('__end__', '__end__')
    return trie
    
def in_trie(trie, word):
    if type(word) != str:
        raise TypeError("Trie only works on str!")
        
    temp_trie = trie
    for letter in word:
        if letter not in temp_trie:
            return False
        temp_trie = temp_trie[letter]
    return True
    
def remove_from_trie(trie, word, depth):
    if word and word[depth] not in trie:
        return False
        
    if len(word) == depth + 1:
        del trie[word[depth]]
        if not trie:
            return True
        return False
    else:
        temp_trie = trie
        
        if remove_from_trie(temp_trie[word[depth]], word, depth + 1):
            if temp_trie:
                del temp_trie[word[depth]]
            return not temp_trie
    return False
    
if __name__ == "__main__":
    trie = make_trie('alan', 'hello', 'ask', 'thanks', 'tire', 'not')
    # print trie
    
    print in_trie(trie, 'thanks')
    print in_trie(trie, 1)