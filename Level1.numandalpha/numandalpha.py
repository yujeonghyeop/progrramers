alpha =["zero","one","two","three","four","five","six","seven","eight","nine"]
a = "one4seveneight"
for i in range(0,10):
    if alpha[i] in a:
        a=a.replace(alpha[i],str(i))
print(int(a))