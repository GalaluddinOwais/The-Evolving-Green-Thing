import math


# adapt tha positions of the gaps (barUp1,barUp2)
def manifest(a, a1, a2,barUp1,barUp2):
    import pygame
    import pymunk
    import pymunk.pygame_util
    import random

    pygame.init()

    WIDTH, HEIGHT = 500, 200

    # barUp1 = 31  # 20-110
    # barUp2 = 57  # 20-110

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
        ########################################
        barDown1 = barUp1 + 70
        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        body.position = (window.get_width(), -HEIGHT / 2 + barUp1)
        shape = pymunk.Poly.create_box(body, (20, window.get_height()))
        shape.elasticity = 0.4
        shape.friction = 0.5
        space.add(body, shape)

        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        body.position = (window.get_width(), window.get_height() / 2 + barDown1)
        shape = pymunk.Poly.create_box(body, (20, window.get_height()))
        shape.elasticity = 0.4
        shape.friction = 0.5
        space.add(body, shape)
        # # # # ##### ## # ## ##
        barDown2 = barUp2 + 70

        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        body.position = (window.get_width() - 100, -HEIGHT / 2 + barUp2)
        shape = pymunk.Poly.create_box(body, (20, window.get_height()))
        shape.elasticity = 0.4
        shape.friction = 0.5
        space.add(body, shape)

        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        body.position = (window.get_width() - 100, window.get_height() / 2 + barDown2)
        shape = pymunk.Poly.create_box(body, (20, window.get_height()))
        shape.elasticity = 0.4
        shape.friction = 0.5
        space.add(body, shape)

        #######################################
        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        body.position = (0, window.get_height() / 2)
        shapee = pymunk.Poly.create_box(body, (20, window.get_height()))
        shapee.elasticity = 0.4
        shapee.friction = 0.5
        space.add(body, shapee)
        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        body.position = (window.get_width() / 2, -30)
        shape = pymunk.Poly.create_box(body, (window.get_width(), 100))
        shape.elasticity = 0.4
        shape.friction = 0.5
        space.add(body, shape)

        center_body = pymunk.Body(body_type=pymunk.Body.DYNAMIC)
        center_body.position = (100, window.get_height() - 40)
        shape = pymunk.Circle(center_body, 14)
        shape.mass = 10
        shape.elasticity = 1
        shape.friction = 2
        shape.color = (21, 120, 20, 0)

        space.add(center_body, shape)

        ball_pos = 50
        circle1 = pymunk.Body(body_type=pymunk.Body.DYNAMIC)
        circle1.position = (WIDTH / 2 + ball_pos, ball_pos)
        shape = pymunk.Circle(circle1, 12)
        shape.mass = 1
        shape.elasticity = 1
        shape.friction = 2
        shape.color = (random.uniform(0, 255), random.uniform(0, 255), random.uniform(0, 255), 0)
        space.add(circle1, shape)

        frame = 0
        max = 0
        body_close_to_ball = False
        while run:
            frame = frame + 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # run = False
                    # break
                    return (max)

            if frame == 140:
                return max

            if frame == a:
                center_body.apply_force_at_local_point((a1, a2), (0, 0))

            if 1 / math.sqrt(math.pow(circle1.position[0] - center_body.position[0], 2) + math.pow(
                    circle1.position[1] - center_body.position[1], 2)) * 10000 > 170:
                body_close_to_ball = True

            if body_close_to_ball:
                if circle1.position[0] > WIDTH:
                    closeness = 3000

                elif circle1.position[0] > WIDTH - 100:
                    closeness = 1000 + 1 / math.sqrt(
                        math.pow(circle1.position[0] - WIDTH, 2) + math.pow(circle1.position[1] - (barUp1 + 35),
                                                                            2)) * 10000
                    if closeness > 2000:
                        closeness = 2000

                else:
                    closeness = 1 / math.sqrt(
                        math.pow(circle1.position[0] - (WIDTH - 100), 2) + math.pow(circle1.position[1] - (barUp2 + 35),
                                                                                    2)) * 10000
                    if closeness > 1000:
                        closeness = 1000

                if max < closeness:
                    max = closeness

            window.fill("black")
            space.debug_draw(window_space_linkage)
            pygame.display.update()

            space.step(dt)
            clock.tick(fps)

        pygame.quit()

    return (run(window))
#

if __name__ == "__main__":
    for i in range(20, 111, 10):
        for j in range(20, 111, 10):


            if (i,j) in [(20, 110), (30, 110), (40, 110), (50, 110), (70, 70), (70, 80), (70, 90), (70, 100), (70, 110), (80, 70), (80, 80), (80, 90), (80, 100), (80, 110), (90, 70), (90, 80), (90, 90), (90, 100), (90, 110), (100, 70), (100, 80), (100, 90), (100, 100), (100, 110), (110, 70), (110, 80), (110, 90), (110, 100), (110, 110)]:
                print(manifest(19, 458652.519605519, -45693.939705564466, i, j))
                continue
            if (i,j) in [(30, 60), (30, 70), (30, 80), (30, 90), (30, 100), (40, 60), (40, 70), (40, 80), (40, 90), (40, 100), (50, 60), (50, 70), (50, 80), (50, 90), (50, 100), (60, 60), (60, 70), (60, 80), (60, 90), (60, 100), (70, 60), (80, 60), (90, 60)]:
                print(manifest(2, 348096.1352706116, -3251.766523247119, i, j))
                continue
            if (i,j) in  [(20, 100)]:
                print(manifest(9, 382259.4466601147, -138186.71780944482, i, j))
                continue
            if (i,j) in [(100, 60), (110, 50)]:
                print(manifest(19, 460146.01898988103, 122233.80376574816, i, j))
                continue
            if (i,j) in [(20, 70), (20, 80), (20, 90)]:
                print(manifest(16, 434114.2763414603, -103044.21386423166, i, j))
                continue
            if (i,j) in [(20, 20), (20, 30), (30, 20), (30, 30), (40, 40), (50, 40), (60, 40), (70, 40), (80, 40), (110, 30)]:
                print(manifest(2, 401872.621277004, 70663.53516655439, i, j))
                continue
            if (i,j) in [(20, 40), (40, 50), (50, 50), (60, 50), (70, 50), (80, 50), (110, 20), (110, 40)]:
                print(manifest(6, 461910.9132717664, 6966.92643095064, i, j))
                continue
            if (i,j) in [(20, 50), (20, 60), (30, 40), (30, 50)]:
                print(manifest(6, 461910.9132717664, 131749.1132374456, i, j))
                continue
            if (i,j) in [(40, 20), (40, 30), (50, 20), (50, 30), (60, 20), (60, 30), (70, 20), (70, 30)]:
                print(manifest(5, 429396.4177094607, -208934.98029169335,i,j))
                continue
            if (i,j) in [(80, 20), (90, 20), (100, 20)]:
                print(manifest(6, 495284.89650030585, -228256.26931282447,i,j))
                continue
            if (i,j) in [(80, 30), (90, 30), (90, 50), (100, 50)]:
                print(manifest(5, 410011.9366025855, 198964.9155717158,i,j))
                continue
            if (i,j) in [(90, 40), (100, 30), (100, 40), (110, 60)]:
                print(manifest(4, 434510.6719955816, 120581.19883688365,i,j))
                continue
            if (i,j) in [(60, 110)]:
                print(manifest(2, 359862.8211968938, 33919.71109586721,i,j))
                continue


