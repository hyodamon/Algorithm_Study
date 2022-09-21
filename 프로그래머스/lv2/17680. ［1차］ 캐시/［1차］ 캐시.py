def solution(cacheSize, cities):
    answer = 0
    
    LRU = [0] * cacheSize
    if cacheSize == 0 :
        return(len(cities) * 5)
    
    
    for i, city in enumerate(cities) :
        _city = city.lower()
        if _city in LRU :
            for i in range(LRU.index(_city), 0, -1) :
                LRU[i] = LRU[i - 1]
            answer += 1
        else :
            answer += 5
            for i in range(cacheSize - 1, 0, -1) :
                LRU[i] = LRU[i - 1]
        LRU[0] = _city
        
    
    return answer