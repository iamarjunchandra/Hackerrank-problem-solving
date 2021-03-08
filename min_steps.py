"""write a function that finds the minimum steps required to equalise atleast 
the threshold number of equal values in a array. """

def minimum_divisible_steps(arr,threshold,k):
    dict_={x:arr.count(x) for x in set(arr)}
    steps={x:0 for x in dict_.keys()}
    while max(dict_.values())<threshold:
        for item in list(map(lambda x:x//k,arr)):
            try:
                if dict_[item]<threshold:
                    dict_[item]+=1
                    steps[item]+=1
            except:
                dict_[item]=1
                steps[item]=1
    return min([steps[x] for x in dict_.keys() if dict_[x]>=threshold])