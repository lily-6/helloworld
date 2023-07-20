ver = "0.2"

class Member:
    def __init__(self, name, words=""):
        self.name = name
        self.words = words
    
    def name(self):
        return self.name

print("メンバーリスト・アプリ  Ver. "+ver)
print("--------------------------------")

# メンバー追加
mlist = []
newmember = Member("江頭2:50", "エガちゃんです！")
mlist.append(newmember)

### 以下に自分を追加する ###

newmember = Member("山口 凜々子", "こんにちは")
mlist.append(newmember)

newmember = Member("房州優樹", "よろしくです！")
mlist.append(newmember)

### 以下に自分を追加する ###
newmember = Member("吉田 羅生", "よろしくです！")
mlist.append(newmember)

### 以下に自分を追加する ###
newmember = Member("渡邉　雄太", "よろしく！")
mlist.append(newmember)


# メンバー表示
print("各メンバーから一言")
print()
for member in mlist:
    print(member.name + " ..... " + member.words)
