num = ""
sum(list(map(lambda y:y%10+(int(y/10))%10,map(lambda x:int(x)*2,num[-2::-2]))))+sum(list(map(int,num[-1::-2])))%10
