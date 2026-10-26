import airsim
import pygame
import time

# 初始化pygame
pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("AirSim 无人机键盘控制")

client = airsim.MultirotorClient(ip="192.168.0.11")
client.confirmConnection()
client.enableApiControl(True)
client.armDisarm(True)

client.takeoffAsync().join()
print("="*40)
print("pygame手动控制已启动！")
print("W前进 S后退 | A左移 D右移")
print("Q上升 E下降 | Z左转 X右转")
print("ESC=退出并降落")
print("="*40)

speed = 3.0
vz_speed = 2.0
yaw_rate = 30

running = True
try:
    while running:
        vx = 0
        vy = 0
        vz = 0
        yaw = 0

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            vx = speed
        if keys[pygame.K_s]:
            vx = -speed
        if keys[pygame.K_a]:
            vy = speed
        if keys[pygame.K_d]:
            vy = -speed
        if keys[pygame.K_q]:
            vz = vz_speed
        if keys[pygame.K_e]:
            vz = -vz_speed
        if keys[pygame.K_z]:
            yaw = yaw_rate
        if keys[pygame.K_x]:
            yaw = -yaw_rate

        client.moveByVelocityAsync(vx, vy, vz, 0.1, yaw_mode=airsim.YawMode(True, yaw))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        time.sleep(0.05)
finally:
    client.landAsync().join()
    client.armDisarm(False)
    client.enableApiControl(False)
    pygame.quit()
    print("降落完成，API控制权已释放")
