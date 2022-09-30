import pygame,sys

pygame.init()
screen = pygame.display.set_mode((800,800))
clock = pygame.time.Clock()

# creating the obstacle
obstacle_surf = pygame.image.load('alpha.png').convert_alpha()
obstacle_pos = (100,100)
obstacle_mask = pygame.mask.from_surface(obstacle_surf)

# Mask -> Surface
new_obstacle_surf = obstacle_mask.to_surface()
# remove the black color from the surface converted from a mask
new_obstacle_surf.set_colorkey((0,0,0))

# Filing in the surface with a color by looping over all pixels if its white change its colour
surf_w, surf_h =new_obstacle_surf.get_size()
for x in range(surf_w):
    for y in range(surf_h):
        # Get color of a specific pixel, check if its not transparent
        if new_obstacle_surf.get_at((x,y))[0] != 0:
            new_obstacle_surf.set_at((x, y), 'orange')


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('white')
    screen.blit(new_obstacle_surf,obstacle_pos)
    screen.blit(obstacle_surf,obstacle_pos)
    

    # Simple way to create an outline from a mask (this does not work if there is a hole in the surface)
    # add the obstacle x or y to it because a mask does not have the posisitioning data so will always be at 0,0 so to put it at the right spot add the positioning
    for point in obstacle_mask.outline():
        x = point[0] + obstacle_pos[0]
        y = point[1] + obstacle_pos[1]
        pygame.draw.circle(screen, 'red', (x, y), 3)
    

    pygame.display.update()
    clock.tick(60)