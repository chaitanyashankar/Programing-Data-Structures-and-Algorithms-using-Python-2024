#You have to write a Python program that reads information about all the matches and compile the following statistics for each player:
#Number of best-of-5 set matches won
#Number of best-of-3 set matches won
#Number of sets won
#Number of games won
#Number of sets lost
#Number of games lost
#You should print out to the screen (standard output) a summary in decreasing order of ranking, where the ranking is according to the criteria 1-6 in that order (compare item 1, if equal compare item 2, if equal compare item 3 etc, noting that for items 5 and 6 the comparison is reversed).


DictionaryStats = dict()
Line_Input= input()
while (Line_Input!="EOF"):
      (winner_set,loser_set,win_games,lose_games) = (0,0,0,0)

      (winner,loser,setscores) = Line_Input.strip().split(':',2)

      sets = setscores.split(',')
      for set in sets:
      
          (winstr,losestr) = set.split('-')
          win = int(winstr)
          lose = int(losestr)
          win_games = win_games +win
          lose_games = lose_games+ lose
          if win > lose:
              winner_set = winner_set+1
          else:
              loser_set=loser_set+1
      for player in [winner,loser]:
          try:
              DictionaryStats[player]
          except KeyError:
              DictionaryStats[player]=[0,0,0,0,0,0]
      if winner_set >=3:
          DictionaryStats[winner][0]=DictionaryStats[winner][0]+1
      else:
          DictionaryStats[winner][1]=DictionaryStats[winner][1]+1
      DictionaryStats[winner][2]=DictionaryStats[winner][2]+ winner_set
      DictionaryStats[winner][3]=DictionaryStats[winner][3]+win_games
      DictionaryStats[winner][4]=DictionaryStats[winner][4]-loser_set
      DictionaryStats[winner][5]=DictionaryStats[winner][5] - lose_games
      DictionaryStats[loser][2] = DictionaryStats[loser][2] + loser_set
      DictionaryStats[loser][3] = DictionaryStats[loser][3] + lose_games
      DictionaryStats[loser][4] = DictionaryStats[loser][4]  - winner_set
      DictionaryStats[loser][5] = DictionaryStats[loser][5]  - win_games
      Line_Input = input()
statlist = [(stat[0],stat[1],stat[2],stat[3],stat[4],stat[5],name) for name in
DictionaryStats.keys() for stat in [DictionaryStats[name]]]

statlist.sort(reverse = True)

for entr in statlist:
      print(entr[6],entr[0],entr[1],entr[2],entr[3],-entr[4],-entr[5])
    
    
       
                
