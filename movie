from moviepy.editor import VideoFileClip

def trim_video(input_path, output_path, start_time, end_time):
    # 载入视频文件
    video = VideoFileClip(input_path)
    
    # 裁剪视频
    trimmed_video = video.subclip(start_time, end_time)
    
    # 输出裁剪后的视频
    trimmed_video.write_videofile(output_path, codec='libx264', audio_codec='aac')

# 使用示例
input_video_path = 'your_video.mp4'  # 输入视频文件路径
output_video_path = 'trimmed_video.mp4'  # 输出视频文件路径
start_time = '00:01:30'  # 裁剪开始时间
end_time = '00:02:30'  # 裁剪结束时间

trim_video(input_video_path, output_video_path, start_time, end_time)
