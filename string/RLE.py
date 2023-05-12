def RLE(S):
    """ランレングス圧縮して文字と数の組のリストで返す"""
    s = []
    cnt = 1
    for i in range(len(S)):
        if i+1<len(S):
            if S[i] == S[i+1]:
                cnt += 1
            else:
                s.append([S[i], cnt])
                cnt = 1
        else:
            s.append([S[i], cnt])
    return s