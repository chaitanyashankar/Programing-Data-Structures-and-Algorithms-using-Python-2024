#Define a Python function orangecap(d) that reads a dictionary d of this form and identifies the player with the highest total score. Your function should return a pair (playername,topscore) where playername is a string, the name of the player with the highest score, and topscore is an integer, the total score of playername.

def orangecap(dict1):
    dict2 = {}
    for k1 in dict1:
        for k2 in dict1[k1]:
            dict2[k2] = dict2.get(k2, 0) + dict1[k1][k2]
    player = max(dict2, key=dict2.get)
    return player, dict2[player]

print (orangecap(adict))

#add and multiply polynomials
def addpoly(p1,p2):
    result=[]
    i1,i2=0,0
    l1,l2=len(p1),len(p2)
    while(i1<l1 and i2<l2):
        if(p1[i1][1]>p2[i2][1]):
            result.append(p1[i1])
            i1+=1
        elif(p1[i1][1]<p2[i2][1]):
            result.append(p2[i2])
            i2+=1
        else:
            if(p1[i1][0]+p2[i2][0]!=0):
                result.append((p1[i1][0]+p2[i2][0],p1[i1][1]))
            i1+=1
            i2+=1
    while(i1<l1):
        result.append(p1[i1])
        i1+=1
    while(i2<l2):
        result.append(p2[i2])
        i2+=1
    return result

def multpoly(p1,p2):
    result_dict=dict()
    for coeff1,exp1 in p1:
        for coeff2,exp2 in p2:
            try:
                result_dict[exp1+exp2] += coeff1*coeff2
            except:
                result_dict[exp1+exp2] = coeff1*coeff2
    return sorted([(coeff,exp) for exp,coeff in result_dict.items() if coeff!=0],key=lambda x: x[1],reverse=True)
