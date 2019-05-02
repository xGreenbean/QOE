delta_t = 5


def add_sessions_by_server(streams, stream_video, video_streams):
    for stream in streams:
        if stream_video.to_same_server_over_port_443(stream):
            video_streams.add(stream.to_string())


def add_sessions_by_time(streams, stream_video, video_streams):
    for stream in streams:
        print('start times:', stream_video.get_start_time() - stream.get_start_time())
        if abs(stream_video.get_start_time() - stream.get_start_time()) < delta_t:
            video_streams.add(stream.to_string())
