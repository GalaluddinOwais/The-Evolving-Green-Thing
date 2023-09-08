def manifest(a, a1, a2, b, b1, b2, c, c1, c2):
    import pygame
    import pymunk
    import pymunk.pygame_util
    import math

    def map(y, x, z, y2, z2):
        return (x - y) / (z - y) * (z2 - y2) + y2


    pygame.init()

    WIDTH, HEIGHT = 250, 600
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




        center_body = pymunk.Body(body_type=pymunk.Body.DYNAMIC)
        center_body.position = (100, window.get_height() - 40)
        shape = pymunk.Segment(center_body, (20, 20), (10, 10), 13)
        shape.mass = 10
        shape.elasticity = 1
        shape.friction = 2
        shape.color = (21, map(0,abs(a1)+abs(a2),2000,40,255), 20, 0)

        center_body_1 = pymunk.Body(body_type=pymunk.Body.DYNAMIC)
        center_body_1.position = (124, window.get_height() - 40)
        shape_1 = pymunk.Segment(center_body_1, (20, 20), (10, 10), 12)
        shape_1.mass = 10
        shape_1.elasticity = 1
        shape_1.friction = 2
        shape_1.color = (21, map(0,abs(b1)+abs(b2),2000,40,255), 20, 0)

        center_joint_1 = pymunk.PinJoint(center_body, center_body_1, (20, 20), (10, 10))

        center_body_2 = pymunk.Body(body_type=pymunk.Body.DYNAMIC)
        center_body_2.position = (148, window.get_height() - 40)
        shape_2 = pymunk.Segment(center_body_2, (20, 20), (10, 10), 11)
        shape_2.mass = 10
        shape_2.elasticity = 1
        shape_2.friction = 2
        shape_2.color = (21, map(0,abs(c1)+abs(c2),2000,40,255), 20, 0)

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

            value =   (1000*6 - (abs(a1)+abs(a2)+abs(b1)+abs(b2)+abs(c1)+abs(c2)) )/10  +   (HEIGHT - center_body.position[1])  #specify maximum force to be 1000


            if value> max:
                max = value

            window.fill("black")
            space.debug_draw(window_space_linkage)
            pygame.display.update()

            space.step(dt)
            clock.tick(fps)

        pygame.quit()

    return (run(window))


if __name__ == "__main__":

   print( manifest(66, 41.07655530862371, 86.97267303168064, 14, -0.1524272947967802, -413.0350742312337, 61, 24.25064793503202, -389.05365543347693))
   print(manifest(72, 41.07655530862371, 86.97267303168064, 45, -0.1524272947967802, -320.9013566353833, 57, 24.25064793503202, -392.1380042646996))
   print(manifest(65, -282.2228102862847, 154.70995425133106, 15, -271.9137681709416, -60.3333414078719, 30, -102.56910332516588, -2.575640071337034))
   print(manifest(56, -472.82174713489474, 456.5015167270708, 63, -480.555761557762, -111.80502219335597, 61, 220.4251079492335, -108.26065385112258))
   print(manifest(77, -93.13356951715264, -490.4391456104533, 5, 76.44809613719463, -200.73405863723372, 58, 23.20738466212697, 45.387708625486084))