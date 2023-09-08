def manifest(a, a1, a2, b, b1, b2, c, c1, c2):
    import pygame
    import pymunk
    import pymunk.pygame_util
    import random

    pygame.init()

    WIDTH, HEIGHT = 800, 400
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
        # body = pymunk.Body(body_type=pymunk.Body.STATIC)
        # body.position = (window.get_width(), window.get_height() / 2)
        # shape = pymunk.Poly.create_box(body, (20, window.get_height()))
        # shape.elasticity = 0.4
        # shape.friction = 0.5
        # space.add(body, shape)
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

        ball_pos = 0
        ball_pos += 50
        circle1 = pymunk.Body(body_type=pymunk.Body.DYNAMIC)
        circle1.position = (WIDTH / 2 + ball_pos, ball_pos)
        shape = pymunk.Circle(circle1, 12)
        shape.mass = 20
        shape.elasticity = 1
        shape.friction = 2
        shape.color = (random.uniform(0, 255), random.uniform(0, 255), random.uniform(0, 255),0)
        space.add(circle1, shape)
        circle1.apply_force_at_local_point((-900000, 0), (0, 0))

        ball_pos += 50
        circle2 = pymunk.Body(body_type=pymunk.Body.DYNAMIC)
        circle2.position = (WIDTH / 2 + ball_pos, ball_pos)
        shape = pymunk.Circle(circle2, 12)
        shape.mass = 20
        shape.elasticity = 1
        shape.friction = 2
        shape.color = (random.uniform(0, 255), random.uniform(0, 255), random.uniform(0, 255),0)
        space.add(circle2, shape)
        circle2.apply_force_at_local_point((-900000, 0), (0, 0))

        ball_pos += 50
        circle3 = pymunk.Body(body_type=pymunk.Body.DYNAMIC)
        circle3.position = (WIDTH / 2 + ball_pos, ball_pos)
        shape = pymunk.Circle(circle3, 12)
        shape.mass = 20
        shape.elasticity = 1
        shape.friction = 2
        shape.color = (random.uniform(0, 255), random.uniform(0, 255), random.uniform(0, 255),0)
        space.add(circle3, shape)
        circle3.apply_force_at_local_point((-900000, 0), (0, 0))




        frame = 0
        max1 = 0
        max2 = 0
        max3 = 0
        max = 0
        while run:
            frame = frame + 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # run = False
                    # break
                    return (max)

            if frame == 170:
                return (max)

            if frame == a:
                center_body.apply_force_at_local_point((a1, a2), (0, 0))
            if frame == b:
                center_body_1.apply_force_at_local_point((b1, b2), (0, 0))
            if frame == c:
                center_body_2.apply_force_at_local_point((c1, c2), (0, 0))


            if frame > 60:
                if max1 < circle1.position[0] and max1 < WIDTH: #want the balls to be aimed to reach farer out the border? add a number to the width in the condition
                    max1 = circle1.position[0]

                if max2 < circle2.position[0] and max2 < WIDTH:
                    max2 = circle2.position[0]

                if max3 < circle3.position[0] and max3 < WIDTH:
                    max3 = circle3.position[0]

                max = max1 + max2 + max3
            window.fill("black")
            space.debug_draw(window_space_linkage)
            pygame.display.update()

            space.step(dt)
            clock.tick(fps)

        pygame.quit()

    return (run(window))


if __name__ == "__main__":
    print(manifest(15, 3300707.966113707, 412312.105587268, 30, -2609096.8477728539, 568673.3436630229, 30, -10399.162353064632, 336506.7713556705))
    print(manifest(37, 524511.6061122897, 95509.14331814437, 20, 693870.9709212566, -661249.2715735566, 50, 761187.2996478037, 917417.6444736074))
    print(manifest(37, 524511.6061122897, 95509.14331814437, 20, 693870.9709212566, -661249.2715735566, 50, 761187.2996478037, -298408.5488473403))
    print(manifest(37, 556753.4963935553, -711206.4899028332, 8, 693870.9709212566, -661249.2715735566, 69, 896759.869807129, -537917.8568839969))
    print(manifest(37, 556753.4963935553, -933028.7341695165, 8, 693870.9709212566, -661249.2715735566, 78, 896759.869807129, 416543.24649979756))
