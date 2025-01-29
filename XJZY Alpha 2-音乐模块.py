import os
import pygame

# 初始化pygame
pygame.init()
pygame.mixer.init()

# 获取音乐文件夹路径
music_dir = os.path.join(os.path.dirname(__file__), 'music')

# 获取音乐文件列表
def get_music_files(directory):
    return [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith(('.mp3', '.ogg'))]

# 播放音乐
def play_music(music_files, index):
    if 0 <= index < len(music_files):
        pygame.mixer.music.load(music_files[index])
        pygame.mixer.music.play(-1)  # 循环播放

# 主函数
def main():
    # 获取音乐文件列表
    music_files = get_music_files(music_dir)
    
    # 如果没有音乐文件，不执行音乐播放代码
    if not music_files:
        return
    
    current_index = 0  # 当前播放的音乐索引
    play_music(music_files, current_index)  # 播放第一首音乐

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F2:
                    # 按F2暂停/恢复播放
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.unpause()
                elif event.key == pygame.K_F1:
                    # 按F1播放上一个音乐
                    current_index = (current_index - 1) % len(music_files)
                    play_music(music_files, current_index)
                elif event.key == pygame.K_F3:
                    # 按F3播放下一个音乐
                    current_index = (current_index + 1) % len(music_files)
                    play_music(music_files, current_index)

    pygame.quit()

if __name__ == "__main__":
    main()