fibionaqui = []
fibionaqui.append(int(input()))
fibionaqui.append(int(input()))
num = int(input())
for i in range (num-2):
    fibionaqui.append(fibionaqui[i]+fibionaqui[i+1])
for i in range(len(fibionaqui)):
    fibionaqui[i] = str(fibionaqui[i])
print(",".join([i for i in fibionaqui]))