import pygal
wm = pygal.maps.world.World()
wm.title = ' North, Central, and South America'
wm.add('North America', ['ca', 'mx', 'us'])
wm.add('Central America', ['bz','cr','gt','hn'])
wm.add('South America', ['ar','bo','cl'])
wm.render_to_file('americas.svg')