import urllib
from bs4 import BeautifulSoup
usernames = open('usernames.txt').readlines()
a=0
n = len(usernames)
followersort = []
followingsort = []
resualt = open('Resualt.txt','w')
print('Total Usernames Are '+str(n))
print('__________')
resualt.write('Total Usernames Are '+str(n)+'\n')
resualt.write('__________'+'\n')
while a<=n-1:
    if a==n-1:
        user = usernames[a]
    else:
        user = usernames[a][:-1]
    data = urllib.urlopen('https://instagram.com/'+user)
    bs = BeautifulSoup(data,'html.parser')
    all = bs.find('meta',property='og:description')
    parts = str(all)[15:-29].split(' ')
    if all != None:
        follower = str(parts[1])[:-1]
        following = str(parts[3])[:-1]
        if parts[0].find('k') != -1:
            fcount = parts[0].replace('k', '00')
            fcount = fcount.replace('.', '')
        else:
            fcount = parts[0]
        if parts[2].find(',') != -1:
            f2count = parts[2].replace(',', '')
        else:
            f2count = parts[2]
        followercount = follower+' = '+fcount
        followingcount = following+' = '+f2count
        followersort.append(fcount)
        followingsort.append(f2count)
        print(a + 1)
        print('Username = ' + user)
        print(followercount)
        print(followingcount)
        print('__________')
        resualt.write(str(a + 1) + '\n')
        resualt.write('Username = ' + user + '\n')
        resualt.write(followercount + '\n')
        resualt.write(followingcount + '\n')
        resualt.write('__________' + '\n')
        a += 1
    else:
        print(a + 1)
        print('Username Is Wrong!')
        print('__________')
        resualt.write(str(a + 1) + '\n')
        resualt.write('Username Is Wrong!' + '\n')
        resualt.write('__________' + '\n')
        a += 1
else:
    followersort = [int(i) for i in followersort]
    followersort.sort(reverse=True)
    counter = 1
    for item in followersort:
        print(str(counter) + ":" + '%s' % item)
        resualt.write(str(counter) + ":" + '%s\n' % item)
        counter+=1
    print('Job Is Finished!!')
    resualt.write('Job Is Finished!!' + '\n')
    resualt.close()
    x = ' '
    while x != 10:
        x = input('Enter 10 To Close! : ')
    else:
        quit()
