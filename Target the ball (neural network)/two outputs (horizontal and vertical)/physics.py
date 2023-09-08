def manifest(v1, w1, d1, v2, w2, d2, v3, w3, d3, v4, w4, d4, VVV1, VVVV1, VVV2, VVVV2, VVV3, VVVV3, VVV4, VVVV4, D1,
             D2):
    import pygame
    import pymunk
    import pymunk.pygame_util
    import random
    import math

    def map(y, x, z, y2, z2):
        return (x - y) / (z - y) * (z2 - y2) + y2

    def neural_network(v1, w1, d1, v2, w2, d2, v3, w3, d3, v4, w4, d4, VVV1, VVVV1, VVV2, VVVV2, VVV3, VVVV3, VVV4,
                       VVVV4, D1, D2, x1, x2):
        hidden_node_1_output = (x1 * v1 + x2 * w1 + d1)
        hidden_node_2_output = (x1 * v2 + x2 * w2 + d2)
        hidden_node_3_output = (x1 * v3 + x2 * w3 + d3)
        hidden_node_4_output = (x1 * v4 + x2 * w4 + d4)
        output1 = VVV1 * hidden_node_1_output + VVV2 * hidden_node_2_output + VVV3 * hidden_node_3_output + VVV4 * hidden_node_4_output + D1
        output2 = VVVV1 * hidden_node_1_output + VVVV2 * hidden_node_2_output + VVVV3 * hidden_node_3_output + VVVV4 * hidden_node_4_output + D2
        return [output1, output2]

    pygame.init()

    WIDTH, HEIGHT = 600, 600
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
        body.position = (window.get_width() / 2, 10)
        shape = pymunk.Poly.create_box(body, (window.get_width(), 20))
        shape.elasticity = 0.4
        shape.friction = 0.5
        space.add(body, shape)

        center_body = pymunk.Body(body_type=pymunk.Body.DYNAMIC)
        center_body.position = (WIDTH / 2, HEIGHT / 2)
        shape = pymunk.Circle(center_body, 14)
        shape.mass = 20
        shape.elasticity = .1
        shape.friction = .11
        shape.color = (21, 60, 20, 0)
        space.add(center_body, shape)

        frame = 0
        max = 0
        r = random.uniform(0, 255)
        g = random.uniform(0, 255)
        b = random.uniform(0, 255)

        # note: frame indexed 0 is not included in the loop .. it starts with frame (index) = 0 + 1 .. consider it when looking at if-conditions that uses the frame index
        circle1 = pymunk.Body(body_type=pymunk.Body.STATIC)
        circle1.position = (random.uniform(20, WIDTH - 20), random.uniform(20, HEIGHT - 20))
        shapec1 = pymunk.Circle(circle1, 12)

        shapec1.color = (r, g, b, 0)
        space.add(circle1, shapec1)

        neural_network_output = neural_network(v1, w1, d1, v2, w2, d2, v3, w3, d3, v4, w4, d4, VVV1, VVVV1, VVV2, VVVV2,
                                               VVV3, VVVV3, VVV4, VVVV4, D1, D2,
                                               center_body.position[0] - circle1.position[0],
                                               center_body.position[1] - circle1.position[1])

        center_body.apply_force_at_world_point((neural_network_output[0], neural_network_output[1]), (0, 0))

        max_value = 0
        while run:

            frame = frame + 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # run = False
                    # break
                    return max

            neural_network_output = neural_network(v1, w1, d1, v2, w2, d2, v3, w3, d3, v4, w4, d4, VVV1, VVVV1, VVV2,
                                                   VVVV2, VVV3, VVVV3, VVV4, VVVV4, D1, D2,
                                                   center_body.position[0] - circle1.position[0],
                                                   center_body.position[1] - circle1.position[1])

            center_body.apply_force_at_world_point((neural_network_output[0], neural_network_output[1]), (0, 0))
            if frame % 240 == 0:
                shape.color = (21, 60, 20, 0)

                max += max_value
                if max_value < 10:
                    return max
                max_value = 0

                #
                # if total_value1 < 0:  # elimination of the bad detected criteria --no further chances if it could not get as close as ((RADIUS-100)/RADIUS) % to the ball
                #     return max        # remove and re add to feel the difference in fitness calculation

                space.remove(circle1, shapec1)

                circle1 = pymunk.Body(body_type=pymunk.Body.STATIC)
                circle1.position = (random.uniform(20, WIDTH - 20), random.uniform(20, HEIGHT - 20))
                shapec1 = pymunk.Circle(circle1, 12)

                shapec1.color = (r, g, b, 0)
                space.add(circle1, shapec1)

            # value1 = RADIUS - math.sqrt(math.pow(abs(center_body.position[0] - circle1.position[0]), 2) + math.pow(abs(center_body.position[1] - circle1.position[1]), 2))
            # if negative -> body is very far from the ball .. it is more than (radius) mm away from the ball

            value = math.sqrt(math.pow(abs(center_body.position[0] - circle1.position[0]), 2) + math.pow(
                abs(center_body.position[1] - circle1.position[1]), 2))
            if max_value < 1000 / value:
                max_value = 1000 / value

                if max_value >= 10:
                    shape.color = (21, map(10, max_value, 100, 135, 255), 20, 0)

            if frame == 24000:
                return max

            window.fill("black")
            space.debug_draw(window_space_linkage)
            pygame.display.update()

            space.step(dt)
            clock.tick(fps)

        pygame.quit()

    return (run(window))


if __name__ == "__main__":
    print(manifest(-0.7540979010233855, 6.778878818143113, -2.6855252451531086, 8.455380288478416, 3.693917348250075,
                   9.306492256022576, -7.236741361017039, -7.0439586699553125, 8.403283162955269, -5.6020558929686555,
                   -6.039465596453688, -9.120959513164772, 1.7652579083178725, -3.123894206518978, -8.740218780670867,
                   -8.15113981921759, -9.979700867248319, 5.557066721407448, 7.707349576922642, 6.073577015082407,
                   9.535713619818168, 9.872941457130725))
    print(manifest(-0.7540979010233855, 6.778878818143113, -2.6855252451531086, 8.455380288478416, 3.693917348250075,
                   9.306492256022576, -7.236741361017039, -7.0439586699553125, 8.403283162955269, -5.6020558929686555,
                   -6.039465596453688, -9.120959513164772, 1.7652579083178725, -3.123894206518978, -8.740218780670867,
                   -8.15113981921759, -9.979700867248319, 5.557066721407448, 7.707349576922642, 6.073577015082407,
                   9.535713619818168, 9.872941457130725))
    print(manifest(-1.3578359800665858, 9.284374159006639, 8.066792658815721, 6.9479588832768115, 6.884154046847314,
                   -1.481814209524197, 2.740731299068864, -2.712296064081279, -6.5567087998025, 8.628310497875738,
                   6.07726590880786, -6.1163829528021925, 0.012738888976009832, 4.874609228895146, 2.440913218137826,
                   -7.6302803170280376, -6.882862895126776, 5.684234193354358, -3.472060878755796, -8.315441991751122,
                   4.192128980799978, 1.1396351908037268))
    print(manifest(-7.890480713512156, -8.623126296566717, 2.0097210563646932, 5.573891598954761, -2.4373370228999853,
                   3.907453808522007, -9.457470050656829, -3.887921292771548, 4.462671444150921, -6.603067431473968,
                   8.329829795224033, 0.666850015716232, 4.279053896754414, 5.140913766375947, 6.491386534888356,
                   6.4170063617061, 5.315504958971307, -1.6636387413075049, 6.250092914988258, -6.294461644019935,
                   6.545112681527431, 2.2627030844662954))
    print(manifest(-7.890480713512156, -8.623126296566717, 2.0097210563646932, 5.573891598954761, -2.4373370228999853,
                   3.907453808522007, -9.457470050656829, -4.885152816959788, 4.462671444150921, -6.603067431473968,
                   8.329829795224033, 0.666850015716232, 8.793972229222888, 5.140913766375947, 6.491386534888356,
                   6.4170063617061, 5.315504958971307, -1.6636387413075049, 6.250092914988258, -6.294461644019935,
                   6.545112681527431, 2.2627030844662954))
    print(manifest(-1.3578359800665858, 9.284374159006639, 8.066792658815721, 6.9479588832768115, 6.884154046847314,
                   -1.481814209524197, 5.88583976183665, -2.712296064081279, -6.5567087998025, 8.628310497875738,
                   6.07726590880786, -6.1163829528021925, 0.012738888976009832, -9.11269803680444, 2.440913218137826,
                   -7.6302803170280376, -6.882862895126776, 5.684234193354358, -3.472060878755796, -8.315441991751122,
                   4.192128980799978, 1.1396351908037268))
    print(manifest(-1.3578359800665858, 9.284374159006639, 8.066792658815721, 6.9479588832768115, 6.884154046847314,
                   -1.481814209524197, 5.88583976183665, -2.712296064081279, -6.5567087998025, 8.628310497875738,
                   6.07726590880786, -6.1163829528021925, 0.012738888976009832, -9.11269803680444, 2.440913218137826,
                   -7.6302803170280376, -6.882862895126776, 5.684234193354358, -3.472060878755796, -8.315441991751122,
                   3.702453919099133, 1.1396351908037268))