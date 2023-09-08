import random
import math


def play():
    import pygame
    import pymunk
    import pymunk.pygame_util
    from pymunk.vec2d import Vec2d



    pygame.init()

    WIDTH, HEIGHT = 400, 400

    window = pygame.display.set_mode((WIDTH, HEIGHT))
    window_space_linkage = pymunk.pygame_util.DrawOptions(window)


    def enemy_neural_network(v1, w1, d1, v2, w2, d2, v3, w3, d3, v4, w4, d4, VVV1, VVVV1, VVV2, VVVV2, VVV3, VVVV3,
                             VVV4,
                             VVVV4, D1, D2, x1, x2):
        hidden_node_1_output = (x1 * v1 + x2 * w1 + d1)
        hidden_node_2_output = (x1 * v2 + x2 * w2 + d2)
        hidden_node_3_output = (x1 * v3 + x2 * w3 + d3)
        hidden_node_4_output = (x1 * v4 + x2 * w4 + d4)
        output1 = VVV1 * hidden_node_1_output + VVV2 * hidden_node_2_output + VVV3 * hidden_node_3_output + VVV4 * hidden_node_4_output + D1
        output2 = VVVV1 * hidden_node_1_output + VVVV2 * hidden_node_2_output + VVVV3 * hidden_node_3_output + VVVV4 * hidden_node_4_output + D2
        return [output1, output2]


    def run(window):

        run = True
        clock = pygame.time.Clock()
        fps = 60
        dt = 1 / fps

        space = pymunk.Space()
        space.gravity = (0, 981)

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
        color = (random.uniform(0, 255), random.uniform(0, 255), random.uniform(0, 255), 0)
        center_body_enemy = pymunk.Body(body_type=pymunk.Body.DYNAMIC)
        center_body_enemy.position = (WIDTH / 3, HEIGHT / 3)
        shape = pymunk.Circle(center_body_enemy, 10)
        shape.mass = 20
        shape.color = color
        space.add(center_body_enemy, shape)

        center_body_enemy2 = pymunk.Body(body_type=pymunk.Body.DYNAMIC)
        center_body_enemy2.position = (WIDTH * 2 / 3, HEIGHT * 2 / 3)
        shape2 = pymunk.Circle(center_body_enemy2, 10)
        shape2.mass = 20
        shape2.color = color
        space.add(center_body_enemy2, shape2)

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
        shapec = pymunk.Circle(center_body, 10)
        shapec.mass = .1
        shapec.elasticity = 2.3
        shapec.friction = 2
        shapec.color = (21, 120, 20, 0)
        space.add(center_body, shapec)

        enemy1_force = (-15000, -35000)
        frame = 0
        pressed_left = False
        pressed_right = False
        pressed_down = False
        pressed_up = False

        previous_pos = center_body.position
        previous_pos_enemy = center_body_enemy.position
        previous_pos_enemy2 = center_body_enemy2.position
        while run:
            frame = frame + 1
            print(int(frame/3600),':',int(frame/60)%60,':',frame%60)
            distance_1 = math.sqrt(math.pow(center_body.position[0] - center_body_enemy.position[0], 2) + math.pow(
                center_body.position[1] - center_body_enemy.position[1], 2))
            distance_2 = math.sqrt(math.pow(center_body.position[0] - center_body_enemy2.position[0], 2) + math.pow(
                center_body.position[1] - center_body_enemy2.position[1], 2))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # run = False
                    # break
                    return (fitness)

                    # Handle keyboard events
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                            pressed_left = True
                    elif event.key == pygame.K_RIGHT:
                            pressed_right = True
                    elif event.key == pygame.K_UP:
                            pressed_up = True
                    elif event.key == pygame.K_DOWN:
                            pressed_down = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                            pressed_left = False
                    elif event.key == pygame.K_RIGHT:
                            pressed_right = False
                    elif event.key == pygame.K_UP:
                            pressed_up = False
                    elif event.key == pygame.K_DOWN:
                            pressed_down = False

            x = 0
            y = 0
            if pressed_left:
                    x -= 300
            if pressed_right:
                    x+= 300


            if pressed_up:
                    y -= 300
            if pressed_down:
                    y += 200

            center_body.apply_force_at_local_point((x,y))

            if distance_1 <= 10 * 2 \
                    or distance_2 <= 10 * 2:
                return 'ouch!'


            if frame == 60 * 60 * 3:
                return 'you win!'

            if center_body.position[0] > WIDTH or center_body.position[0] < 0 or center_body.position[1] > HEIGHT or \
                    center_body.position[1] < 0:

                space.remove(center_body, shapec)
                center_body = pymunk.Body(body_type=pymunk.Body.DYNAMIC)
                center_body.position = previous_pos
                shapec = pymunk.Circle(center_body, 10)
                shapec.mass = .1
                shapec.elasticity = 2.3
                shapec.friction = 2
                shapec.color = (21, 120, 20, 0)
                space.add(center_body, shapec)
                print('glitch handled! too fast friendly ball went out of the boundaries')


            if center_body_enemy.position[0] > WIDTH or center_body_enemy.position[0] < 0 or \
                    center_body_enemy.position[1] > HEIGHT or center_body_enemy.position[1] < 0 :

                space.remove(center_body_enemy, shape)
                center_body_enemy = pymunk.Body(body_type=pymunk.Body.DYNAMIC)
                center_body_enemy.position = previous_pos_enemy
                shape = pymunk.Circle(center_body_enemy, 10)
                shape.mass = 20
                shape.color = color
                space.add(center_body_enemy, shape)
                print('glitch handled! too fast enemy1 ball went out of the boundaries')



            if    center_body_enemy2.position[0] > WIDTH or center_body_enemy2.position[0] < 0 or \
                center_body_enemy2.position[1] > HEIGHT or center_body_enemy2.position[1] < 0:
                space.remove(center_body_enemy2, shape2)
                center_body_enemy2 = pymunk.Body(body_type=pymunk.Body.DYNAMIC)
                center_body_enemy2.position = previous_pos_enemy2
                shape2 = pymunk.Circle(center_body_enemy2, 10)
                shape2.mass = 20
                shape2.color = color
                space.add(center_body_enemy2, shape2)
                print('glitch handled! too fast enemy2 ball went out of the boundaries')



            # # # # # #

            if frame % 240 == 0:
                enemy1_force = (-15000, -35000)

            elif frame % 180 == 0:
                enemy1_force = (15000, -35000)

            elif frame % 120 == 0:
                enemy1_force = (-15000, 0)

            elif frame % 60 == 0:
                enemy1_force = (15000, 0)

            center_body_enemy.apply_force_at_local_point(enemy1_force, (0, 0))

            enemy2_neural_network_output = enemy_neural_network(-0.7540979010233855, 6.778878818143113, -2.6855252451531086, 8.455380288478416, 3.693917348250075,
                   9.306492256022576, -7.236741361017039, -7.0439586699553125, 8.403283162955269, -5.6020558929686555,
                   -6.039465596453688, -9.120959513164772, 1.7652579083178725, -3.123894206518978, -8.740218780670867,
                   -8.15113981921759, -9.979700867248319, 5.557066721407448, 7.707349576922642, 6.073577015082407,
                   9.535713619818168, 9.872941457130725,
                                                                center_body_enemy2.position[0] - center_body.position[
                                                                    0],
                                                                center_body_enemy2.position[1] - center_body.position[
                                                                    1])

            center_body_enemy2.apply_force_at_local_point(
                (enemy2_neural_network_output[0], enemy2_neural_network_output[1]), (0, 0))




            if center_body.position[0]>10 and center_body.position[0]<WIDTH-10 and center_body.position[1]>10 and center_body.position[1]<HEIGHT-10:
                previous_pos = center_body.position

            if center_body_enemy.position[0]>10 and center_body_enemy.position[0]<WIDTH-10 and center_body_enemy.position[1]>10 and center_body_enemy.position[1]<HEIGHT-10:
                previous_pos_enemy = center_body_enemy.position

            if center_body_enemy2.position[0] > 10 and center_body_enemy2.position[0] < WIDTH - 10 and \
                    center_body_enemy2.position[1] > 10 and center_body_enemy2.position[1] < HEIGHT - 10:
                previous_pos_enemy2 = center_body_enemy2.position

            window.fill("black")
            space.debug_draw(window_space_linkage)
            pygame.display.update()

            space.step(dt)
            clock.tick(fps)

        pygame.quit()

    return (run(window))


if __name__ == "__main__":
    print(play())

