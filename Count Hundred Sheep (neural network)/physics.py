import random
import math


def manifest(vv1, vv2, vv3, vv4, vv5, vvv1, vvv2, vvv3, vvv4, vvv5, vvvv1, vvvv2, vvvv3,
             vvvv4, vvvv5, d, D):
    import pygame
    import pymunk
    import pymunk.pygame_util

    pygame.init()

    WIDTH, HEIGHT = 350, 200

    window = pygame.display.set_mode((WIDTH, HEIGHT))
    window_space_linkage = pymunk.pygame_util.DrawOptions(window)

    def neural_network(vv1, vv2, vv3, vv4, vv5, vvv1, vvv2, vvv3, vvv4, vvv5, vvvv1, vvvv2, vvvv3,
                       vvvv4, vvvv5, d, D, x2):
        node1 = x2 * vv1 + d
        node2 = x2 * vv2 + d
        node3 = x2 * vv3 + d
        node4 = x2 * vv4 + d
        node5 = x2 * vv5 + d
        output1 = node1 * vvv1 + node2 * vvv2 + node3 * vvv3 + node4 * vvv4 + node5 * vvv5 + D
        output2 = node1 * vvvv1 + node2 * vvvv2 + node3 * vvvv3 + node4 * vvvv4 + node5 * vvvv5 + D
        return [output1, output2]

    def run(window):

        run = True
        clock = pygame.time.Clock()
        fps = 60
        dt = 1 / fps

        space = pymunk.Space()
        space.gravity = (0, 981)

        bar2revpos = WIDTH * 3 / 5

        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        body.position = (WIDTH / 2, window.get_height() - 10)
        shape = pymunk.Poly.create_box(body, (WIDTH, 20))
        # shape.elasticity = .4
        # shape.friction = .5
        space.add(body, shape)

        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        body.position = (WIDTH, HEIGHT / 2)
        shape = pymunk.Poly.create_box(body, (20, window.get_height()))
        # shape.elasticity = .4
        # shape.friction = .5
        space.add(body, shape)

        ########################################
        bar2Color = (random.uniform(0, 255), random.uniform(0, 255), random.uniform(0, 255), 0)
        barUp2 = random.uniform(20, 111)  # random.uniform(20, 111)

        barDown2 = barUp2 + 70
        bodyu2 = pymunk.Body(body_type=pymunk.Body.STATIC)
        bodyu2.position = (window.get_width() - bar2revpos, -HEIGHT / 2 + barUp2)
        shapeu2 = pymunk.Poly.create_box(bodyu2, (20, window.get_height()))
        shapeu2.color = bar2Color
        space.add(bodyu2, shapeu2)

        bodyd2 = pymunk.Body(body_type=pymunk.Body.STATIC)
        bodyd2.position = (window.get_width() - bar2revpos, window.get_height() / 2 + barDown2)
        shaped2 = pymunk.Poly.create_box(bodyd2, (20, window.get_height()))
        shaped2.color = bar2Color
        space.add(bodyd2, shaped2)

        #######################################
        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        body.position = (0, window.get_height() / 2)
        shapee = pymunk.Poly.create_box(body, (20, window.get_height()))
        # shapee.elasticity = 0.4
        # shapee.friction = 0.5
        space.add(body, shapee)
        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        body.position = (window.get_width() / 2, -30)
        shape = pymunk.Poly.create_box(body, (window.get_width(), 100))
        # shape.elasticity = 0.4
        # shape.friction = 0.5
        space.add(body, shape)

        center_body = pymunk.Body(body_type=pymunk.Body.DYNAMIC)
        center_body.position = (35, HEIGHT - 30)
        shape = pymunk.Circle(center_body, 10)
        shape.mass = .1
        shape.elasticity = 2.3
        shape.friction = 2
        shape.color = (21, 120, 20, 0)
        space.add(center_body, shape)

        neural_network_output = neural_network(vv1, vv2, vv3, vv4, vv5, vvv1, vvv2, vvv3, vvv4, vvv5, vvvv1, vvvv2,
                                               vvvv3,
                                               vvvv4, vvvv5, d, D, barUp2)
        center_body.apply_force_at_local_point((neural_network_output[0], neural_network_output[1]), (0, 0))
        # print(barUp2)
        # print(neural_network_output[0], neural_network_output[1])

        frame = 0
        maxclosenessBar2 = 0
        fitness = 0
        max = 0

        while run:
            frame = frame + 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # run = False
                    # break
                    return (max)

            # glitch handing
            if (center_body.position[0] > WIDTH) or (center_body.position[0] < 0) or (
                    center_body.position[1] > HEIGHT) or (center_body.position[1] < 0) or ((center_body.position[0] > WIDTH-bar2revpos) and  maxclosenessBar2 < 1000):
                return fitness


            if frame % 120 == 0:
                fitness += max
                if maxclosenessBar2 < 1000:
                    return fitness
                max = 0
                maxclosenessBar2 = 0

                space.remove(center_body, shape)
                center_body = pymunk.Body(body_type=pymunk.Body.DYNAMIC)
                center_body.position = (35, HEIGHT - 30)
                shape = pymunk.Circle(center_body, 10)
                shape.mass = .1
                shape.elasticity = 2.3
                shape.friction = 2
                shape.color = (21, 120, 20, 0)
                space.add(center_body, shape)

                ########################################
                barUp2 = random.uniform(20, 111)  # 20-110

                barDown2 = barUp2 + 70

                space.remove(bodyu2, shapeu2)
                bodyu2 = pymunk.Body(body_type=pymunk.Body.STATIC)
                bodyu2.position = (window.get_width() - bar2revpos, -HEIGHT / 2 + barUp2)
                shapeu2 = pymunk.Poly.create_box(bodyu2, (20, window.get_height()))
                shapeu2.color = bar2Color
                space.add(bodyu2, shapeu2)

                space.remove(bodyd2, shaped2)
                bodyd2 = pymunk.Body(body_type=pymunk.Body.STATIC)
                bodyd2.position = (window.get_width() - bar2revpos, window.get_height() / 2 + barDown2)
                shaped2 = pymunk.Poly.create_box(bodyd2, (20, window.get_height()))
                shaped2.color = bar2Color
                space.add(bodyd2, shaped2)
                # # # # # #

                neural_network_output = neural_network(vv1, vv2, vv3, vv4, vv5, vvv1, vvv2, vvv3, vvv4, vvv5, vvvv1,
                                                       vvvv2, vvvv3,
                                                       vvvv4, vvvv5, d, D,
                                                       barUp2)

                # print(barUp2)
                # print(neural_network_output[0],neural_network_output[1])
                center_body.apply_force_at_local_point((neural_network_output[0], neural_network_output[1]), (0, 0))

                #######################################

            if frame == 120 * 100 + 1:
                return fitness

            if center_body.position[0] >= WIDTH - (bar2revpos + 10) and center_body.position[0] <= WIDTH - (
                    bar2revpos - 10) and center_body.position[1] >= barUp2 and center_body.position[1] <= barUp2 + 70:
                if maxclosenessBar2 < 1000:
                    maxclosenessBar2 = 1000
            else:
                closeness = 1 / math.sqrt(
                    math.pow(center_body.position[0] - (WIDTH - bar2revpos), 2) + math.pow(
                        center_body.position[1] - (barUp2 + 35), 2)) * 10000
                if closeness > 500:
                    if maxclosenessBar2 < 500:
                        maxclosenessBar2 = 500
                else:
                    if maxclosenessBar2 < closeness:
                        maxclosenessBar2 = closeness
            # print(maxclosenessBar2 , maxclosenessBar1)
            if max < maxclosenessBar2:
                max =  maxclosenessBar2

            window.fill("black")
            space.debug_draw(window_space_linkage)
            pygame.display.update()

            space.step(dt)
            clock.tick(fps)

        pygame.quit()

    return (run(window))


if __name__ == "__main__":


    #input representing gap height is like (0--> high ... 110 --> low) ((barup2))
    print(manifest(-0.5966169844532274, 4.659810432996961, -4.439229317873677, 3.6708108424268264, -0.8934192029435488, 0.5321215572477804, 3.46813371371163, -0.8397812693273812, -5.125815295769623, 1.2729439646093539, -2.5338562037928085, 0.9321027284426631, -2.595274162874369, 4.642493369272117, 3.8072319742179523, -2186.651767291215, 3176.9528628551343))
    print(manifest(-1.3329890266125606, 1.32417755396237, -0.16684576448801636, -3.3799866944295474, 2.285138914570325, -4.472159584544198, 0.8373729255794053, 3.209830500193247, -0.05878275825463852, 0.3635859668375421, 3.5675020364073333, 3.4497505793533048, -1.04412352374875, -4.514909985174332, 4.767584733120486, -786.9190064853337, 1092.273953161085))
    print(manifest(-1.1754399727152176, 1.32417755396237, 5.579853992744958, -3.3799866944295474, 2.285138914570325, -4.472159584544198, 0.8373729255794053, 3.209830500193247, -0.05878275825463852, 0.3635859668375421, 3.5675020364073333, 3.4497505793533048, -1.04412352374875, -4.514909985174332, 4.767584733120486, -786.9190064853337, 1092.273953161085))
    print(manifest(-2.641647158885496, -0.246155374184446, 0.4700553838685515, -3.0554564818487413, 1.754526558464626, -3.9964298316482205, 2.6385993687879736, 2.9713855343933755, 2.109661704097178, -3.951301716592456, -1.3544870370446942, 1.1600741023607402, 5.3612151964600585, -5.4740979257350055, 4.197966158720295, -2078.006477297592, 2814.820894766748))
    print(manifest(3.423220271272678, -2.0764955891220476, 5.925281807553482, 1.4102560816843361, 4.313546338875453, -3.9964298316482205, 2.6385993687879736, 2.9713855343933755, 2.109661704097178, -3.951301716592456, -1.3544870370446942, 1.1600741023607402, 5.3612151964600585, -5.4740979257350055, 4.197966158720295, -2078.006477297592, 2814.820894766748))
    print(manifest(1.848689923563012, -1.5365328463847145, -2.1497370075197177, 5.150556630359748, -1.7523033846300642, -0.7425936236036694, -1.4751783453827514, 4.9518554839804345, -0.4322956611805093, -5.86432487486402, -4.819104056471831, 4.971908580054972, 3.400997671111316, -5.349451462205343, 0.7598171765422137, -1772.5039630954443, -5202.1028402049815))

    #input representing gap height is like (110--> high ... 0 --> low) ((HEIGHT-barup2))
    # print(manifest(-5.390137514407987, 1.063825957454437, 2.0586056294028303, -0.09331829003349412, 3.0102868168668184, -2.337459617937613, 0.1716992826173822, 1.7493171557710676, -1.1179085753452647, 3.6541479036452547, 4.237965262947476, -0.02618995282994696, 2.4259733239883197, 2.6029911587463825, -4.051024310971963, 711.391869592866, -2660.373350631056))
