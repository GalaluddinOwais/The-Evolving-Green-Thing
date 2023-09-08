import math


def manifest(a, a1, a2, b, b1, b2, c, c1, c2,d, d1, d2, e, e1, e2, f, f1, f2):
    import pygame
    import pymunk
    import pymunk.pygame_util

    def map(y, x, z, y2, z2):
        return (x - y) / (z - y) * (z2 - y2) + y2

    pygame.init()

    WIDTH, HEIGHT = 800, 200
    RADIUS = math.sqrt(WIDTH*WIDTH+HEIGHT*HEIGHT) #max possible distance

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
        body.position = (window.get_width(), window.get_height()*3 / 4)
        shape = pymunk.Poly.create_box(body, (150, window.get_height()*3/5))
        shape.elasticity = 0.4
        shape.friction = 0.5
        shape.color = (21, 90, 20, 0)
        space.add(body, shape)
        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        body.position = (0, window.get_height()*3/4 )
        shape = pymunk.Poly.create_box(body, (150, window.get_height()*3/5))
        shape.elasticity = 0.4
        shape.friction = 0.5
        shape.color = (200, 120, 20, 0)
        space.add(body, shape)




        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        body.position = (window.get_width() / 2, window.get_height() - 10)
        shape = pymunk.Poly.create_box(body, (window.get_width(), 20))
        shape.elasticity = 0.4
        shape.friction = 0.5
        space.add(body, shape)

        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        body.position = (window.get_width(), window.get_height()/2)
        shape = pymunk.Poly.create_box(body, (20, window.get_height()))
        shape.elasticity = 0.4
        shape.friction = 0.5
        space.add(body, shape)
        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        body.position = (0, window.get_height()/2)
        shape = pymunk.Poly.create_box(body, (20, window.get_height()))
        shape.elasticity = 0.4
        shape.friction = 0.5
        space.add(body, shape)
        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        body.position = (window.get_width() / 2, 10)
        shape = pymunk.Poly.create_box(body, (window.get_width(), 20))
        shape.elasticity = 0.4
        shape.friction = 0.5
        space.add(body, shape)

        circle2 = pymunk.Body(body_type=pymunk.Body.DYNAMIC)
        circle2.position = (40, 30)
        shapec2 = pymunk.Circle(circle2, 12)
        shapec2.mass = 20
        shapec2.elasticity = 1
        shapec2.friction = 2
        shapec2.color=(170, 90, 10, 0)
        space.add(circle2, shapec2)
        circle2.apply_force_at_local_point((25000, 0), (0, 0))

        circle1 = pymunk.Body(body_type=pymunk.Body.DYNAMIC)
        circle1.position = (WIDTH-40, 30)
        shapec1 = pymunk.Circle(circle1, 12)
        shapec1.mass = 20
        shapec1.elasticity = 1
        shapec1.friction = 2
        shapec1.color=(21, 60, 20, 0)
        space.add(circle1, shapec1)
        circle1.apply_force_at_local_point((-25000, 0), (0, 0))


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



        center_body_3 = pymunk.Body(body_type=pymunk.Body.DYNAMIC)
        center_body_3.position = (700-25, window.get_height() - 40)
        shape_3 = pymunk.Segment(center_body_3, (20, 20), (10, 10), 13)
        shape_3.mass = 10
        shape_3.elasticity = 1
        shape_3.friction = 2
        shape_3.color = (230, 160, 30, 0)

        center_body_4 = pymunk.Body(body_type=pymunk.Body.DYNAMIC)
        center_body_4.position = (676-25, window.get_height() - 40)
        shape_4 = pymunk.Segment(center_body_4, (20, 20), (10, 10), 12)
        shape_4.mass = 10
        shape_4.elasticity = 1
        shape_4.friction = 2
        shape_4.color =  (200, 120, 20, 0)

        center_joint_3 = pymunk.PinJoint(center_body_3, center_body_4, (10, 10), (20, 20))

        center_body_5 = pymunk.Body(body_type=pymunk.Body.DYNAMIC)
        center_body_5.position = (652-25, window.get_height() - 40)
        shape_5 = pymunk.Segment(center_body_5, (20, 20), (10, 10), 11)
        shape_5.mass = 10
        shape_5.elasticity = 1
        shape_5.friction = 2
        shape_5.color =  (170, 90, 10, 0)
        center_joint_4 = pymunk.PinJoint(center_body_4, center_body_5, (10, 10), (20, 20))

        space.add(center_body_3, shape_3, center_body_4, shape_4, center_body_5, shape_5, center_joint_3, center_joint_4)






        frame = 0
        max = 0
        max_value1=0
        max_value2=0

        while run:
            frame = frame + 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # run = False
                    # break
                    return max

            if frame == 170:
                return max

            if frame == a:
                center_body.apply_force_at_local_point((a1, a2), (0, 0))
            if frame == b:
                center_body_1.apply_force_at_local_point((b1, b2), (0, 0))
            if frame == c:
                center_body_2.apply_force_at_local_point((c1, c2), (0, 0))

            if frame == d:
                center_body_3.apply_force_at_local_point((d1, d2), (0, 0))
            if frame == e:
                center_body_4.apply_force_at_local_point((e1, e2), (0, 0))
            if frame == f:
                center_body_5.apply_force_at_local_point((f1, f2), (0, 0))

            # center_body.position = pygame.mouse.get_pos()
            # center_body_3.position = (abs(center_body.position[0]-800),center_body.position[1])



            if frame>0:
                value1 = RADIUS - math.sqrt(math.pow(abs(center_body.position[0] - circle1.position[0]),2) + math.pow(abs(center_body.position[1] - circle1.position[1]),2))
                value2 =   RADIUS - math.sqrt(math.pow(abs(center_body_3.position[0]-circle2.position[0]),2) + math.pow(abs(center_body_3.position[1]-circle2.position[1]),2))


                if value1 > max_value1:
                    max_value1 = value1
                    shapec1.color = (map(0, value1, 800, 20/3, 20+20), map(0, value1, 800, 120/3, 120+20), map(0, value1, 800, 20/3, 20+20), 0)

                if value2 > max_value2:
                    max_value2 = value2
                    shapec2.color = (map(0, value2, 800, 230/3, 230+20), map(0, value2, 800, 160/3, 160+20), map(0, value2, 800, 30/3, 30+20), 0)




                max = max_value1 + max_value2



            window.fill("black")
            space.debug_draw(window_space_linkage)
            pygame.display.update()

            space.step(dt)
            clock.tick(fps)

        pygame.quit()

    return (run(window))


if __name__ == "__main__":
   for i in range(200):
       manifest(108, 453452.19646117697, 402894.2199713106, 24, 680169.5128475998, -938922.1063067226, 10, -893225.7867322288, -828281.1047303482, 138, 752463.7411711372, -220225.8341499206, 10, 353556.6253572181, 67175.3507712502, 81, -580275.5881358702, 261790.94647690677)
       manifest(117, 939391.4354474426, -115193.798426606, 110, 290275.8045962162, 647591.8693387334, 24, 657818.7392670175, 62053.153193650534, 105, 588951.0024288252, 688857.7990654008, 91, 979429.8492896021, -768175.4954669797, 87, -46429.78187509091, -637264.8719770485)
       manifest(117, 939391.4354474426, -115193.798426606, 110, 290275.8045962162, 647591.8693387334, 24, 657818.7392670175, 62053.153193650534, 105, 588951.0024288252, 688857.7990654008, 91, 979429.8492896021, -768175.4954669797, 87, -46429.78187509091, -637264.8719770485)
       manifest(117, 939391.4354474426, -115193.798426606, 110, 290275.8045962162, 647591.8693387334, 24, 657818.7392670175, 62053.153193650534, 105, 588951.0024288252, 688857.7990654008, 91, 979429.8492896021, -768175.4954669797, 87, -46429.78187509091, -637264.8719770485)
       manifest(147, 939391.4354474426, 565245.7831826995, 110, 290275.8045962162, -265986.3438301103, 24, 657818.7392670175,62053.153193650534, 105, -207237.84233848623, 688857.7990654008, 91, 979429.8492896021, -768175.4954669797, 87,-46429.78187509091, -637264.8719770485)
       manifest(147, 939391.4354474426, 565245.7831826995, 119, 290275.8045962162, -265986.3438301103, 24, 657818.7392670175, 62053.153193650534, 105, -207237.84233848623, 688857.7990654008, 91, 979429.8492896021, -768175.4954669797, 87, -46429.78187509091, -637264.8719770485)
       manifest(61, -480127.7938808435, -319172.5775297376, 85, 909923.0002995867, 24411.654559691786, 101, 538987.035569658, -575537.6562530647, 122, 231377.1730074233, -249279.47990056884, 47, -49645.56772282068, -908013.7477894577, 31, -700986.8322514963, 734786.5047141262)
       manifest(39, 943608.2902939555, -106479.52757068072, 72, 666360.2248278332, -499305.3134384238, 43, 824580.1945323797, 634751.3935972787, 93, -639488.1557489913, -731585.8163509425, 15, -647643.9184564397, 374883.2856540957, 122, -922758.8036900283, -121046.42523794726)
       manifest(122, 840678.7176452728, 881730.6920745303, 68, -632329.081860199, -364661.10804407333, 32, 986236.4613307649, -52643.83809908817, 89, -850272.4548874649, 676602.8019689065, 137, -410888.4828504438, 733903.1101632088, 25, -486083.81072064245, -935461.843548014)
       manifest(88, 89879.98662669212, 748463.4999272984, 58, 763635.5358714485, -864374.4257851247, 26, 426472.2694961631, -897084.1331151726, 88, -115126.65873945435, -368348.4093834149, 49, 936108.4435310811, 20245.28466598864, 10, -802724.4850565143, 833935.8145113164)
       manifest(88, 89879.98662669212, 748463.4999272984, 58, 763635.5358714485, -864374.4257851247, 26, 426472.2694961631, -897084.1331151726, 88, -334467.711134013, 864448.4655215084, 49, 626303.3279546765, -489836.3762918854, 10, -802724.4850565143, 833935.8145113164)
       manifest(88, 89879.98662669212, -304279.6995524813, 58, 53154.50580243883, -175740.68327083567, 26, 426472.2694961631, -897084.1331151726, 88, 869316.9889658398, 864448.4655215084, 49, 626303.3279546765, -489836.3762918854, 10, -802724.4850565143, 833935.8145113164)

