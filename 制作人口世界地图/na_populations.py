import pygal_maps_world.maps

wm = pygal_maps_world.maps.World()
wm.title = 'Populations of Countries in North American'
wm.add('North American', {'ca':34126000, 'us': 309349000, 'mx': 113423000})
wm.render_to_file('na_populations.svg')