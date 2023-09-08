import math


# adapt the positions of the gaps (barUp1,barUp2)
def manifest(a, a1, a2):
    import pygame
    import pymunk
    import pymunk.pygame_util
    import random

    pygame.init()

    WIDTH, HEIGHT = 500, 200

    barUp1 = 31  # 20-110
    barUp2 = 57  # 20-110

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

            if frame == 170:
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

if __name__ == "__main__":
    print(manifest(18, 491645.6155351049, 113943.04494820873))


