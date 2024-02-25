import pandas as pd

def getDataframeSize(players):
    return list(players.shape)
    
    


data = {
    'player_id': [1, 2, 3, 4],
    'name': ['Player1', 'Player2', 'Player3', 'Player4'],
    'age': [25, 28, 22, 30],
    'position': ['Forward', 'Midfielder', 'Defender', 'Goalkeeper']
}

players=pd.DataFrame(data)
result_list=getDataframeSize(players)
print(result_list)
