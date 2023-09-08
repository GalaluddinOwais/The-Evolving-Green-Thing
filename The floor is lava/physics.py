def manifest(a, a1, a2, b, b1, b2, c, c1, c2):
    import pygame
    import pymunk
    import pymunk.pygame_util
    import math

    pygame.init()

    WIDTH, HEIGHT = 300, 300
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    window_space_linkage = pymunk.pygame_util.DrawOptions(window)

    def run(window):

        run = True
        clock = pygame.time.Clock()
        fps = 60
        dt = 1 / fps

        space = pymunk.Space()
        space.gravity = (0, 981)

        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        body.position = (window.get_width() / 2, window.get_height() - 10)
        shape = pymunk.Poly.create_box(body, (window.get_width(), 20))
        shape.elasticity = 0.4
        shape.friction = 0.5
        space.add(body, shape)
        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        body.position = (window.get_width(), window.get_height() / 2)
        shape = pymunk.Poly.create_box(body, (20, window.get_height()))
        shape.elasticity = 0.4
        shape.friction = 0.5
        space.add(body, shape)
        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        body.position = (0, window.get_height() / 2)
        shapee = pymunk.Poly.create_box(body, (20, window.get_height()))
        shapee.elasticity = 0.4
        shapee.friction = 0.5
        space.add(body, shapee)
        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        body.position = (window.get_width() / 2, 10)
        shape = pymunk.Poly.create_box(body, (window.get_width(), 20))
        shape.elasticity = 0.4
        shape.friction = 0.5
        space.add(body, shape)

        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        body.position = (window.get_width()*3 / 4, window.get_height()/2)
        shape = pymunk.Poly.create_box(body, (60, 20))
        shape.elasticity = 0.4
        shape.friction = 0.5
        space.add(body, shape)


        center_body = pymunk.Body(body_type=pymunk.Body.DYNAMIC)
        center_body.position = (100, window.get_height() - 40)
        shape = pymunk.Segment(center_body, (20, 20), (10, 10), 13)
        shape.mass = 10
        shape.elasticity = 1
        shape.friction = 2
        shape.color = (21, 120, 20, 0)

        center_body_1 = pymunk.Body(body_type=pymunk.Body.DYNAMIC)
        center_body_1.position = (124, window.get_height() - 40)
        shape_1 = pymunk.Segment(center_body_1, (20, 20), (10, 10), 12)
        shape_1.mass = 10
        shape_1.elasticity = 1
        shape_1.friction = 2
        shape_1.color = (21, 90, 20, 0)

        center_joint_1 = pymunk.PinJoint(center_body, center_body_1, (20, 20), (10, 10))

        center_body_2 = pymunk.Body(body_type=pymunk.Body.DYNAMIC)
        center_body_2.position = (148, window.get_height() - 40)
        shape_2 = pymunk.Segment(center_body_2, (20, 20), (10, 10), 11)
        shape_2.mass = 10
        shape_2.elasticity = 1
        shape_2.friction = 2
        shape_2.color = (21, 60, 20, 0)

        center_joint_2 = pymunk.PinJoint(center_body_1, center_body_2, (20, 20), (10, 10))

        space.add(center_body, shape, center_body_1, shape_1, center_body_2, shape_2, center_joint_1, center_joint_2)

        frame = 0
        max = 0
        while run:
            frame = frame + 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # run = False
                    # break
                    return (max)

            if frame == 60 * 3.5:
                return (max)

            if frame == a:
                center_body.apply_force_at_local_point((a1, a2), (0, 0))
            if frame == b:
                center_body_1.apply_force_at_local_point((b1, b2), (0, 0))
            if frame == c:
                center_body_2.apply_force_at_local_point((c1, c2), (0, 0))

            # if center_body.position[1] < 440:
            #     max = max + 1
            #
            # if center_body_1.position[1] < 440:
            #     max = max + 1
            #
            # if center_body_2.position[1] < 440:
            #     max = max + 1

            max = max + (HEIGHT - center_body.position[1] + HEIGHT - center_body_1.position[1] + HEIGHT - center_body_2.position[1])*100000 # so the lower is very low compared to the higher

            window.fill("black")
            space.debug_draw(window_space_linkage)
            pygame.display.update()

            space.step(dt)
            clock.tick(fps)

        pygame.quit()

    return (run(window))


if __name__ == "__main__":
    manifest(23, 332020.0946403692, -454947.29166982573, 20, 299853.5923478793, -369494.7349892085, 55, -281345.6643782024, -464545.476953906)