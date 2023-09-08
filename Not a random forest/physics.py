def manifest(a1, a2, b1, b2, c1, c2, d1, d2, e1, e2, f1, f2, g1, g2, h1, h2, i1, i2):
    import pygame
    import pymunk
    import pymunk.pygame_util

    pygame.init()

    WIDTH, HEIGHT = 800, 800
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
        body.position = (window.get_width() / 2, 10)
        shape = pymunk.Poly.create_box(body, (window.get_width(), 20))
        shape.elasticity = 0.4
        shape.friction = 0.5
        space.add(body, shape)

        center_body = pymunk.Body(body_type=pymunk.Body.DYNAMIC)
        center_body.position = (100, 40)
        shape = pymunk.Segment(center_body, (20, 20), (10, 10), 13)
        shape.mass = 10
        shape.elasticity = 1
        shape.friction = 2
        shape.color = (149, 164, 164, 0)

        center_body_1 = pymunk.Body(body_type=pymunk.Body.DYNAMIC)
        center_body_1.position = (124, 40)
        shape_1 = pymunk.Segment(center_body_1, (20, 20), (10, 10), 12)
        shape_1.mass = 10
        shape_1.elasticity = 1
        shape_1.friction = 2
        shape_1.color = (120, 135, 135, 0)

        center_joint_1 = pymunk.PinJoint(center_body, center_body_1, (20, 20), (10, 10))

        center_body_2 = pymunk.Body(body_type=pymunk.Body.DYNAMIC)
        center_body_2.position = (148, 40)
        shape_2 = pymunk.Segment(center_body_2, (20, 20), (10, 10), 11)
        shape_2.mass = 10
        shape_2.elasticity = 1
        shape_2.friction = 2
        shape_2.color = (90, 100, 100, 0)

        center_joint_2 = pymunk.PinJoint(center_body_1, center_body_2, (20, 20), (10, 10))

        space.add(center_body, shape, center_body_1, shape_1, center_body_2, shape_2, center_joint_1, center_joint_2)

        center_body_2.apply_force_at_local_point((1000000, 0), (0, 0))

        list_of_widths = [a1, a2, b1, b2, c1, c2, d1, d2, e1, e2, f1, f2, g1, g2, h1, h2, i1, i2]
        widths_index = -1
        height = 0
        list_of_bars = []
        for _ in range(18):
            list_of_bars.append(pymunk.Body(body_type=pymunk.Body.STATIC))
        bars_index = -1
        green = 200 + 20

        for _ in range(9):
            x_pos = 0
            negative = 1
            height += HEIGHT / 9
            green -= 20
            for _ in range(2):
                widths_index += 1
                bars_index += 1
                list_of_bars[bars_index].position = (x_pos, height)
                x_pos = 800
                shape = pymunk.Segment(list_of_bars[bars_index], (list_of_widths[widths_index]*negative, 0), (0, 0), 25) # pymunk.Poly.create_box(list_of_bars[bars_index], (list_of_widths[widths_index], 20))
                negative = -1
                shape.elasticity = 1.1
                shape.friction = 0.5
                shape.color = (21, green, 20, 0)

                space.add(list_of_bars[bars_index], shape)

        x = 0
        for _ in range(4):  # المفروض 2 ... خليها 2 بقى كدا وشوف
            bodyyy = pymunk.Body(body_type=pymunk.Body.STATIC)
            bodyyy.position = (x, window.get_height() / 2)
            x = WIDTH
            shapeee = pymunk.Poly.create_box(bodyyy, (20, window.get_height()))
            shapeee.elasticity = 0.4
            shapeee.friction = 0.5

            space.add(shapeee, bodyyy)

        frame = 0
        max = 0

        while run:
            frame = frame + 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # run = False
                    # break
                    return max

            if frame == 170:
                return max

            # center_body.position = pygame.mouse.get_pos()
            # center_body_3.position = (abs(center_body.position[0]-800),center_body.position[1])

            if frame > 40:
                how_down = center_body.position[1] * 18
                sum_of_area_covered_by_bars = 0  # just_proportional
                for i in list_of_widths:
                    sum_of_area_covered_by_bars += i
                value = how_down + sum_of_area_covered_by_bars
                if value > max:
                    max = value

            window.fill("black")
            space.debug_draw(window_space_linkage)
            pygame.display.update()

            space.step(dt)
            clock.tick(fps)

        pygame.quit()

    return (run(window))

if __name__ == "__main__":
    manifest(110.17884518386501, 397.15796794617114, 216.30542233714615, 323.40666702629943, 353.8603005132919, 266.32431257404147, 314.38347125742484, 213.9271714336115, 357.40405282249503, 252.4978776658531, 356.7606441316995, 215.924759862902, 336.4625317279635, 238.35901651187692, 346.3321409473805, 310.0919735228176, 342.2919695785009, 264.67824647876716)
    manifest(110.17884518386501, 397.15796794617114, 227.43951907522103, 359.9271150243192, 353.8603005132919,266.32431257404147, 388.2328662143098, 213.9271714336115, 382.6953662283587, 252.4978776658531, 376.3960981728211,215.924759862902, 364.4367827353044, 238.35901651187692, 346.3321409473805, 310.0919735228176, 342.2919695785009,283.0341780225827)
    manifest(110.17884518386501, 397.3954411386429, 227.43951907522103, 359.9271150243192, 353.8603005132919, 266.4356175593585, 388.2328662143098, 213.9271714336115, 398.8390591454806, 252.4978776658531, 376.3960981728211, 215.924759862902, 364.4367827353044, 267.42857072567597, 346.3321409473805, 310.0919735228176, 342.2919695785009, 283.0341780225827)
    manifest(110.17884518386501, 397.3954411386429, 260.7636080855819, 359.9271150243192, 353.8603005132919, 266.4356175593585, 388.2328662143098, 213.9271714336115, 398.8390591454806, 261.0458016842029, 376.3960981728211, 215.924759862902, 375.31875982176825, 267.42857072567597, 367.2102669534873, 313.93812730679997, 342.2919695785009, 292.3628531376432)
    manifest(110.17884518386501, 397.3954411386429, 260.7636080855819, 362.45525256269764, 353.8603005132919, 266.4356175593585, 388.2328662143098, 213.9271714336115, 398.8390591454806, 261.0458016842029, 376.3960981728211, 215.924759862902, 375.31875982176825, 300.2508565194118, 362.586731203391, 313.93812730679997, 393.67226796582986, 292.362853137643) # more forced