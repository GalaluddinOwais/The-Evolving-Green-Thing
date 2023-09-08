def manifest(v1, w1, d1, v2, w2, d2, v3, w3, d3, v4, w4, d4,VVV1,VVV2,VVV3,VVV4, D):
    import pygame
    import pymunk
    import pymunk.pygame_util
    import random
    import math


    def neural_network(v1, w1, d1, v2, w2, d2, v3, w3, d3, v4, w4, d4,VVV1,VVV2,VVV3,VVV4, D, x1, x2): #VVV1,VVV2,VVV3,VVV4 are dispensable (one output.. the other weights take care of it)
                                                                                                       #x2 (y position) is dispensible .. won't have affect on output
        return VVV1*(x1 * v1 + x2 * w1 + d1) + VVV2*(x1 * v2 + x2 * w2 + d2) + VVV3*(x1 * v3 + x2 * w3 + d3) + VVV4*(x1 * v4 + x2 * w4 + d4) + D

    pygame.init()

    WIDTH, HEIGHT = 600, 400
    RADIUS = math.sqrt(WIDTH * WIDTH + HEIGHT * HEIGHT)  # max possible distance
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
        shape = pymunk.Poly.create_box(body, (20, window.get_height()))
        shape.elasticity = 0.4
        shape.friction = 0.5
        space.add(body, shape)

        #############
        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        body.position = (window.get_width()/2, 10)
        shape = pymunk.Poly.create_box(body, (window.get_width(), 20))
        shape.elasticity = 0.4
        shape.friction = 0.5
        space.add(body, shape)

        ############
        # center_body = pymunk.Body(body_type=pymunk.Body.DYNAMIC)
        # center_body.position = (WIDTH/2, HEIGHT/2)
        # shape = pymunk.Segment(center_body, (0, 0), (0, WIDTH/2-40), 10)
        # shape.elasticity = 1
        # shape.friction = 2
        # shape.mass =40
        # shape.color = (21,120,20,0)
        #
        # hidden_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        # hidden_body.position = (WIDTH/2, HEIGHT/2)
        # rotation_center_joint = pymunk.PinJoint(center_body, hidden_body, (0, 0), (0, 0))
        #
        # space.add(center_body,shape,hidden_body,rotation_center_joint)

        center_body = pymunk.Body(body_type=pymunk.Body.DYNAMIC)
        center_body.position = (100, window.get_height() - 40)
        shape = pymunk.Circle(center_body,14)
        shape.mass = 1
        shape.elasticity = 0
        shape.friction = 2
        shape.color = (21, 120, 20, 0)
        space.add(center_body,shape)


        # balls_conuter = 0
        frame = 0
        max_value1 = 0
        max = 0
        r = random.uniform(0, 255)
        g = random.uniform(0, 255)
        b = random.uniform(0, 255)


        # note: frame indexed 0 is not included in the loop .. it starts with frame (index) = 0 + 1 .. consider it when looking at if-conditions that uses the frame index
        circle1 = pymunk.Body(body_type=pymunk.Body.DYNAMIC)
        circle1.position = (random.uniform(20, WIDTH - 20), 30)
        shapec1 = pymunk.Circle(circle1, 12)
        shapec1.mass = 10
        shapec1.elasticity = 1
        shapec1.friction = 2
        shapec1.color = (r, g, b, 0)
        space.add(circle1, shapec1)

        neural_network_output = neural_network(v1, w1, d1, v2, w2, d2, v3, w3, d3, v4, w4, d4,VVV1, VVV2, VVV3, VVV4, D,
                                               center_body.position[0] - circle1.position[0],
                                               center_body.position[1] - circle1.position[1])

        center_body.apply_force_at_world_point((neural_network_output, 0), (0, 0))

        while run:
            frame = frame + 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # run = False
                    # break
                    return max


            neural_network_output = neural_network(v1, w1, d1, v2, w2, d2, v3, w3, d3, v4, w4, d4, VVV1, VVV2, VVV3, VVV4, D,
                                                       center_body.position[0] - circle1.position[0],
                                                       center_body.position[1] - circle1.position[1])

            center_body.apply_force_at_world_point((neural_network_output, 0), (0, 0))
            if frame % 120 == 0:



                if max_value1 < RADIUS-100:  # elimination of the bad detected criteria --no further chances if it could not get as close as ((RADIUS-100)/RADIUS) % to the ball
                    return max        # remove and re add to feel the difference in fitness calculation


                max += max_value1
                max_value1 = 0

                space.remove(circle1, shapec1)

                circle1 = pymunk.Body(body_type=pymunk.Body.DYNAMIC)
                circle1.position = (random.uniform(20, WIDTH - 20), 30)
                shapec1 = pymunk.Circle(circle1, 12)
                shapec1.mass = 10
                shapec1.elasticity = 1
                shapec1.friction = 2
                shapec1.color = (r, g, b, 0)
                space.add(circle1, shapec1)

                # balls_conuter +=1
                # print(balls_conuter)



            # center_body.position = pygame.mouse.get_pos()
            # center_body_3.position = (abs(center_body.position[0]-800),center_body.position[1])

            value1 = RADIUS - math.sqrt(math.pow(abs(center_body.position[0] - circle1.position[0]), 2) + math.pow(
                abs(center_body.position[1] - circle1.position[1]), 2))

            if value1 > max_value1:
                max_value1 = value1

            if frame == 12000:
                return max

            window.fill("black")
            space.debug_draw(window_space_linkage)
            pygame.display.update()

            space.step(dt)
            clock.tick(fps)

        pygame.quit()

    return (run(window))


if __name__ == "__main__":
    print(manifest(-0.21960389774798894, 0.27463501229769627, 0.02958436603350445, 0.2607442234335149, 0.34312072016187045, -0.21018705259333093, 0.28108344941520214, 0.10109002644668463, 0.1111585592233405, 0.02919141265494285, -0.14209077388060254, -0.18933585556957222, 0.26177195445493173, -0.24331865434249256, -0.23626545734285864, -0.327333640252388, -0.13850530704983433))
    print(manifest(-0.21960389774798894, 0.27463501229769627, 0.09133782635905252, 0.2607442234335149, 0.34312072016187045, -0.21018705259333093, 0.4197281217599218, 0.10109002644668463, 0.1111585592233405, 0.02919141265494285, -0.14209077388060254, -0.18933585556957222, 0.26177195445493173, -0.24331865434249256, -0.23626545734285864, -0.327333640252388, -0.13850530704983433))
    print(manifest(-0.21960389774798894, 0.27463501229769627, 0.02958436603350445, 0.2607442234335149, 0.34312072016187045, -0.21018705259333093, 0.4197281217599218, 0.10109002644668463, 0.1111585592233405, 0.02919141265494285, -0.14209077388060254, -0.18933585556957222, 0.26177195445493173, -0.24331865434249256, -0.23626545734285864, -0.327333640252388, -0.13850530704983433))