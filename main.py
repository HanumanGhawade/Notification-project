from pushbullet import Pushbullet

api_keys = 'o.66zcRZLoj1s1KIRQSiZi1VRUSSRJnXRy'
file = 'content.txt'

with open(file, 'r') as f:
    text = f.read()
    print(text)

pb = Pushbullet(api_keys)
push = pb.push_note('Good Morning', text)
