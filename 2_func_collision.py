import pygame,sys

pygame.init()
screen = pygame.display.set_mode((800,800))
clock = pygame.time.Clock()

player_surf = pygame.Surface((50,50))
player_surf.fill('red')
player_rect = player_surf.get_rect(center = (300,300))
player_mask = pygame.mask.from_surface(player_surf)

obstacle_surf = pygame.image.load('alpha.png').convert_alpha()
obstalce_pos = (100,100)
obstacle_mask = pygame.mask.from_surface(obstacle_surf)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	screen.fill('white')

	# obstacle 
	screen.blit(obstacle_surf,obstalce_pos)
	
	# moving part
	if pygame.mouse.get_pos(): 
		player_rect.center = pygame.mouse.get_pos()
	screen.blit(player_surf,player_rect)

	# Collision
	offset_x = obstalce_pos[0] - player_rect.left
	offset_y = obstalce_pos[1] - player_rect.top
	# This collision get run as soon as one pixel overlaps
	# Mask.overlap also returns the point of the player mask that collides with the obstacle
	# Offset is so that the top left of the player mask is in the same spot as the top left of the obstacle mask
	# if player_mask.overlap(obstacle_mask, (offset_x, offset_y)):
	# 	print('collision')

	# A more foregiving collision with overlap where it only says collision if 10 or more pixels overlap
	if player_mask.overlap_area(obstacle_mask, (offset_x, offset_y)) >= 10:
		print('collision')

	pygame.display.update()
	clock.tick(60)