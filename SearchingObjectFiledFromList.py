class Music():

    def __init__(self,name,type):
        self.name = name
        self.type = type

listMusics = [Music('music1','type1'),Music('music2','type2'),Music('music3','type3'),Music('music4','type1')]
      
for music in listMusics:
  print(music.name)

print('-------------------------------------------------------------')

listType1Music = [music for music in listMusics if music.type=='type1']

for music in listType1Music:
  print(music.name)
