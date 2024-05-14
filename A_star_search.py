treee = {'S': [['A',1],['B',5]],
         'A':[['S',1],['D',3],['E',7],['G',9],
         'C':[['S',8],['G',5]],
         'D':[['A',3]],
         'E':[['A',7]]}

heuristic = {'S': 8,'A':8,'B':4,'C':3,'D':5000,'G':0}
cost = {'S':0}


def AStarSearch():


if__name__=='__main__':
visited_nodes , optimal_nodes = AStarSearch()
print("visited nodes :"+str(visted_nodes))
print('optimal nodes sequence :'+str(optimal_nodes))
