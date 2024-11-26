import ffmpy
ff = ffmpy.FFmpeg(
    inputs={'indian.gif': None},
    outputs={'indian.mp4': None}
)
ff.run()